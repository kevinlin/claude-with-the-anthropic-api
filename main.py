#!/usr/bin/env python3
"""
Simple Python project to interact with Anthropic API
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

def main():
    # Initialize the Anthropic client
    client = Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key or set it as an environment variable.")
        return
    
    try:
        # Example: Simple conversation with Claude
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": "Hello! Can you tell me a fun fact about Python programming?"
                }
            ]
        )
        
        print("Claude's response:")
        print(message.content[0].text)
        
    except Exception as e:
        print(f"Error calling Anthropic API: {e}")

def interactive_chat():
    """Interactive chat function for ongoing conversation"""
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        return
    
    print("Interactive Chat with Claude (type 'quit' to exit)")
    print("-" * 50)
    
    conversation_history = []
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})
        
        try:
            # Get response from Claude
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                temperature=0.7,
                messages=conversation_history
            )
            
            response = message.content[0].text
            print(f"\nClaude: {response}")
            
            # Add Claude's response to history
            conversation_history.append({"role": "assistant", "content": response})
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Anthropic API Python Project")
    print("=" * 30)
    
    # Run simple example
    print("\n1. Running simple example...")
    main()
    
    # Ask if user wants interactive chat
    print("\n" + "=" * 50)
    choice = input("Would you like to start interactive chat? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes']:
        interactive_chat() 