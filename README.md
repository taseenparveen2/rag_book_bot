AI-Powered Multi-Document Q&A Bot using RAG

--> This project is a Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload and query multiple document formats such as PDF, TXT, and DOCX file.


Document Upload
      ↓
Document Loader
      ↓
Text Chunking
      ↓
Embedding Generation
      ↓
FAISS Vector Store
      ↓
User Query
      ↓
Similarity Search
      ↓
Relevant Chunks Retrieved
      ↓
LLM Response Generation
      ↓
Final Answer with Sources



Embedding Model

HuggingFace Embeddings were used because they are lightweight, open-source, and provide good semantic understanding for similarity search.

Vector Database

FAISS was used as the vector database because it is fast, easy to integrate, and suitable for local RAG applications.



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




Example Queries:

1 . Summarize this document.
2 . What are the main topics discussed?
3 .Explain the conclusion section.
4 . Which technologies are mentioned in the document?
5 .Give important points from a specific page.


Limitations:

* The chatbot may struggle with very large documents because of memory limitations.
* Scanned PDFs may not work properly if text    extraction fails.
* Retrieval quality depends on chunk size and embedding quality.
* Responses may occasionally contain hallucinations if the retrieved context is weak.
* Currently optimized mainly for English-language documents.