import streamlit as st
from threat_detector import detect_threats, calculate_risk_score
from ai_analyzer import analyze_logs

st.set_page_config(page_title="AI Cybersecurity Advisor", layout="wide")

st.title("🛡️ AI Cybersecurity Advisor")
st.write("Upload a log file and receive AI-powered threat analysis.")

uploaded_file = st.file_uploader("Upload log file", type=["log", "txt", "csv"])

if uploaded_file:
    logs = uploaded_file.read().decode("utf-8", errors="ignore")

    st.subheader("Log Preview")
    st.text_area("Logs", logs[:5000], height=250)

    if st.button("Analyze Threats"):
        threats = detect_threats(logs)
        risk_score = calculate_risk_score(threats)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Risk Score", f"{risk_score}/100")
        with col2:
            st.metric("Threats Found", len(threats))

        st.subheader("Detected Threats")
        if threats:
            for threat in threats:
                st.warning(f"{threat['type']} ({threat['severity']})")
        else:
            st.success("No obvious threats detected.")

        with st.spinner("Generating AI report..."):
            report = analyze_logs(logs, threats, risk_score)

        st.subheader("AI Security Report")
        st.markdown(report)
