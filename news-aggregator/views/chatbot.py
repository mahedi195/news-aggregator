# views/chat.py
'''

import streamlit as st
import os
import glob
import re
from datetime import datetime
from gemini import ask_gemini  # Assumes you have a function to ask Gemini

# Utility to get latest news markdown files
def get_news_files(num_files=5):
    news_dir = os.path.join(os.path.dirname(__file__), "..", "news")
    if not os.path.exists(news_dir):
        return []
    md_files = glob.glob(os.path.join(news_dir, "news_*.md"))
    md_files.sort(key=os.path.getmtime, reverse=True)
    return md_files[:num_files]  # Return the N most recent files

# Load and concatenate selected news files
def load_news_content(files):
    contents = []
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            contents.append(file.read())
    return "\n\n".join(contents)

def show():
    st.title("🗣️ Chat with News")
    st.markdown("Ask questions and get AI-powered insights from recent news stories.")

    # Option to choose number of days
    num_files = st.slider("How many past news days to include:", 1, 7, 3)
    news_files = get_news_files(num_files)

    if not news_files:
        st.warning("No news data available to chat with.")
        return

    news_text = load_news_content(news_files)

    # Ask question
    question = st.text_input("Ask something about recent news:", "What were the top issues this week?")

    if st.button("Ask AI"):
        with st.spinner("Thinking..."):
            prompt = (
                f"You are an intelligent assistant analyzing Bangladeshi news.\n"
                f"Below is the latest news content.\n"
                f"Answer the following question: \"{question}\"\n"
                f"\nNEWS CONTENT:\n{news_text}"
            )
            answer = ask_gemini(prompt)
            st.markdown("### 🧠 AI Answer:")
            st.write(answer)

    # Optionally show raw news content for context
    with st.expander("📰 Show raw news content"):
        st.text(news_text)
'''