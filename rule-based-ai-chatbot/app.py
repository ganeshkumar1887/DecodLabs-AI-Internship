import streamlit as st
import datetime

st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Rule-Based AI Chatbot")
st.write("### DecodeLabs AI Internship Project 1")

st.markdown("---")

# Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

name = st.text_input("👤 Enter Your Name")

user_input = st.text_input("💬 Ask Something")

def chatbot_response(text, name):
    text = text.lower().strip()

    if text in ["hi", "hello", "hey"]:
        return f"Hello {name}! 😊"

    elif text == "how are you":
        return "I'm doing great! 😊"

    elif text in ["your name", "what is your name"]:
        return "I am a Rule-Based AI Chatbot."

    elif text == "my name":
        return f"Your name is {name}."

    elif text == "date":
        return str(datetime.date.today())

    elif text == "time":
        return datetime.datetime.now().strftime("%I:%M:%S %p")

    elif text == "day":
        return datetime.datetime.now().strftime("%A")

    elif text == "python":
        return "Python is a programming language widely used in AI."

    elif text in ["ai", "artificial intelligence"]:
        return "Artificial Intelligence enables machines to think and solve problems."

    elif text == "joke":
        return "😂 Why do programmers love Python? Because it's easy to understand."

    elif text == "motivate me":
        return "🌟 Success comes to those who never stop learning."

    elif text == "help":
        return """
Available Commands:

• hello
• how are you
• your name
• my name
• date
• time
• day
• python
• ai
• joke
• motivate me
• calculate 10+20
"""

    elif text.startswith("calculate"):
        try:
            expression = text.replace("calculate", "").strip()
            result = eval(expression)
            return f"Answer = {result}"
        except:
            return "Invalid Expression."

    elif text in ["bye", "exit", "quit"]:
        return "👋 Goodbye! Have a Nice Day."

    else:
        return "Sorry, I don't understand that. Type 'help'."

if st.button("Send"):

    if name == "":
        st.warning("Please Enter Your Name")
    elif user_input == "":
        st.warning("Please Enter Message")
    else:

        bot = chatbot_response(user_input, name)

        st.session_state.chat_history.append(
            ("You", user_input)
        )

        st.session_state.chat_history.append(
            ("Bot", bot)
        )

st.markdown("---")

st.subheader("💬 Chat History")

for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.success(f"🧑 {message}")
    else:
        st.info(f"🤖 {message}")