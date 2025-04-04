import streamlit as st
import random
from datetime import date

# --- Streamlit Page Config ---
st.set_page_config(page_title="🌞 Daily Motivation", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);  /* Dark overlay */
            z-index: -1;
        }
    </style>
""", unsafe_allow_html=True)



# --- Pre-defined Quotes ---
quotes = [
    {"text": "Believe you can and you're halfway there.", "category": "Success"},
    {"text": "Your limitation—it’s only your imagination.", "category": "Positivity"},
    {"text": "Push yourself, because no one else is going to do it for you.", "category": "Success"},
    {"text": "Sometimes later becomes never. Do it now.", "category": "Discipline"},
    {"text": "Great things never come from comfort zones.", "category": "Growth"},
    {"text": "Success doesn’t just find you. You have to go out and get it.", "category": "Success"},
    {"text": "Dream it. Wish it. Do it.", "category": "Action"},
    {"text": "Stay positive, work hard, make it happen.", "category": "Positivity"},
    {"text": "Patience is not the ability to wait, but the ability to keep a good attitude while waiting.", "category": "Patience"},
    {"text": "Difficult roads often lead to beautiful destinations.", "category": "Inspiration"}
]

# --- Session State for User Quotes ---
if "user_quotes" not in st.session_state:
    st.session_state.user_quotes = []

# --- UI Styling ---
st.title("🌞 Daily Motivational Quotes App")
st.markdown("Welcome to your daily dose of **motivation and positivity!** ✨")

# --- 1. Quote of the Day ---
st.subheader("☀️ Quote of the Day")
quote_of_day_index = date.today().toordinal() % len(quotes)
qod = quotes[quote_of_day_index]
st.info(f"📌 *{qod['text']}* \n\n_Category: {qod['category']}_")

# --- 2. Random Quote Button ---
if st.button("🎲 Show Me a Random Quote"):
    random_quote = random.choice(quotes + st.session_state.user_quotes)
    st.success(f"💬 *{random_quote['text']}* \n\n_Category: {random_quote.get('category', 'User Submitted')}_")

# --- 3. Add Your Own Quote ---
st.markdown("---")
st.subheader("✍️ Submit Your Own Quote")
user_quote = st.text_input("💡 Your Motivational Quote:")
if st.button("➕ Add Quote"):
    if user_quote.strip() != "":
        st.session_state.user_quotes.append({"text": user_quote.strip(), "category": "User"})
        st.success("✅ Quote added successfully!")
    else:
        st.warning("🚫 Please enter a valid quote.")

# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3859/3859509.png", use_container_width=True)
st.sidebar.markdown("## 💡 Motivation Tip")
st.sidebar.write("Start your day with a positive thought. Repeat: *Today is going to be amazing!* ✨")
st.sidebar.markdown("---")

# 📬 Contact Section
st.sidebar.markdown("### 📬 Contact")
st.sidebar.write("📧 [Email Us](mailto:ismailahmedshahpk@gmail.com)")
st.sidebar.write("🔗 [Connect on LinkedIn](https://www.linkedin.com/in/ismail-ahmed-shah-2455b01ba/)")
st.sidebar.write("💬 [Chat on WhatsApp](https://wa.me/923322241405)")

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='text-align: center; color: grey;'>Build with ❤️ By Ismail Ahmed Shah</p>", unsafe_allow_html=True)

st.sidebar.markdown("---")
