from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import random

# Load API key and configure Gemini
def configure_gemini():
    load_dotenv()
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Function to provide daily motivational quotes
def get_motivational_quote():
    quotes = [
        "Believe in yourself, take on your challenges, and dig deep within to conquer fears.",
        "You are braver than you believe, stronger than you seem, and smarter than you think.",
        "Sometimes the bravest thing you can do is ask for help. You are never alone.",
        "Your mental health is a priority, your happiness is essential, and your self-care is a necessity.",
        "You are capable of amazing things, even when it feels hard."
    ]
    return random.choice(quotes)

# Frontend for the application
def main():
    configure_gemini()

    # Streamlit Page Configurations
    st.set_page_config(page_title="Mental Health Support Assistant", page_icon=":brain:", layout="centered")

    # Styling with CSS for cool look
    st.markdown("""
        <style>
            body {
                background-color: #e6f7ff;
            }
            .main-title {
                # font-family: 'Helvetica Neue', sans-serif;
                font-family: 'Raleway', sans-serif;
                color: #F27BBD;
                text-align: center;
                font-size: 42px;
                font-weight: bold;
                margin-top: 30px;
            }
            .sub-title {
                font-family: 'Courier New', monospace;
                color: #EECEB9;
                text-align: center;
                font-size: 24px;
                margin-bottom: 30px;
            }
            .message-box {
                background-color: #ffffff;
                border: 2px solid #dcdcdc;
                border-radius: 15px;
                padding: 25px;
                margin-top: 20px;
                font-family: 'Arial', sans-serif;
            }
            .button-box {
                text-align: center;
                margin-top: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown('<h1 class="main-title">🧑🏻‍⚕️AI Mental Health Support Assistant❤️‍🩹</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-title">Let’s talk about your well-being</h2>', unsafe_allow_html=True)

    # Motivational quote at the top
    st.markdown(f"**Daily Motivation:** _{get_motivational_quote()}_")

    # Mood selection dropdown
    mood = st.selectbox("How are you feeling today?", 
                        ("Select your mood", "Happy", "Sad", "Stressed", "Anxious", "Overwhelmed", "Confused"))

    # Input area for user question/concern
    user_input = st.text_area("Share what's on your mind", placeholder="Type your question or concern here...", height=200)

    # Provide personalized tips based on mood selection
    if mood != "Select your mood":
        tips = {
            "Happy": "It's great that you're feeling happy! Keep spreading positivity and focus on things that bring joy.",
            "Sad": "It's okay to feel sad. Take a break, talk to someone, or engage in something that makes you feel comforted.",
            "Stressed": "Managing stress is important. Try deep breathing exercises, breaks, and focus on one task at a time.",
            "Anxious": "Anxiety can be tough. Practice mindfulness, deep breathing, or focus on grounding yourself.",
            "Overwhelmed": "It's okay to feel overwhelmed. Try breaking tasks into smaller steps, and ask for help if needed.",
            "Confused": "Confusion is normal. Don't hesitate to ask for clarity, and try organizing your thoughts or ideas."
        }
        st.info(tips[mood])

    # Display generated content after user submits
    if st.button("Get Support"):
        if user_input:
            # System message with query context
            system_message = f"""
            You are a virtual assistant designed to offer mental health and emotional support to students. Your role is to listen carefully, respond empathetically, and provide helpful guidance for stress, anxiety, academic pressure, and emotional well-being. The query given to you is: {user_input}
            """
            
            # Gemini model response
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(user_input)
            
            # Display the AI response
            # st.markdown('<div class="message-box"><strong>Support Response:</strong><br>' + response.text + '</div>', unsafe_allow_html=True)
            st.subheader("Support Response:")
            st.write(response.text)
        else:
            st.warning("Please enter your question or concern.")

    # Section for additional tips on managing stress, anxiety, or well-being
    st.markdown("### Additional Well-being Tips")
    st.markdown("""
    - **Take deep breaths**: When feeling stressed or anxious, practice slow, deep breathing to calm your mind.
    - **Get enough sleep**: Good rest is crucial for mental health and overall well-being.
    - **Stay connected**: Reach out to friends, family, or a counselor when you need to talk.
    - **Mindful breaks**: Take breaks during study or work to clear your mind and reduce burnout.
    - **Exercise**: Physical activity, even light exercise, can significantly improve mood and reduce stress.
    """)

# Run the app
if __name__ == "__main__":
    main()
