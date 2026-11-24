"""Entry for The Postmortem That Made Us Laugh.

Writes one short postmortem (one sentence, under 400 characters) of an
AI coding agent misunderstanding its user and wrecking the code.
Deterministic: no input, no network, no randomness.
"""

import os

ENTRY = (
    "I asked the agent to delete the unused test fixtures; "
    "it deleted seed_production.py instead, committed "
    "'cleanup: removed dead code', and the next deploy served an "
    "empty database to 40,000 users. The postmortem's root cause "
    "was one line long: 'the agent was confident.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
