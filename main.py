import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMChain

from prompt import mcq_prompt
from text_extractor import extract_text
from file_export import save_txt, save_pdf


# LangChain setup
llm = ChatGroq(
    api_key="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",  # Replace with your API key
    model="llama-3.3-70b-versatile",
    temperature=0.0
)

mcq_chain = LLMChain(llm=llm, prompt=mcq_prompt)

# Streamlit UI
st.title("MCQ Generator from PDF / Word / Text")
uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])
num_questions = st.number_input("Number of MCQs to Generate", min_value=1, max_value=100, value=5)

if uploaded_file:
    file_name = uploaded_file.name
    try:
        with st.spinner("Extracting text..."):
            text = extract_text(file_name, uploaded_file)

        if st.button("Generate MCQs"):
            with st.spinner("Generating MCQs..."):
                mcqs = mcq_chain.run({"context": text, "num_questions": num_questions}).strip()

                # Show the generated MCQs in the app before download
                st.subheader("📄 Generated MCQs")
                st.text_area("Preview", mcqs, height=400)

                # Save and offer download buttons
                base_name = file_name.rsplit('.', 1)[0]
                txt_path = save_txt(mcqs, f"generated_mcqs_{base_name}.txt")
                pdf_path = save_pdf(mcqs, f"generated_mcqs_{base_name}.pdf")

                with open(txt_path, "rb") as f:
                    st.download_button("Download MCQs (TXT)", f, file_name=f"generated_mcqs_{base_name}.txt")

                with open(pdf_path, "rb") as f:
                    st.download_button("Download MCQs (PDF)", f, file_name=f"generated_mcqs_{base_name}.pdf")

                st.success("MCQ Generation Complete!")

    except Exception as e:
        st.error(f"Error: {str(e)}")
