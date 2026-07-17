import csv
import os


def generate_user_report(users):
    os.makedirs("reports", exist_ok=True)

    with open("reports/users_report.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Name"])

        for user in users:
            writer.writerow([user["id"], user["name"]])

    print("\nReport generated: reports/users_report.csv")