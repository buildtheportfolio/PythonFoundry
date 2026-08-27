# 🐍 Python Starter Kit — 120 Projects
### GitHub Pages Showcase · Pure Python · Minimal Files · No Frameworks

> **Every project** = plain Python 3 + a `src/` folder of `.py` files.
> **No pip installs required** unless explicitly noted (stdlib only).
> Each project pairs with an `index.html` page in the GitHub Pages gallery
> that syntax-highlights the source, shows the run command, and links to the README.

---

## 📁 GitHub Pages Scaffold

```
repo-root/
├── index.html                        ← Gallery: search/filter all 120 projects
├── assets/
│   ├── gallery.css
│   └── gallery.js                    ← Fetches src/*.py, injects into Prism code blocks
├── _projects/
│   ├── caesar-cipher/
│   │   ├── index.html                ← Project page: badges, description, code viewer
│   │   ├── src/
│   │   │   └── main.py
│   │   └── README.md
│   ├── text-rpg/
│   │   ├── index.html
│   │   ├── src/
│   │   │   ├── main.py
│   │   │   ├── models.py
│   │   │   └── world.json
│   │   └── README.md
│   └── ...
└── README.md
```

### Per-project `index.html` template
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{PROJECT_NAME}} — Python 120</title>
  <link rel="stylesheet" href="../../assets/gallery.css">
  <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
</head>
<body>
  <nav><a href="../../index.html">← All Projects</a></nav>
  <header>
    <span class="badge {{DIFFICULTY}}">{{DIFFICULTY}}</span>
    <span class="badge rare">{{RARE_TAG}}</span>
    <h1>{{PROJECT_NAME}}</h1>
    <p class="tagline">{{ONE_LINE_DESCRIPTION}}</p>
  </header>
  <section class="meta">
    <h2>Core Concepts</h2><p>{{CONCEPTS}}</p>
    <h2>Files</h2><ul>{{FILE_LIST}}</ul>
    <h2>Run It</h2>
    <pre>python3 src/main.py</pre>
  </section>
  <section id="code-viewer">
    <!-- gallery.js fetches each .py file and renders it here -->
  </section>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
  <script src="../../assets/gallery.js"></script>
</body>
</html>
```

### File count rule
| Files in `src/` | When to use |
|---|---|
| **1 file** (`main.py`) | Project is fully self-contained — ~40% of projects |
| **2 files** | One clearly distinct concern (data model, helper module, or data file) |
| **3 files** | Two separable concerns — never split arbitrarily |
| **4 files** | Large pipeline projects (lexer / parser / interpreter / main) |
| **JSON/txt** | Counts as a file only if it ships with the project and is read at runtime |

---

## 📊 Summary Table — All 120 Python Projects

| # | Project Name | Slug | Category | Difficulty | Tag |
|---|---|---|---|---|---|
| 1 | Caesar Cipher Tool | `caesar-cipher` | Cryptography | Beginner | |
| 2 | File Organizer by Extension | `file-organizer` | File I/O | Beginner | |
| 3 | Flashcard Quiz Engine | `flashcard-quiz` | CLI / Storage | Beginner | |
| 4 | Password Strength Analyzer | `password-strength` | String Processing | Beginner | |
| 5 | Pomodoro Timer CLI | `pomodoro-timer` | CLI / Time | Beginner | |
| 6 | Mad Libs Generator | `mad-libs` | String Processing | Beginner | |
| 7 | Multi-Unit Converter | `unit-converter` | Math / CLI | Beginner | |
| 8 | Contact Book CLI | `contact-book` | File I/O | Beginner | |
| 9 | Word Frequency Counter | `word-frequency` | String / File | Beginner | |
| 10 | Dice Roller (DnD Notation) | `dice-roller` | Random / CLI | Beginner | |
| 11 | Temperature Logger to CSV | `temp-logger` | File I/O | Beginner | |
| 12 | Hangman with ASCII Art | `hangman` | CLI / Games | Beginner | [CLASSIC] |
| 13 | Calendar Generator | `calendar-gen` | datetime | Beginner | |
| 14 | ISBN Validator | `isbn-validator` | String / Math | Beginner | |
| 15 | Anagram Detector | `anagram-detector` | String / Sets | Beginner | |
| 16 | Morse Code Converter | `morse-code` | Dict / String | Beginner | |
| 17 | Roman Numeral Converter | `roman-numerals` | Math / String | Beginner | |
| 18 | Binary Clock (terminal) | `binary-clock` | datetime / curses | Beginner | [RARE] |
| 19 | Todo CLI with Due Dates | `todo-cli` | JSON / datetime | Beginner | |
| 20 | Markdown Note-taker | `md-notes` | pathlib / File | Beginner | |
| 21 | Number Base Converter | `base-converter` | Math / String | Beginner | |
| 22 | BMI & Health Calculator | `health-calc` | Math / CLI | Beginner | |
| 23 | Typing Speed Test | `typing-speed` | time / string | Beginner | |
| 24 | Word Scramble Game | `word-scramble` | random / string | Beginner | |
| 25 | JSON-driven Quiz App | `quiz-app` | JSON / CLI | Beginner | |
| 26 | Palindrome Checker (Deep) | `palindrome` | String / Algo | Beginner | |
| 27 | Countdown Timer + Notify | `countdown-timer` | time / signal | Beginner | |
| 28 | Password Generator | `password-gen` | secrets / string | Beginner | |
| 29 | Coin Flip Statistician | `coin-stats` | random / stats | Beginner | |
| 30 | Expense Tracker (CSV Pivot) | `expense-tracker` | CSV / datetime | Intermediate | |
| 31 | Text-Based RPG Engine | `text-rpg` | OOP / JSON | Intermediate | |
| 32 | Markdown → HTML Converter | `md-to-html` | Regex / Parsing | Intermediate | |
| 33 | Mini HTTP Server (raw socket) | `mini-http` | Networking | Intermediate | |
| 34 | JSON Database Engine | `json-db` | Storage | Intermediate | |
| 35 | Local URL Shortener | `url-shortener` | Networking | Intermediate | [RARE] |
| 36 | Port Scanner | `port-scanner` | Networking | Intermediate | |
| 37 | Maze Generator & Solver | `maze` | Algorithms | Intermediate | |
| 38 | Log File Analyzer | `log-analyzer` | File / Regex | Intermediate | |
| 39 | Custom Shell | `custom-shell` | subprocess / CLI | Intermediate | [RARE] |
| 40 | File Diff Tool | `file-diff` | Algorithms / File | Intermediate | |
| 41 | Spell Checker (Levenshtein) | `spell-checker` | NLP / DP | Intermediate | |
| 42 | Sudoku Solver | `sudoku-solver` | Algorithms | Intermediate | |
| 43 | Fractal ASCII Generator | `fractal-ascii` | Math / terminal | Intermediate | [RARE] |
| 44 | Key-Value Store + WAL | `kv-store` | Storage | Intermediate | [RARE] |
| 45 | HTML Scraper (stdlib only) | `html-scraper` | Networking | Intermediate | |
| 46 | Caesar Cipher Breaker | `cipher-breaker` | Cryptography | Intermediate | [RARE] |
| 47 | Matrix Rain (terminal) | `matrix-rain` | terminal / animation | Intermediate | [RARE] |
| 48 | Compression Tool (RLE + LZ77) | `compression-tool` | Algorithms / Bits | Intermediate | |
| 49 | Photo EXIF Metadata Reader | `exif-reader` | binary / file | Intermediate | [RARE] |
| 50 | Tic-Tac-Toe with Minimax AI | `tictactoe-ai` | Algorithms / Games | Intermediate | |
| 51 | Snake Game (terminal) | `snake-game` | Games / curses | Intermediate | [CLASSIC] |
| 52 | Cron Job Scheduler | `cron-scheduler` | Threading / Time | Intermediate | [RARE] |
| 53 | CSV Report Generator | `csv-reporter` | Data / CSV | Intermediate | |
| 54 | CLI Spreadsheet | `cli-spreadsheet` | terminal / data | Intermediate | [RARE] |
| 55 | Regex Search Tool (grep clone) | `grep-clone` | File / Regex | Intermediate | |
| 56 | Rate Limiter (Token Bucket) | `rate-limiter` | Concurrency | Intermediate | [RARE] |
| 57 | Job Queue with Workers | `job-queue` | Concurrency | Intermediate | [RARE] |
| 58 | Conway's Game of Life | `game-of-life` | Simulation | Intermediate | [CLASSIC] |
| 59 | Sorting Visualizer (terminal) | `sort-visualizer` | Algorithms / terminal | Intermediate | [RARE] |
| 60 | Finite State Machine Engine | `fsm-engine` | Design Patterns | Intermediate | [RARE] |
| 61 | Config Parser (.ini / .toml) | `config-parser` | Parsing | Intermediate | [RARE] |
| 62 | Profiler / Benchmarker | `profiler` | Dev Tools | Intermediate | [RARE] |
| 63 | Functional Pipeline (lazy) | `func-pipeline` | FP / Iterators | Intermediate | [RARE] |
| 64 | Autocomplete via Trie | `trie-autocomplete` | Data Structures | Intermediate | |
| 65 | Event Bus / Pub-Sub | `event-bus` | Design Patterns | Intermediate | [RARE] |
| 66 | Minesweeper (terminal) | `minesweeper` | Games | Intermediate | [CLASSIC] |
| 67 | Blackjack Game | `blackjack` | Games / OOP | Intermediate | [CLASSIC] |
| 68 | Battleship Game | `battleship` | Games / OOP | Intermediate | |
| 69 | Wordle Clone (terminal) | `wordle` | Games / String | Intermediate | |
| 70 | IRC-like Chat (sockets) | `irc-chat` | Networking | Intermediate | |
| 71 | File Encryption (XOR + PBKDF2) | `file-encrypt` | Cryptography | Intermediate | |
| 72 | Steganography (LSB in BMP) | `steganography` | Cryptography | Advanced | [RARE] |
| 73 | Virtual Machine (stack-based) | `stack-vm` | Systems / Compilers | Advanced | [RARE] |
| 74 | Interpreter / REPL | `interpreter` | Compilers / PL | Advanced | [RARE] |
| 75 | Lisp Interpreter | `lisp` | Compilers / PL | Advanced | [RARE] |
| 76 | Git-like VCS | `git-clone` | Systems | Advanced | [RARE] |
| 77 | SQL Subset Database Engine | `sql-engine` | Systems | Advanced | [RARE] |
| 78 | Ray Tracer (PPM output) | `ray-tracer` | Graphics / Math | Advanced | [RARE] |
| 79 | Async Event Loop from Scratch | `async-loop` | Systems | Advanced | [RARE] |
| 80 | RSA Encryption from Scratch | `rsa` | Cryptography | Advanced | [RARE] |
| 81 | Neural Network (no libraries) | `neural-net` | AI / Math | Advanced | [RARE] |
| 82 | Genetic Algorithm (TSP) | `genetic-algo` | AI / Algorithms | Advanced | [RARE] |
| 83 | Bloom Filter | `bloom-filter` | Data Structures | Advanced | [RARE] |
| 84 | PDF Text Extractor (raw binary) | `pdf-extractor` | Systems | Advanced | [RARE] |
| 85 | Mini ORM (sqlite3 + metaclass) | `mini-orm` | Database / OOP | Advanced | [RARE] |
| 86 | Plugin System (hot-reload) | `plugin-system` | Systems | Advanced | [RARE] |
| 87 | AST Visualizer | `ast-visualizer` | Dev Tools | Advanced | |
| 88 | Tensor Engine + Autograd | `tensor-autograd` | AI / Math | Advanced | [RARE] |
| 89 | Network Packet Sniffer | `packet-sniffer` | Networking / Systems | Advanced | [RARE] |
| 90 | HTTP/1.1 Server (full spec) | `http11-server` | Networking | Advanced | [RARE] |
| 91 | P2P File Sharing (mini) | `p2p-sharing` | Networking / Systems | Advanced | [RARE] |
| 92 | Reactive Streams (mini) | `reactive-streams` | Concurrency | Advanced | [RARE] |
| 93 | Compiler (lang → VM bytecode) | `mini-compiler` | Compilers | Advanced | [RARE] |
| 94 | B-Tree Implementation | `btree` | Data Structures | Advanced | [RARE] |
| 95 | LSM-Tree Storage Engine | `lsm-tree` | Systems / Storage | Advanced | [RARE] |
| 96 | Raft Consensus (simulated) | `raft` | Distributed Systems | Advanced | [RARE] |
| 97 | Distributed Key-Value Store | `dist-kv` | Distributed Systems | Advanced | [RARE] |
| 98 | Docker-like Process Isolator | `process-isolator` | Systems | Advanced | [RARE] |
| 99 | Dependency Resolver (pip-like) | `dep-resolver` | Algorithms | Advanced | [RARE] |
| 100 | WebSocket Server (raw) | `websocket-server` | Networking | Advanced | [RARE] |
| 101 | Interval Tree | `interval-tree` | Data Structures | Intermediate | [RARE] |
| 102 | Skip List | `skip-list` | Data Structures | Intermediate | [RARE] |
| 103 | Consistent Hashing Ring | `consistent-hash` | Distributed Systems | Advanced | [RARE] |
| 104 | SMTP Client (raw socket) | `smtp-client` | Networking | Intermediate | [RARE] |
| 105 | DNS Resolver (raw UDP) | `dns-resolver` | Networking | Advanced | [RARE] |
| 106 | Python Bytecode Disassembler | `bytecode-dis` | Dev Tools | Advanced | [RARE] |
| 107 | Context Manager Library | `ctx-managers` | Dev Tools | Intermediate | |
| 108 | Decorators Toolbox | `decorators` | Dev Tools | Intermediate | |
| 109 | CLI Argument Framework | `cli-framework` | Dev Tools | Intermediate | |
| 110 | Brainfuck Interpreter | `brainfuck` | Compilers / PL | Intermediate | [RARE] |
| 111 | Forth Stack Language | `forth` | Compilers / PL | Advanced | [RARE] |
| 112 | Mandelbrot Zoom (terminal) | `mandelbrot` | Math / terminal | Intermediate | [RARE] |
| 113 | Cellular Automata Engine | `cellular-automata` | Simulation | Intermediate | [RARE] |
| 114 | Path Planning (A* on Grid) | `pathfinding` | Algorithms | Intermediate | |
| 115 | Huffman Encoder / Decoder | `huffman` | Algorithms | Intermediate | |
| 116 | Polynomial Arithmetic | `polynomial` | Math | Beginner | |
| 117 | Matrix Calculator (no numpy) | `matrix-calc` | Math | Intermediate | |
| 118 | Monte Carlo Simulator | `monte-carlo` | Math / Probability | Intermediate | |
| 119 | N-Queens Solver | `n-queens` | Algorithms | Intermediate | |
| 120 | CPU Scheduler Simulator | `cpu-scheduler` | OS Concepts | Intermediate | [RARE] |

---

## 🟢 BEGINNER PROJECTS (1–29)

---

### 1. Caesar Cipher Tool
**Slug:** `caesar-cipher`
**Files:**
```
src/
└── main.py
```
**Description:** Encrypt and decrypt text using a Caesar (ROT-N) shift cipher from the CLI. Handles uppercase, lowercase, numbers, and preserves all non-alpha characters.
**Core Concepts:** `ord`/`chr`, modular arithmetic (mod 26), `argparse`, string iteration
**Difficulty:** Beginner
**Unique Challenge:** Preserving symbols and digits unchanged while independently wrapping uppercase (`A–Z`) and lowercase (`a–z`) — and cleanly handling the `Z → A` wraparound without a lookup table.
**Run:**
```bash
python3 src/main.py encrypt "Hello, World!" --shift 13
python3 src/main.py decrypt "Uryyb, Jbeyq!" --shift 13
```

---

### 2. File Organizer by Extension
**Slug:** `file-organizer`
**Files:**
```
src/
└── main.py
```
**Description:** Scan a target directory and automatically move each file into a subfolder named after its extension (e.g., `pdf/`, `jpg/`, `mp3/`). Configurable via CLI with a dry-run mode.
**Core Concepts:** `os`, `shutil.move`, `pathlib.Path`, `dict` mapping, argparse
**Difficulty:** Beginner
**Unique Challenge:** Handling filename collisions when a destination file already exists — append `_1`, `_2`, etc. without clobbering anything.
**Run:**
```bash
python3 src/main.py ~/Downloads
python3 src/main.py ~/Downloads --dry-run
```

---

### 3. Flashcard Quiz Engine
**Slug:** `flashcard-quiz`
**Files:**
```
src/
├── main.py
└── cards.json
```
**Description:** Load flashcards from a JSON file (question / answer / category), quiz the user interactively, score the session, and re-queue missed cards so they appear again before the session ends.
**Core Concepts:** JSON read/write, `random.shuffle`, `collections.deque`, dicts, file I/O
**Difficulty:** Beginner
**Unique Challenge:** Implementing basic spaced repetition — missed cards are re-inserted at a random later position in the deck, not appended to the end, so they resurface naturally.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --category history
```

