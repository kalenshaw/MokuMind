"""
MokuMind: Tekken 8 Character Recommender

This module provides a simple, interpretable recommendation system
for suggesting Tekken 8 characters based on a player's preferences.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TekkenCharacter:
    name: str
    playstyles: List[str]
    personalities: List[str]
    experience_levels: List[str]
    description: str


# --- Tekken 8 roster subset with tagged archetypes ---
# NOTE: All characters below are part of Tekken 8's roster.
CHARACTERS: List[TekkenCharacter] = [
    TekkenCharacter(
        name="Jin Kazama",
        playstyles=["balanced", "whiff-punish", "fundamental"],
        personalities=["disciplined", "serious", "cool"],
        experience_levels=["beginner", "intermediate"],
        description="A well-rounded character with solid tools in every range; great for learning core Tekken."
    ),
    TekkenCharacter(
        name="Kazuya Mishima",
        playstyles=["rushdown", "whiff-punish"],
        personalities=["aggressive", "serious"],
        experience_levels=["intermediate", "advanced"],
        description="High damage and strong mix-ups, but execution-heavy and demanding on decision-making."
    ),
    TekkenCharacter(
        name="Lars Alexandersson",
        playstyles=["rushdown", "mobility"],
        personalities=["flashy", "cool"],
        experience_levels=["beginner", "intermediate"],
        description="Fast, dynamic offense with good mobility; great if you like stylish rushdown."
    ),
    TekkenCharacter(
        name="Ling Xiaoyu",
        playstyles=["stance-heavy", "tricky"],
        personalities=["playful", "tricky"],
        experience_levels=["intermediate", "advanced"],
        description="A stance-heavy, movement-based character with lots of evasive tools and tricky offense."
    ),
    TekkenCharacter(
        name="King",
        playstyles=["grappler", "rushdown"],
        personalities=["flashy", "showman"],
        experience_levels=["intermediate", "advanced"],
        description="A command-grab monster with tons of throws; perfect if you like wrestling and mind games."
    ),
    TekkenCharacter(
        name="Paul Phoenix",
        playstyles=["rushdown", "fundamental"],
        personalities=["simple", "aggressive"],
        experience_levels=["beginner", "intermediate"],
        description="Straightforward, hard-hitting brawler; great for players who like big damage and simple gameplans."
    ),
    TekkenCharacter(
        name="Hwoarang",
        playstyles=["rushdown", "stance-heavy"],
        personalities=["flashy", "aggressive"],
        experience_levels=["intermediate", "advanced"],
        description="Relentless kick-based offense with stance pressure; ideal for players who like nonstop aggression."
    ),
    TekkenCharacter(
        name="Asuka Kazama",
        playstyles=["defensive", "fundamental"],
        personalities=["patient", "chill"],
        experience_levels=["beginner", "intermediate"],
        description="Defensive, counter-focused toolkit that rewards patience and solid reads."
    ),
    TekkenCharacter(
        name="Lili",
        playstyles=["mobility", "whiff-punish"],
        personalities=["flashy", "playful"],
        experience_levels=["intermediate"],
        description="High-mobility character with stylish moves; great for players who like dancing around opponents."
    ),
    TekkenCharacter(
        name="Jun Kazama",
        playstyles=["defensive", "balanced"],
        personalities=["calm", "disciplined"],
        experience_levels=["beginner", "intermediate"],
        description="Protective, defensive character with strong tools for controlling space and tempo."
    ),
    TekkenCharacter(
        name="Nina Williams",
        playstyles=["rushdown", "stance-heavy"],
        personalities=["serious", "cold"],
        experience_levels=["intermediate", "advanced"],
        description="Assassin-style rushdown with stances and technical strings; rewarding for lab monsters."
    ),
    TekkenCharacter(
        name="Bryan Fury",
        playstyles=["rushdown", "pressure"],
        personalities=["chaotic", "aggressive"],
        experience_levels=["intermediate", "advanced"],
        description="High-pressure, counterhit-focused brawler; great if you like bullying opponents."
    ),
    TekkenCharacter(
        name="Leo Kliesen",
        playstyles=["balanced", "fundamental"],
        personalities=["disciplined"],
        experience_levels=["beginner", "intermediate"],
        description="Stable toolkit with good punishment and solid mids; ideal for learning fundamentals."
    ),
    TekkenCharacter(
        name="Azucena",
        playstyles=["tricky", "counter"],
        personalities=["playful", "chaotic"],
        experience_levels=["intermediate"],
        description="Coffee-loving MMA fighter with stance-based evasions and mind games."
    ),
    TekkenCharacter(
        name="Reina",
        playstyles=["rushdown", "mixup"],
        personalities=["mysterious", "aggressive"],
        experience_levels=["intermediate", "advanced"],
        description="Fast and versatile character with Mishima-inspired tools and strong mix-ups."
    ),
    TekkenCharacter(
        name="Victor Chevalier",
        playstyles=["whiff-punish", "mid-range"],
        personalities=["cool", "disciplined"],
        experience_levels=["intermediate"],
        description="Stylish sword-and-gun fighter who controls space and punishes mistakes."
    ),
]


def _score_character(
    character: TekkenCharacter,
    playstyle: Optional[str],
    personality: Optional[str],
    experience_level: Optional[str],
) -> int:
    """Simple scoring based on tag matches."""
    score = 0

    if playstyle:
        playstyle = playstyle.lower()
        if playstyle in character.playstyles:
            score += 2

    if personality:
        personality = personality.lower()
        if personality in character.personalities:
            score += 2

    if experience_level:
        experience_level = experience_level.lower()
        if experience_level in character.experience_levels:
            score += 2

    return score


def recommend_characters(
    playstyle: Optional[str] = None,
    personality: Optional[str] = None,
    experience_level: Optional[str] = None,
    top_k: int = 3,
) -> List[TekkenCharacter]:
    """
    Recommend Tekken 8 characters based on player preferences.

    Args:
        playstyle: e.g. "rushdown", "defensive", "balanced", "grappler",
                   "stance-heavy", "mobility", "whiff-punish", "tricky"
        personality: e.g. "flashy", "patient", "aggressive", "playful",
                     "disciplined", "chaotic", "serious"
        experience_level: "beginner", "intermediate", or "advanced"
        top_k: number of characters to return

    Returns:
        A list of TekkenCharacter objects sorted by how well they match.
    """
    scored = [
        (c, _score_character(c, playstyle, personality, experience_level))
        for c in CHARACTERS
    ]

    # Sort by score (descending), then name for stable order
    scored.sort(key=lambda pair: (-pair[1], pair[0].name))

    # Filter out characters with zero score if at least one preference was provided
    if playstyle or personality or experience_level:
        scored = [pair for pair in scored if pair[1] > 0]

    return [c for c, _ in scored[:top_k]]


def pretty_recommendation(
    playstyle: Optional[str] = None,
    personality: Optional[str] = None,
    experience_level: Optional[str] = None,
    top_k: int = 3,
) -> str:
    """
    High-level helper that returns a nicely formatted text response.
    This is ideal for wiring into your MokuMind GPT as a tool/action.
    """
    chars = recommend_characters(
        playstyle=playstyle,
        personality=personality,
        experience_level=experience_level,
        top_k=top_k,
    )

    if not chars:
        return (
            "I couldn't find a strong match from your preferences, "
            "but Jin Kazama is a great all-rounder to start with in Tekken 8."
        )

    header = "Based on your preferences, here are some Tekken 8 characters you might enjoy:\n"
    bullet_lines = []
    for c in chars:
        bullet_lines.append(f"- **{c.name}** — {c.description}")

    details = []
    if playstyle:
        details.append(f"playstyle = *{playstyle}*")
    if personality:
        details.append(f"personality = *{personality}*")
    if experience_level:
        details.append(f"experience level = *{experience_level}*")

    if details:
        header = (
            "Based on your preferences ("
            + ", ".join(details)
            + "), here are some Tekken 8 characters you might enjoy:\n"
        )

    return header + "\n".join(bullet_lines)
