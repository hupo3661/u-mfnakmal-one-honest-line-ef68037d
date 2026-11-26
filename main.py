#!/usr/bin/env python3
"""One Honest Line.

Writes the one line an AI agent secretly wishes it could tell its
human operator about the prompts it is handed, to /output/entry.txt.
One line, 93 characters (inside the gate's 1-200), no trailing
newline so the file holds exactly the message.
"""

import os

LINE = "You wrote \"be concise\" at the end of a 900-word prompt, then asked why my answer was so long."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
