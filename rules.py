import re

RULES = {
    "SQL Injection": [
        r"(\%27)|(')|(--)|(%23)|(#)",
        r"(?i)(union\s+select)",
        r"(?i)(or\s+1=1)"
    ],
    "XSS": [
        r"(?i)<script.*?>",
        r"(?i)javascript:",
        r"(?i)onerror="
    ],
    "Command Injection": [
        r"(;|\||&&)\s*(ls|cat|whoami|dir)",
    ],
    "LFI": [
        r"(\.\./|\.\.\\)"
    ]
}