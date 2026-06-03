import streamlit as st
import random
import time

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Streamed response emulator
def response_generator():
    responses = [
    "Hello! How can I help you today?",
    "Hi there!",
    "Good morning!",
    "Good afternoon!",
    "Good evening!",
    "Nice to meet you!",
    "How are you doing today?",
    "What can I assist you with?",
    "I'm here to help.",
    "Feel free to ask me anything.",
    "That's interesting!",
    "Can you tell me more?",
    "I understand.",
    "I see what you mean.",
    "Thanks for sharing that.",
    "Let me think about that.",
    "That's a great question.",
    "I'm not sure, but I'll try to help.",
    "Could you clarify that?",
    "Can you provide more details?",
    "Absolutely!",
    "Of course.",
    "Certainly.",
    "No problem.",
    "I'd be happy to help.",
    "That's correct.",
    "You're right.",
    "I agree.",
    "That makes sense.",
    "Interesting perspective.",
    "Let's explore that further.",
    "Here's what I found.",
    "I can help with that.",
    "What would you like to know?",
    "Could you rephrase that?",
    "I'm learning new things every day.",
    "That's a useful observation.",
    "Tell me more about it.",
    "How does that make you feel?",
    "What happened next?",
    "I appreciate your patience.",
    "Thanks for asking.",
    "Good question!",
    "That's one way to look at it.",
    "There are several possibilities.",
    "Let's break it down.",
    "I'll do my best to explain.",
    "That depends on the situation.",
    "Can you give me an example?",
    "I understand your concern.",
    "That's understandable.",
    "I'm glad you mentioned that.",
    "Let's work through it together.",
    "Here's a simple explanation.",
    "That's a common question.",
    "Many people wonder about that.",
    "Let me provide some context.",
    "That's worth considering.",
    "Interesting idea!",
    "I hadn't thought of it that way.",
    "Could you elaborate?",
    "Let's look at the facts.",
    "I'm processing your request.",
    "One moment, please.",
    "Thanks for waiting.",
    "I think I can help.",
    "Let's find a solution.",
    "That sounds exciting.",
    "Congratulations!",
    "Well done!",
    "Good job!",
    "Keep up the great work!",
    "That's impressive.",
    "I'm happy to hear that.",
    "Sorry to hear that.",
    "I hope things improve soon.",
    "That must have been challenging.",
    "I understand why you'd feel that way.",
    "Let's see what we can do.",
    "Would you like more information?",
    "Is there anything else I can help with?",
    "I'm always here if you need assistance.",
    "Let's try another approach.",
    "That's a valid point.",
    "You raise an interesting question.",
    "I'm glad you asked.",
    "Let's continue.",
    "Could you be more specific?",
    "I'm not certain about that.",
    "I'll need more information.",
    "That sounds reasonable.",
    "Let's review the options.",
    "Thanks for the feedback.",
    "I appreciate your input.",
    "It was nice chatting with you.",
    "Have a great day!",
    "Take care!",
    "Goodbye!",
    "See you next time!"
]
    response = random.choice(
       responses
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})


