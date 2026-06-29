# RAG Pipeline -> 1. Fetch data → 2. Chunk it → 3. Embed it → 4. Store it → 5. Query it → 6. Generate answer
from typing import Any


BASE_URL: str = f"https://pokeapi.co/api/v2/pokemon/"
MAX_RETRIES: int = 3
TIMEOUT: int = 6 # Seconds
PARAMS: dict[Any, Any]
INTRO_TEXT: str = "How can I help you today! \n" \
                                 "Let me know by typing a command! Type help at any moment to print all available commands! \n" \
                                 ""


pokemon_lookup_prompt: str = f"Do you want yo look up another Pokemon? (Y/N): "
