"""
provider_factory.py

Creates the appropriate provider based on the project configuration.
"""

from .mock_provider import MockProvider
from .openai_provider import OpenAIProvider
from .gemini_provider import GeminiProvider


class ProviderFactory:
    """
    Creates the correct provider.
    """

    @staticmethod
    def create_provider(provider_name: str):

        provider_name = provider_name.lower()

        if provider_name == "mock":
            return MockProvider()

        elif provider_name == "openai":
            return OpenAIProvider()

        elif provider_name == "gemini":
            return GeminiProvider()

        raise ValueError(
            f"Unknown provider: {provider_name}"
        )