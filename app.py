from utils.knowledge_base import get_answer
from utils.ai import ask_ai
import streamlit as st

st.set_page_config(
    page_title="AI Help Desk Assistant",
    page_icon="💻",
    layout="wide",
)

# ---------- Sidebar ----------
with st.sidebar:
    st.title("💻 AI Help Desk")
    st.caption("Version 1.0")

    st.divider()

    st.markdown("### 👤 User")

    st.success("Status: Online")

    issue = st.selectbox(
        "Choose an IT issue",
        [
            "Password Reset",
            "VPN Problem",
            "Printer Issue",
            "Email Problem",
            "Wi-Fi Problem",
        ],
    )

    st.divider()

    st.markdown("### 📊 Support")

    st.metric("Open Tickets", "12")
    st.metric("Resolved Today", "31")

# ---------- Main Page ----------

st.title("💻 AI Help Desk Assistant")

st.subheader("Your virtual IT support companion")

st.info(
    "Select an issue from the left sidebar and click the button below."
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🔧 Common Services")

    st.write("• Password Reset")
    st.write("• VPN Support")
    st.write("• Printer Setup")
    st.write("• Email Support")
    st.write("• Network Troubleshooting")

with col2:

    st.markdown("### ⚡ Benefits")

    st.write("✔ Instant troubleshooting")

    st.write("✔ Available 24/7")

    st.write("✔ AI-powered recommendations")

    st.write("✔ Easy to use")

st.divider()

if st.button("Get Troubleshooting Steps", use_container_width=True):

    if issue == "Password Reset":

        st.success(
            "Reset your password using the company password portal."
        )

    elif issue == "VPN Problem":

        st.success(
            "Verify internet connectivity and restart the VPN client."
        )

    elif issue == "Printer Issue":

        st.success(
            "Ensure the printer is online and connected to the network."
        )

    elif issue == "Email Problem":

        st.success(
            "Verify Outlook settings and your email credentials."
        )

    elif issue == "Wi-Fi Problem":

        st.success(
            "Reconnect to Wi-Fi or restart your network adapter."
        )


''''''
question = st.text_area(
    "Describe your IT problem",
    placeholder="Example: My Outlook keeps asking for my password..."
)

if st.button("Ask AI"):

    if question.strip():

        with st.spinner("Analyzing your issue..."):

            answer = ask_ai(question)

        st.success(answer)

    else:
        st.warning("Please describe your problem.")
        st.divider()
question = st.chat_input("Ask an IT question...")
''''''

if question:

    with st.chat_message("user"):
        st.write(question)

    answer = get_answer(question)

    with st.chat_message("assistant"):

        if answer:

            st.write(answer)

        else:

            st.warning(
                "I don't know that answer yet.\n\n"
                "When Gemini is available, I'll generate an AI response."
            )
st.caption(
    "Built with ❤️ using Python and Streamlit by Kuldip Singh"
)