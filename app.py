from utils.knowledge_base import get_answer
from utils.ai import ask_ai
import streamlit as st

st.set_page_config(

    page_title="AI Help Desk Assistant",
    page_icon="💻",
    layout="wide",
)
if "messages" not in st.session_state:
    st.session_state.messages = []
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
    st.sidebar.write(f"Messages: {len(st.session_state.messages)}")
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

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
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.subheader("💡 Suggested Questions")
question = None
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔑 Reset Password"):
        question = "How do I reset my password?"

with col2:
    if st.button("🌐 VPN Problem"):
        question = "VPN is not connecting."

with col3:
    if st.button("🖨 Printer Offline"):
        question = "Printer is offline."


typed_question = st.chat_input("Ask an IT question...")

if typed_question:
    question = typed_question
if question:
    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Search knowledge base
    answer = get_answer(question)

    # Decide response
    if answer:
        response = answer
    else:
        with st.spinner("🤖 Thinking..."):
            response = ask_ai(question)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

st.caption(
    "Built with ❤️ using Python and Streamlit by Kuldip Singh"
)