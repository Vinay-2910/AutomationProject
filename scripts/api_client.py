import requests
from logger import logger


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        logger.info("Successfully fetched users from API")

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("API request timed out")
        return []

    except requests.exceptions.ConnectionError:
        logger.error("Unable to connect to API")
        return []

    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP Error: {err}")
        return []

    except Exception as err:
        logger.error(f"Unexpected Error: {err}")
        return []