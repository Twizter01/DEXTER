from typing import TypedDict
from typing import Any
from typing import Optional
from typing import TYPE_CHECKING

class Pokemon(TypedDict):
    name: str | None 
    age: int | float | None
    height: int | None
    abilities: list[dict[str, Any]]
    id: int | float | None
    moves: list[dict[Any, Any]]
    past_abilities: list[dict[Any, Any]]
    base_experience: int | None
    held_items: list[dict[Any, Any]]
    is_default: bool
    past_stats: list[dict[Any, Any]]
    cries: dict
    generation_chain: list[dict[Any, Any]]
    version_group_details: list[dict[Any, Any]]
    stats: list[dict[Any, Any]]
    game_indices: list[dict[Any, Any]]
    location_area_encounters: str | None
    past_type: list | None
    order: int | None
    species: dict[str, str]
    types: dict[Any, Any]
    sprites: dict[Any, Any]
    growth_rates: list[dict[Any, Any]]
    evolution_chain: list[dict[Any, Any]]



