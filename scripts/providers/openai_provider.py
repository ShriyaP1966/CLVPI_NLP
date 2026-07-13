"""
openai_provider.py

Placeholder OpenAI provider.
"""

from .base_provider import BaseProvider


class OpenAIProvider(BaseProvider):
    """
    Placeholder provider.
    """

    def generate_response(self, prompt: str) -> str:

        raise NotImplementedError(
            "OpenAI provider not implemented yet."
        )