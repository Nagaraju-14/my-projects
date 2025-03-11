import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# ✅ Fix: Ensure __file__ is defined correctly
dotenv_path = os.path.join(os.getcwd(), ".env")  # Correct way to find .env

if os.path.exists(dotenv_path):
    print(f"✅ Found .env file at: {dotenv_path}")  # Debugging line)
    import codecs
    with codecs.open(dotenv_path, "r", encoding="utf-8", errors="ignore") as f:
       load_dotenv(dotenv_path)

    load_dotenv(dotenv_path)
else:
    raise FileNotFoundError("❌ .env file not found in the project directory!")

# ✅ Fetch API Key from .env
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("❌ Google API Key not found! Check your .env file.")
print(f"✅ API Key Loaded Successfully: {API_KEY[:5]}")  # Debugging line

# ✅ Initialize LangChain model with Gemini API
try:
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=API_KEY)
    print("✅ Gemini Model Initialized Successfully!")
except Exception as e:
    print(f"❌ Error Initializing Gemini Model: {e}")

# ✅ Streamlit App Interface
st.title("🤖 AI Data Science Tutor")
st.write("Ask your data science questions!")

# User Input
user_query = st.text_input("Enter your question:")

if user_query:
    try:
        response = llm.invoke(user_query)
        st.write("### 🤖 AI Response:")
        st.write(response)
    except Exception as e:
        st.error(f"❌ Error generating response: {e}")