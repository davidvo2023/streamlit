import random
import time
import streamlit as st

# Streamed response emulator
def response_generator():
    response = random.choice([
        "Hello! How can I assist you today?",
        "I'm here to help. What would you like to know?",
        "Good day! Feel free to ask me anything.",
        "Sure thing! Let me know how I can be of service.",
        "Hi there! What's on your mind?",
        "I'm happy to chat! Do you have any questions?",
        "Yes, absolutely. Please go ahead!",
        "I'm a chatbot, always ready to help!",
        "Let’s talk! I'm here to answer your queries.",
        "How’s it going? Do you need any assistance?",
        "You can ask me anything!",
        "Hello again! Ready to chat?",
        "Hi! Need help with something specific?",
        "Sure, I can answer that. What do you want to know?",
        "I’m here! Go ahead with your question.",
        "No problem, ask me anything you'd like.",
        "Let’s dive right in. What would you like help with?",
        "I'm here 24/7! What's up?",
        "Tell me your question, and I'll do my best to answer it.",
        "Hey there! What can I help you with today?"
    ])
    for word in response.split():
        yield word + " "
        time.sleep(0.1)

# Tựa đề của ứng dụng
st.title("Chatbot")

# Khởi tạo lịch sử tin nhắn
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị các tin nhắn từ lịch sử trò chuyện mỗi khi ứng dụng chạy lại
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Hiển thị tin nhắn yêu cầu người dùng nhập trước khi gửi tin nhắn
if len(st.session_state.messages) == 0:  # Nếu chưa có tin nhắn nào trong lịch sử
    with st.chat_message("assistant"):
        st.markdown("Please enter your message...")  # Tin nhắn yêu cầu người dùng nhập

# Nhận tin nhắn từ người dùng
if prompt := st.chat_input("Type your message..."):
    # Thêm tin nhắn của người dùng vào lịch sử
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Hiển thị tin nhắn của người dùng
    with st.chat_message("user"):
        st.markdown(prompt)

    # Hiển thị phản hồi của bot
    with st.chat_message("assistant"):
        response_content = ''.join(response_generator())
        st.markdown(response_content)

    # Thêm phản hồi của bot vào lịch sử
    st.session_state.messages.append({"role": "assistant", "content": response_content})
