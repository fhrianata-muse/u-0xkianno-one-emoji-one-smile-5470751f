import os

EMOJI = "😄"

OUT = "/output/entry.txt"

if __name__ == "__main__":
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters (gate)"
    assert EMOJI.strip() != "", "entry must not be only whitespace (gate)"
    assert "\n" not in EMOJI and "\r" not in EMOJI, "entry must be one emoji, no line breaks"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)
