# src/main.py

import argparse
import json
import csv
import os
import sys
import time
import random
import string
from collections import Counter
from datetime import datetime

VERSION = "6.0.0"
HISTORY_FILE = "history.log"

ENGLISH_FREQ = {
    "e": 12.70, "t": 9.06, "a": 8.17, "o": 7.51, "i": 6.97, "n": 6.75,
    "s": 6.33, "h": 6.09, "r": 5.99, "d": 4.25, "l": 4.03, "c": 2.78,
    "u": 2.76, "m": 2.41, "w": 2.36, "f": 2.23, "g": 2.02, "y": 1.97,
    "p": 1.93, "b": 1.49, "v": 0.98, "k": 0.77, "j": 0.15, "x": 0.15,
    "q": 0.10, "z": 0.07
}


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log_event(action, text):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{now()} | {action} | {text[:150]}\n")


def shift_char(ch, shift):
    if "A" <= ch <= "Z":
        return chr((ord(ch) - 65 + shift) % 26 + 65)
    if "a" <= ch <= "z":
        return chr((ord(ch) - 97 + shift) % 26 + 97)
    return ch


def caesar(text, shift, decrypt=False):
    s = -shift if decrypt else shift
    return "".join(shift_char(c, s) for c in text)


def read_text(text=None, file=None):
    if file:
        with open(file, "r", encoding="utf-8") as f:
            return f.read()
    if text:
        return text
    if not sys.stdin.isatty():
        return sys.stdin.read()
    sys.exit("Provide text, --file or stdin.")


def write_text(text, output=None):
    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        print(text)


def letter_freq(text):
    letters = [c.lower() for c in text if c.isalpha()]
    total = len(letters)
    if total == 0:
        return {}
    counts = Counter(letters)
    return {k: counts[k] / total * 100 for k in counts}


def chi_square(freq):
    score = 0.0
    for ch, exp in ENGLISH_FREQ.items():
        obs = freq.get(ch, 0)
        score += ((obs - exp) ** 2) / exp
    return score


def crack(text):
    rows = []
    for shift in range(1, 26):
        plain = caesar(text, shift)
        score = chi_square(letter_freq(plain))
        rows.append((shift, score, plain))
    rows.sort(key=lambda x: x[1])
    return rows


def brute(text):
    return [(i, caesar(text, i)) for i in range(1, 26)]


def wheel(shift):
    abc = string.ascii_uppercase
    return abc, "".join(shift_char(c, shift) for c in abc)


def stats(text):
    freq = letter_freq(text)
    for ch in sorted(freq):
        bar = "█" * int(freq[ch] / 2)
        print(f"{ch}: {freq[ch]:5.2f}% {bar}")


def benchmark():
    sample = "Hello World " * 300000
    start = time.time()
    caesar(sample, 13)
    end = time.time()
    print("chars:", len(sample))
    print("seconds:", round(end - start, 4))


def random_text(size):
    chars = string.ascii_letters + string.digits + " .,!?-"
    return "".join(random.choice(chars) for _ in range(size))


def export_csv(rows, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["rank", "shift", "score", "text"])
        for i, row in enumerate(rows, 1):
            writer.writerow([i, row[0], row[1], row[2]])


def export_json(data):
    print(json.dumps(data, indent=2))


def show_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            print(f.read())


def interactive():
    while True:
        cmd = input("caesar> ").strip()
        if cmd in ("exit", "quit"):
            break
        parts = cmd.split()
        if len(parts) < 3:
            print("encrypt TEXT SHIFT")
            continue
        action = parts[0]
        text = parts[1]
        shift = int(parts[2])
        if action == "encrypt":
            print(caesar(text, shift))
        elif action == "decrypt":
            print(caesar(text, shift, True))


def self_test():
    assert caesar("Hello", 13) == "Uryyb"
    assert caesar("Uryyb", 13, True) == "Hello"
    assert caesar("ABC", 3) == "DEF"
    assert caesar("XYZ", 3) == "ABC"
    assert crack("Khoor")[0][2].lower().startswith("hello")
    print("tests passed")


def build_parser():
    parser = argparse.ArgumentParser(prog="caesar")
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name in ("encrypt", "decrypt"):
        p = sub.add_parser(name)
        p.add_argument("text", nargs="?")
        p.add_argument("--shift", type=int, default=13)
        p.add_argument("--file")
        p.add_argument("-o", "--output")
        p.add_argument("--json", action="store_true")

    p = sub.add_parser("crack")
    p.add_argument("text", nargs="?")
    p.add_argument("--file")
    p.add_argument("--top", type=int, default=5)
    p.add_argument("--csv")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("brute")
    p.add_argument("text", nargs="?")
    p.add_argument("--file")

    p = sub.add_parser("wheel")
    p.add_argument("--shift", type=int, default=13)

    p = sub.add_parser("stats")
    p.add_argument("text", nargs="?")
    p.add_argument("--file")

    p = sub.add_parser("random")
    p.add_argument("--size", type=int, default=100)

    sub.add_parser("bench")
    sub.add_parser("shell")
    sub.add_parser("tests")
    sub.add_parser("version")
    sub.add_parser("history")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.cmd == "encrypt":
        text = read_text(args.text, args.file)
        result = caesar(text, args.shift)
        log_event("encrypt", text)
        if args.json:
            export_json({"result": result})
        else:
            write_text(result, args.output)

    elif args.cmd == "decrypt":
        text = read_text(args.text, args.file)
        result = caesar(text, args.shift, True)
        log_event("decrypt", text)
        if args.json:
            export_json({"result": result})
        else:
            write_text(result, args.output)

    elif args.cmd == "crack":
        text = read_text(args.text, args.file)
        rows = crack(text)[:args.top]
        log_event("crack", text)

        if args.csv:
            export_csv(rows, args.csv)

        if args.json:
            export_json(
                [{"shift": r[0], "score": r[1], "text": r[2]} for r in rows]
            )
        else:
            for i, r in enumerate(rows, 1):
                print(f"{i}. shift={r[0]} score={r[1]:.2f} {r[2]}")

    elif args.cmd == "brute":
        text = read_text(args.text, args.file)
        for shift, value in brute(text):
            print(f"ROT-{shift:02}: {value}")

    elif args.cmd == "wheel":
        a, b = wheel(args.shift)
        print(a)
        print(b)

    elif args.cmd == "stats":
        stats(read_text(args.text, args.file))

    elif args.cmd == "random":
        print(random_text(args.size))

    elif args.cmd == "bench":
        benchmark()

    elif args.cmd == "shell":
        interactive()

    elif args.cmd == "tests":
        self_test()

    elif args.cmd == "version":
        print(VERSION)

    elif args.cmd == "history":
        show_history()


if __name__ == "__main__":
    main()