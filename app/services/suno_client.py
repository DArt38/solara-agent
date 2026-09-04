import os

import httpx
from dotenv import load_dotenv

load_dotenv()

class SunoClient:
    BASE_URL = "https://api.sunoapi.org"

    def __init__(self):
        self.api_key = os.getenv("SUNO_API_KEY")

        if not self.api_key:
            raise ValueError("SUNO_API_KEY no está configurada")

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    async def get_credits(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/api/v1/generate/credit",
                headers=self.headers,
            )

            response.raise_for_status()

            return response.json()

    async def generate_song(self, payload: dict):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.BASE_URL}/api/v1/generate",
                headers=self.headers,
                json=payload,
            )

            response.raise_for_status()

            return response.json()

    def build_song_payload(self,song):
        return{
            "customMode": True,
            "instrumental": False,
            "model": "V5",
            "prompt": song.lyrics,
            "style": song.style_prompt,
            "title": song.title
        }