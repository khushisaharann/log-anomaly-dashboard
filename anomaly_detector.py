import pandas as pd
from sklearn.ensemble import IsolationForest
from log_parser import parse_logs

model = IsolationForest(contamination=0.1, random_state=42)

def feature_engineering(df):
    df["is_login_attempt"] = df["message"].apply(
        lambda x: 1 if "login" in x.lower() else 0
    )
    
    df["is_error"] = df["level"].apply(
        lambda x: 1 if x == "ERROR" else 0
    )
    
    return df

def train_model(df):
    features = df[["severity", "is_login_attempt", "is_error"]]
    model.fit(features)

def detect_anomalies(df):
    features = df[["severity", "is_login_attempt", "is_error"]]
    df["anomaly"] = model.predict(features)
    return df

if __name__ == "__main__":
    df = parse_logs()
    df = feature_engineering(df)

    train_model(df)
    result = detect_anomalies(df)

    print(result.tail(15))