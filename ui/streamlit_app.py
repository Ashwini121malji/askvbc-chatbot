import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(
    page_title="AskVBC",
    layout="centered"
)

# ---------- Header ----------
st.title("🧠 AskVBC")
st.caption("Simple explanations for VBC attribution decisions")

st.divider()

# ---------- Input ----------
question = st.text_input(
    "Ask a question",
    placeholder="Explain attribution for member 101"
)

ask_clicked = st.button("Ask")

# ---------- API Call ----------
if ask_clicked and question.strip():
    with st.spinner("Analyzing attribution..."):
        response = requests.post(
            API_URL,
            json={"question": question}
        )

    if response.status_code != 200:
        st.error("Something went wrong. Please try again.")
    else:
        data = response.json()

        # ---------- Main Answer ----------
        st.subheader("✅ Attribution Result")
        st.write(data["answer"])

        # ---------- Confidence ----------
        level = data["confidence_level"]["level"]
        warning = data["confidence_level"].get("warning")

        if level == "HIGH":
            st.success("🟢 High confidence")
        elif level == "MEDIUM":
            st.warning("🟡 Medium confidence")
        else:
            st.error("🔴 Low confidence")

        if warning:
            st.caption(f"⚠️ {warning}")

        # ---------- Why this decision ----------
        with st.expander("🔍 Why this decision?"):
            for reason in data["confidence_explanation"]:
                st.write(f"• {reason}")

        # ---------- Rule confidence ----------
        if "rule_confidence" in data:
            with st.expander("📊 Rule confidence breakdown"):
                st.json(data["rule_confidence"])

        # ---------- Audit Trace ----------
        with st.expander("🧾 View audit trace"):
            st.json(data["trace"])

elif ask_clicked:
    st.info("Please enter a question.")
