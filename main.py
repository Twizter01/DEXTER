"""
██████╗ ███████╗██╗  ██╗████████╗███████╗██████╗
██╔══██╗██╔════╝╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗
██║  ██║█████╗   ╚███╔╝    ██║   █████╗  ██████╔╝
██║  ██║██╔══╝   ██╔██╗    ██║   ██╔══╝  ██╔══██╗
██████╔╝███████╗██╔╝ ██╗   ██║   ███████╗██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

    ◄ POKEDEX COMPANION ►  [ GEN III EDITION ]
    ════════════════════════════════════════════
    » Region  : Hoenn / Kanto / Johto
    » Version : 1.0.0
    » Mode    : LOYAL — Original mechanics only
    ════════════════════════════════════════════
    "Gotta catch 'em all."  — Prof. Oak, 1996
"""

from __future__ import annotations

import sys
import os

from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
from rich.console import Console
from _console import console

from assets.ascii_art import * # All Ascii art is import for now TODO Remove later when the actual art has been chosen
from cli.prompts import  intro_screen
from poke_exceptions import PokemonNotFound
from cli.commands import *



def command_dispatch_helper(user_command: str) -> None:
    command = COMMAND_TABLE.get(user_command)

    if command is None:
        console.print(Panel.fit(f"User Command: [red]{user_command}[/red] not recognized, try again or type help to check all the available commands",style="cyan",))
        return

    try:
        if callable(command):
            command()
        else:
            console.print(Text(f"Command '{user_command}' is not implemented yet."), style="yellow")
    except PokemonNotFound:
        console.print(Text("Pokemon not found"), style="red")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as exc:
        console.print(Text(f"An unexpected error occurred: {exc}"), style="red")


def main() -> None:

    intro_screen(INTRO_TEXT)
    

    while True:
        user_command = input(">").strip().lower()
        
        if not user_command:
            continue    
        command_dispatch_helper(user_command)

if __name__ == "__main__":
    main()


