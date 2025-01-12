import os
import logging
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

def process_pdf(pdf_file):
    """
    Processes the uploaded PDF to extract and translate text,
    then formats it into chunks for caching.
    """
    loader = PyPDFLoader(pdf_file)
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=150)
    context = []
    chunk_count = 0

    for page in pages:
        chunks = text_splitter.split_text(page.page_content)
        context.extend(chunks)
        chunk_count += len(chunks)

    logger.info(f"Processed {chunk_count} chunks from {pdf_file}")
    return context, chunk_count
