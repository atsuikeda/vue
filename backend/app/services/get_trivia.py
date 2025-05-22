import httpx
import logging
from fastapi import HTTPException
from .translation import translation_service

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TriviaService:
    def __init__(self):
        self.api_url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
        self.client = httpx.AsyncClient(timeout=30.0)

    async def get_random_trivia(self, target_lang: str = "ja") -> dict:
        try:
            logger.info("Fetching random trivia from API...")
            # 英語の豆知識を取得
            response = await self.client.get(
                self.api_url,
                params={"language": "en"}
            )
            response.raise_for_status()
            trivia_data = response.json()
            logger.info(f"Received trivia: {trivia_data['text'][:50]}...")

            logger.info("Translating trivia...")
            # 豆知識のテキストを翻訳
            translated_text = await translation_service.translate_text(
                text=trivia_data["text"],
                source_lang="en",
                target_lang=target_lang
            )
            logger.info(f"Translation completed: {translated_text[:50]}...")

            # 翻訳済みの豆知識を返す
            return {
                "original_text": trivia_data["text"],
                "translated_text": translated_text,
                "source": trivia_data.get("source", ""),
                "source_url": trivia_data.get("source_url", "")
            }

        except httpx.HTTPError as e:
            logger.error(f"HTTP Error: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch trivia: {str(e)}"
            )
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Unexpected error: {str(e)}"
            )

trivia_service = TriviaService()
