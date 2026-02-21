from flask import Flask, jsonify, render_template
from flask import Flask, jsonify
from log_parser import parse_logs
from anomaly_detector import feature_engineering, train_model, detect_anomalies

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/logs")
def get_logs():
    df = parse_logs()
    df = feature_engineering(df)
    train_model(df)
    df = detect_anomalies(df)

    data = df.tail(50).to_dict(orient="records")
    return jsonify(data)

@app.route("/stats")
def stats():
    df = parse_logs()
    df = feature_engineering(df)
    train_model(df)
    df = detect_anomalies(df)

    total = len(df)
    anomalies = len(df[df["anomaly"] == -1])

    return jsonify({
        "total_logs": total,
        "anomalies": anomalies
    })

if __name__ == "__main__":
    app.run(debug=True)
    
    app.run(debug=True, port=5050)