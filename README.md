# Anthropic API Python Project

A simple Python project to interact with Anthropic's Claude API.

## Setup

1. **Clone or download this project**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   - Copy `.env.example` to `.env`
   - Add your Anthropic API key to the `.env` file
   ```bash
   cp .env.example .env
   ```
   - Edit `.env` and replace `your_api_key_here` with your actual API key

4. **Get your Anthropic API key**
   - Go to [Anthropic Console](https://console.anthropic.com/)
   - Create an account or log in
   - Generate an API key
   - Copy it to your `.env` file

## Usage

### Basic Usage

Run the main script:
```bash
python main.py
```

This will:
1. Run a simple example query to Claude
2. Optionally start an interactive chat session

### Interactive Chat

The script includes an interactive chat mode where you can have an ongoing conversation with Claude. Type 'quit' to exit.

### Customization

You can modify `main.py` to:
- Change the model (e.g., `claude-3-haiku-20240307` for faster responses)
- Adjust temperature for more/less creative responses
- Modify max_tokens for longer/shorter responses
- Add system messages for specific behavior

## Project Structure

```
claude-with-the-anthropic-api/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment file
├── .env               # Your actual environment variables (create this)
└── README.md          # This file
```

## Available Models

- `claude-3-5-sonnet-20241022` (default) - Most capable model
- `claude-3-haiku-20240307` - Fastest model
- `claude-3-opus-20240229` - Most powerful model

## Example Code

```python
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)
```

## Error Handling

The project includes basic error handling for:
- Missing API key
- API call failures
- Network issues

## Next Steps

You can extend this project by:
- Adding more sophisticated conversation management
- Implementing different chat modes or personas
- Adding file upload capabilities
- Creating a web interface
- Adding logging and conversation history 