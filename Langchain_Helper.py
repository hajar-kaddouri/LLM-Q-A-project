
import os

from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_google_genai import GoogleGenerativeAI
from  dotenv import load_dotenv
load_dotenv()


os.environ["GOOGLE_API_KEY"]= ""
# Create Google Gen LLM model
llm = GoogleGenerativeAI(google_api_key= os.environ["GOOGLE_API_KEY"], model="gemini-1.5-flash")


# Use SentenceTransformer with LangChain's embedding wrapper
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb_file_path = "faiss_index"

# Create FAISS vector store from documents
def create_vector_db(): 
  
    loader =CSVLoader(file_path= 'codebasics_faqs.csv', source_column = 'prompt',encoding='latin-1')  # or 'cp1252', 'ISO-8859-1')

    data = loader.load()

    vectordb = FAISS.from_documents(documents=data, embedding=embedding_model)

    vectordb.save_local(vectordb_file_path)


def get_qa_chain():
        # Load the vector database from the local folder
        # Set allow_dangerous_deserialization=True to load the index
    vectordb = FAISS.load_local(vectordb_file_path, embedding_model, allow_dangerous_deserialization=True)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain


if __name__ == "__main__":
    create_vector_db() # Calling the function name
    chain = get_qa_chain()
    print(chain("Do you have javascript course?"))
