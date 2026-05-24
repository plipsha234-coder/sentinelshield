from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, limit=5, window=10):
        self.limit = limit
        self.window = window
        self.requests = defaultdict(list)

    def is_allowed(self, ip):
        now = time.time()
        self.requests[ip] = [t for t in self.requests[ip] if now - t < self.window]

        if len(self.requests[ip]) >= self.limit:
            return False

        self.requests[ip].append(now)
        return True