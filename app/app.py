import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from predict import UAVIntrusionDetector


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI-Based UAV Intrusion Detection System",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI-Based UAV Intrusion Detection System")
st.caption(
    "Machine Learning Based Detection of Cyber Attacks in UAV Communication Networks"
)

st.markdown("---")


# --------------------------------------------------
# Upload Dataset
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload UAV Communication Dataset (.csv)",
    type=["csv"]
)


if uploaded_file:

    df = pd.read_csv(uploaded_file)

    detector = UAVIntrusionDetector()

    result, summary = detector.predict(df)

    result["Confidence"] = (
        result["Confidence"] * 100
    ).round(2).astype(str) + "%"

    total_packets = len(result)
    benign_packets = summary.get("Benign", 0)
    attack_packets = total_packets - benign_packets

    attack_ratio = attack_packets / total_packets


    # --------------------------------------------------
    # Threat Level
    # --------------------------------------------------

    if attack_ratio < 0.20:
        threat_level = "🟢 LOW"

    elif attack_ratio < 0.50:
        threat_level = "🟡 MEDIUM"

    else:
        threat_level = "🔴 HIGH"


    # --------------------------------------------------
    # Dashboard Cards
    # --------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📦 Total Packets",
        total_packets
    )

    c2.metric(
        "⚠️ Malicious Packets",
        attack_packets
    )

    c3.metric(
        "📈 Attack Ratio",
        f"{attack_ratio*100:.1f}%"
    )

    c4.metric(
        "Threat Level",
        threat_level
    )

    st.markdown("---")


    # --------------------------------------------------
    # Dataset Preview
    # --------------------------------------------------

    with st.expander("📂 View Uploaded Dataset"):

        st.dataframe(
            df.head(10),
            use_container_width=True
        )



    # --------------------------------------------------
    # Prediction Section
    # --------------------------------------------------

    left, right = st.columns([2.2, 1])


    with left:

        st.subheader("📝 Prediction Results")

        display = result.copy()

        display.insert(
            0,
            "Packet ID",
            range(1, len(display)+1)
        )

        display = display[
            [
                "Packet ID",
                "Prediction",
                "Confidence"
            ]
        ]

        st.dataframe(
            display,
            use_container_width=True,
            height=430
        )

        # --------------------------------------------------
    # Right Side Dashboard
    # --------------------------------------------------

    with right:

        st.subheader("📊 Attack Distribution")

        chart_df = pd.DataFrame({
            "Attack Type": list(summary.keys()),
            "Count": list(summary.values())
        })

        st.bar_chart(
            chart_df.set_index("Attack Type")
        )

        st.markdown("### 📋 Attack Summary")

        summary_df = pd.DataFrame({
            "Attack Type": list(summary.keys()),
            "Packets": list(summary.values())
        })

        st.dataframe(
            summary_df,
            hide_index=True,
            use_container_width=True,
            height=210
        )

    st.markdown("---")

    # --------------------------------------------------
    # Security Assessment
    # --------------------------------------------------

    st.subheader("🛡 Security Assessment")

    if attack_ratio < 0.20:

        st.success(
            """
### 🟢 LOW THREAT

**Assessment**

The uploaded UAV communication traffic is predominantly benign with only a small proportion of suspicious packets.

**Recommendation**

- Continue routine monitoring.
- No immediate mitigation is required.
- Maintain regular network surveillance.
"""
        )

    elif attack_ratio < 0.50:

        st.warning(
            """
### 🟡 MEDIUM THREAT

**Assessment**

Moderate suspicious activity has been detected within the uploaded traffic.

Multiple attack signatures are present and should be investigated.

**Recommendation**

- Review suspicious communication sessions.
- Verify UAV network integrity.
- Continue enhanced monitoring.
"""
        )

    else:

        st.error(
            """
### 🔴 HIGH THREAT

**Assessment**

A significant portion of the uploaded traffic has been classified as malicious.

Multiple cyber attack patterns have been identified which may compromise UAV communication.

**Recommendation**

- Immediate investigation is recommended.
- Isolate suspicious communication channels.
- Initiate appropriate mitigation and incident response procedures.
"""
        )

    st.markdown("---")

    # --------------------------------------------------
    # Model Information
    # --------------------------------------------------

    with st.expander("ℹ Model Information"):

        st.write("**Model :** XGBoost Classifier")

        st.write("**Classes Detected :**")
        st.write("- Benign")
        st.write("- DoS Attack")
        st.write("- Replay Attack")
        st.write("- Evil Twin")
        st.write("- False Data Injection")

        st.write(f"**Packets Analysed :** {total_packets}")

        st.write(f"**Attack Ratio :** {attack_ratio*100:.2f}%")

    st.markdown("---")

    st.caption(
        "Developed as part of the DRDO Machine Learning Internship | "
        "Project: AI-Based Intrusion Detection for UAV Communication Networks"
    )