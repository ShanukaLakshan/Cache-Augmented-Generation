# Cache-Augmented Generation (CAG) System

## Overview
The Cache-Augmented Generation (CAG) System is a FastAPI-based API that leverages preloaded document contexts to answer questions using cache-augmented generation models. The system allows users to upload PDF files, processes them, and then uses those documents' content to answer questions posed by the user. The answers are generated using Gemini AI and can be translated into different languages.

## Features
- **PDF Upload**: Upload multiple PDF files for processing and extraction of text.
- **Text Chunking**: Split extracted text into chunks for better caching and faster processing.
- **Question Answering**: Use preloaded contexts to answer questions based on the content of the uploaded PDFs.
- **Multilingual Support**: Answers can be translated into different languages, including Sinhala.
- **Health Check**: An endpoint to verify the system's health status.

## Requirements
- Python 3.10 or higher
- `pip` (Python package installer)
- Virtual environment (optional but recommended)

## Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/ShanukaLakshan/Cache-Augmented-Generation.git
    cd Cache-Augmented-Generation
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables by creating a `.env` file in the root directory and adding the following variables:

    ```ini
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

5. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

   The server will start on `http://127.0.0.1:8000`.

## Endpoints

### `/health`
- **GET**: Returns the health status of the API.
- **Response**: `{"status": "OK"}`

### `/`
- **GET**: Returns a welcome message.
- **Response**: `{"message": "Welcome to the Cache-Augmented Generation API."}`

### `/upload`
- **POST**: Uploads one or more PDF files for processing.
- **Request**: Form data with the files (`files`).
- **Response**: JSON with a summary of the processed files and total chunks.

### `/document-status`
- **GET**: Returns the status of document processing, including metadata and processing time.

### `/ask-question`
- **POST**: Ask a question based on the preloaded context. The system will return the answer using the cache-augmented generation model.
- **Request**: JSON with `language` and `question` fields.
- **Response**: JSON with the translated answer.

### `/ask-question-response-sinhala`
- **POST**: Ask a question and receive the answer in Sinhala.
- **Request**: JSON with `question`.
- **Response**: JSON with the translated answer in Sinhala.

### `/clear-cache`
- **POST**: Clears the cached contexts and session state.
- **Response**: JSON with a confirmation message.

## Troubleshooting

- Ensure all dependencies are installed correctly by running `pip install -r requirements.txt`.
- Verify that the environment variable `GEMINI_API_KEY` is set correctly in the `.env` file.
- If you encounter any errors, check the logs in the terminal for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
