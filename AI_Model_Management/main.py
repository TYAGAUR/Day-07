from model_manager import ModelManager
from config import APP_NAME
from logger import logger


def main():

    print("=" * 45)
    print(APP_NAME)
    print("=" * 45)

    manager = ModelManager()

    print("\nAvailable Models:")

    for model in manager.list_models():
        print("-", model)

    model_name = input("\nSelect model: ")

    try:

        tokens = int(input("Enter token count: "))

        response = manager.process_request(
            model_name,
            tokens
        )

        print("\nRequest Result")
        print("-" * 30)

        for key, value in response.items():
            print(f"{key}: {value}")

    except (ValueError, TypeError) as error:

        logger.exception("Request failed")
        print("Error:", error)

    except Exception:

        logger.exception("Unexpected application failure")
        print("Something went wrong.")


if __name__ == "__main__":
    main()