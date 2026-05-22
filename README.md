AI-Powered Multi-Document Q&A Bot using RAG

--> This project is a Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload and query multiple document formats such as PDF, TXT, and DOCX file.



#Rag pipeline
                ┌────────────────────┐
                │  User Uploads File │
                │ PDF / TXT / DOCX   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Document Loaders   │
                │ PyPDF / TXT / DOCX │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Text Chunking      │
                │ Recursive Splitter │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Generate Embeddings│
                │ HuggingFace Model  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Store in FAISS DB  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ User Question      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Similarity Search  │
                │ Retrieve Chunks    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ LLM Generation     │
                │ Groq + Llama 3.1   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Final Answer       │
                └────────────────────┘



# Setup Instructions

## 1. Clone the Repository

```bash
git clone <your-repository-url>

cd document-qa-bot


python -m venv venv

.venv\Scripts\activate

##Install Dependencies
pip install -r requirements.txt

#Create a .env File

Create a .env file in the root directory and add:

##GROQ_API_KEY=your_groq_api_key

##Run the Application
streamlit run app.py