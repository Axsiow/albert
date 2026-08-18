# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "openai>=2.53.0",
#     "path>=17.1.1",
#     "pathlib>=1.0.1",
# ]
# ///

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

models = client.models.list().data
print([m.id for m in models])
