config.py — all constants, nothing else
pythonBASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_RETRIES = 3
TIMEOUT = 6

utils/validators.py — pure functions, no I/O, no side effects, easily unit testable
pythondef is_valid_pokemon_name(name: str) -> bool:
    return bool(name) and name.replace("-", "").isalpha()
cli/prompts.py — everything that touches the user: input, display, rich console
pythondef get_pokemon_name() -> str: ...
def display_pokemon(data: dict) -> None: ...
api/client.py — everything that touches the network
pythondef fetch_pokemon_data(url: str, pokemon_name: str) -> dict: ...
def fetch_evolution_chain(...): ...
main.py — only orchestration, imports from all layers, no logic of its own
pythonfrom config import BASE_URL
from api.client import fetch_pokemon_data
from cli.prompts import get_pokemon_name, display_pokemon

def main() -> None:
    while True:
        pokemon = get_pokemon_name()
        try:
            data = fetch_pokemon_data(BASE_URL, pokemon)
            display_pokemon(data)
            return
        except ...

*The principle behind this is separation of layers — each layer has one external dependency:*
main → orchestrates
 ├── cli/     → only talks to the user
 ├── api/     → only talks to the network  
 └── utils/   → talks to nothing, pure logic



 