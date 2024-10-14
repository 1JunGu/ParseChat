import json
from html import escape
import os
from datetime import datetime

def parse_iso_datetime(date_string):
    return datetime.fromisoformat(date_string.replace('Z', '+00:00'))

def create_conversation_html(chat_messages, output_file, font_family, conversation_name):
    # Sort messages by created_at time
    sorted_messages = sorted(chat_messages, key=lambda x: parse_iso_datetime(x['created_at']))

    # HTML template with escaped curly braces in CSS, parameterized font-family, and conversation name
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{conversation_name}</title>
        <style>
            body {{ font-family: {font_family}; max-width: 800px; margin: 0 auto; padding: 20px; }}
            .message {{ padding: 10px; margin-bottom: 10px; border-radius: 5px; }}
            .Koo {{ background-color: #e6f3ff; }}
            .Claude {{ background-color: #f0f0f0; }}
            .sender {{ font-weight: bold; margin-bottom: 5px; }}
            .text {{ white-space: pre-wrap; }}
            .timestamp {{ font-size: 0.8em; color: #666; margin-top: 5px; }}
        </style>
    </head>
    <body>
        <h1>{conversation_name}</h1>
        {content}
    </body>
    </html>
    """

    # Generate message blocks
    message_blocks = []
    for message in sorted_messages:
        sender = message['sender']
        if sender == 'human':
            sender_name = 'Koo'
        elif sender == 'assistant':
            sender_name = 'Claude 3.5 Sonnet'
        else:
            sender_name = sender.capitalize()
        
        text = escape(message['text'])  # Escape HTML special characters
        timestamp = parse_iso_datetime(message['created_at']).strftime('%Y-%m-%d %H:%M:%S')
        block = f"""
        <div class="message {sender_name.split()[0]}">
            <div class="sender">{sender_name}</div>
            <div class="text">{text}</div>
            <div class="timestamp">{timestamp}</div>
        </div>
        """
        message_blocks.append(block)

    # Combine message blocks and insert into template
    content = "\n".join(message_blocks)
    html_content = html_template.format(content=content, font_family=font_family, conversation_name=conversation_name)

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Conversation HTML saved as {output_file}")

def process_json_file(json_file_path, output_directory, font_family):
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Read JSON data from file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Function to get the created_at time for sorting
    def get_creation_time(item):
        return parse_iso_datetime(item.get('created_at', '1970-01-01T00:00:00Z'))

    # Process the data based on its structure
    if isinstance(data, list):
        for i, item in enumerate(data):
            if 'chat_messages' in item:
                conversation_name = item.get('name', f'Conversation {i+1}')
                created_at = get_creation_time(item).strftime('%Y-%m-%d_%H')
                output_file = os.path.join(output_directory, f'{i+1:03d}_{created_at}_{conversation_name}.html')
                create_conversation_html(item['chat_messages'], output_file, font_family, conversation_name)
    elif isinstance(data, dict):
        if 'chat_messages' in data:
            conversation_name = data.get('name', 'Conversation')
            created_at = get_creation_time(data).strftime('%Y-%m-%d %H:%M:%S')
            output_file = os.path.join(output_directory, f'{created_at}_{conversation_name}.html')
            create_conversation_html(data['chat_messages'], output_file, font_family, conversation_name)
    else:
        print("Unexpected JSON structure. Please check your JSON file.")

# Usage
json_file_path = 'conversations.json'  # Replace with your JSON file path
output_directory = 'conversations_output'  # Replace with your desired output directory

# Choose one of these font family options:
system_fonts = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif'
arial_fonts = 'Arial, Helvetica, "Nimbus Sans", "Liberation Sans", Arimo, sans-serif'
times_fonts = 'Times, "Times New Roman", serif'

# Set your preferred font family here:
chosen_font_family = arial_fonts

process_json_file(json_file_path, output_directory, chosen_font_family)