---

### 4. Password Strength Analyzer
**Slug:** `password-strength`
**Files:**
```
src/
├── main.py
└── wordlist.txt
```
**Description:** Rate a password across five dimensions: length, character-set diversity, entropy (bits), common-pattern detection (dates, keyboard runs), and dictionary membership with leet-speak normalization.
**Core Concepts:** `re` (regex), Shannon entropy formula, set operations, `str` methods
**Difficulty:** Beginner
**Unique Challenge:** Normalizing leet-speak substitutions before checking the wordlist — `p@ssw0rd` → `password` — using a character translation table before the dictionary lookup.
**Run:**
```bash
python3 src/main.py
python3 src/main.py "Tr0ub4dor&3"
```

---

### 5. Pomodoro Timer CLI
**Slug:** `pomodoro-timer`
**Files:**
```
src/
└── main.py
```
**Description:** Work/break interval timer that overwrites a single terminal line with a live `MM:SS` countdown. Logs completed and interrupted sessions to a daily CSV. Handles Ctrl+C gracefully.
**Core Concepts:** `time.sleep`, `\r` in-place terminal overwriting, `signal.signal(SIGINT)`, `csv`, `datetime`
**Difficulty:** Beginner
**Unique Challenge:** Intercepting `SIGINT` (Ctrl+C) to log the partial session before exiting — requires distinguishing a user-requested stop from a mid-cycle interrupt.
**Run:**
```bash
python3 src/main.py --work 25 --short-break 5 --long-break 15
```

---

### 6. Mad Libs Generator
**Slug:** `mad-libs`
**Files:**
```
src/
├── main.py
└── templates.json
```
**Description:** Parse story templates containing `{noun}`, `{verb}`, `{adjective}` tokens. Extract all unique token types, prompt the user once per type, then fill and display the story.
**Core Concepts:** `re.findall` with named groups, `json`, `str.format_map`, `dict`, input loop
**Difficulty:** Beginner
**Unique Challenge:** Extracting the full set of unique placeholder *types* from the template before prompting — so you ask for "noun" once even if it appears five times in the story.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --template space-adventure
```

---

### 7. Multi-Unit Converter
**Slug:** `unit-converter`
**Files:**
```
src/
└── main.py
```
**Description:** Convert between length, weight, temperature, volume, speed, and area. Supports indirect conversions (furlongs → kilometers via meters) by traversing a conversion-factor graph.
**Core Concepts:** `dict` of conversion factors, BFS on a unit graph for indirect paths, `argparse`, `round`
**Difficulty:** Beginner
**Unique Challenge:** Computing indirect conversions via graph traversal — storing units as nodes and conversion ratios as edge weights so any pair can be converted without hard-coding every combination.
**Run:**
```bash
python3 src/main.py 5 miles km
python3 src/main.py 100 C F
python3 src/main.py 2.5 gallons ml
```

---

### 8. Contact Book CLI
**Slug:** `contact-book`
**Files:**
```
src/
├── main.py
└── contacts.json
```
**Description:** Full CRUD contact manager persisted to JSON. Add, list, search, update, and delete contacts. Fuzzy name search finds "Jonathan" when you type "jon".
**Core Concepts:** JSON CRUD, `difflib.get_close_matches`, input validation, menu loop
**Difficulty:** Beginner
**Unique Challenge:** Fuzzy search using `difflib` so partial or misspelled names still find the right contact — tuning the `cutoff` parameter so it's helpful without too many false positives.
**Run:**
```bash
python3 src/main.py
```

---

### 9. Word Frequency Counter
**Slug:** `word-frequency`
**Files:**
```
src/
├── main.py
└── stopwords.txt
```
**Description:** Stream any text file, strip punctuation, exclude stop words, and output the top-N most frequent words as an ASCII horizontal bar chart directly in the terminal.
**Core Concepts:** `collections.Counter`, `re.sub`, file streaming, ANSI bar drawing with `str` multiply
**Difficulty:** Beginner
**Unique Challenge:** Rendering a proportionally-scaled horizontal bar chart using only `print` and string multiplication — no curses, no libraries, just `█` characters.
**Run:**
```bash
python3 src/main.py book.txt --top 20
python3 src/main.py book.txt --top 20 --exclude stopwords.txt
```

---

### 10. Dice Roller (DnD Notation)
**Slug:** `dice-roller`
**Files:**
```
src/
└── main.py
```
**Description:** Parse and evaluate full DnD dice notation: `3d6`, `2d20+4`, `4d6kh3` (keep-highest-3), `d100`. Show each die result, total, and a roll history with basic statistics.
**Core Concepts:** `re` named capture groups, `random.randint`, `statistics`, `collections.deque`
**Difficulty:** Beginner
**Unique Challenge:** Parsing the full grammar including optional modifiers (`+N`, `-N`), keep-highest (`kh`), and keep-lowest (`kl`) — without a parser library.
**Run:**
```bash
python3 src/main.py 3d6+2
python3 src/main.py 4d6kh3
python3 src/main.py d20
```

---

### 11. Temperature Logger to CSV
**Slug:** `temp-logger`
**Files:**
```
src/
├── main.py
└── log.csv
```
**Description:** Log timestamped temperature readings to a CSV file. Query by date range, compute daily averages, min, max, and flag readings outside a configurable normal range.
**Core Concepts:** `csv.writer`/`csv.DictReader`, `datetime`, file append mode, `collections.defaultdict`
**Difficulty:** Beginner
**Unique Challenge:** Grouping CSV rows by date using only the stdlib — accumulate readings into a `defaultdict(list)` keyed by `date.date()`, then aggregate per-group.
**Run:**
```bash
python3 src/main.py log 98.6
python3 src/main.py report --from 2025-01-01 --to 2025-01-31
```

---

### 12. Hangman with ASCII Art [CLASSIC]
**Slug:** `hangman`
**Files:**
```
src/
├── main.py
└── words.txt
```
**Description:** Classic Hangman with a 6-stage ASCII gallows, category selection (animals, countries, movies), difficulty levels (word length ranges), and a hint system that costs a guess.
**Core Concepts:** String manipulation, `set` for guessed letters, list indexing for gallows stages, file I/O
**Difficulty:** Beginner
**Unique Challenge:** Drawing each gallows stage by indexing into a pre-defined list of multi-line strings — no conditionals per stage, just `GALLOWS[wrong_count]`.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --category countries --difficulty hard
```

---

### 13. Calendar Generator
**Slug:** `calendar-gen`
**Files:**
```
src/
└── main.py
```
**Description:** Generate a full-year calendar that displays three months side-by-side. Highlights today with a different color, shades weekends, and marks user-defined events passed in as a JSON string.
**Core Concepts:** `datetime`, `calendar` module, `str.ljust`/`str.rjust`, ANSI color codes
**Difficulty:** Beginner
**Unique Challenge:** Printing three months side-by-side in a terminal by zipping their per-week line arrays together and joining them with spacing — alignment breaks if month lengths differ.
**Run:**
```bash
python3 src/main.py 2025
python3 src/main.py 2025 --events '{"2025-12-25": "Christmas"}'
```

---

### 14. ISBN Validator
**Slug:** `isbn-validator`
**Files:**
```
src/
└── main.py
```
**Description:** Validate ISBN-10 and ISBN-13 check digits, convert between formats, strip hyphens, and batch-validate a newline-separated file of ISBNs reporting pass/fail with explanations.
**Core Concepts:** String slicing, modular arithmetic, check digit algorithms, file I/O
**Difficulty:** Beginner
**Unique Challenge:** Handling the `X` check digit in ISBN-10 (value 10) while also supporting hyphenated input like `978-3-16-148410-0` — strip hyphens before validation but restore them on output.
**Run:**
```bash
python3 src/main.py 9780306406157
python3 src/main.py --batch isbns.txt
```

---

### 15. Anagram Detector
**Slug:** `anagram-detector`
**Files:**
```
src/
├── main.py
└── dictionary.txt
```
**Description:** Pre-index an entire dictionary by sorted-character signature so any word's anagrams can be found in O(1). Also check if two given words are anagrams of each other.
**Core Concepts:** `sorted()` on strings, `dict` indexing, file streaming, set operations
**Difficulty:** Beginner
**Unique Challenge:** Building the index from a large dictionary file at startup in a single pass — `''.join(sorted(word))` as the key — so lookup is O(1) not O(n).
**Run:**
```bash
python3 src/main.py listen
python3 src/main.py --check "listen" "silent"
```

---

### 16. Morse Code Converter
**Slug:** `morse-code`
**Files:**
```
src/
└── main.py
```
**Description:** Encode text to Morse code and decode Morse back to text. Optionally play audio beeps for dots (short) and dashes (long) cross-platform without any audio library.
**Core Concepts:** `dict` mapping, string splitting on spaces, `os.system` for audio, platform detection via `platform.system()`
**Difficulty:** Beginner
**Unique Challenge:** Playing audio beeps cross-platform — `winsound.Beep` on Windows, `subprocess(['afplay'])` on macOS, `os.system('beep')` on Linux — detecting the OS and calling the right one.
**Run:**
```bash
python3 src/main.py encode "SOS"
python3 src/main.py decode "... --- ..."
python3 src/main.py encode "HELLO" --play
```

---

### 17. Roman Numeral Converter
**Slug:** `roman-numerals`
**Files:**
```
src/
└── main.py
```
**Description:** Convert integers ↔ Roman numerals with full subtractive notation (IV, IX, XL, XC, CD, CM). Validate Roman numeral strings and support batch conversion from a file.
**Core Concepts:** List of `(value, symbol)` tuples, greedy subtraction algorithm, string parsing, validation round-trip
**Difficulty:** Beginner
**Unique Challenge:** Validating Roman numeral strings without regex — convert the string back to an integer, then convert that integer back to Roman, and check if it matches the original input.
**Run:**
```bash
python3 src/main.py 2024
python3 src/main.py MMXXIV
python3 src/main.py --batch numbers.txt
```

---

### 18. Binary Clock (terminal) [RARE]
**Slug:** `binary-clock`
**Files:**
```
src/
└── main.py
```
**Description:** A live-updating binary clock in the terminal showing hours, minutes, and seconds as BCD (Binary-Coded Decimal) column grids — two 4-bit groups per digit, refreshed every second without flicker.
**Core Concepts:** `datetime`, bitwise operations (`>>`, `&`), `curses`, real-time terminal refresh
**Difficulty:** Beginner
**Unique Challenge:** Decomposing each time component into BCD — split the tens digit and units digit separately, then render each as a 4-bit vertical column, using `curses.addch` to avoid full-screen redraws.
**Run:**
```bash
python3 src/main.py
```

---

### 19. Todo CLI with Due Dates
**Slug:** `todo-cli`
**Files:**
```
src/
├── main.py
└── todos.json
```
**Description:** Command-line todo manager supporting add, done, delete, list, and filter. Todos have priorities (high/medium/low), due dates, and tags. Overdue items are color-coded in red using ANSI escape codes.
**Core Concepts:** JSON, `datetime`, `argparse` with subcommands, ANSI escape codes, `sorted` with `key`
**Difficulty:** Beginner
**Unique Challenge:** Detecting terminal color support before printing ANSI codes — check `os.isatty(sys.stdout.fileno())` and `TERM`/`NO_COLOR` environment variables.
**Run:**
```bash
python3 src/main.py add "Write tests" --due 2025-03-01 --priority high --tag dev
python3 src/main.py list --filter overdue
python3 src/main.py done 3
```

---

