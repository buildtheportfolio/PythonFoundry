"""Pure password-analysis logic used by both the Streamlit UI and tests."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass

LOWER = set("abcdefghijklmnopqrstuvwxyz")
UPPER = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = set("0123456789")
SYMBOLS = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
COMMON_PASSWORDS = {
    "password",
    "password1",
    "123456",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "letmein",
    "welcome",
    "iloveyou",
}


@dataclass(frozen=True)
class PasswordAnalysis:
    length: int
    pool_size: int
    entropy_bits: float
    effective_entropy_bits: float
    strength: str
    score: int
    common_password: bool
    repeated_pattern: bool
    sequence_pattern: bool
    keyboard_pattern: bool
    theoretical_seconds: float
    recommendations: tuple[str, ...]


def _pool_size(password: str) -> int:
    pool = 0
    if any(char in LOWER for char in password):
        pool += 26
    if any(char in UPPER for char in password):
        pool += 26
    if any(char in DIGITS for char in password):
        pool += 10
    if any(char in SYMBOLS for char in password):
        pool += len(SYMBOLS)
    # For non-ASCII characters, add their observed alphabet contribution once.
    if any(ord(char) > 127 and char.isalpha() for char in password):
        pool += 26
    return pool


def _has_sequence(password: str) -> bool:
    lowered = password.lower()
    common_sequences = (
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "9876543210",
        "qwerty",
        "asdfgh",
        "zxcvbn",
    )
    for sequence in common_sequences:
        if sequence in lowered or sequence[::-1] in lowered:
            return True
    for index in range(len(password) - 2):
        values = [ord(char) for char in password[index : index + 3]]
        if values[1] - values[0] == values[2] - values[1] and abs(values[1] - values[0]) == 1:
            return True
    return False


def _has_repetition(password: str) -> bool:
    if re.search(r"(.)\1{2,}", password):
        return True
    if len(password) >= 6 and len(set(password)) <= max(2, len(password) // 3):
        return True
    return False


def analyze_password(password: str, guesses_per_second: float = 10_000_000_000.0) -> PasswordAnalysis:
    if guesses_per_second <= 0:
        raise ValueError("guesses_per_second must be positive")

    length = len(password)
    pool_size = _pool_size(password)
    entropy = length * math.log2(pool_size) if length and pool_size else 0.0
    normalized = password.casefold()
    common = normalized in COMMON_PASSWORDS
    repetition = _has_repetition(password)
    sequence = _has_sequence(password)
    keyboard = any(token in normalized for token in ("qwerty", "asdf", "zxcv", "1q2w3e", "qazwsx"))

    penalty = 0.0
    if common:
        penalty += 35.0
    if repetition:
        penalty += min(15.0, max(3.0, length * 0.7))
    if sequence:
        penalty += 10.0
    if keyboard:
        penalty += 10.0
    if length < 12:
        penalty += (12 - length) * 1.5

    effective_entropy = max(0.0, entropy - penalty)
    if common:
        strength = "Critical"
        score = 5
    elif effective_entropy < 35:
        strength = "Weak"
        score = 25
    elif effective_entropy < 55:
        strength = "Fair"
        score = 50
    elif effective_entropy < 75:
        strength = "Strong"
        score = 75
    else:
        strength = "Very strong"
        score = 95

    if length >= 16 and effective_entropy >= 70:
        score = 100
    if not password:
        score = 0
        strength = "Not evaluated"

    guesses = 2 ** effective_entropy if effective_entropy < 1024 else float("inf")
    theoretical_seconds = guesses / guesses_per_second if math.isfinite(guesses) else float("inf")

    recommendations: list[str] = []
    if length < 12:
        recommendations.append("Use at least 12 characters; 16+ is better for high-value accounts.")
    if not any(char in LOWER for char in password):
        recommendations.append("Add lowercase letters.")
    if not any(char in UPPER for char in password):
        recommendations.append("Add uppercase letters.")
    if not any(char in DIGITS for char in password):
        recommendations.append("Add digits.")
    if not any(char in SYMBOLS for char in password):
        recommendations.append("Add symbols or use a longer passphrase.")
    if common:
        recommendations.append("Avoid common passwords and predictable variants.")
    if repetition:
        recommendations.append("Avoid repeated characters or repeated blocks.")
    if sequence:
        recommendations.append("Avoid alphabetical, numeric, or keyboard sequences.")
    if not recommendations and password:
        recommendations.append("Good composition. Prefer a unique password and store it in a password manager.")

    return PasswordAnalysis(
        length=length,
        pool_size=pool_size,
        entropy_bits=entropy,
        effective_entropy_bits=effective_entropy,
        strength=strength,
        score=score,
        common_password=common,
        repeated_pattern=repetition,
        sequence_pattern=sequence,
        keyboard_pattern=keyboard,
        theoretical_seconds=theoretical_seconds,
        recommendations=tuple(recommendations),
    )


def format_duration(seconds: float) -> str:
    if not math.isfinite(seconds):
        return "effectively infeasible at the selected rate"
    if seconds < 1:
        return "less than a second"
    units = (
        (365.25 * 24 * 3600, "year"),
        (30.44 * 24 * 3600, "month"),
        (24 * 3600, "day"),
        (3600, "hour"),
        (60, "minute"),
        (1, "second"),
    )
    for size, name in units:
        if seconds >= size:
            value = seconds / size
            return f"{value:,.1f} {name}{'' if value == 1 else 's'}"
    return "less than a second"
