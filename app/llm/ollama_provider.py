from ollama import chat

from llm.base import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(
        self,
        model: str = "qwen3.6:latest"
    ):
        self.model = model

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        response_schema: dict | None = None
    ) -> str:

        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]

        response = chat(
            model=self.model,
            messages=messages,
            format=response_schema
        )

        return response.message.content