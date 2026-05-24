import re
from rules import RULES

class WAFEngine:

    def analyze(self, request_text):
        detected = []

        for attack_type, patterns in RULES.items():
            for pattern in patterns:
                if re.search(pattern, request_text):
                    detected.append(attack_type)
                    break

        return detected if detected else ["Clean"]