from pydantic import BaseModel
from typing import List

class DocumentStatus(BaseModel):
    status: str
    processed_files: List[str]
    total_chunks: int
    start_time: str
    end_time: str
    processing_time_seconds: float

class QuestionResponse(BaseModel):
    response: str
