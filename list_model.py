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

models = client.models.list().data
print([m.id for m in models])
