from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

all_documents = []

data_folder = "data"

for file in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file)

    if file.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = file
            doc.metadata["page_number"] = doc.metadata.get("page", 0) + 1

        all_documents.extend(docs)

    elif file.endswith(".txt"):
        loader = TextLoader(file_path, encoding="utf-8")
        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = file
            doc.metadata["page_number"] = "TXT File"

        all_documents.extend(docs)

    elif file.endswith(".docx"):
        loader = Docx2txtLoader(file_path)
        docs = loader.load()

        for doc in docs:
            doc.metadata["source_file"] = file
            doc.metadata["page_number"] = "DOCX File"

        all_documents.extend(docs)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(all_documents)

embedding = HuggingFaceEmbeddings()

vector_store = FAISS.from_documents(chunks, embedding)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    result = qa_chain.invoke({"query": query})

    print("\nAnswer:\n")
    print(result["result"])

    print("\nSources:\n")

    shown = set()

    for doc in result["source_documents"]:
        source = doc.metadata.get("source_file")
        page = doc.metadata.get("page_number")

        key = f"{source}-{page}"

        if key not in shown:
            print(f"File: {source} | Page: {page}")
            shown.add(key)

    print("\n" + "=" * 50 + "\n")