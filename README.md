# README

## Chat with Multiple PDFs

This application allows you to interact with multiple PDF documents through a conversational interface. By uploading PDF files, you can ask questions about their contents and receive responses powered by the Google Generative AI model. The application utilizes the LangChain framework for text processing, embeddings, and conversational memory.

### Features

- Upload multiple PDF files.
- Extract and process text from PDFs.
- Generate text embeddings using the HuggingFace library.
- Create a FAISS vector store for efficient text retrieval.
- Interact with the PDFs through a conversational AI model.

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Iftekhar-w/chat-with-multiple-PDFs.git
cd chat-with-multiple-PDFs
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory and add your Google API key:

```env
GOOGLE_API_KEY=your_google_api_key
```

### Usage

1. **Run the Streamlit application**

```bash
streamlit run app.py
```

2. **Upload PDF files**

- Use the sidebar to upload your PDF documents.
- Click on the "Process" button to extract and process the text.

3. **Ask questions**

- Enter your questions in the text input field and get responses based on the content of the uploaded PDFs.

### Code Overview

- `app.py`: The main script for the Streamlit application.
- `get_pdf_text(pdf_docs)`: Extracts text from the uploaded PDF files.
- `get_text_chunks(text)`: Splits the extracted text into manageable chunks.
- `get_vectorstore(text_chunks)`: Creates a FAISS vector store from the text chunks.
- `get_conversation_chain(vectorstore)`: Sets up the conversational AI model with the vector store and memory.
- `handle_userinput(user_question)`: Handles user questions and displays responses.
- `main()`: Initializes the Streamlit app and handles the user interface.

### Dependencies

- streamlit
- python-dotenv
- PyPDF2
- langchain
- FAISS
- HuggingFaceEmbeddings
- langchain-google-genai

### Acknowledgements

This project uses the following third-party libraries:

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [LangChain](https://github.com/langchain-ai/langchain)
- [FAISS](https://github.com/facebookresearch/faiss)
- [HuggingFace](https://huggingface.co/)

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Contact

For any questions or issues, please contact mdiftekharsalam@gmail.com.

---
