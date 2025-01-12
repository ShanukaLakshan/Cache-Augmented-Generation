from deep_translator import GoogleTranslator
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GEMINI_API_KEY
import logging

logger = logging.getLogger(__name__)

def ask_question_to_gemini(context, question, language):
    prompt = f"""
    Answer the question based on the following context:
    {context}

    Question: {question}
    """
    
    chat_llm = ChatGoogleGenerativeAI(
        api_key=GEMINI_API_KEY,
        model="gemini-1.5-flash",
        temperature=0.7
    )
    result = chat_llm.invoke(prompt)
    response = result.content if hasattr(result, "content") else "Sorry, I couldn't retrieve a proper response."
    
    # Translate response to target language
    translator = GoogleTranslator(source="en", target=language)
    translated_response = translator.translate(response)
    
    logger.info(f"Generated response for question: {question}")
    return translated_response
