from openai import OpenAI
import streamlit as st

PROMPT_TEMPLATE = '''
You are a senior cybersecurity analyst.

Analyze the supplied logs and detected threats.

Provide:
1. Executive Summary
2. Threat Analysis
3. Severity Assessment
4. Plain-English Explanation
5. Mitigation Recommendations
6. Incident Response Plan

Detected Threats:
{threats}

Risk Score:
{risk_score}/100

Logs:
{logs}
'''

def analyze_logs(logs, threats, risk_score):
    api_key = st.secrets.get("OPENAI_API_KEY", None)

    if not api_key:
        return "⚠️ Add OPENAI_API_KEY to Streamlit Secrets before deployment."

    client = OpenAI(api_key=api_key)

    prompt = PROMPT_TEMPLATE.format(
        threats=threats,
        risk_score=risk_score,
        logs=logs[:12000]
    )

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
