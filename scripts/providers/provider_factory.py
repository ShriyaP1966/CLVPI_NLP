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
    def create_provider(config):

        provider_name = config["provider"].lower()

        if provider_name == "mock":
            return MockProvider(config)

        elif provider_name == "openai":
            return OpenAIProvider(config)

        elif provider_name == "gemini":
            return GeminiProvider(config)

        raise ValueError(
            f"Unknown provider: {provider_name}"
        )