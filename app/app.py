from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "activity2-web-api",
        "message": "Automated Jenkins CI/CD Build Successful",
        "version": "2.0.0"
    }), 200

@app.route("/api/status")
def status():
    return jsonify({
        "activity": "Activity 2",
        "pipeline": "Jenkins-GitHub",
        "status": "operational"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
