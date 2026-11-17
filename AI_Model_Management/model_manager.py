from models import AIModel
from config import AVAILABLE_MODELS
from logger import logger


class ModelManager:

    def __init__(self):

        self.models = {}

        self.load_models()

    def load_models(self):

        for name, details in AVAILABLE_MODELS.items():

            model = AIModel(
                name=name,
                provider=details["provider"],
                price=details["price_per_1000_tokens"]
            )

            self.models[name] = model

        logger.info("AI models loaded successfully")

    def list_models(self):

        return list(self.models.keys())

    def get_model(self, model_name):

        model_name = model_name.lower()

        if model_name not in self.models:
            raise ValueError(f"Model {model_name} is unavailable")

        return self.models[model_name]

    def process_request(self, model_name, tokens):

        model = self.get_model(model_name)

        cost = model.calculate_cost(tokens)

        logger.info(
            "Request processed: model=%s tokens=%s cost=%s",
            model_name,
            tokens,
            cost
        )

        return {
            "model": model.name,
            "provider": model.provider,
            "tokens": tokens,
            "estimated_cost": round(cost, 6),
            "status": "success"
        }