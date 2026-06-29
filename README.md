# DEXTER — Pokédex Companion CLI
> ◄ POKÉDEX COMPANION ► [ GEN III EDITION ]  
> Region: Hoenn / Kanto / Johto · Version: 1.0.0 · Mode: LOYAL — Original mechanics only

* A terminal-based Pokédex companion powered by [PokéAPI](https://pokeapi.co/). Dexter talks back.

---

## Features

- **Pokémon Lookup** — stats, types, abilities, and base info
- **Weakness Calculator** — full type matchup breakdown
- **Evolution Chains** — complete family trees
- **Move Lists** — learnsets with method and level
- **Battle Recommendations** — counters and coverage suggestions
- **Generation Info** — Gen III regional data (Hoenn / Kanto / Johto)
- **Team Builder** — assemble and analyze a party of six
- **Voice Feedback** — Dexter reads responses aloud via `pyttsx3`
- **Rich UI** — styled panels, tables, and ASCII art via `rich`

---

## Project Structure

```
pokedex/
├── assets/
│   └── ascii_art.py         # ASCII art assets
├── cli/
│   ├── commands.py          # Command table & handlers
│   └── prompts.py           # CLI prompt helpers
├── ui/
│   ├── boxes.py             # Layout boxes
│   └── panels.py            # Rich panel components
├── utils/
│   └── validators.py        # Input validation
├── config.py                # Base URL, constants, config
├── exceptions.py            # Custom exceptions
├── pokemon.py               # Pokémon data models
├── main.py                  # Entry point & dispatcher
├── requirements.txt
└── README.md
```

---

## Flow

```
User Input
    ↓
CLI Dispatcher (command table lookup)
    ↓
Service Layer (logic & validation)
    ↓
PokéAPI (HTTP via requests)
    ↓
Rich UI + pyttsx3 voice output
```

---

## Installation

```bash
git clone https://github.com/your-username/pokedex.git
cd pokedex
pip install -r requirements.txt
python main.py
```

> **Note:** `pyttsx3` may require a system TTS engine.  
> On Linux: `sudo apt install espeak`  
> On macOS: built-in `NSSpeechSynthesizer` is used automatically.

---

## Usage

```
► pokemon <name>       Look up a Pokémon
► weakness <name>      Show type weaknesses
► evolution <name>     Display evolution chain
► moves <name>         List learnable moves
► battle <name>        Get battle recommendations
► team                 Open team builder
► gen <number>         Generation info
► help                 List all commands
► exit                 Quit
```

```                     ARCHITECTURE

                    ┌─────────────────────┐
                    │      main.py        │
                    │   Entry Point / UI  │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │      cli/commands.py    │
                 │ Command Dispatcher      │
                 └──────────┬──────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
   prompts.py         api/client.py      ui/panels.py
 Business Logic       API Layer          Presentation
        │                   │                   │
        └───────────────┬───┘                   │
                        ▼                       ▼
                 validators.py          Rich Components
                        │
                        ▼
                  exceptions.py

```
* Separation of Concern
* Modular Structure
* Testable
* Each layer has its own responsability


## Dependencies

| Package    | Purpose                  |
|------------|--------------------------|
| `requests` | PokéAPI HTTP client      |
| `rich`     | Terminal UI & styling    |
| `pyttsx3`  | Text-to-speech (Dexter)  |
| `pprint`   | Debug output             |

---

## Scope

Dexter is intentionally scoped to **Generation III** mechanics. Moves, abilities, and type interactions reflect Hoenn/Kanto/Johto rules. No fairy type. No mega evolutions.

---

*"Gotta catch 'em all." — Prof. Oak, 1996*


> TODO: POKEDEX/ SUGGESTED ARCHITECTURE

│
├── main.py
│
├── api/
│   ├── client.py
│   └── endpoints.py
│
├── services/
│   ├── pokemon_service.py
│   ├── search_service.py
│   └── cache_service.py
│
├── cli/
│   ├── commands.py
│   ├── parser.py
│   └── dispatcher.py
│
├── ui/
│   ├── panels.py
│   ├── themes.py
│   ├── boxes.py
│   └── render.py
│
├── models/
│   ├── pokemon.py
│   ├── move.py
│   └── type.py
│
├── validators/
│   ├── pokemon_validator.py
│   └── input_validator.py
│
├── assets/
│
├── tests/
│
├── config.py
├── constants.py
└── exceptions.py