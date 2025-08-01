#!/usr/bin/env python3
"""
Simple Python project to interact with Anthropic API
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# LLM Configuration Constants
API_KEY = os.getenv("ANTHROPIC_API_KEY")
MODEL = "claude-3-5-haiku-20241022"
MAX_TOKENS = 1000
TEMPERATURE = 0.7

conversation_history = []

def single_chat():
    # Initialize the Anthropic client
    client = Anthropic(api_key=API_KEY)

    if not API_KEY:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key or set it as an environment variable.")
        return

    try:
        append_user_message(conversation_history, "What is quantum computing?")

        # Example: Simple conversation with Claude
        message = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            messages=conversation_history
        )

        print("Claude's response:")
        print(message.content[0].text)
        append_assistant_message(conversation_history, message.content[0].text)

    except Exception as e:
        print(f"Error calling Anthropic API: {e}")

def interactive_chat():
    """Interactive chat function for ongoing conversation"""
    client = Anthropic(api_key=API_KEY)
    
    if not API_KEY:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        return
    
    print("Interactive Chat with Claude (type 'quit' to exit)")
    print("-" * 50)
        
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        append_user_message(conversation_history, user_input)
        
        try:
            # Get response from Claude
            message = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                temperature=TEMPERATURE,
                messages=conversation_history
            )
            
            response = message.content[0].text
            print(f"\nClaude: {response}")
            
            # Add Claude's response to history
            append_assistant_message(conversation_history, response)
            
        except Exception as e:
            print(f"Error: {e}")

def append_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def append_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

if __name__ == "__main__":
    print("Anthropic API Python Project")
    print("=" * 30)
    
    # Run simple example
    print("\n1. Running simple example...")
    single_chat()
    
    # Ask if user wants interactive chat
    print("\n" + "=" * 50)
    choice = input("Would you like to start interactive chat? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes']:
        interactive_chat() 
