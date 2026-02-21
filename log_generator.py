import random
import time
from datetime import datetime

LOG_LEVELS = ["INFO", "WARNING", "ERROR"]
MESSAGES = [
    "User logged in",
    "File uploaded",
    "Database connection failed",
    "Multiple login attempts detected",
    "User logged out",
    "Unauthorized access attempt"
]

def generate_log():
    level = random.choice(LOG_LEVELS)

    # simulate heavy login attack burst
    if random.random() < 0.35:
        message = "Multiple login attempts detected"
    elif random.random() < 0.15:
        message = "Unauthorized access attempt"
    else:
        message = random.choice(MESSAGES)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{timestamp} | {level} | {message}"

if __name__ == "__main__":
    while True:
        log = generate_log()
        with open("logs/system.log", "a") as f:
            f.write(log + "\n")
        print(log)
        time.sleep(1)