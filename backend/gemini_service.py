from google import genai
import os
from dotenv import load_dotenv
from backend.logger import setup_logger

load_dotenv()

logger = setup_logger()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_response(chat_history):
    try:
        user_prompt = chat_history[-1]["content"]

        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=user_prompt
        )

        logger.info("API call successful")
        return response.text

    except Exception as e:
        logger.error(f"Gemini API Error: {str(e)}")
        return "Error occurred while generating response."