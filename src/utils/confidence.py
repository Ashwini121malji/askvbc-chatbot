import os
import yaml

CONFIG_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../config/app_config.yaml"
)

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

WEIGHTS = config["confidence"]["weights"]
THRESHOLDS = config["confidence"]["thresholds"]

def calculate_confidence(data: dict) -> tuple[float, list[str], dict]:
    score = 0.0
    explanation = []
    rule_confidence = {}

    if data.get("attribution_type") == "DIRECT":
        score += 0.4
        explanation.append("DIRECT attribution contributes 0.4 to confidence.")
        rule_confidence["ATTRIBUTION_MODEL:DIRECT"] = 0.4

    if data.get("provider_id"):
        score += 0.2
        explanation.append("Provider present adds 0.2 to confidence.")
        rule_confidence["PROVIDER_PRESENT"] = 0.2

    if data.get("member_state") == data.get("provider_state"):
        score += 0.15
        explanation.append("Member and provider state match adds 0.15.")
        rule_confidence["STATE_MATCH"] = 0.15

    if data.get("rule_applied"):
        score += 0.1
        explanation.append("Delegation rule applied adds 0.1.")
        rule_confidence[f"DELEGATION_RULE:{data['rule_applied']}"] = 0.1

    return round(score, 2), explanation, rule_confidence


def classify_confidence(score: float) -> dict:
    if score >= 0.8:
        return {"level": "HIGH", "warning": None}
    elif score >= 0.6:
        return {"level": "MEDIUM", "warning": "Review recommended"}
    else:
        return {"level": "LOW", "warning": "Manual review required"}

def generate_confidence_summary(confidence: float, level: str, signals: list[str]) -> str:
    """
    Generates a short business-friendly summary explaining confidence.
    """

    if level == "HIGH":
        tone = "High confidence attribution due to"
    elif level == "MEDIUM":
        tone = "Moderate confidence attribution based on"
    else:
        tone = "Low confidence attribution due to limited"

    # Pick top 2–3 strongest signals
    key_signals = ", ".join(signals[:3])

    return f"{tone} {key_signals}."
