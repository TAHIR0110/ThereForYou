from dataclasses import dataclass
from typing import Literal

import streamlit as st
import streamlit.components.v1 as components
from chatbot import ai_chatbot, load_dataset


@dataclass
class Message:
    """Class for keeping track of a chat message."""

    origin: Literal["human", "ai"]
    message: str


def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state.history = []
    if "dataset" not in st.session_state:
        st.session_state.dataset = load_dataset("therapy_dataset.csv")


def on_click_callback():
    user_prompt = st.session_state.human_prompt
    if user_prompt.lower() in ["hello", "hello bot"]:
        response = (
            "Hello! How are you feeling today? Please tell me more about your feelings."
        )
    else:
        response = ai_chatbot(user_prompt, st.session_state.dataset)
        if response is None:
            response = "I'm sorry, I don't understand. Can you please rephrase or provide more information?"
    st.session_state.history.append(Message("human", user_prompt))
    st.session_state.history.append(Message("ai", response))


load_css()
initialize_session_state()

st.title("Depression Support Chatbot 🤖")

chat_placeholder = st.container()
prompt_placeholder = st.form("chat-form")

with chat_placeholder:
    for chat in st.session_state.history:
        icon = "🤖" if chat.origin == "ai" else "👤"
        div = f"""
<div class="chat-row 
    {'' if chat.origin == 'ai' else 'row-reverse'}">
    <div class="chat-icon">{icon}</div>
    <div class="chat-bubble {'ai-bubble' if chat.origin == 'ai' else 'human-bubble'}">
        &#8203;{chat.message}
    </div>
</div>
        """
        st.markdown(div, unsafe_allow_html=True)

    for _ in range(3):
        st.markdown("")

with prompt_placeholder:
    st.markdown("**Chat**")
    cols = st.columns((7, 1))
    cols[0].text_input(
        "Chat",
        value="Hello bot",
        label_visibility="collapsed",
        key="human_prompt",
    )
    cols[1].form_submit_button(
        "Submit",
        type="primary",
        on_click=on_click_callback,
    )

components.html(
    """
<script>
const streamlitDoc = window.parent.document;

const buttons = Array.from(
    streamlitDoc.querySelectorAll('.stButton > button')
);
const submitButton = buttons.find(
    el => el.innerText === 'Submit'
);

streamlitDoc.addEventListener('keydown', function(e) {
    switch (e.key) {
        case 'Enter':
            submitButton.click();
            break;
    }
});
</script>
""",
    height=0,
    width=0,
)
