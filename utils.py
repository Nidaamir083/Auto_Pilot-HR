import streamlit as st

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
        /* Hide Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}

        /* Page Background */
        .stApp {{background-color: {bg_color};}}

        /* Chat Bubble Styling */
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

        /* Button Styling */
        div.stButton > button {{
            border-radius: 12px;
            background-color: #056162;
            color: white;
            font-weight: bold;
        }}

        /* Sticky Input Bar */
        .sticky-bar {{
            position: fixed; bottom: 0; left: 0; right: 0;
            background: white; padding: 10px;
            border-top: 1px solid #ddd;
            display: flex; gap: 10px; z-index: 1000; align-items: center;
        }}
        </style>
    """, unsafe_allow_html=True)

    return title_color, subtitle_color

           