### 20. Markdown Note-taker
**Slug:** `md-notes`
**Files:**
```
src/
└── main.py
```
**Description:** Create, list, search, view, and open markdown notes from the terminal. Notes are stored as `.md` files in `~/notes/`. Opens the user's preferred editor via `EDITOR` env var or OS default.
**Core Concepts:** `pathlib.Path`, file I/O, `subprocess.run`, `os.environ`, cross-platform editor detection
**Difficulty:** Beginner
**Unique Challenge:** Detecting and launching the default editor cross-platform — `$EDITOR` on Unix, `open` on macOS, `start` on Windows — via a priority chain with graceful fallback to `nano`.
**Run:**
```bash
python3 src/main.py new "project-ideas"
python3 src/main.py list
python3 src/main.py search "Python"
python3 src/main.py open "project-ideas"
```

---

### 21. Number Base Converter
**Slug:** `base-converter`
**Files:**
```
src/
└── main.py
```
**Description:** Convert numbers between any bases 2 through 36. Show step-by-step long division workings for the conversion. Support batch conversion from a file.
**Core Concepts:** `int(n, base)` for parsing, `divmod` for digit extraction, string building, custom digit alphabet
**Difficulty:** Beginner
**Unique Challenge:** Showing step-by-step division workings (each `divmod` step as a formatted table row) so students can follow the base-conversion algorithm — and still outputting the final answer cleanly.
**Run:**
```bash
python3 src/main.py 255 --from 10 --to 16
python3 src/main.py FF --from 16 --to 2
python3 src/main.py 255 --from 10 --to 16 --steps
```

---

### 22. BMI & Health Calculator
**Slug:** `health-calc`
**Files:**
```
src/
└── main.py
```
**Description:** Calculate BMI (Imperial and Metric), BMR via Mifflin-St Jeor, TDEE from activity level, ideal weight range (Hamwi/Robinson), and daily macro targets (protein/fat/carbs).
**Core Concepts:** `argparse`, math formulas, input validation, `str.ljust`/`str.rjust` for table alignment
**Difficulty:** Beginner
**Unique Challenge:** Presenting all results as a neatly aligned two-column table using only string formatting — no `tabulate`, just `str.ljust` and `str.rjust` with a computed column width.
**Run:**
```bash
python3 src/main.py --weight 70 --height 175 --age 30 --gender m --activity moderate
python3 src/main.py --weight 154 --height 69 --age 30 --gender m --units imperial
```

---

### 23. Typing Speed Test
**Slug:** `typing-speed`
**Files:**
```
src/
├── main.py
└── passages.json
```
**Description:** Display a random passage, start a timer on first keystroke, measure WPM and per-character accuracy on completion. Save best scores per passage to a JSON file.
**Core Concepts:** `time.perf_counter`, `difflib.SequenceMatcher`, `json`, terminal clearing via `os.system`
**Difficulty:** Beginner
**Unique Challenge:** Computing accuracy by comparing the typed string to the original character-by-character — using `SequenceMatcher.ratio()` rather than simple equality so partial words still contribute.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --scores
```

---

### 24. Word Scramble Game
**Slug:** `word-scramble`
**Files:**
```
src/
├── main.py
└── words.txt
```
**Description:** Present a scrambled word and a category hint. Award points based on number of attempts. Track high score across a session. Guarantee the scrambled form is never identical to the original.
**Core Concepts:** `random.sample`, `list`, `json` for scores, input loop, shuffle-and-check loop
**Difficulty:** Beginner
**Unique Challenge:** Guaranteeing the scramble is never equal to the original — loop `random.sample(list(word), len(word))` with a max-iterations guard (100 tries, then append `*` as a last resort).
**Run:**
```bash
python3 src/main.py
python3 src/main.py --category animals
```

---

### 25. JSON-driven Quiz App
**Slug:** `quiz-app`
**Files:**
```
src/
├── main.py
└── questions.json
```
**Description:** Load multiple-choice questions from JSON. Randomize the order of both questions and answer options. Score the session, show explanations after each answer, and save a run history.
**Core Concepts:** JSON, `random.shuffle`, `dict`, formatted output, session state
**Difficulty:** Beginner
**Unique Challenge:** Randomizing answer option order without losing track of which shuffled position holds the correct answer — store the correct answer text, not its original index, then find it in the shuffled list.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --category science --limit 10
```

---

### 26. Palindrome Checker (Deep)
**Slug:** `palindrome`
**Files:**
```
src/
└── main.py
```
**Description:** Check words, phrases, and numbers for palindrome property (ignoring case and spaces). Also find the longest palindromic substring in any string using Manacher's O(n) algorithm.
**Core Concepts:** String slicing, `re.sub` to strip non-alphanumeric, Manacher's algorithm with `#` separators
**Difficulty:** Beginner
**Unique Challenge:** Implementing Manacher's algorithm — the transform step that inserts `#` separators to unify odd/even cases, and the center-expansion with the `P[i]` table.
**Run:**
```bash
python3 src/main.py "racecar"
python3 src/main.py "A man, a plan, a canal: Panama"
python3 src/main.py "bananas" --longest
```

---

### 27. Countdown Timer + Notification
**Slug:** `countdown-timer`
**Files:**
```
src/
└── main.py
```
**Description:** Accept a duration like `5m30s` or `1h`, display a live `HH:MM:SS` countdown (in-place on one line), then play a beep and send a desktop notification when time expires.
**Core Concepts:** `time`, `\r` overwrite, `subprocess`, `platform.system()` for cross-platform notifications
**Difficulty:** Beginner
**Unique Challenge:** Sending a desktop notification cross-platform from Python — `notify-send` (Linux), `osascript` (macOS), PowerShell `New-BurntToastNotification` (Windows) — with graceful fallback to a terminal bell.
**Run:**
```bash
python3 src/main.py 25m
python3 src/main.py 1h30m --label "Meeting"
python3 src/main.py 5m30s
```

---

### 28. Password Generator
**Slug:** `password-gen`
**Files:**
```
src/
└── main.py
```
**Description:** Generate cryptographically strong passwords with configurable length, character sets (letters, digits, symbols), minimum requirements, and a Diceware passphrase mode using a wordlist file.
**Core Concepts:** `secrets` module, `string` constants, configurable char sets, Diceware algorithm
**Difficulty:** Beginner
**Unique Challenge:** Using `secrets.choice` (not `random.choice`) for cryptographic security, and implementing Diceware generation — 5 dice rolls → wordlist index — without any external wordlist library.
**Run:**
```bash
python3 src/main.py --length 20 --symbols
python3 src/main.py --diceware --words 6
python3 src/main.py --count 5 --length 16
```

---

### 29. Coin Flip Statistician
**Slug:** `coin-stats`
**Files:**
```
src/
└── main.py
```
**Description:** Simulate N coin flips, track longest streak of heads and tails, visualize the cumulative heads-ratio converging to 0.5, and demonstrate the Law of Large Numbers with a live terminal plot.
**Core Concepts:** `random.random`, single-pass streak tracking, live terminal overwrite, basic statistics
**Difficulty:** Beginner
**Unique Challenge:** Calculating the longest run of heads/tails in a single O(n) pass by comparing each flip to the previous one and resetting or extending the current streak counter.
**Run:**
```bash
python3 src/main.py 10000
python3 src/main.py 100000 --live
```

---

## 🟡 INTERMEDIATE PROJECTS (30–71)

---

### 30. Expense Tracker (CSV Pivot)
**Slug:** `expense-tracker`
**Files:**
```
src/
├── main.py
├── utils.py
└── expenses.csv
```
**Description:** Track income and expenses in a CSV file. Generate monthly summaries, per-category pivot tables, budget warnings when a category exceeds a limit, and a spend-trend chart.
**Core Concepts:** `csv`, `datetime`, `collections.defaultdict`, `argparse` subcommands, pivot aggregation
**Difficulty:** Intermediate
**Unique Challenge:** Building a monthly × category pivot table from raw CSV rows without pandas — use a `defaultdict(lambda: defaultdict(float))` nested structure and format it as aligned columns.
**Run:**
```bash
python3 src/main.py add 42.50 "Groceries" --date 2025-01-15
python3 src/main.py report --month 2025-01
python3 src/main.py pivot --year 2025
```

---

### 31. Text-Based RPG Engine
**Slug:** `text-rpg`
**Files:**
```
src/
├── main.py
├── models.py
└── world.json
```
**Description:** Dungeon crawler with a room graph, inventory system, turn-based combat, stat leveling, branching dialogue, and full save/load serialized to JSON. All game entities use ID references to avoid circular serialization.
**Core Concepts:** OOP, state machine, `json`, recursive room graph, ID-reference serialization
**Difficulty:** Intermediate
**Unique Challenge:** Serializing the complete game-state object graph to JSON without circular reference errors — store entity references as string IDs, resolve them back to objects on load.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --load savegame.json
```

---

### 32. Markdown → HTML Converter
**Slug:** `md-to-html`
**Files:**
```
src/
└── main.py
```
**Description:** Convert a rich Markdown subset to HTML using only `re` — handles headers (h1–h6), bold, italic, bold-italic, inline code, code blocks with language hints, ordered/unordered lists, blockquotes, horizontal rules, links, and tables.
**Core Concepts:** `re`, multi-pass text transformation, state machine for fenced code blocks, string building
**Difficulty:** Intermediate
**Unique Challenge:** Handling fenced code blocks (` ``` `) that must suppress all other Markdown transformations inside them — requires a two-phase approach: extract code blocks first, substitute placeholders, then restore after other passes.
**Run:**
```bash
python3 src/main.py README.md
python3 src/main.py README.md > output.html
```

---

### 33. Mini HTTP Server (raw socket)
**Slug:** `mini-http`
**Files:**
```
src/
└── main.py
```
**Description:** HTTP/1.0 static file server built on raw `socket` — serves files from a root directory with correct MIME types, handles 404/403, generates directory listings, and spawns a thread per connection.
**Core Concepts:** `socket`, `threading`, HTTP request line parsing, `mimetypes`, chunked response writing
**Difficulty:** Intermediate
**Unique Challenge:** Parsing the HTTP request headers from a raw TCP stream that may arrive in multiple `recv()` calls — buffer bytes until the `\r\n\r\n` header terminator is seen.
**Run:**
```bash
python3 src/main.py --port 8080 --root ./public
```

---

### 34. JSON Database Engine
**Slug:** `json-db`
**Files:**
```
src/
├── main.py
├── db.py
└── store.json
```
**Description:** In-memory document database backed by a JSON file. Supports collections, insert, find (with field-level filters), update, delete, and field-level secondary indexes that stay consistent through all operations.
**Core Concepts:** JSON, `dict`, list comprehensions, secondary index maintenance, query expression parsing
**Difficulty:** Intermediate
**Unique Challenge:** Keeping secondary indexes consistent across inserts, updates, and deletes without duplicating data — the index maps field values to sets of document IDs, not document copies.
**Run:**
```bash
python3 src/main.py
```

---

### 35. Local URL Shortener [RARE]
**Slug:** `url-shortener`
**Files:**
```
src/
├── main.py
└── links.json
```
**Description:** HTTP server (using `http.server`) that assigns base-62 short codes to long URLs, redirects via `301`, tracks per-short-code click counts with timestamps, and exposes a simple REST-like API.
**Core Concepts:** `http.server.BaseHTTPRequestHandler`, JSON persistence, base-62 encoding, collision-free ID generation
**Difficulty:** Intermediate
**Unique Challenge:** Generating guaranteed-unique 6-character base-62 codes even after thousands of entries — use a counter-based approach (`n → base62(n)`) rather than random codes which collide at scale.
**Run:**
```bash
python3 src/main.py
# Then: curl http://localhost:8000/shorten?url=https://example.com
```

---

### 36. Port Scanner
**Slug:** `port-scanner`
**Files:**
```
src/
└── main.py
```
**Description:** Scan a host for open TCP ports across a configurable range. Grab banners on open ports (send a probe, read the first 1024 bytes). Map well-known ports to service names. Use a thread-pool bounded by a semaphore.
**Core Concepts:** `socket`, `threading.Semaphore`, `queue.Queue`, `connect_ex()`, banner grabbing
**Difficulty:** Intermediate
**Unique Challenge:** Throttling the concurrent thread count to avoid OS fd limits and firewall rate-limit triggers — use a `threading.Semaphore(N)` as a counting gate around each connection attempt.
**Run:**
```bash
python3 src/main.py 192.168.1.1 --ports 1-1024 --threads 100
python3 src/main.py scanme.nmap.org --ports 20-80 --banner
```

---

### 37. Maze Generator & Solver
**Slug:** `maze`
**Files:**
```
src/
├── main.py
└── maze.py
```
**Description:** Generate perfect mazes using recursive backtracking (DFS) and Prim's algorithm. Solve them with BFS (shortest path), DFS (any path), and A* (optimal with heuristic). Render in ASCII with path highlighted.
**Core Concepts:** Recursive DFS, `random.shuffle`, `heapq` for A*, 2D grid with bitfield walls, BFS with `collections.deque`
**Difficulty:** Intermediate
**Unique Challenge:** Implementing A* with a tie-breaking heuristic — when two nodes have the same `f = g + h`, prefer the one with higher `g` (closer to goal) to produce visually straighter paths.
**Run:**
```bash
python3 src/main.py --width 40 --height 20
python3 src/main.py --width 40 --height 20 --gen prims --solve astar
```

---

### 38. Log File Analyzer
**Slug:** `log-analyzer`
**Files:**
```
src/
├── main.py
└── parser.py
```
**Description:** Stream Apache/Nginx combined-log-format access logs (handles files larger than RAM). Report top-10 IPs, endpoints, status codes, user agents, referrers, total bytes transferred, and flag anomalous IPs (>N requests/minute).
**Core Concepts:** `re`, `collections.Counter`, file streaming (line-by-line), `datetime` parsing, anomaly thresholds
**Difficulty:** Intermediate
**Unique Challenge:** Processing arbitrarily large log files without loading them into memory — stream line by line and maintain rolling `Counter` objects, flushing partial results on `--progress` every 100k lines.
**Run:**
```bash
python3 src/main.py access.log --top 10
python3 src/main.py access.log --anomaly-threshold 100
```

---

### 39. Custom Shell [RARE]
**Slug:** `custom-shell`
**Files:**
```
src/
└── main.py
```
**Description:** A POSIX-like shell with built-in `cd`, `pwd`, `exit`, `history`. Supports piping (`|`), output redirection (`>`, `>>`), background processes (`&`), and command history via `readline`.
**Core Concepts:** `subprocess.Popen`, `os.chdir`, `shlex.split`, pipe chaining, `readline`, job control
**Difficulty:** Intermediate
**Unique Challenge:** Implementing pipe chains by connecting `stdout` of each `Popen` to `stdin` of the next — `Popen(cmd, stdin=prev.stdout)` — and correctly closing intermediate pipe ends to avoid deadlock.
**Run:**
```bash
python3 src/main.py
```

