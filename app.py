import streamlit as st
import google.generativeai as genai

# Configure Google Gemini AI
GEMINI_API_KEY = ""
genai.configure(api_key=GEMINI_API_KEY)

# Streamlit UI
st.title("🚀 AI Travel Planner")
st.write("Find the best travel options between any two locations.")

# User Inputs
source = st.text_input("Enter Source Location", placeholder="e.g., New York")
destination = st.text_input("Enter Destination", placeholder="e.g., Los Angeles")

if st.button("Find Travel Options"):
    if source and destination:
        st.info(f"Fetching best travel options from {source} to {destination}...")

        # Generate travel options using AI
        prompt = f"""
        Suggest the best travel options from {source} to {destination}, including:
        - Flights (airlines, estimated cost)
        - Trains (available routes, estimated cost)
        - Buses (companies, estimated cost)
        - Cabs (Uber, Lyft, estimated fare)
        Provide the results in a structured format.
        """
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            travel_info = response.text

            # Display AI-generated travel options
            st.subheader("✈🚆🚖 Available Travel Options")
            st.markdown(travel_info)
        except Exception as e:
            st.error("⚠ Error fetching travel data. Please check your API key or try again later.")

    else:
        st.warning("⚠ Please enter both source and destination!")