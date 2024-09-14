# 🚀 Tech Query Assistant: Your Ultimate Course Information Companion! 📚🤖

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-brightgreen)](https://streamlit.io)
[![Langchain](https://img.shields.io/badge/Langchain-GeminiAI-orange)](https://www.langchain.com)

## Overview

**Tech Query Assistant** is an AI-powered web app designed to help users quickly find course information. It combines a static FAQ lookup with dynamic AI-generated responses, ensuring users get the information they need, whether from a pre-defined dataset or advanced AI insights.

### 🌟 Features:

- **FAQ Lookup**: Instantly searches a CSV file of frequently asked questions.
- **AI-Powered Insights**: Utilizes Google’s Gemini LLM to generate responses if the question is not in the FAQ.
- **Streamlit Interface**: A user-friendly web application that provides a seamless experience.
- **Error Handling**: Robust validation of user input and file availability to ensure smooth operation.


### Requirements 🛠️
```bash
- pip install streamlit==1.25.0
- pip install langchain-google-genai==0.0.2
- pip install google-cloud==0.34.0
- pip install python-dotenv==0.21.0
- pip install difflib
```
## Demo

👉 Check out the live demo: [Tech Query Assistant](https://www.linkedin.com/feed/update/urn:li:activity:7240699837174702080/) 

## Key Technologies

- **Streamlit**: Front-end framework to build an interactive web interface.
- **Google Gemini AI (via Langchain)**: Provides natural language understanding and AI-generated responses.
- **CSV File Handling**: Stores and processes the FAQ dataset for static queries.
- **Python**: Core programming language used throughout the project.

## Project Structure

```bash
├── app.py                   # Main app file to run the Streamlit application
├── faq.csv                  # CSV file containing frequently asked questions
└── README.md                # Project documentation (this file)
