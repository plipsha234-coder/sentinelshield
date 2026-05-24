from flask import Flask, request, render_template
from waf_engine import WAFEngine
from rate_limiter import RateLimiter
from logger import log_event

app = Flask(__name__)

waf = WAFEngine()
limiter = RateLimiter(limit=5, window=10)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test", methods=["POST"])
def test_request():
    ip = request.remote_addr
    user_input = request.form.get("input")

    if not limiter.is_allowed(ip):
        log_event(ip, user_input, "BLOCKED", "Rate Limit Exceeded")
        return "Blocked: Too many requests"

    result = waf.analyze(user_input)

    if "Clean" in result:
        log_event(ip, user_input, "ALLOWED", "Clean")
        return "Request Allowed"

    log_event(ip, user_input, "BLOCKED", result)
    return f"Blocked Attack Detected: {result}"

@app.route("/dashboard")
def dashboard():
    try:
        with open("logs/security.log") as f:
            logs = f.readlines()
    except:
        logs = []

    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)