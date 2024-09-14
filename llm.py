import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import csv
from difflib import get_close_matches

def load_data(file_path):
    questions_answers = {}
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            questions_answers[row['prompt']] = row['response']
    return questions_answers

def initialize_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-pro",api_key="")
    return llm

def ask_model(llm, question):
    prompt = f"Provide a concise answer to the following question: {question}"
    response = llm.invoke(prompt)
    if hasattr(response, 'content'):
        return response.content.strip() 
    elif isinstance(response, dict) and 'content' in response:
        return response['content'].strip()  
    else:
        return str(response).strip() 

def find_closest_match(user_question, questions_answers):
    questions = list(questions_answers.keys())
    close_matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    if close_matches:
        return close_matches[0], questions_answers[close_matches[0]].strip()
    else:
        return None, None

def main():
    st.title("EdTech Query Assistant")

    st.write("Ask me anything about the courses on our platform!")

    file_path = "FAQs.csv" 
    try:
        questions_answers = load_data(file_path)
    except FileNotFoundError as e:
        st.error(str(e))
        return

    question = st.text_input("Enter your question:")

    if st.button("Get Answer"):
        if question:
            closest_question, csv_answer = find_closest_match(question, questions_answers)

            if csv_answer:
                st.write(f"Answer: {csv_answer}")
            else:
                llm = initialize_llm()
                generated_answer = ask_model(llm, question)
                st.write(f"Answer: {generated_answer}")
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
