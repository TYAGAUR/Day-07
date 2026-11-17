APP_NAME = "AI Model Management Platform"

AVAILABLE_MODELS = {
    "gpt": {
        "provider": "OpenAI",
        "price_per_1000_tokens": 0.002
    },
    "claude": {
        "provider": "Anthropic",
        "price_per_1000_tokens": 0.003
    },
    "gemini": {
        "provider": "Google",
        "price_per_1000_tokens": 0.001
    }
}