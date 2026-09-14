def detect_threats(log_text):
    threats = []
    text = log_text.lower()

    if text.count("failed password") > 5:
        threats.append({"type": "SSH Brute Force Attack", "severity": "High"})

    if "powershell" in text:
        threats.append({"type": "Suspicious PowerShell Activity", "severity": "Medium"})

    if "nmap" in text:
        threats.append({"type": "Port Scan Detected", "severity": "Medium"})

    return threats


def calculate_risk_score(threats):
    score = 0

    for threat in threats:
        if threat["severity"] == "High":
            score += 40
        elif threat["severity"] == "Medium":
            score += 20
        else:
            score += 10

    return min(score, 100)
