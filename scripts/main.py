from config_loader import load_devices
from api_client import get_users
from report_generator import generate_user_report
from logger import logger


def main():

    logger.info("Application Started")

    print("=" * 40)
    print("Network Device Monitoring System")
    print("=" * 40)

    devices = load_devices("configs/devices.json")

    logger.info("Device configuration loaded successfully")

    print("\nConfigured Devices")
    print("------------------")

    for device in devices:
        print(f"{device['hostname']} - {device['ip']}")

    print("\nUsers from REST API")
    print("------------------")

    users = get_users()

    if users:
        logger.info("REST API data fetched successfully")
    else:
        logger.warning("No users returned from API")

    generate_user_report(users)

    logger.info("CSV report generated successfully")

    for user in users:
        print(f"{user['id']} - {user['name']}")

    logger.info("Application Finished")


if __name__ == "__main__":
    main()