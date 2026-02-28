import streamlit as st
from CSS import styles
from services import generate_questions, is_valid_email, is_valid_phone


st.set_page_config(page_title="TalentScout Hiring Assistant")
st.title("TalentScout Hiring Assistant 🤖")

st.markdown( styles , unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.stage = "greeting"
    st.session_state.candidate_info = {}

# Function to add bot message
def bot_message(text):
    st.session_state.messages.append({"role": "assistant", "content": text})

# Function to add user message
def user_message(text):
    st.session_state.messages.append({"role": "user", "content": text})

# Greeting (only first time)
if st.session_state.stage == "greeting":
    bot_message("👋 Hello! Welcome to TalentScout Hiring Assistant.\n\n I will help you with the initial screening process.\n\nLet's begin. What is your full name?")
    st.session_state.stage = "collect_name"



if st.session_state.stage != "completed":
    prompt = st.chat_input("Type your response here...")
else:
    prompt = None

if prompt:

    user_message(prompt)

    if st.session_state.stage == "collect_name":
        st.session_state.candidate_info["name"] = prompt
        bot_message(f"Nice to meet you, {prompt} 😊\n\n Please enter your email address.")
        # bot_message("Please enter your email address.")
        st.session_state.stage = "collect_email"

    elif st.session_state.stage == "collect_email":
        if is_valid_email(prompt):
            st.session_state.candidate_info["email"] = prompt
            bot_message("Please enter your phone number.")
            st.session_state.stage = "phone"
        else:
            bot_message("That doesn't look like a valid email. Please enter a valid email address.")

    elif st.session_state.stage == "phone":
        if is_valid_phone(prompt):
            st.session_state.candidate_info["phone"] = prompt
            bot_message("Please enter your Experience in years.")
            st.session_state.stage = "experience"
        else:
            bot_message("That doesn't look like a valid phone number. Please enter a valid 10-digit phone number starting with 6-9.")

    elif st.session_state.stage == "experience":
        if prompt.isdigit() and 0 <= int(prompt) <= 50:
            st.session_state.candidate_info["experience"] = prompt
            bot_message("Please enter your Desired position.")
            st.session_state.stage = "position"
        else:
            bot_message("Please enter a valid number for years of experience (0-50).")

    elif st.session_state.stage == "position":
        st.session_state.candidate_info["position"] = prompt
        bot_message("Please enter your current location.")
        st.session_state.stage = "location"

    elif st.session_state.stage == "location":
        st.session_state.candidate_info["location"] = prompt
        bot_message("Please enter your technical skills (comma separated).")
        st.session_state.stage = "skills"

    elif st.session_state.stage == "skills":

        # Call LLM with raw user input
        result = generate_questions(prompt)

        if result["is_questions"]:

            # Save cleaned skills
            st.session_state.candidate_info["skills"] = result["skills"]

            # Save generated questions
            st.session_state.questions = result["questions"]
            st.session_state.answers = []
            st.session_state.current_question_index = 0

            bot_message(
                f"Based on your skill set: {', '.join(result['skills'])}, "
                f"please answer the following {len(result['questions'])} questions:"
            )

            # Ask first question
            bot_message(result["questions"][0])
            st.session_state.stage = "answering"
            result["is_questions"] = False


        else:
            bot_message("No valid technical skills were found. Please enter valid technical skills.")
        
    elif st.session_state.stage == "answering":

        # Save user's answer
        st.session_state.answers.append(prompt)
        st.session_state.current_question_index += 1

        if st.session_state.current_question_index < len(st.session_state.questions):
            # Ask next question
            next_q = st.session_state.questions[st.session_state.current_question_index]
            bot_message(next_q)

        if st.session_state.current_question_index == len(st.session_state.questions):
            # All questions answered
            st.session_state.candidate_info["answers"] = st.session_state.answers
            bot_message("Thank you for completing the technical screening.")
            bot_message("Our team will review your responses and contact you soon.")
            st.session_state.stage = "completed"
            
    else:
        bot_message("No valid technical skills were found. Please enter valid technical skills.")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