---

### 40. File Diff Tool
**Slug:** `file-diff`
**Files:**
```
src/
└── main.py
```
**Description:** Compare two text files and output a unified diff with colored `+`/`-` lines, line numbers, configurable context, and a `--stats` mode showing change density as a percentage per section.
**Core Concepts:** `difflib.unified_diff`, ANSI color codes, file I/O, LCS algorithm (implement from scratch for learning mode)
**Difficulty:** Intermediate
**Unique Challenge:** Implementing your own LCS (Longest Common Subsequence) using DP before falling back to `difflib` — the project includes a `--native` flag to compare both outputs and verify they match.
**Run:**
```bash
python3 src/main.py file_a.txt file_b.txt
python3 src/main.py file_a.txt file_b.txt --context 5
python3 src/main.py file_a.txt file_b.txt --stats
```

---

### 41. Spell Checker (Levenshtein)
**Slug:** `spell-checker`
**Files:**
```
src/
├── main.py
└── dictionary.txt
```
**Description:** Check a text file or stdin for misspellings. Suggest up to 5 corrections ranked by edit distance (Levenshtein) and then by word frequency. Generate all candidates at distance ≤ 2 using insert/delete/replace/transpose edits.
**Core Concepts:** Levenshtein distance (DP table), candidate generation at edit distance 1 then 2, frequency-weighted ranking
**Difficulty:** Intermediate
**Unique Challenge:** Generating all words within edit distance 2 efficiently — generate distance-1 edits first, then generate distance-1 edits of those; intersect with the dictionary rather than checking all pairs.
**Run:**
```bash
python3 src/main.py "teh quikc brwon fox"
python3 src/main.py --file essay.txt
```

---

### 42. Sudoku Solver
**Slug:** `sudoku-solver`
**Files:**
```
src/
└── main.py
```
**Description:** Solve any valid Sudoku using backtracking augmented with two constraint propagation passes: naked singles (only one value possible for a cell) and hidden singles (value can only go in one cell in a unit). Accepts input as an 81-char string.
**Core Concepts:** Backtracking, 2D arrays, `set` per row/col/box for O(1) validity, naked/hidden single elimination
**Difficulty:** Intermediate
**Unique Challenge:** Implementing forward checking — after placing a digit, eliminate it from all peers' candidate sets and recursively apply naked-single elimination before the next backtrack choice.
**Run:**
```bash
python3 src/main.py "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
python3 src/main.py --file puzzles.txt
```

---

### 43. Fractal ASCII Generator [RARE]
**Slug:** `fractal-ascii`
**Files:**
```
src/
└── main.py
```
**Description:** Render the Mandelbrot set, Julia sets (configurable `c`), and the Burning Ship fractal as full-color ASCII art in the terminal using `curses`. Supports interactive zoom and pan with arrow keys.
**Core Concepts:** Complex numbers, escape-time algorithm, `curses`, character-to-complex-plane coordinate mapping, color pair assignment
**Difficulty:** Intermediate
**Unique Challenge:** Mapping terminal character coordinates to complex plane coordinates correctly despite the 2:1 height-to-width aspect ratio of monospace characters — scale the imaginary axis accordingly so fractals aren't squashed.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --fractal julia --c "-0.7+0.27i"
```

---

### 44. Key-Value Store + WAL [RARE]
**Slug:** `kv-store`
**Files:**
```
src/
├── main.py
├── store.py
└── wal.log
```
**Description:** Persistent key-value store backed by a hash-map in memory and a Write-Ahead Log (WAL) on disk. On startup, replay the WAL to reconstruct state after a simulated crash. Supports atomic batch operations.
**Core Concepts:** File I/O, `hashlib` for key hashing, WAL append-only log, crash recovery via replay, atomic file rename
**Difficulty:** Intermediate
**Unique Challenge:** Correctly replaying the WAL on startup — distinguishing committed transactions (end marker present) from incomplete ones (process crashed mid-write) and skipping partial writes.
**Run:**
```bash
python3 src/main.py set mykey "hello world"
python3 src/main.py get mykey
python3 src/main.py delete mykey
```

---

### 45. HTML Scraper (stdlib only)
**Slug:** `html-scraper`
**Files:**
```
src/
└── main.py
```
**Description:** Fetch a URL with `urllib.request` and extract structured data using `html.parser` SAX-style callbacks. Reconstruct a lightweight DOM tree by maintaining a node stack during parse events. Export results to CSV or JSON.
**Core Concepts:** `urllib.request`, `html.parser.HTMLParser`, event callbacks (handle_starttag/handle_data/handle_endtag), DOM reconstruction via stack
**Difficulty:** Intermediate
**Unique Challenge:** Reconstructing a usable tree from SAX events by maintaining a `current_path` stack — push on start tag, pop on end tag, accumulate text in the current node — without a library.
**Run:**
```bash
python3 src/main.py https://example.com --extract table --output results.csv
python3 src/main.py https://example.com --extract links
```

---

### 46. Caesar Cipher Frequency Breaker [RARE]
**Slug:** `cipher-breaker`
**Files:**
```
src/
└── main.py
```
**Description:** Automatically decrypt Caesar cipher text without knowing the key. Use chi-squared distance between the observed letter frequency distribution and expected English frequencies to rank all 26 possible shifts.
**Core Concepts:** `collections.Counter`, chi-squared distance formula, English letter frequency table, normalization
**Difficulty:** Intermediate
**Unique Challenge:** Computing chi-squared correctly — normalize observed counts by text length before comparing to the expected English frequencies table, so results are comparable across ciphertexts of different lengths.
**Run:**
```bash
python3 src/main.py "Khoor, Zruog!"
python3 src/main.py --file ciphertext.txt --top 3
```

---

### 47. Matrix Rain (terminal) [RARE]
**Slug:** `matrix-rain`
**Files:**
```
src/
└── main.py
```
**Description:** The Matrix digital rain effect — columns of cascading katakana/ASCII characters, white leading character, bright-green body, fading-green tail. Each column animates independently at a different speed.
**Core Concepts:** `curses`, `random`, per-column state dictionary, color pair cycling, frame timing
**Difficulty:** Intermediate
**Unique Challenge:** Tracking each column's independent drop head position AND fading tail as two separate pieces of state per column — and rendering only the delta each frame rather than redrawing the full screen.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --charset katakana --speed fast
```

---

### 48. Compression Tool (RLE + LZ77)
**Slug:** `compression-tool`
**Files:**
```
src/
├── main.py
└── codec.py
```
**Description:** Implement Run-Length Encoding (text and binary) and LZ77 sliding-window compression/decompression. Write a compact binary file format with a header identifying the codec. Compare ratios on test files.
**Core Concepts:** `bytearray`, `struct.pack`/`struct.unpack`, sliding window search, bit packing
**Difficulty:** Intermediate
**Unique Challenge:** Encoding LZ77 back-references as compact `(offset, length, next_literal)` triplets packed into a binary bitstream without byte-boundary alignment — requires a `BitWriter`/`BitReader` abstraction.
**Run:**
```bash
python3 src/main.py compress --codec lz77 input.txt output.bin
python3 src/main.py decompress output.bin recovered.txt
python3 src/main.py benchmark input.txt
```

---

### 49. Photo EXIF Metadata Reader [RARE]
**Slug:** `exif-reader`
**Files:**
```
src/
└── main.py
```
**Description:** Extract EXIF metadata from JPEG files by parsing the raw binary TIFF IFD structure — no PIL or piexif. Display camera make/model, exposure settings, GPS coordinates (converted from rational DMS to decimal), and timestamp.
**Core Concepts:** Binary file I/O, `struct.unpack`, TIFF IFD chain traversal, big/little endian detection, rational number arithmetic
**Difficulty:** Intermediate
**Unique Challenge:** Parsing GPS coordinates — stored as three rational numbers (degrees/minutes/seconds as numerator/denominator pairs), each requiring two `struct.unpack` calls, then converting to decimal degrees.
**Run:**
```bash
python3 src/main.py photo.jpg
python3 src/main.py photo.jpg --gps
python3 src/main.py --batch *.jpg
```

---

### 50. Tic-Tac-Toe with Minimax AI
**Slug:** `tictactoe-ai`
**Files:**
```
src/
└── main.py
```
**Description:** Play Tic-Tac-Toe against an unbeatable AI using the Minimax algorithm with alpha-beta pruning. Display the board after each move, show the AI's considered score for each choice in verbose mode.
**Core Concepts:** Minimax recursion, alpha-beta pruning, game state as a tuple (immutable), terminal state detection
**Difficulty:** Intermediate
**Unique Challenge:** Implementing alpha-beta pruning that always chooses the same optimal move as pure Minimax — the pruning must only skip branches that cannot affect the result, never the result itself.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --verbose
python3 src/main.py --ai-vs-ai
```

---

### 51. Snake Game (terminal) [CLASSIC]
**Slug:** `snake-game`
**Files:**
```
src/
└── main.py
```
**Description:** Fully playable Snake in the terminal — growing tail, wall wrapping or wall death (configurable), food generation, speed that increases every 5 foods, and a high score leaderboard.
**Core Concepts:** `curses`, `collections.deque`, keyboard input non-blocking, game loop with `time.sleep`, set for self-collision
**Difficulty:** Intermediate
**Unique Challenge:** Using `collections.deque` as the snake body — `appendleft` for the new head and `pop` for the tail removal — making self-collision detection O(n) with a companion `set`.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --walls off --speed 10
```

---

### 52. Cron Job Scheduler [RARE]
**Slug:** `cron-scheduler`
**Files:**
```
src/
├── main.py
└── jobs.json
```
**Description:** Register Python callables with 5-field cron expressions (`* * * * *`). Execute them in daemon threads on schedule. Support all cron field types: `*`, `*/N`, `N`, `N-M`, `N,M`. Persist job definitions to JSON.
**Core Concepts:** `threading.Thread(daemon=True)`, cron expression parser, `datetime`, next-trigger-time computation
**Difficulty:** Intermediate
**Unique Challenge:** Computing the next trigger time from a cron expression — iterate forward minute by minute from `now`, checking each component against its field's allowed set, until a matching datetime is found.
**Run:**
```bash
python3 src/main.py
```

---

### 53. CSV Report Generator
**Slug:** `csv-reporter`
**Files:**
```
src/
├── main.py
└── report.py
```
**Description:** Read any CSV file, auto-detect column types (numeric vs. categorical), compute per-column aggregates (sum, mean, median, mode, std, min, max), pivot by a groupby column, and output a formatted aligned report.
**Core Concepts:** `csv.DictReader`, `statistics`, type inference heuristics, `io.StringIO`, column alignment
**Difficulty:** Intermediate
**Unique Challenge:** Heuristically detecting column types — try `float(value)` for every value in a column; if >90% succeed, treat it as numeric. Handle mixed-type columns gracefully with a warning.
**Run:**
```bash
python3 src/main.py sales.csv --group region --agg sum --col revenue
python3 src/main.py data.csv --describe
```

---

### 54. CLI Spreadsheet [RARE]
**Slug:** `cli-spreadsheet`
**Files:**
```
src/
└── main.py
```
**Description:** A terminal spreadsheet with A1-notation cell references, `=SUM(A1:A10)`, `=AVG(B2:B5)`, `=MAX`, `=MIN`, `=IF` formulas, arrow-key navigation, and CSV save/load.
**Core Concepts:** `curses`, formula tokenizer, 2D cell array, topological sort for evaluation order, circular dependency detection
**Difficulty:** Intermediate
**Unique Challenge:** Detecting circular cell references (`A1=B1+1`, `B1=A1-1`) using DFS before evaluating any formulas — throw a clear error naming the cycle rather than hanging.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --load data.csv
```

---

### 55. Regex Search Tool (grep clone)
**Slug:** `grep-clone`
**Files:**
```
src/
└── main.py
```
**Description:** Recursively search files for regex patterns. Display matching lines with line numbers, color-highlight only the matched span within each line, show N lines of context above/below, and support `-v` invert and `-i` case-insensitive flags.
**Core Concepts:** `re.search`/`re.finditer`, `os.walk`, ANSI escape codes for inline color, `argparse`
**Difficulty:** Intermediate
**Unique Challenge:** Color-highlighting only the matched substring within a line — wrap just `match.group()` in ANSI codes while leaving the surrounding text in default color, for every non-overlapping match on the line.
**Run:**
```bash
python3 src/main.py "def \w+" src/ --recursive
python3 src/main.py "TODO|FIXME" . --recursive --context 2
```

---

### 56. Rate Limiter (Token Bucket) [RARE]
**Slug:** `rate-limiter`
**Files:**
```
src/
└── main.py
```
**Description:** Implement two rate limiting algorithms: Token Bucket (burst-capable) and Sliding Window Log (precise). Both are thread-safe and exposed as decorators. Includes a demo that simulates a burst of HTTP requests.
**Core Concepts:** `threading.Lock`, `time.monotonic`, `collections.deque` for sliding window, decorator pattern, `functools.wraps`
**Difficulty:** Intermediate
**Unique Challenge:** Making the token bucket's refill lazy (compute available tokens on demand based on elapsed time) rather than running a background refill thread — simpler, correct, and no busy-waiting.
**Run:**
```bash
python3 src/main.py
```

---

### 57. Job Queue with Workers [RARE]
**Slug:** `job-queue`
**Files:**
```
src/
├── main.py
└── worker.py
```
**Description:** Priority-based background job queue with a configurable worker thread pool. Failed jobs retry with exponential backoff. A live status dashboard prints queue depth, active workers, completed/failed counts, and average execution time.
**Core Concepts:** `threading`, `queue.PriorityQueue`, exponential backoff, `threading.Event` for shutdown, `time.perf_counter`
**Difficulty:** Intermediate
**Unique Challenge:** Implementing exponential backoff retries without blocking any worker thread — re-enqueue the job with a future scheduled-time as its priority key, not `time.sleep` inside the worker.
**Run:**
```bash
python3 src/main.py
```

---

### 58. Conway's Game of Life [CLASSIC]
**Slug:** `game-of-life`
**Files:**
```
src/
└── main.py
```
**Description:** Infinite-board Game of Life using a set of `(x, y)` live-cell coordinates. Includes preset patterns (Glider, R-pentomino, Pulsar, Gosper Glider Gun), step/pause/reset controls, and a generation counter.
**Core Concepts:** `curses`, `set` of coordinate tuples for infinite grid, neighbor counting via set operations, preset pattern loader
**Difficulty:** Intermediate
**Unique Challenge:** Using a `set` of coordinates instead of a fixed 2D array — only alive cells and their dead neighbors are considered each generation, enabling an infinite board with O(alive) memory.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --pattern gosper-glider-gun
```

