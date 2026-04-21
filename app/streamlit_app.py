import streamlit as st
from backend.main import analyze_threat
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

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

            # ✅ CONFIDENCE WITH PERCENTAGE
            confidence_percent = int(result["confidence"] * 100)
            st.markdown(f"### Confidence: {confidence_percent}%")
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

            def format_report_text(text, styles):
                # Remove markdown symbols like **
                text = text.replace("**", "")

                # Split into sentences for better readability
                sentences = text.split(". ")

                formatted = []
                current_para = ""

                for i, sentence in enumerate(sentences):
                    current_para += sentence.strip() + ". "

                    # Break every 2 sentences into a paragraph
                    if (i + 1) % 2 == 0:
                        formatted.append(Paragraph(current_para.strip(), styles["Normal"]))
                        formatted.append(Paragraph("<br/>", styles["Normal"]))
                        current_para = ""

                if current_para:
                    formatted.append(Paragraph(current_para.strip(), styles["Normal"]))

                return formatted

            # ✅ PDF DOWNLOAD FEATURE
            def create_pdf(result):
                buffer = io.BytesIO()
                doc = SimpleDocTemplate(buffer)
                styles = getSampleStyleSheet()

                content = []

                # Title
                content.append(Paragraph("THREAT ASSESSMENT REPORT", styles["Title"]))

                # Spacer
                content.append(Paragraph("<br/><br/>", styles["Normal"]))

                # Object info
                content.append(Paragraph(
                    f"<b>Object:</b> {result['object_type'].upper()}",
                    styles["Normal"]
                ))

                confidence_percent = int(result["confidence"] * 100)
                content.append(Paragraph(
                    f"<b>Confidence:</b> {confidence_percent}%",
                    styles["Normal"]
                ))

                content.append(Paragraph("<br/>", styles["Normal"]))

                # Threat level
                content.append(Paragraph(
                    f"<b>Threat Level:</b> {result['threat_level']}",
                    styles["Heading2"]
                ))

                content.append(Paragraph("<br/>", styles["Normal"]))

                # Summary
                content.append(Paragraph("<b>Summary:</b>", styles["Heading3"]))
                formatted_summary = format_report_text(result["report"], styles)
                for para in formatted_summary:
                    content.append(para)

                content.append(Paragraph("<br/>", styles["Normal"]))

                # Reasoning
                content.append(Paragraph("<b>Key Reasoning:</b>", styles["Heading3"]))
                for r in result["reasoning"]:
                    content.append(Paragraph(f"- {r}", styles["Normal"]))

                content.append(Paragraph("<br/>", styles["Normal"]))

                # Action
                content.append(Paragraph("<b>Recommended Action:</b>", styles["Heading3"]))
                content.append(Paragraph(result["recommended_action"], styles["Normal"]))

                content.append(Paragraph("<br/><br/>", styles["Normal"]))

                # Footer
                content.append(Paragraph(
                    "<i>Generated by Threat Assessment System</i>",
                    styles["Normal"]
                ))

                doc.build(content)
                buffer.seek(0)
                return buffer

            pdf_file = create_pdf(result)

            st.download_button(
                label="📄 Download Report as PDF",
                data=pdf_file,
                file_name="intelligence_report.pdf",
                mime="application/pdf"
            )