import streamlit as st
from backend.main import analyze_threat

st.set_page_config(page_title="Threat Assessment System", layout="centered")

st.title("🚀 Threat Assessment System")
st.markdown("### Real-time AI-based threat detection and decision support")
st.divider()
st.subheader("Input Parameters")

col1, col2 = st.columns(2)

with col1:
    speed = st.number_input("Speed", min_value=0)
    altitude = st.number_input("Altitude", min_value=0)

with col2:
    distance = st.number_input("Distance", min_value=0)
    direction = st.selectbox("Direction", ["approaching", "hovering", "leaving"])

st.divider()

if st.button("Analyze Threat"):

    if speed == 0 or altitude == 0 or distance == 0:
        st.warning("Please fill all fields properly")
    else:
        with st.spinner("Analyzing threat..."):
            result = analyze_threat({
                "speed": speed,
                "altitude": altitude,
                "direction": direction,
                "distance": distance
            })

        st.divider()
        st.subheader("Results")

        if "error" in result:
            st.error(result["error"])
        else:

            st.markdown(f"### 🛩️ Object: **{result['object_type']}**")

            st.markdown("### Confidence")
            st.progress(result["confidence"])

            threat = result["threat_level"]

            if threat in ["CRITICAL", "HIGH"]:
                st.error(f"Threat Level: {threat}")
            elif threat == "MEDIUM":
                st.warning(f"Threat Level: {threat}")
            else:
                st.success(f"Threat Level: {threat}")

            st.markdown(f"### 🎯 Recommended Action: {result['recommended_action']}")

            st.markdown("### 🧠 Reasoning")
            for r in result["reasoning"]:
                st.write(f"- {r}")

            st.markdown("### 📝 Intelligence Report")
            st.info(result["report"])