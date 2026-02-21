import pandas as pd

LOG_FILE = "logs/system.log"

SEVERITY_MAP = {
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3
}

def parse_logs():
    data = []

    with open(LOG_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                timestamp, level, message = parts
                severity = SEVERITY_MAP.get(level, 0)

                data.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message,
                    "severity": severity
                })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = parse_logs()
    print(df.tail())
    import pandas as pd

LOG_FILE = "logs/system.log"

SEVERITY_MAP = {
    "INFO": 1,
    "WARNING": 2,
    "ERROR": 3
}

def parse_logs():
    data = []

    with open(LOG_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                timestamp, level, message = parts
                severity = SEVERITY_MAP.get(level, 0)

                data.append({
                    "timestamp": timestamp,
                    "level": level,
                    "message": message,
                    "severity": severity
                })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = parse_logs()
    print(df.tail())