from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text: str
    source_lang: str = "en"  # デフォルトは英語
    target_lang: str = "ja"  # デフォルトは日本語

class TranslationResponse(BaseModel):
    translated_text: str
    source_lang: str
    target_lang: str