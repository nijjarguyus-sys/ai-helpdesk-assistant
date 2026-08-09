from utils.knowledge_base import get_answer
from utils.ai import ask_ai
import streamlit as st
from datetime import datetime


# ---------- Page Configuration ----------

st.set_page_config(
    page_title="AI Help Desk Assistant",
    page_icon="💻",
    layout="wide",
)


# ---------- Session State ----------

if "messages" not in st.session_state:
    st.session_state.messages = []


def save_message(role, content):
    """Save a message to the current chat session."""
    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )


def create_chat_export():
    """Create a plain-text export of the conversation."""

    lines = [
        "AI Help Desk Assistant - Chat History",
        "=" * 40,
        "",
    ]

    for message in st.session_state.messages:
        sender = (
            "You"
            if message["role"] == "user"
            else "Assistant"
        )

        lines.append(f"{sender}:")
        lines.append(message["content"])
        lines.append("")

    return "\n".join(lines)


# ---------- Sidebar ----------

with st.sidebar:

    st.title("💻 AI Help Desk")
    st.caption("Version 1.2")

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

    st.write(
        f"Messages: {len(st.session_state.messages)}"
    )

    st.metric("Open Tickets", "12")
    st.metric("Resolved Today", "31")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

    # ---------- Export Chat ----------

    st.download_button(
        label="📥 Export Chat as Text",
        data=create_chat_export(),
        file_name=f"helpdesk-chat-{datetime.now():%Y-%m-%d}.txt",
        mime="text/plain",
        disabled=not st.session_state.messages,
        use_container_width=True,
    )


# ---------- Main Page ----------

st.title("💻 AI Help Desk Assistant")

st.subheader(
    "Your virtual IT support companion"
)

st.info(
    "Select an issue from the left sidebar "
    "and click the button below."
)


# ---------- Services and Benefits ----------

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


# ---------- Troubleshooting ----------

st.divider()


if st.button(
    "Get Troubleshooting Steps",
    use_container_width=True,
):

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


# ---------- Suggested Questions ----------

st.subheader("💡 Suggested Questions")

question = None

col1, col2, col3 = st.columns(3)


with col1:

    if st.button(
        "🔑 Reset Password",
        use_container_width=True,
    ):

        question = "How do I reset my password?"


with col2:

    if st.button(
        "🌐 VPN Problem",
        use_container_width=True,
    ):

        question = "VPN is not connecting."


with col3:

    if st.button(
        "🖨️ Printer Offline",
        use_container_width=True,
    ):

        question = "Printer is offline."


# ---------- Display Chat History ----------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------- Chat Input ----------

typed_question = st.chat_input(
    "Ask an IT question..."
)


if typed_question:

    question = typed_question


# ---------- Process Question ----------

if question:

    # Save user question

    save_message(
        "user",
        question,
    )

    with st.chat_message("user"):

        st.markdown(question)


    # Search Knowledge Base

    answer = get_answer(question)


    # Generate Response

    with st.chat_message("assistant"):

        if answer:

            response = answer

        else:

            with st.spinner("🤖 Thinking..."):

                response = ask_ai(question)

        st.markdown(response)


    # Save assistant response

    save_message(
        "assistant",
        response,
    )


# ---------- Footer ----------

st.caption(
    "Built with ❤️ using Python and Streamlit by Kuldip Singh"
)