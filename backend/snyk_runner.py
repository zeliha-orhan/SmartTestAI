import subprocess
import json
import os
from datetime import datetime

SNYK_PATH = r"C:\Users\gocer\AppData\Roaming\npm\snyk.cmd"
REPORT_DIR = "reports"

def run_snyk_scan():
    try:
        result = subprocess.run(
            [SNYK_PATH, "container", "test", "flask-demo", "--json"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        try:
            data = json.loads(result.stdout)
            return data
        except json.JSONDecodeError:
            print("❌ JSON parse error:", result.stdout, result.stderr)
            return None

    except Exception as e:
        print("⚠️ Snyk çalıştırma hatası:", e)
        return None


def summarize(data):
    vulns = data.get("vulnerabilities", [])
    summary = {"critical": 0, "high": 0, "medium": 0, "low": 0}

    for v in vulns:
        sev = v.get("severity", "")
        if sev in summary:
            summary[sev] += 1
    return summary


def save_report(data, summary):
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)

    filename = f"snyk-report-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    path = os.path.join(REPORT_DIR, filename)
    with open(path, "w") as f:
        json.dump({"summary": summary, "full": data}, f, indent=2)

    return path


def run_and_return():
    """Flask içinden çağrılacak fonksiyon"""
    data = run_snyk_scan()
    if not data:
        return None, None
    summary = summarize(data)
    file_path = save_report(data, summary)
    return summary, file_path


if __name__ == "__main__":
    s, p = run_and_return()
    print("SUMMARY:", s)
    print("Saved:", p)
