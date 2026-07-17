from config_loader import load_devices
from api_client import get_users
from report_generator import generate_user_report
from logger import logger


def main():
    print("=" * 40)
    print("Network Device Monitoring System")
    print("=" * 40)

    devices = load_devices("configs/devices.json")

    print("\nConfigured Devices")
    print("------------------")

    for device in devices:
        print(f"{device['hostname']} - {device['ip']}")

    print("\nUsers from REST API")
    print("------------------")

    users = get_users()
    generate_user_report(users)
    for user in users:
        print(f"{user['id']} - {user['name']}")


if __name__ == "__main__":
    main()
    logger.info("Application Started")
    logger.info("Device configuration loaded successfully")
    logger.info("REST API data fetched successfully")
    logger.info("CSV report generated successfully")
    logger.info("Application Finished")
    
    