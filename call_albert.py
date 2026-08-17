#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "openai>=3.1.0",
# ]
# ///

# requirements: openai>=2.53.0
import os
import sys
from pathlib import Path
from openai import OpenAI

key_path = Path("albert_key")
API_KEY = None
if key_path.exists():
    API_KEY = key_path.read_text().strip()
else:
    API_KEY = os.environ.get("ALBERT_API_KEY")

if not API_KEY:
    print("Clé API introuvable: ajouter le fichier albert_key ou définisez ALBERT_API_KEY")
    sys.exit(1)

client = OpenAI(
    base_url="https://albert.api.etalab.gouv.fr/v1",
    api_key=API_KEY,
)

def new_conversation():
    return [ 
        {"role": "system", "content": "Tu réponds en français, de façon concise."}
    ]

messages = new_conversation()

def send_message(user_text):
    messages.append({"role": "user", "content": user_text})
    resp = client.chat.completions.create(
        model="qwen3-coder-30b-A3b-instruct",
        messages=messages,
        max_tokens=600,
        temperature=0.2,
    )
    assistant_msg = resp.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_msg})
    return assistant_msg

def repl():
    print("Agent Albert - tapez /quit pour quitter, /reset pour recommencer")
    try:
        while True:
            user = input("Vous: ").strip()
            if not user:
                continue
            if user.lower() == "/quit":
                print("Au revoir")
                break
            if user.lower() == "/reset":
                global messages
                messages = new_conversation()
                print("Conversation réinitialisée")
                continue
            reply = send_message(user)
            print("Albert:", reply)
    except(KeyboardInterrupt, EOFError):
        print("\nInterromy, Au revoir")

if __name__ == "__main__":
    repl()
