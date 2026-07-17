from config_loader import load_devices
from api_client import get_users


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

    for user in users:
        print(f"{user['id']} - {user['name']}")


if __name__ == "__main__":
    main()