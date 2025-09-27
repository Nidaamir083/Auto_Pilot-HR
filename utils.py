import streamlit as st
import re

def apply_css(theme):
    if theme == "Light":
        bg_color, user_color, bot_color, bot_border = "#FFFFFF", "#DCF8C6", "#FFFFFF", "#DDD"
        title_color, subtitle_color, user_text_color, bot_text_color = "black", "gray", "black", "black"
    elif theme == "Dark":
        bg_color, user_color, bot_color, bot_border = "#1E1E1E", "#056162", "#2A2A2A", "#444"
        title_color, subtitle_color, user_text_color, bot_text_color = "white", "lightgray", "white", "white"
    else:  # Custom
        bg_color, user_color, bot_color, bot_border = "#87F1DC", "#B6F7C1", "#FFFFFF", "#DDD"
        title_color, subtitle_color, user_text_color, bot_text_color = "black", "gray", "black", "black"

    st.markdown(f"""
        <style>
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        .stApp {{background-color: {bg_color};}}
        .chat-container {{max-width: 600px; margin: auto; padding-bottom: 100px;}}
        .message {{
            padding: 10px 15px;
            border-radius: 20px;
            margin: 10px;
            display: inline-block;
            max-width: 80%;
            word-wrap: break-word;
            font-size: 15px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.08);
        }}
        .user {{
            background-color: {user_color};
            margin-left: auto;
            display: block;
            text-align: right;
            color: {user_text_color};
        }}
        .bot  {{
            background-color: {bot_color};
            border: 1px solid {bot_border};
            margin-right: auto;
            display: block;
            text-align: left;
            color: {bot_text_color};
        }}
        div.stButton > button {{
            border-radius: 12px;
            background-color: #056162;
            color: white;
            font-weight: bold;
        }}
        .sticky-bar {{
            position: fixed; bottom: 0; left: 0; right: 0;
            background: white; padding: 10px;
            border-top: 1px solid #ddd;
            display: flex; gap: 10px; z-index: 1000; align-items: center;
        }}
        </style>
    """, unsafe_allow_html=True)

    return title_color, subtitle_color


# -------------------- NEW FUNCTION --------------------
def load_policy_texts(txt_path, chunk_size=500):
    with open(txt_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    # Split into chunks
    chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]
    return chunks

   


           
