# MokuMind – Tekken 8 Character Recommender

MokuMind is a small, focused recommendation engine that suggests **Tekken 8 characters** based on a player's preferred **playstyle**, **personality**, and **experience level**.

This repo complements my custom **MokuMind GPT** created in ChatGPT.  
The GPT uses this logic behind the scenes to recommend characters to new players.

---

## 🎮 What it does

Given inputs like:

- Playstyle: `rushdown`, `defensive`, `balanced`, `grappler`, `stance-heavy`, `mobility`, `whiff-punish`, `tricky`, etc.
- Personality: `flashy`, `patient`, `aggressive`, `playful`, `disciplined`, `chaotic`, `serious`, etc.
- Experience level: `beginner`, `intermediate`, `advanced`

MokuMind returns Tekken 8 characters whose archetypes best match those preferences, along with a short description of why they fit.

> ✅ All characters in this project are from the **Tekken 8 roster**.  
> No legacy-only or non-Tekken-8 guests (e.g. Akuma) are used.

---

## 🗂 Project structure

```text
MokuMind-Tekken8-Agent/
├── src/
│   ├── mokumind.py        # Core recommendation logic
│   └── __init__.py
├── examples/
│   └── demo_usage.py      # Simple script to try the recommender
├── tests/
│   └── test_mokumind.py   # Basic tests
├── README.md
├── LICENSE
└── requirements.txt
