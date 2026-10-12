from dotenv import load_dotenv
import os

load_dotenv()

class Enviroments():
    """Class for config enviroments and validate then"""
    api_key_groq = os.getenv("GROQ_API_KEY")
    api_key_gemini = os.getenv("GEMINI_API_KEY")
    api_key_ombd = os.getenv("OMBD_API_KEY")
    model_ai_gemini = os.getenv("MODEL_AI_GEMINI")
    model_ai_groq = os.getenv("MODEL_AI_GROQ")

    @classmethod
    def api_key_groq_validation(cls):
        """validade api key groq"""
        if(not cls.api_key_groq):
            raise ValueError("api_key_groq is missing")
        else:
            return cls.api_key_groq

    @classmethod
    def api_key_gemini_validation(cls):
        """validade api key gemini"""
        if(not cls.api_key_gemini):
            raise ValueError("api_key_gemini is missing")
        else:
            return cls.api_key_gemini

    @classmethod
    def api_key_ombd_validation(cls):
        """validade api key ombd"""
        if(not cls.api_key_ombd):
            raise ValueError("api_key_ombd is missing")
        else:
            return cls.api_key_ombd

    @classmethod
    def model_ai_validation_gemini(cls):
        """validade model AI"""
        if(not cls.model_ai_gemini):
            raise ValueError("model_ai is missing")
        else:
            return cls.model_ai_gemini

    @classmethod
    def model_ai_validation_groq(cls):
        """validade model AI"""
        if(not cls.model_ai_groq):
            raise ValueError("model_ai is missing")
        else:
            return cls.model_ai_groq