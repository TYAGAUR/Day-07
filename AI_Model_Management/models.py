class AIModel:

    def __init__(self, name, provider, price):
        self.name = name
        self.provider = provider
        self.price = price

    def calculate_cost(self, tokens):

        if not isinstance(tokens, int) or isinstance(tokens, bool):
            raise TypeError("Tokens must be an integer.")

        if tokens <= 0:
            raise ValueError("Tokens must be greater than zero.")

        return (tokens / 1000) * self.price

    def get_details(self):

        return {
            "name": self.name,
            "provider": self.provider,
            "price": self.price
        }