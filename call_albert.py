# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "openai>=2.53.0",
# ]
# ///

import os
from openai import OpenAI

client = OpenAI(
    base_url="https://albert.api.etalab.gouv.fr/v1",
    api_key=os.environ["ALBERT_API_KEY"],
)

r = client.chat.completions.create(
    model="qwen3-coder-30b-A3b-instruct",
    messages=[
        {"role": "system", "content": "Tu réponds en français, de façon concise."},
        {"role": "user", "content": "Explique ce qu'est une API compatible OpenAI en deux phrases."},
    ],
)
print(r.choices[0].message.content)