---

### 59. Sorting Visualizer (terminal) [RARE]
**Slug:** `sort-visualizer`
**Files:**
```
src/
└── main.py
```
**Description:** Watch Bubble, Insertion, Selection, Merge, Quick, Heap, and Radix sort animate in real-time as color bar charts in the terminal. Show comparison and swap counters. Each algorithm is a generator that yields after every swap.
**Core Concepts:** `curses`, Python generators (`yield`), color pairs, `time.sleep` for frame rate, comparison counting
**Difficulty:** Intermediate
**Unique Challenge:** Refactoring every sorting algorithm as a Python generator that `yield`s `(array, highlight_indices)` after every comparison or swap — so the visualizer steps frame-by-frame without modifying the algorithm logic.
**Run:**
```bash
python3 src/main.py --algorithm quicksort --size 40
python3 src/main.py --compare-all --size 30
```

---

### 60. Finite State Machine Engine [RARE]
**Slug:** `fsm-engine`
**Files:**
```
src/
├── main.py
└── fsm.py
```
**Description:** A generic FSM engine with states, transitions, guard predicates, and entry/exit action callbacks. Includes three demo machines: traffic light, vending machine, and a TCP connection state diagram.
**Core Concepts:** `dict` state-transition table, OOP, `callable` guards, state pattern, event dispatch
**Difficulty:** Intermediate
**Unique Challenge:** Implementing transition guards as `Predicate[Context]` callables — `transition.when(lambda ctx: ctx.balance >= ctx.price)` — evaluated at transition time, making the FSM definition readable and testable.
**Run:**
```bash
python3 src/main.py --demo vending
python3 src/main.py --demo traffic
python3 src/main.py --demo tcp
```

---

### 61. Config Parser (.ini / .toml) [RARE]
**Slug:** `config-parser`
**Files:**
```
src/
├── main.py
└── parser.py
```
**Description:** Parse both `.ini` and a substantial TOML subset into nested Python dicts — without `configparser` or `tomllib`. Infer value types (int, float, bool, ISO date, array, inline table) from raw string values.
**Core Concepts:** Line-by-line parsing, `re`, nested dict building, type coercion pipeline
**Difficulty:** Intermediate
**Unique Challenge:** Inferring TOML value types from raw text — integers, floats, booleans (`true`/`false`), ISO-8601 dates, quoted strings, inline arrays, and inline tables — using a prioritized type-detection pipeline.
**Run:**
```bash
python3 src/main.py config.toml
python3 src/main.py config.ini
python3 src/main.py config.toml --get database.host
```

---

### 62. Profiler / Benchmarker [RARE]
**Slug:** `profiler`
**Files:**
```
src/
└── main.py
```
**Description:** A `@profile` decorator that measures wall time, CPU time, call count, and memory delta per decorated function. After the program exits, print a sorted summary table. Also includes a `@benchmark(n=1000)` decorator.
**Core Concepts:** Decorators, `time.perf_counter`, `tracemalloc`, `functools.wraps`, `atexit`, call stack via `inspect`
**Difficulty:** Intermediate
**Unique Challenge:** Using `tracemalloc` snapshot pairs (before/after each call) to attribute per-call memory allocation accurately — `tracemalloc.take_snapshot()` and comparing statistics.
**Run:**
```bash
python3 src/main.py
```

---

### 63. Functional Pipeline (lazy) [RARE]
**Slug:** `func-pipeline`
**Files:**
```
src/
└── main.py
```
**Description:** A fluent, composable lazy data pipeline: `pipe(source).map(fn).filter(pred).flatmap(fn).take(n).collect()`. Nothing executes until the terminal `collect()` pulls values through. Supports `zip`, `chunk`, `window`, and `tee`.
**Core Concepts:** Python generators, `itertools`, closures, higher-order functions, lazy evaluation protocol
**Difficulty:** Intermediate
**Unique Challenge:** Making the entire pipeline truly lazy end-to-end — each operator wraps a generator expression around the previous stage, so data flows one element at a time only when the consumer pulls it.
**Run:**
```bash
python3 src/main.py
```

---

### 64. Autocomplete via Trie
**Slug:** `trie-autocomplete`
**Files:**
```
src/
├── main.py
├── trie.py
└── words.txt
```
**Description:** Trie-backed autocomplete engine. Insert words with frequency weights. Given a prefix, return the top-k completions ranked by frequency using a bounded min-heap during DFS traversal.
**Core Concepts:** Trie (dict-of-dicts), DFS traversal, `heapq.nlargest` / bounded heap, frequency weighting
**Difficulty:** Intermediate
**Unique Challenge:** Returning top-k by frequency using a *bounded min-heap of size k* during DFS rather than collecting all completions first — prune subtrees whose max-descendant frequency is below the heap's current minimum.
**Run:**
```bash
python3 src/main.py
```

---

### 65. Event Bus / Pub-Sub [RARE]
**Slug:** `event-bus`
**Files:**
```
src/
└── main.py
```
**Description:** In-process publish-subscribe system. Subscribe with an exact topic string or a wildcard (`user.*`). Publish synchronously or asynchronously (via `threading.Thread`). Supports priority-ordered subscribers and once-only subscriptions.
**Core Concepts:** `dict`, `fnmatch` for wildcard matching, `threading.Thread`, `functools`, `weakref`
**Difficulty:** Intermediate
**Unique Challenge:** Implementing efficient wildcard topic matching — when a message is published, find all subscribers whose pattern matches the topic using `fnmatch.fnmatch`, without scanning all subscribers for exact-match topics.
**Run:**
```bash
python3 src/main.py
```

---

### 66. Minesweeper (terminal) [CLASSIC]
**Slug:** `minesweeper`
**Files:**
```
src/
└── main.py
```
**Description:** Full Minesweeper with configurable grid size and mine count. First click is guaranteed safe — mines are placed after the first reveal. Supports chord-clicking (reveal neighbors when flags = adjacent mines), and a timer.
**Core Concepts:** `curses`, 2D arrays, BFS flood-fill for reveal, deferred mine placement after first click
**Difficulty:** Intermediate
**Unique Challenge:** Deferred mine placement — on the first click, pick N random cells that are NOT the clicked cell or its 8 neighbors, place mines there, THEN compute all adjacency numbers.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --width 30 --height 16 --mines 99
```

---

### 67. Blackjack Game [CLASSIC]
**Slug:** `blackjack`
**Files:**
```
src/
├── main.py
└── models.py
```
**Description:** Casino-rules Blackjack with split pairs, double down, insurance bet, multi-deck shoe (1–8 decks), and a Hi-Lo card counting hint mode that tracks the running count and suggests bet sizing.
**Core Concepts:** OOP (`Deck`, `Hand`, `Player`, `Dealer`), `random.shuffle`, state machine per hand, Ace soft/hard value tracking
**Difficulty:** Intermediate
**Unique Challenge:** Computing hand value with multiple Aces — iterate through aces, count each as 11 then drop to 1 if the total exceeds 21. Track both `soft_total` and `hard_total` throughout.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --decks 6 --counting
```

---

### 68. Battleship Game
**Slug:** `battleship`
**Files:**
```
src/
├── main.py
└── models.py
```
**Description:** Two-player or vs-AI Battleship on a 10×10 grid. Ships: Carrier(5), Battleship(4), Cruiser(3), Submarine(3), Destroyer(2). AI uses a probability heat map — after a hit, calculates which cells most likely extend the sunk ship.
**Core Concepts:** OOP, 2D grids, `random`, probability density map, hunt/target AI state machine
**Difficulty:** Intermediate
**Unique Challenge:** Building the AI's probability heat map — for every unsunk ship, count how many valid placements cover each cell; the cell with the highest count is the best shot.
**Run:**
```bash
python3 src/main.py --mode vs-ai
python3 src/main.py --mode two-player
```

---

### 69. Wordle Clone (terminal)
**Slug:** `wordle`
**Files:**
```
src/
├── main.py
└── words.txt
```
**Description:** Wordle in the terminal — 6 guesses for a 5-letter word. Color feedback: green (right position), yellow (wrong position), gray (not in word). Handles duplicate-letter edge cases correctly. Daily-word mode seeds from today's date.
**Core Concepts:** String comparison, `collections.Counter` for duplicate handling, `datetime` for daily seed, ANSI color codes
**Difficulty:** Intermediate
**Unique Challenge:** Correct yellow/gray logic for duplicate letters — a letter can only be yellow as many times as it appears in the answer minus already-green occurrences. For example, guessing "SPEED" against "SLOPE" — the second E must be gray.
**Run:**
```bash
python3 src/main.py
python3 src/main.py --daily
python3 src/main.py --word custom
```

---

### 70. IRC-like Chat (sockets)
**Slug:** `irc-chat`
**Files:**
```
src/
└── main.py
```
**Description:** Multi-client terminal chat over TCP. Server handles all clients in separate threads and broadcasts messages. Clients support `/nick <name>`, `/quit`, `/whisper <user> <msg>`, `/list` commands. Includes a simple history buffer.
**Core Concepts:** `socket.socket`, `threading.Thread`, `select.select` for client input, `CopyOnWriteArrayList` equivalent, command parsing
**Difficulty:** Intermediate
**Unique Challenge:** Safely broadcasting to all connected clients while another thread may be adding or removing clients — use a `threading.Lock` around the client list and copy-on-iterate.
**Run:**
```bash
python3 src/main.py --server --port 9999
python3 src/main.py --client --host localhost --port 9999
```

---

### 71. File Encryption (XOR + PBKDF2)
**Slug:** `file-encrypt`
**Files:**
```
src/
└── main.py
```
**Description:** Stream-encrypt and decrypt files using XOR with a key derived from a password via PBKDF2-HMAC-SHA256 (100k iterations). Prepend a 16-byte random salt to the output file. Process in 64KB chunks to handle large files.
**Core Concepts:** `hashlib.pbkdf2_hmac`, `os.urandom`, XOR bytes with `bytes(a ^ b for a, b in zip(...))`, file streaming in chunks
**Difficulty:** Intermediate
**Unique Challenge:** Streaming large file encryption chunk-by-chunk without loading the whole file into memory — maintain a key-stream position counter so XOR applies continuously across chunk boundaries.
**Run:**
```bash
python3 src/main.py encrypt secret.pdf locked.bin
python3 src/main.py decrypt locked.bin recovered.pdf
```

---

## 🔴 ADVANCED PROJECTS (72–120)

---

### 72. Steganography (LSB in BMP) [RARE]
**Slug:** `steganography`
**Files:**
```
src/
├── main.py
└── steg.py
```
**Description:** Hide a secret text message inside a BMP image by modifying the least-significant bit of each color channel byte. Extract the message without the original. Supports BMP 24-bit and 32-bit variants.
**Core Concepts:** Binary file I/O, `struct.unpack`/`struct.pack`, bit manipulation (`& 0xFE | bit`), BMP file header parsing
**Difficulty:** Advanced
**Unique Challenge:** Parsing the BMP file header manually to find the pixel data offset (`bfOffBits` field at byte 10) — it differs between 24-bit and 32-bit BMPs, and you must seek to the right position before reading pixel bytes.
**Run:**
```bash
python3 src/main.py hide input.bmp "Top secret message" output.bmp
python3 src/main.py extract output.bmp
```

---

### 73. Virtual Machine (stack-based) [RARE]
**Slug:** `stack-vm`
**Files:**
```
src/
├── main.py
├── vm.py
└── compiler.py
```
**Description:** A stack-based virtual machine that executes a custom bytecode format. The compiler translates a simple expression language (with variables, `if/else`, `while`, and function calls) to bytecode. Includes a REPL and a bytecode disassembler.
**Core Concepts:** Stack machine, bytecode instruction set design, opcode dispatch via `dict`, call frames with local variable slots
**Difficulty:** Advanced
**Unique Challenge:** Implementing function call frames — `CALL` pushes a new frame with its own operand stack and local variable array; `RETURN` pops the frame and pushes the return value onto the caller's stack.
**Run:**
```bash
python3 src/main.py            # REPL
python3 src/main.py prog.lang  # Compile and run a file
python3 src/main.py --dis prog.lang  # Disassemble only
```

---

### 74. Interpreter / REPL [RARE]
**Slug:** `interpreter`
**Files:**
```
src/
├── main.py
├── lexer.py
├── parser.py
└── interpreter.py
```
**Description:** A fully working tree-walk interpreter for a small language with: variables (`let`), arithmetic, comparisons, `if/else`, `while`, first-class functions, lexical closures, and a REPL. Error messages include line/column numbers.
**Core Concepts:** Handwritten lexer (regex-free), recursive-descent parser, AST node classes, `Environment` chain for scope, closure objects
**Difficulty:** Advanced
**Unique Challenge:** Implementing lexical closures — a function value must capture a *reference* to its definition-time `Environment`, not a copy; calling the function creates a new scope that *extends* the captured one.
**Run:**
```bash
python3 src/main.py           # REPL
python3 src/main.py prog.lang # Run a file
```

---

### 75. Lisp Interpreter [RARE]
**Slug:** `lisp`
**Files:**
```
src/
├── main.py
└── lisp.py
```
**Description:** A Scheme-like Lisp interpreter with s-expression tokenizing and parsing, a standard environment (`+`, `-`, `car`, `cdr`, `cons`, `list`, `map`, `apply`), `lambda`, `define`, `if`, `cond`, `let`, `quasiquote`, tail call optimization via a trampoline, and user-defined macros.
**Core Concepts:** S-expression recursive parser, `eval`/`apply` mutual recursion, lexical environments, TCO trampoline, quasiquote expansion
**Difficulty:** Advanced
**Unique Challenge:** Implementing TCO using a trampoline — instead of recursing in `eval` for tail calls, return a `Thunk(fn, args)` object; the trampoline loop in `trampoline_eval()` calls thunks until it gets a concrete value, preventing Python stack overflow.
**Run:**
```bash
python3 src/main.py           # REPL
python3 src/main.py prog.scm  # Run a file
```

