from scripts.config_loader import load_devices


def test_load_dev_config():
    devices = load_devices("configs/dev.json")

    assert len(devices) == 2


def test_first_router():
    devices = load_devices("configs/dev.json")

    assert devices[0]["hostname"] == "Router-1"