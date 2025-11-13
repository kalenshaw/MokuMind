from src.mokumind import recommend_characters

def test_recommend_returns_at_least_one():
    chars = recommend_characters(playstyle="rushdown")
    assert len(chars) >= 1

def test_only_known_names():
    chars = recommend_characters(playstyle="rushdown", top_k=10)
    names = {c.name for c in chars}
    # Add any character you defined in CHARACTERS here
    allowed = {
        "Jin Kazama", "Kazuya Mishima", "Lars Alexandersson", "Ling Xiaoyu",
        "King", "Paul Phoenix", "Hwoarang", "Asuka Kazama", "Lili",
        "Jun Kazama", "Nina Williams", "Bryan Fury", "Leo Kliesen",
        "Azucena", "Reina", "Victor Chevalier",
    }
    assert names.issubset(allowed)
