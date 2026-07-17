from config_loader import load_devices


def main():
    print("===================================")
    print(" Network Device Monitoring System ")
    print("===================================")

    devices = load_devices("configs/devices.json")

    print("\nConfigured Devices:")
    print("-------------------")

    for device in devices:
        print(f"Hostname : {device['hostname']}")
        print(f"IP       : {device['ip']}")
        print(f"Location : {device['location']}")
        print()


if __name__ == "__main__":
    main()