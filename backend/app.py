from flask import Flask, jsonify, send_file
import os
from snyk_runner import run_and_return, REPORT_DIR

app = Flask(__name__)

@app.route("/scan", methods=["POST"])
def scan():
    summary, file_path = run_and_return()
    if not summary:
        return jsonify({"error": "scan failed"}), 500

    return jsonify({
        "message": "scan completed",
        "summary": summary,
        "report_file": file_path
    })


@app.route("/scan/latest", methods=["GET"])
def latest():
    files = os.listdir(REPORT_DIR)
    if not files:
        return jsonify({"error": "no reports found"}), 404

    latest = sorted(files)[-1]
    return send_file(os.path.join(REPORT_DIR, latest))


@app.route("/scan/file/<name>", methods=["GET"])
def file(name):
    return send_file(os.path.join(REPORT_DIR, name))


if __name__ == "__main__":
    app.run(port=5001, debug=True)
