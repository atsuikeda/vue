import httpx
from fastapi import HTTPException
from app.config import settings

class TranslationService:
    def __init__(self):
        # ポート番号を5001に変更
        self.api_url = "http://libretranslate:5000/translate"
        self.client = httpx.AsyncClient(timeout=30.0)

    async def translate_text(self, text: str, source_lang: str = "en", target_lang: str = "ja") -> str:
        print(f"Translating text: {text} from {source_lang} to {target_lang}")
        try:
            response = await self.client.post(
                self.api_url,
                json={
                    "q": text,
                    "source": source_lang,
                    "target": target_lang,
                    "format": "text"
                }
            )
            
            response.raise_for_status()
            result = response.json()
            
            if "translatedText" not in result:
                raise HTTPException(
                    status_code=500,
                    detail=f"Unexpected response format: {result}"
                )
                
            return result["translatedText"]
            
        except httpx.HTTPError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Translation service error: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Unexpected error: {str(e)}"
            )

translation_service = TranslationService()
