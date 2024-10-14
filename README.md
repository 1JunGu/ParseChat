# ParseChat
Parse exported JSON data from AI Chat (e.g., Claude)

## Usage
`python convert2html.py`
>[!NOTE]
>remember replace the specified json filename in scirpt

## Example
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Conversation</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
            .message { padding: 10px; margin-bottom: 10px; border-radius: 5px; }
            .human { background-color: #e6f3ff; }
            .assistant { background-color: #f0f0f0; }
            .sender { font-weight: bold; margin-bottom: 5px; }
            .text { white-space: pre-wrap; }
        </style>
    </head>
    <body>
        <h1>Conversation</h1>
        
        <div class="message human">
            <div class="sender">Human</div>
            <div class="text">1</div>
        </div>
        

        <div class="message assistant">
            <div class="sender">Assistant</div>
            <div class="text">2</div>
        </div>
        

        <div class="message human">
            <div class="sender">Human</div>
            <div class="text">3</div>
        </div>
        

        <div class="message assistant">
            <div class="sender">Assistant</div>
            <div class="text">4</div>
        </div>
        

        <div class="message human">
            <div class="sender">Human</div>
            <div class="text">6</div>
        </div>
        

        <div class="message assistant">
            <div class="sender">Assistant</div>
            <div class="text"></div>
        </div>
        
    </body>
    </html>
