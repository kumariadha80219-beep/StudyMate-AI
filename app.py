import streamlit as st

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚"
)

st.title("📚 StudyMate AI")
st.subheader("Private On-Device AI Study Companion")

st.write(
    "Upload your study material and use AI to understand, "
    "summarize and revise your notes."
)

uploaded_file = st.file_uploader(
    "Upload your study PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

question = st.text_input(
    "Ask a question about your study material:"
)

if st.button("Ask AI"):
    if question:
        st.info("AI response will appear here.")
    else:
        st.warning("Please enter a question.")
