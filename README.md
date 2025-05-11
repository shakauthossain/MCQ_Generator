# MCQ Generator using Streamlit + LangChain + Groq

Generate multiple-choice questions (MCQs) from uploaded PDF, DOCX, or TXT documents using LLMs via LangChain and Groq.

---

## Features

* Upload `.pdf`, `.docx`, or `.txt` files
* Automatically extract text content
* Generate high-quality MCQs using LLMs (Groq via LangChain)
* Preview MCQs before download
* Download generated MCQs as `.pdf` or `.txt`

---

## Project Structure

```bash
MCQ_Generator/
├── file_export.py         # Handles saving MCQs to PDF/TXT
├── main.py                # Main Streamlit UI application
├── text_extractor.py      # Utility for extracting text from documents
├── prompt.py              # LLM chain setup and prompt templates
└── results/               # Directory where output files are saved
```

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MCQ_Generator.git
cd MCQ_Generator
```

### 2. Install Dependencies

Using a virtual environment is recommended.

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Edit the `prompt.py` file:

```python
api_key="your_groq_api_key_here"
```

### 4. Launch the App

```bash
streamlit run main.py
```

---

## Example Workflow

1. Upload a document (`.pdf`, `.docx`, or `.txt`).
2. Enter the number of MCQs to generate.
3. Click "Generate MCQs".
4. Review the MCQs.
5. Download the output as `.txt` or `.pdf`.

---

## Requirements (in `requirements.txt`)

* streamlit
* langchain
* langchain\_groq
* fpdf
* python-docx
* pdfplumber

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome! Please open an issue before submitting major changes.

---

## Contact

For questions or suggestions, contact: [shakauthossain0@gmail.com](mailto:shakauthossain0@gmail.com)
