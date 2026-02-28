# TalentScout -- AI Hiring Assistant 🤖

An intelligent AI-powered Hiring Assistant chatbot built using Streamlit
and Groq LLM. The system automates the initial screening process for
technical candidates by collecting information, validating skills,
generating relevant technical questions, and recording responses.

------------------------------------------------------------------------

## 📌 Project Overview

TalentScout is a fictional recruitment agency specializing in technology
placements.

This chatbot is designed to:

-   Greet candidates professionally
-   Collect structured candidate details
-   Extract and validate technical skills using an LLM
-   Generate tailored technical interview questions
-   Collect candidate answers sequentially
-   Maintain structured conversation state
-   Conclude the screening process gracefully

The system demonstrates controlled LLM integration within a
deterministic conversational workflow.

------------------------------------------------------------------------

## 🎯 Objectives

-   Demonstrate prompt engineering capability
-   Maintain context-aware interactions
-   Build a clean conversational UI
-   Ensure structured and safe LLM usage
-   Prevent hallucination and uncontrolled responses

------------------------------------------------------------------------

## 🧠 Core Features

### 1. Structured Candidate Information Collection

The chatbot collects:

-   Full Name
-   Email Address
-   Phone Number
-   Years of Experience
-   Desired Position
-   Current Location
-   Technical Skills

All handled using stage-based state management (no LLM guessing).

------------------------------------------------------------------------

### 2. Intelligent Skill Extraction

-   Accepts raw user input for skills
-   LLM extracts only valid technical skills
-   Ignores irrelevant or non-technical terms
-   Does NOT hallucinate or assume missing skills
-   Returns structured JSON output

Example LLM Output:

``` json
{
  "is_questions": true,
  "skills": ["Python", "Django"],
  "questions": [
    "Explain Python decorators.",
    "What is Django ORM?",
    "How does middleware work in Django?"
  ]
}
```

------------------------------------------------------------------------

### 3. Dynamic Technical Question Generation

-   Generates 3--5 professional technical questions
-   Questions are skill-specific
-   Focuses on practical understanding
-   Output is strictly structured JSON

------------------------------------------------------------------------

### 4. Controlled Question-Answer Flow

-   Questions are asked one-by-one
-   Each answer is stored sequentially
-   Context maintained using session state

------------------------------------------------------------------------

### 5. State-Based Conversation Architecture

Stages: - greeting - collect_name - collect_email - phone - experience -
position - location - skills - answering - completed

This ensures deterministic and predictable behavior.

------------------------------------------------------------------------

## 🏗️ Architecture

User Input\
→ Stage Transition\
→ LLM Processing (skill extraction + question generation only)\
→ Structured JSON Response\
→ Session Memory Update

No vector databases, embeddings, RAG, or agent orchestration are used.

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python
-   Streamlit
-   Groq LLM API
-   LangChain (ChatPromptTemplate + Runnable)
-   Session-based memory (Streamlit session state)

------------------------------------------------------------------------

## 📁 Project Structure

TalentScout/ 
│ 
├── main.py      ( Streamlit application )
├── services.py  ( LLM integration logic )
├── prompts.py   ( System prompt definitions )
├──requirements.txt
├── CSS.py 
└── README.md

------------------------------------------------------------------------

## 🔐 Data Handling & Privacy

-   Candidate data stored only in session memory
-   No permanent storage unless enabled
-   API keys stored via environment variables
-   No sensitive information exposed publicly

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1. Clone Repository

git clone https://github.com/surya-vennapu/TalentScout-Hiring-Assistant-.git

cd TalentScout

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Set Environment Variable

Open a `.env` file and replace with your api key:

GROQ_API_KEY=your_api_key_here

### 4. Run Application

streamlit run main.py

------------------------------------------------------------------------

## 🚧 Challenges & Solutions

  Challenge                        Solution
  -------------------------------- -------------------------------
  Preventing hallucinated skills   Strict system prompt rules
  Maintaining conversation flow    Stage-based state machine
  JSON parsing reliability         Structured output enforcement
  Streamlit rerun behavior         Proper execution order

------------------------------------------------------------------------

## 📊 Evaluation Alignment

This project satisfies:

-   Technical Proficiency
-   Prompt Engineering
-   Context Management
-   UI & User Experience
-   Clean Code Structure

------------------------------------------------------------------------

## 👨‍💻 Author

Surya Vennapu\
AI/ML Enthusiast \| Backend Developer \| LLM Application Builder

------------------------------------------------------------------------

## ✅ Conclusion

This project demonstrates how Large Language Models can be integrated
into structured conversational systems for real-world hiring automation
while maintaining control, reliability, and architectural clarity.