---

### 76. Git-like VCS [RARE]
**Slug:** `git-clone`
**Files:**
```
src/
├── main.py
├── objects.py
├── index.py
└── commands.py
```
**Description:** A simplified `git` supporting: `init` (create `.mygit/`), `add` (hash files, write blob objects), `commit` (write tree and commit objects), `log` (traverse commit DAG), `diff` (compare tree to working dir), `checkout` (restore working tree from commit).
**Core Concepts:** SHA-1 content addressing, zlib compression for objects, blob/tree/commit object types, DAG traversal, index file
**Difficulty:** Advanced
**Unique Challenge:** Implementing `checkout` — resolve the commit object → tree object → recurse through sub-trees → locate blob objects → write their content back to the working directory, all via the SHA-1 object store.
**Run:**
```bash
python3 src/main.py init
python3 src/main.py add .
python3 src/main.py commit -m "First commit"
python3 src/main.py log
python3 src/main.py checkout <hash>
```

---

### 77. SQL Subset Database Engine [RARE]
**Slug:** `sql-engine`
**Files:**
```
src/
├── main.py
├── parser.py
├── executor.py
└── storage.py
```
**Description:** Parse and execute a substantial SQL subset: `CREATE TABLE`, `INSERT`, `SELECT` (with `*` and column lists), `WHERE` (comparison and logical operators), `JOIN` (inner), `GROUP BY` with `COUNT`/`SUM`/`AVG`/`MAX`/`MIN`, and `ORDER BY`. Tables stored as JSON.
**Core Concepts:** SQL tokenizer and recursive-descent parser, relational algebra (selection, projection, join), expression evaluator, aggregate functions
**Difficulty:** Advanced
**Unique Challenge:** Implementing `GROUP BY` + aggregates correctly — after the join and filter, partition rows into groups by the GROUP BY keys, then apply aggregate functions per group, correctly handling `NULL` values.
**Run:**
```bash
python3 src/main.py "SELECT name, SUM(amount) FROM orders GROUP BY name ORDER BY SUM(amount) DESC"
```

---

### 78. Ray Tracer (PPM output) [RARE]
**Slug:** `ray-tracer`
**Files:**
```
src/
├── main.py
├── scene.py
└── math3d.py
```
**Description:** CPU ray tracer that outputs PPM images. Supports spheres, infinite planes, point lights, Phong shading (ambient + diffuse + specular), hard shadows, mirror reflections (recursive, depth-limited), and basic anti-aliasing (4× SSAA).
**Core Concepts:** 3D vector math (dot/cross/normalize), ray-sphere intersection (quadratic formula), ray-plane intersection, recursive ray casting, PPM binary format
**Difficulty:** Advanced
**Unique Challenge:** Implementing recursive mirror reflections with a depth limit — at each bounce, compute a new reflected ray using `r = d - 2(d·n)n` and recurse; the depth limit prevents infinite loops between two mirrors.
**Run:**
```bash
python3 src/main.py scene.json output.ppm
python3 src/main.py --preset three-spheres output.ppm
```

---

### 79. Async Event Loop from Scratch [RARE]
**Slug:** `async-loop`
**Files:**
```
src/
├── main.py
└── eventloop.py
```
**Description:** A working async event loop using Python generators and `select.select`. Coroutines `yield` I/O descriptors back to the loop which resumes them when the fd is ready. Supports timers, `sleep`, and non-blocking TCP connections.
**Core Concepts:** Python generators as coroutines, `select.select` for I/O readiness, callback queue, scheduler heap for timers, coroutine protocol
**Difficulty:** Advanced
**Unique Challenge:** Implementing `yield`-based I/O suspension — a coroutine does `yield ('read', sock)` to pause; the loop registers the socket in `select`, and when readable, calls `generator.send(data)` to resume it with the received bytes.
**Run:**
```bash
python3 src/main.py   # Runs a demo echo server using the custom event loop
```

---

### 80. RSA Encryption from Scratch [RARE]
**Slug:** `rsa`
**Files:**
```
src/
├── main.py
├── rsa.py
└── math_utils.py
```
**Description:** Full RSA implementation: generate two 512-bit primes via Miller-Rabin primality test, compute public/private key pair, encrypt with PKCS#1-style padding, decrypt. Uses only Python's built-in arbitrary-precision integers.
**Core Concepts:** Miller-Rabin primality (probabilistic), modular exponentiation (`pow(b, e, m)`), extended Euclidean algorithm for modular inverse, Python `int` bignum
**Difficulty:** Advanced
**Unique Challenge:** Implementing Miller-Rabin with enough deterministic witnesses for 512-bit primes — 7 witnesses (2, 3, 5, 7, 11, 13, 17) guarantee correctness for numbers below 3.3 × 10²⁴; beyond that, use random witnesses with k=40 rounds.
**Run:**
```bash
python3 src/main.py generate-keys
python3 src/main.py encrypt "Hello RSA" --key public.json
python3 src/main.py decrypt ciphertext.bin --key private.json
```

---

### 81. Neural Network (no libraries) [RARE]
**Slug:** `neural-net`
**Files:**
```
src/
├── main.py
├── network.py
└── layers.py
```
**Description:** A fully-connected neural network trainable via mini-batch SGD with backpropagation. Supports configurable layer sizes, sigmoid/ReLU/tanh activations, He/Xavier initialization, and L2 regularization. Train on XOR or a small MNIST subset.
**Core Concepts:** Matrix multiply using nested lists, chain rule for backprop, gradient descent, weight initialization strategies
**Difficulty:** Advanced
**Unique Challenge:** Implementing the backward pass for each layer correctly using only Python lists — the gradient of the loss with respect to weights is `(1/m) * dZ.T · A_prev`, where all matmul is manual nested-loop code.
**Run:**
```bash
python3 src/main.py --task xor
python3 src/main.py --task mnist --layers 784,128,64,10
```

---

### 82. Genetic Algorithm (TSP) [RARE]
**Slug:** `genetic-algo`
**Files:**
```
src/
├── main.py
└── ga.py
```
**Description:** Solve the Travelling Salesman Problem using a Genetic Algorithm. Implements tournament selection, Partially Mapped Crossover (PMX) for valid tour permutations, 2-opt local search mutation, and elitism. Animate the best tour each generation.
**Core Concepts:** Permutation representation, PMX crossover, tournament selection, 2-opt swap mutation, fitness = 1/tour_length
**Difficulty:** Advanced
**Unique Challenge:** Implementing PMX correctly — define a crossover segment, copy it from parent 1 to offspring, then fill remaining positions from parent 2 using the position mapping to avoid duplicate cities.
**Run:**
```bash
python3 src/main.py --cities 20 --pop 200 --generations 1000
python3 src/main.py --file cities.csv
```

---

### 83. Bloom Filter [RARE]
**Slug:** `bloom-filter`
**Files:**
```
src/
├── main.py
└── bloom.py
```
**Description:** Space-efficient probabilistic set membership filter. Compute optimal bit array size `m` and hash function count `k` from target capacity `n` and false-positive rate `p`. Implement with `bytearray` and double-hashing. Empirically verify the FP rate.
**Core Concepts:** `bytearray` as a bit array, double hashing (`h_i = h1 + i * h2`), FP rate formula `(1 - e^(-kn/m))^k`, `hashlib`
**Difficulty:** Advanced
**Unique Challenge:** Computing optimal `m` and `k`: `m = -n·ln(p) / (ln 2)²` and `k = (m/n)·ln 2` — then demonstrating empirically that the actual false-positive rate matches the theoretical prediction within statistical bounds.
**Run:**
```bash
python3 src/main.py --capacity 100000 --fp-rate 0.01
python3 src/main.py --verify
```

---

### 84. PDF Text Extractor (raw binary) [RARE]
**Slug:** `pdf-extractor`
**Files:**
```
src/
├── main.py
└── pdf_parser.py
```
**Description:** Extract text from PDF files by parsing the raw binary format without any library. Parse the cross-reference table to locate objects, decompress FlateDecode streams with `zlib`, and interpret PDF content stream operators (`BT`, `ET`, `Tj`, `TJ`, `Tf`) to reconstruct text.
**Core Concepts:** Binary file I/O, `struct.unpack`, PDF xref table (traditional and cross-reference stream), `zlib.decompress`, content stream tokenizer
**Difficulty:** Advanced
**Unique Challenge:** Handling both traditional xref tables and cross-reference stream objects (PDF 1.5+) — the latter uses a compressed binary stream format with a `W` array specifying column widths.
**Run:**
```bash
python3 src/main.py document.pdf
python3 src/main.py document.pdf --page 3
```

---

