from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.utils.pdf_utils import save_uploaded_file
from app.services.document_service import process_pdf
from app.services.gemini_service import ask_question_to_gemini
from app.models.document import DocumentStatus, QuestionResponse
import os
import time

router = APIRouter()

# Global session state for preloaded context
session_state = {
    "contexts": {},
    "processComplete": False,
    "start_time": None,
    "end_time": None,
    "document_names": [],
    "total_chunk_count": 0
}

@router.post("/upload")
async def upload_pdfs(files: list[UploadFile] = File(...)):
    if not all(file.filename.endswith(".pdf") for file in files):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    session_state["start_time"] = time.time()
    total_chunk_count = 0

    for file in files:
        file_path = save_uploaded_file(file)
        context, chunk_count = process_pdf(file_path)
        session_state["contexts"][file.filename] = context
        session_state["document_names"].append(file.filename)
        total_chunk_count += chunk_count

    session_state["total_chunk_count"] = total_chunk_count
    session_state["processComplete"] = True
    session_state["end_time"] = time.time()

    return JSONResponse(content={
        "message": "PDFs uploaded and processed successfully.",
        "processed_files": session_state["document_names"],
        "total_chunks": total_chunk_count
    })

@router.get("/document-status", response_model=DocumentStatus)
async def document_status():
    if session_state["processComplete"]:
        total_time = session_state["end_time"] - session_state["start_time"]
        return DocumentStatus(
            status="Documents processed successfully.",
            processed_files=session_state["document_names"],
            total_chunks=session_state["total_chunk_count"],
            start_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(session_state["start_time"])),
            end_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(session_state["end_time"])),
            processing_time_seconds=round(total_time, 2)
        )
    return {"status": "Document processing in progress."}

@router.post("/ask-question", response_model=QuestionResponse)
async def ask_question(language: str, question: str):
    if not session_state["processComplete"]:
        raise HTTPException(status_code=400, detail="No documents processed yet.")
    
    combined_context = "\n".join(chunk for context in session_state["contexts"].values() for chunk in context)
    response = ask_question_to_gemini(combined_context, question, language)
    
    return QuestionResponse(response=response)