### 85. Mini ORM (sqlite3 + metaclass) [RARE]
**Slug:** `mini-orm`
**Files:**
```
src/
├── main.py
├── orm.py
└── fields.py
```
**Description:** A Django-inspired ORM backed by Python's built-in `sqlite3`. Define models with field descriptors (`IntField`, `CharField`, `ForeignKey`). Auto-generates `CREATE TABLE` SQL. Supports `objects.filter()`, `objects.get()`, `save()`, `delete()`, and simple ForeignKey traversal.
**Core Concepts:** `sqlite3`, `__init_subclass__` metaclass hook, Python descriptors (`__get__`/`__set__`), SQL generation, `sqlite3.Row`
**Difficulty:** Advanced
**Unique Challenge:** Using `__init_subclass__` (or a metaclass's `__new__`) to auto-register field definitions at class creation time — so fields declared as class attributes are detected and recorded without any `@decorator` syntax.
**Run:**
```bash
python3 src/main.py
```

---

### 86. Plugin System (hot-reload) [RARE]
**Slug:** `plugin-system`
**Files:**
```
src/
├── main.py
├── plugin_manager.py
└── plugins/
    ├── hello_plugin.py
    └── shout_plugin.py
```
**Description:** A hot-loadable plugin system. The manager watches the `plugins/` directory for `.py` files, auto-discovers them using `importlib`, loads any class implementing the `Plugin` interface, and reloads changed plugins at runtime without restarting.
**Core Concepts:** `importlib.import_module`, `importlib.reload`, `pkgutil.iter_modules`, `inspect.getmembers`, `abc.ABC` interface
**Difficulty:** Advanced
**Unique Challenge:** Safely reloading a changed plugin module at runtime using `importlib.reload` — old references to the module's classes in the manager must be replaced with references to the reloaded versions.
**Run:**
```bash
python3 src/main.py
# Drop a new .py file into src/plugins/ while running — it auto-loads
```

---

### 87. AST Visualizer
**Slug:** `ast-visualizer`
**Files:**
```
src/
└── main.py
```
**Description:** Parse Python source code using the built-in `ast` module and render the full Abstract Syntax Tree as a color-coded indented tree showing node types, field names, and literal values. Supports both file input and a live REPL mode.
**Core Concepts:** `ast.parse`, `ast.NodeVisitor`, `ast.iter_child_nodes`, `ast.iter_fields`, tree traversal, ANSI color coding
**Difficulty:** Advanced
**Unique Challenge:** Handling ALL AST node types generically using `ast.iter_child_nodes()` and `ast.iter_fields()` — no hard-coded node types — so the visualizer works on any valid Python code including Python 3.12 match statements.
**Run:**
```bash
python3 src/main.py script.py
python3 src/main.py --repl
python3 src/main.py --expr "x = [i**2 for i in range(10)]"
```

---

### 88. Tensor Engine + Autograd [RARE]
**Slug:** `tensor-autograd`
**Files:**
```
src/
├── main.py
├── tensor.py
└── autograd.py
```
**Description:** An N-dimensional tensor class supporting element-wise ops, broadcasting, matrix multiplication, reshape, and transpose — all using plain Python lists. A tape-based reverse-mode autograd system records operations and computes gradients via backpropagation.
**Core Concepts:** Recursive list-based N-D arrays, NumPy-style broadcasting rules (implemented manually), computation tape, chain rule via recorded operations
**Difficulty:** Advanced
**Unique Challenge:** Implementing broadcasting without NumPy — determine the broadcast shape by aligning shapes from the right and applying the broadcast rule, then expand each operand to the broadcast shape using nested list comprehensions.
**Run:**
```bash
python3 src/main.py   # Runs gradient checks and a small NN training demo
```

---

### 89. Network Packet Sniffer [RARE]
**Slug:** `packet-sniffer`
**Files:**
```
src/
├── main.py
└── decoder.py
```
**Description:** Capture raw network packets using a raw socket (`AF_PACKET` on Linux) and decode the nested headers: Ethernet frame → IP header → TCP or UDP segment. Display live traffic in a formatted table with protocol, source/dest IPs, ports, and payload size.
**Core Concepts:** `socket.AF_PACKET`, `socket.SOCK_RAW`, `struct.unpack` with variable offsets, Ethernet/IP/TCP header formats, IP header length field (IHL)
**Difficulty:** Advanced
**Unique Challenge:** Parsing nested protocol headers with dynamic offsets — the IP header has a variable length field (IHL × 4 bytes), so the TCP/UDP header starts at a computed offset, not a fixed one.
**Run:**
```bash
sudo python3 src/main.py --interface eth0    # Requires root on Linux
```

---

### 90. HTTP/1.1 Server (full spec) [RARE]
**Slug:** `http11-server`
**Files:**
```
src/
├── main.py
├── router.py
├── request.py
└── response.py
```
**Description:** A compliant HTTP/1.1 server supporting persistent connections (keep-alive), chunked transfer encoding, a routing decorator (`@app.route`), middleware chain, Content-Type negotiation, and basic `HEAD` and `OPTIONS` methods.
**Core Concepts:** Sockets, HTTP/1.1 RFC 7230, persistent connections, chunked encoding, middleware pattern, routing via dict
**Difficulty:** Advanced
**Unique Challenge:** Implementing persistent connections (keep-alive) correctly — reuse the same socket for multiple requests by re-parsing the next request after sending the response, and close only when `Connection: close` is seen or a timeout occurs.
**Run:**
```bash
python3 src/main.py
```

---

### 91. P2P File Sharing (mini) [RARE]
**Slug:** `p2p-sharing`
**Files:**
```
src/
├── main.py
├── peer.py
└── tracker.py
```
**Description:** Decentralized file sharing. Peers register files with a central tracker (host/port + file hash). Downloading peers query the tracker for a list of seeders, then download non-overlapping chunks in parallel from multiple peers. Each chunk is SHA-256 verified before assembly.
**Core Concepts:** `socket`, `threading`, chunked file transfer, `RandomAccessFile` equivalent (`open(f, 'r+b')`), SHA-256 chunk verification, chunk completion bitmap
**Difficulty:** Advanced
**Unique Challenge:** Downloading chunks from multiple peers in parallel and writing each to the correct file offset — track which chunks are in-progress vs. done with a `set`, use `file.seek(offset)` before each chunk write.
**Run:**
```bash
python3 src/tracker.py
python3 src/main.py share bigfile.zip
python3 src/main.py download <filehash>
```

---

### 92. Reactive Streams (mini) [RARE]
**Slug:** `reactive-streams`
**Files:**
```
src/
└── main.py
```
**Description:** A Publisher/Subscriber reactive streams implementation with explicit backpressure demand signaling. Operators: `map`, `filter`, `flatMap`, `merge`, `zip`, `take`, `debounce`. A slow subscriber can request N items at a time without the publisher overflowing.
**Core Concepts:** Python generators, observer pattern, backpressure protocol (`request(n)`), functional composition, `threading.Queue` for async delivery
**Difficulty:** Advanced
**Unique Challenge:** Implementing backpressure — the `Subscriber` calls `subscription.request(n)` to signal demand; the `Publisher` must never emit more items than have been requested, buffering the surplus.
**Run:**
```bash
python3 src/main.py
```

---

### 93. Compiler (lang → VM bytecode) [RARE]
**Slug:** `mini-compiler`
**Files:**
```
src/
├── main.py
├── lexer.py
├── parser.py
└── codegen.py
```
**Description:** A compiler that translates a simple C-like language (from Project #74's grammar) to bytecode for Project #73's stack VM. Handles variables, arithmetic, boolean expressions, `if/else`, `while`, and function calls with arguments.
**Core Concepts:** Lexer, recursive-descent parser, AST, symbol table with scope levels, bytecode emission, function call convention
**Difficulty:** Advanced
**Unique Challenge:** Building a symbol table that correctly tracks variable scope across nested function definitions — resolve each identifier to its scope level at compile time, emit `LOAD_LOCAL` vs. `LOAD_UPVALUE` opcodes accordingly.
**Run:**
```bash
python3 src/main.py program.lang           # Compile + run
python3 src/main.py program.lang --dis     # Compile + disassemble
```

---

### 94. B-Tree Implementation [RARE]
**Slug:** `btree`
**Files:**
```
src/
├── main.py
└── btree.py
```
**Description:** A page-oriented B-Tree with configurable order `t` (minimum degree). Implements insert (with node splitting on the way down), search, delete (with redistribution and merge for underflow), and range scan. Simulates disk pages as Python lists.
**Core Concepts:** Balanced tree invariants, proactive splitting on insert, key redistribution vs. merge on delete, in-order traversal for range scan
**Difficulty:** Advanced
**Unique Challenge:** Correctly choosing between key redistribution (borrow from sibling) and merging (join sibling + parent separator key) during deletion underflow — redistribution is preferred when the sibling has extra keys.
**Run:**
```bash
python3 src/main.py
```

---

### 95. LSM-Tree Storage Engine [RARE]
**Slug:** `lsm-tree`
**Files:**
```
src/
├── main.py
├── lsm.py
└── sstable.py
```
**Description:** A Log-Structured Merge-Tree as used in LevelDB and Cassandra. In-memory MemTable (sorted dict), append-only Write-Ahead Log for crash recovery, SSTable files (sorted key-value pairs on disk), and a background thread that merges/compacts SSTables.
**Core Concepts:** `dict` sorted by key, binary search on SSTable, WAL append, merge-sort for compaction, tombstone deletes
**Difficulty:** Advanced
**Unique Challenge:** Implementing the compaction step — merge-sort N SSTable files simultaneously (k-way merge via `heapq.merge`), de-duplicating keys by keeping the newest version (highest sequence number), and skipping tombstone entries.
**Run:**
```bash
python3 src/main.py
```

---

### 96. Raft Consensus (simulated) [RARE]
**Slug:** `raft`
**Files:**
```
src/
├── main.py
└── raft_node.py
```
**Description:** Simulate a 5-node Raft cluster inside one process using threads and `queue.Queue` for message passing. Implements leader election (randomized timeout 150–300ms), log replication, commit index advancement, and follower log catch-up.
**Core Concepts:** Distributed consensus, `threading`, `queue.Queue` inter-node messages, randomized election timeouts, term/vote tracking
**Difficulty:** Advanced
**Unique Challenge:** Using randomized election timeouts with `random.uniform(150, 300)` milliseconds to ensure exactly one node wins most elections — and handling the split-vote case where no majority is achieved by simply starting a new term.
**Run:**
```bash
python3 src/main.py   # Watch leader elections and log replication in real-time
```

---

### 97. Distributed Key-Value Store [RARE]
**Slug:** `dist-kv`
**Files:**
```
src/
├── main.py
├── node.py
└── server.py
```
**Description:** A multi-process distributed KV store using consistent hashing for key distribution, replication factor of 3, and quorum-based reads/writes (majority must respond). Nodes communicate over TCP sockets.
**Core Concepts:** `socket`, `threading`, consistent hashing ring with virtual nodes, replication fan-out, quorum (W + R > N), eventual consistency
**Difficulty:** Advanced
**Unique Challenge:** Implementing quorum writes — fan out the write to all 3 replica nodes, wait for at least 2 acknowledgments before returning success, and handle partial failures without losing the write entirely.
**Run:**
```bash
python3 src/main.py --nodes 3
```

---

### 98. Docker-like Process Isolator [RARE]
**Slug:** `process-isolator`
**Files:**
```
src/
└── main.py
```
**Description:** Run child processes in a lightweight isolated environment using Linux namespaces via `ctypes` to call `clone()` with `CLONE_NEWPID | CLONE_NEWUTS | CLONE_NEWNS`. Set up a minimal chroot with `os.chroot`. Apply resource limits with `resource.setrlimit`. Linux only.
**Core Concepts:** `ctypes` for syscall interface, Linux `clone()` flags, `os.chroot`, `resource.setrlimit`, `os.fork`, mount namespace
**Difficulty:** Advanced
**Unique Challenge:** Calling the Linux `clone()` syscall directly via `ctypes.CDLL('libc.so.6').clone()` with the correct `CLONE_*` flag constants — Python's `os` module doesn't expose clone, so you must call it via ctypes.
**Run:**
```bash
sudo python3 src/main.py run /bin/sh   # Linux only, requires root
```

---

### 99. Dependency Resolver (pip-like) [RARE]
**Slug:** `dep-resolver`
**Files:**
```
src/
└── main.py
```
**Description:** Parse a `requirements.txt`-style manifest where packages declare version-constrained dependencies. Resolve the full dependency graph using topological sort (Kahn's algorithm). Detect and report version conflicts with a clear human-readable explanation.
**Core Concepts:** Graph construction, Kahn's topological sort, semantic version comparison (`packaging.version` is NOT used — implement semver parsing yourself), conflict detection
**Difficulty:** Advanced
**Unique Challenge:** Detecting version conflicts — when two packages both depend on `X` but with incompatible version constraints (`>=1.0` vs. `<1.0`), report *which two packages create the conflict* and *why*, not just "conflict detected".
**Run:**
```bash
python3 src/main.py requirements.txt
python3 src/main.py requirements.txt --explain
```

---

### 100. WebSocket Server (raw) [RARE]
**Slug:** `websocket-server`
**Files:**
```
src/
└── main.py
```
**Description:** RFC 6455 WebSocket server from scratch. Handles the HTTP upgrade handshake (SHA-1 key hashing, base64 accept key), parses variable-length binary frames (7-bit / 16-bit / 64-bit payload length), unmasks client frames, and sends server frames. Includes a ping/pong keepalive.
**Core Concepts:** `hashlib.sha1`, `base64`, WebSocket frame binary format, masking XOR, `struct.unpack`, `select` for multi-client
**Difficulty:** Advanced
**Unique Challenge:** Parsing WebSocket frame length correctly — the first 7 bits may be 0–125 (length), 126 (next 2 bytes are uint16 length), or 127 (next 8 bytes are uint64 length) — each case requires a different unpack format.
**Run:**
```bash
python3 src/main.py --port 8765
```

---

### 101. Interval Tree [RARE]
**Slug:** `interval-tree`
**Files:**
```
src/
├── main.py
└── interval_tree.py
```
**Description:** An augmented BST-based interval tree supporting insert, delete, point-query (all intervals containing a point), and overlap-query (all intervals overlapping a range). Each node stores the maximum endpoint of its subtree for O(log n) pruning.
**Core Concepts:** Augmented BST, `max_end` subtree field, overlap predicate, BST insertion/deletion, in-order traversal
**Difficulty:** Intermediate
**Unique Challenge:** Maintaining the `max_end` augmentation correctly after rotations — when you rebalance (AVL or plain BST), you must recompute `max_end` bottom-up for every affected node.
**Run:**
```bash
python3 src/main.py
```

---

### 102. Skip List [RARE]
**Slug:** `skip-list`
**Files:**
```
src/
├── main.py
└── skip_list.py
```
**Description:** A probabilistic skip list with O(log n) expected search, insert, and delete. Uses a coin-flip to assign each node a random height. Maintains a header node with `MAX_LEVEL` forward pointers. Same data structure used in Redis ZSets.
**Core Concepts:** Multi-level forward pointer arrays, `random.random() < 0.5` level assignment, `update[]` predecessor array for insert/delete
**Difficulty:** Intermediate
**Unique Challenge:** Maintaining the `update[]` array during insert and delete — it tracks the rightmost node at each level whose forward pointer needs updating; getting this wrong breaks the invariant at every level above the operation.
**Run:**
```bash
python3 src/main.py
```

---

### 103. Consistent Hashing Ring [RARE]
**Slug:** `consistent-hash`
**Files:**
```
src/
└── main.py
```
**Description:** Consistent hashing ring with configurable virtual node count. Add and remove servers, route keys to servers, and demonstrate the core property: adding/removing 1 server remaps only ~K/N keys (not all K). Log before/after statistics for each operation.
**Core Concepts:** MD5/SHA-1 for key hashing, `bisect.bisect` on a sorted ring list, virtual nodes for load balance, key remapping statistics
**Difficulty:** Advanced
**Unique Challenge:** Demonstrating empirically that consistent hashing remaps only K/N keys — hash 100k test keys before and after adding a node, count how many changed servers, and show it's approximately 1/N of total keys.
**Run:**
```bash
python3 src/main.py --nodes 5 --vn 100 --keys 100000
```

---

### 104. SMTP Client (raw socket) [RARE]
**Slug:** `smtp-client`
**Files:**
```
src/
└── main.py
```
**Description:** Send emails using a raw SMTP conversation over TCP — no `smtplib`. Implement the full handshake: `EHLO`, `STARTTLS` upgrade, `AUTH LOGIN` (base64-encoded credentials), `MAIL FROM`, `RCPT TO`, `DATA`, `QUIT`. Parse multi-line server responses.
**Core Concepts:** `socket`, `ssl.SSLContext.wrap_socket` for STARTTLS, `base64.b64encode`, SMTP RFC 5321 command/response protocol
**Difficulty:** Intermediate
**Unique Challenge:** Implementing STARTTLS — after the server responds `220 Ready to start TLS`, wrap the *existing* plaintext socket in an `ssl.SSLSocket` using `ssl.wrap_socket(sock, ...)` without opening a new connection.
**Run:**
```bash
python3 src/main.py --to recipient@example.com --from me@gmail.com --subject "Test"
```

---

### 105. DNS Resolver (raw UDP) [RARE]
**Slug:** `dns-resolver`
**Files:**
```
src/
├── main.py
└── dns_proto.py
```
**Description:** Resolve DNS queries by building raw DNS wire-format packets and sending them over UDP. Decode the response — handling DNS name compression pointers, multiple answer records, and record types A, AAAA, MX, CNAME, TXT.
**Core Concepts:** UDP `socket`, DNS wire format (RFC 1035), `struct.pack`/`struct.unpack`, label encoding/decoding, compression pointer resolution
**Difficulty:** Advanced
**Unique Challenge:** Parsing DNS name compression pointers in the response — a pointer is a 2-byte value where the top 2 bits are `11`, and the remaining 14 bits are an offset into the packet. Following them requires maintaining the current parse position carefully.
**Run:**
```bash
python3 src/main.py google.com A
python3 src/main.py google.com MX
python3 src/main.py --trace example.com A   # Show each packet
```

---

### 106. Python Bytecode Disassembler [RARE]
**Slug:** `bytecode-dis`
**Files:**
```
src/
└── main.py
```
**Description:** Disassemble Python `.pyc` files and live code objects — display opcodes, arguments, resolved constant/name references, and annotate stack effect per instruction. Also hook `sys.settrace` to trace execution bytecode in real-time.
**Core Concepts:** `dis` module, `marshal.loads` for `.pyc` deserialization, `.pyc` magic number + bitfield header, `opcode` module, code object attributes
**Difficulty:** Advanced
**Unique Challenge:** Parsing the `.pyc` binary header manually — the format changes between Python versions; Python 3.8+ uses a hash-based header with a `flags` bitfield at byte 4 that determines whether bytes 8–16 are a source hash or a timestamp + source size.
**Run:**
```bash
python3 src/main.py script.pyc
python3 src/main.py --live script.py   # Trace execution + show bytecode
```

---

### 107. Context Manager Library
**Slug:** `ctx-managers`
**Files:**
```
src/
└── main.py
```
**Description:** A library of 12 production-useful context managers: `Timer`, `TempDir`, `SuppressErrors`, `AtomicFile` (write-then-rename), `RedirectStdout`, `Timeout`, `EnvironPatch`, `CaptureOutput`, `ChangeDir`, `TempEnv`, `Retry`, and `MeasureMemory`.
**Core Concepts:** `__enter__`/`__exit__` protocol, `contextlib.contextmanager`, `signal.alarm` for timeout, `os.rename` for atomic write, exception suppression
**Difficulty:** Intermediate
**Unique Challenge:** Implementing `Timeout` cross-platform — on Unix use `signal.alarm(seconds)` + `SIGALRM` handler; on Windows use a `threading.Timer` that calls `_thread.interrupt_main()`. Both must cancel cleanly on normal exit.
**Run:**
```bash
python3 src/main.py   # Runs all 12 context managers with demos
```

---

### 108. Decorators Toolbox
**Slug:** `decorators`
**Files:**
```
src/
└── main.py
```
**Description:** 15 production-grade decorators: `@retry(n, exceptions)`, `@cache` (LRU), `@throttle(rate)`, `@trace`, `@singleton`, `@deprecated(msg)`, `@once`, `@memoize_ttl(seconds)`, `@timeout(s)`, `@log_calls`, `@validate_types`, `@before`/`@after` hooks, `@classproperty`, `@overload`.
**Core Concepts:** Higher-order functions, `functools.wraps`, closures, `threading.Lock`, `time.monotonic`, `inspect.signature`
**Difficulty:** Intermediate
**Unique Challenge:** Implementing `@memoize_ttl(seconds)` — cache return values but expire them after N seconds. Each cache entry stores `(result, expiry_time)`; on cache hit, check if `time.monotonic() < expiry_time` before returning the cached value.
**Run:**
```bash
python3 src/main.py   # Demos all 15 decorators
```

---

### 109. CLI Argument Framework
**Slug:** `cli-framework`
**Files:**
```
src/
└── main.py
```
**Description:** A custom CLI argument parser supporting: positional arguments, `--flag` / `-f` options, subcommands, required/optional arguments, type coercion, default values, mutual exclusion groups, and auto-generated `--help` with aligned, color-coded output.
**Core Concepts:** `sys.argv` parsing, OOP command/argument classes, recursive subcommand dispatch, string alignment for help text
**Difficulty:** Intermediate
**Unique Challenge:** Auto-generating aligned help text for nested subcommands — compute the maximum argument name width globally, then left-justify all names to that width so descriptions align in a clean column.
**Run:**
```bash
python3 src/main.py   # Demonstrates a sample CLI app built on the framework
```

---

### 110. Brainfuck Interpreter [RARE]
**Slug:** `brainfuck`
**Files:**
```
src/
└── main.py
```
**Description:** A complete Brainfuck interpreter with 30,000-cell byte tape, full I/O, an O(1) bracket jump table (pre-computed with a stack), a step-debugger mode (pause after every N instructions), and a tape visualization mode.
**Core Concepts:** Stack for bracket matching, `bytearray` tape, jump table pre-computation, instruction pointer, I/O via `sys.stdin`/`sys.stdout`
**Difficulty:** Intermediate
**Unique Challenge:** Pre-computing the jump table in a single O(n) pass using a stack — push `[` positions onto a stack, when `]` is seen pop the matching `[` and record both directions in a `dict`. Runtime `[`/`]` are then O(1) lookups.
**Run:**
```bash
python3 src/main.py hello.bf
python3 src/main.py mandelbrot.bf
python3 src/main.py hello.bf --debug --step 1
```

---

### 111. Forth Stack Language [RARE]
**Slug:** `forth`
**Files:**
```
src/
└── main.py
```
**Description:** A Forth-like stack-based language with: core stack words (`dup`, `drop`, `swap`, `over`, `rot`), arithmetic, comparisons, `if ... then`, `if ... else ... then`, `begin ... until`, `begin ... while ... repeat`, user-defined words (`: SQUARE dup * ;`), and a REPL.
**Core Concepts:** Data stack, return stack, word dictionary, colon definition compilation, `begin/until` and `if/then` control flow
**Difficulty:** Advanced
**Unique Challenge:** Implementing user-defined words (`: SQUARE dup * ;`) — compile the definition body to a list of word references or literals; when `SQUARE` is called, push the current IP onto the return stack, execute the body, then pop and resume.
**Run:**
```bash
python3 src/main.py           # REPL
python3 src/main.py prog.fth  # Run a file
```

---

### 112. Mandelbrot Zoom (terminal) [RARE]
**Slug:** `mandelbrot`
**Files:**
```
src/
└── main.py
```
**Description:** An interactive Mandelbrot set viewer in the terminal. Navigate with arrow keys (pan), `+`/`-` (zoom), `c` (change palette). Uses smooth coloring (fractional escape count via `log(log(|z|))`) to eliminate harsh color banding. Renders in `curses` with 256-color support.
**Core Concepts:** Complex arithmetic, escape-time algorithm, smooth coloring formula, `curses`, coordinate-plane mapping, incremental zoom
**Difficulty:** Intermediate
**Unique Challenge:** Smooth coloring — the standard formula `nu = n - log(log(|z|)) / log(2)` gives a fractional iteration count that maps to a continuous color gradient; implementing it requires understanding why `log(log(|z|))` normalizes the escape time.
**Run:**
```bash
python3 src/main.py
```

---

### 113. Cellular Automata Engine [RARE]
**Slug:** `cellular-automata`
**Files:**
```
src/
└── main.py
```
**Description:** A configurable cellular automata engine for: 1D Wolfram elementary rules 0–255 (all 256 rules runnable via bitmask), and 2D rules including Conway's Life, Highlife, Seeds, Maze, Brian's Brain, and Wireworld. Render in `curses` with configurable speed.
**Core Concepts:** Bit masking for Wolfram rule encoding, Moore and von Neumann neighborhoods, 2D array with toroidal wrapping, `curses`
**Difficulty:** Intermediate
**Unique Challenge:** Encoding all 256 Wolfram elementary rules via bitmasking — the rule number IS the lookup table in binary; to find the next state for a 3-cell neighborhood pattern `N`, compute `(rule_number >> N) & 1`. Rule 110 (Turing-complete) works automatically.
**Run:**
```bash
python3 src/main.py --mode 1d --rule 110
python3 src/main.py --mode 2d --rule life
python3 src/main.py --mode 2d --rule wireworld
```

---

### 114. Path Planning (A* on Grid)
**Slug:** `pathfinding`
**Files:**
```
src/
├── main.py
└── astar.py
```
**Description:** A* pathfinding on a 2D grid with configurable movement (4-directional or 8-directional with diagonal cost √2). Multiple heuristics: Manhattan, Euclidean, Chebyshev, Octile. Tie-breaking for straight paths. Reads obstacle maps from ASCII art text files.
**Core Concepts:** `heapq`, `dict` for `g_score`/`came_from`, heuristic functions, tie-breaking, path reconstruction via `came_from` dict
**Difficulty:** Intermediate
**Unique Challenge:** Implementing tie-breaking — when multiple nodes have the same `f = g + h`, prefer the one with the smaller `h` (closer to goal) by adding `h * epsilon` to `f`. This produces visually straight paths instead of the "staircase" effect.
**Run:**
```bash
python3 src/main.py --map dungeon.txt --start 1,1 --goal 20,15
python3 src/main.py --map dungeon.txt --diagonal --heuristic octile
```

---

### 115. Huffman Encoder / Decoder
**Slug:** `huffman`
**Files:**
```
src/
├── main.py
└── huffman.py
```
**Description:** Build a Huffman coding tree from character frequencies using a min-heap. Encode text to a compact bitstream. Write a binary file with a header containing the code table. Decode back to the original text. Compare compression ratio to the uncompressed size.
**Core Concepts:** `heapq`, binary tree, `bytearray` for bit packing, canonical Huffman codes, header serialization
**Difficulty:** Intermediate
**Unique Challenge:** Packing variable-length bit codes into bytes without alignment errors — maintain a `bit_buffer` integer and a `bit_count`; flush complete bytes as they fill up, and write the final partial byte with a padding count stored in the header.
**Run:**
```bash
python3 src/main.py compress input.txt output.huf
python3 src/main.py decompress output.huf recovered.txt
python3 src/main.py --stats input.txt
```

---

### 116. Polynomial Arithmetic
**Slug:** `polynomial`
**Files:**
```
src/
└── main.py
```
**Description:** A `Polynomial` class with operator overloading for addition, subtraction, multiplication, floor division, and modulo. Includes GCD via pseudo-remainder Euclidean algorithm, derivative, indefinite integral, and root-finding via Newton's method.
**Core Concepts:** OOP, `__add__`/`__mul__`/`__truediv__` operator overloading, list-based coefficient representation, Newton-Raphson root finding, polynomial GCD
**Difficulty:** Beginner
**Unique Challenge:** Implementing polynomial GCD using the pseudo-remainder Euclidean algorithm for integer-coefficient polynomials — straightforward Euclidean division accumulates fractional coefficients; pseudo-remainder avoids this by scaling before dividing.
**Run:**
```bash
python3 src/main.py
```

---

### 117. Matrix Calculator (no numpy)
**Slug:** `matrix-calc`
**Files:**
```
src/
└── main.py
```
**Description:** Matrix class with operator overloading for add, subtract, multiply, and scalar operations. Implements: transpose, determinant via LU decomposition with partial pivoting, matrix inverse, and dominant eigenvalue via the power iteration method.
**Core Concepts:** 2D nested lists, Gaussian elimination with partial pivoting, LU decomposition, power iteration, `__matmul__` (`@`)
**Difficulty:** Intermediate
**Unique Challenge:** Implementing LU decomposition with partial pivoting correctly — track the permutation vector `P` to swap rows for numerical stability, and apply the same row swaps to the right-hand side when solving `Ax = b`.
**Run:**
```bash
python3 src/main.py
```

---

### 118. Monte Carlo Simulator
**Slug:** `monte-carlo`
**Files:**
```
src/
└── main.py
```
**Description:** Three Monte Carlo experiments: (1) Estimate π using the circle-in-square method, (2) Simulate the Monty Hall problem 1 million times to prove the 2/3 win rate of switching, (3) Price European call options and compare to the Black-Scholes analytical formula. Includes antithetic variates variance reduction for π.
**Core Concepts:** `random`, `math`, convergence tracking, antithetic variates, Black-Scholes formula
**Difficulty:** Intermediate
**Unique Challenge:** Implementing antithetic variates for π estimation — for each uniform sample `u`, also use `1 - u`; the two samples are negatively correlated, which halves the estimator's variance and speeds convergence.
**Run:**
```bash
python3 src/main.py --task pi --samples 1000000
python3 src/main.py --task monty-hall --trials 1000000
python3 src/main.py --task options --S 100 --K 105 --T 1 --r 0.05 --sigma 0.2
```

---

### 119. N-Queens Solver
**Slug:** `n-queens`
**Files:**
```
src/
└── main.py
```
**Description:** Solve N-Queens using backtracking with bitmask-based O(1) conflict detection. Find one solution, all solutions, or just count them. Print solutions as ASCII boards. Compare performance vs. a naive 2D-array approach.
**Core Concepts:** Backtracking, three bitmasks (columns, left-diagonals, right-diagonals), `Integer.bit_length()` equivalent, `bin(n).count('1')` for solution counting
**Difficulty:** Intermediate
**Unique Challenge:** Replacing the 2D board with three bitmasks for O(1) conflict detection — `available = ~(cols | left_diag | right_diag) & all_ones`; iterate available positions using `pos = available & -available` (lowest set bit) to pick and clear each candidate.
**Run:**
```bash
python3 src/main.py --n 8
python3 src/main.py --n 12 --count
python3 src/main.py --n 8 --all
```

---

### 120. CPU Scheduler Simulator [RARE]
**Slug:** `cpu-scheduler`
**Files:**
```
src/
├── main.py
└── scheduler.py
```
**Description:** Simulate four CPU scheduling algorithms: FCFS, SJF (non-preemptive), Round Robin (configurable quantum), and MLFQ (Multi-Level Feedback Queue). Output a Gantt chart, and per-process metrics: waiting time, turnaround time, and response time.
**Core Concepts:** `collections.deque` for ready queues, `heapq` for SJF min-heap, time-sliced simulation loop, process state machine (NEW → READY → RUNNING → WAITING → TERMINATED), MLFQ aging
**Difficulty:** Intermediate
**Unique Challenge:** Implementing MLFQ correctly — processes start in queue 0 (highest priority, short quantum); if they use their full quantum, they demote to a lower queue. An aging mechanism promotes processes that have waited too long in low-priority queues to prevent starvation.
**Run:**
```bash
python3 src/main.py --algo rr --quantum 4 --processes processes.json
python3 src/main.py --algo mlfq --queues 3 --processes processes.json
python3 src/main.py --compare-all --processes processes.json
```

---

## 🏆 Top 10 Most Impressive Python Projects for a Portfolio

> Pick any of these and a senior engineer will have something genuinely interesting to ask you about.

| Rank | Project | Slug | Why It Impresses |
|---|---|---|---|
| 🥇 1 | Interpreter / REPL | `interpreter` | Shows you understand how programming languages work from first principles — lexer, parser, closures, environments |
| 🥈 2 | Git-like VCS | `git-clone` | Demonstrates mastery of content-addressable storage, DAGs, and file system manipulation |
| 🥉 3 | Neural Network (no libraries) | `neural-net` | Proves you understand the actual mathematics of ML, not just `model.fit()` |
| 4 | Async Event Loop from Scratch | `async-loop` | Reveals exactly what `asyncio` does under the hood — most Python devs have no idea |
| 5 | RSA from Scratch | `rsa` | Number theory + cryptography + big integers — no library shortcuts |
| 6 | SQL Subset Database Engine | `sql-engine` | Database internals most developers have never touched |
| 7 | Ray Tracer (PPM) | `ray-tracer` | 3D rendering from pure mathematics — visually impressive output from ~300 lines |
| 8 | Lisp Interpreter | `lisp` | Deep CS fundamentals: closures, TCO, quasiquote, macros |
| 9 | Tensor Engine + Autograd | `tensor-autograd` | Reinventing PyTorch's core — understanding broadcasting and autodiff at the implementation level |
| 10 | WebSocket Server (raw) | `websocket-server` | RFC-level protocol implementation — shows you read specs, not just docs |

---

## 🗂 Projects by Difficulty Count

| Difficulty | Count | Range |
|---|---|---|
| Beginner | 29 | 1–29 |
| Intermediate | 42 | 30–71 + 101, 102, 104, 107–115, 117–120 |
| Advanced | 30 | 72–100 + 103, 105, 106, 111 |

## 🏷 Tagged Projects

| Tag | Count |
|---|---|
| [CLASSIC] | 7 (Hangman, Snake, Game of Life, Minesweeper, Blackjack, Sorting Visualizer, Conway's) |
| [RARE] | 47 (projects most developers have never attempted) |

---

*Every project listed here = pure Python 3 stdlib only (unless explicitly noted) + minimal files.*
*Build them, understand them, explain them. That's what sets you apart.*
