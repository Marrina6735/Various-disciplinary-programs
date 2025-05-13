import csv
import json
from pathlib import Path
from typing import List


def save_json(data: List[dict], file_path: str):
    """_summary_

    Args:
        data (List[dict]): _description_
        file_path (str): _description_
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def process_csv_data(file_path: str) -> List[dict]:
    """_summary_

    Args:
        file_path (str): _description_

    Returns:
        List[dict]: _description_
    """
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            # Fullname,Gender,Age,Skills,Company,Salary (SEK),Location,Registration Date
            name, gender, age, skills, company, salary, location, registered_date = row

            age = int(age)
            skills = skills.split("; ")
            lat = float(location.split("; ")[0])
            lon = float(location.split("; ")[1])

            data_dict = {
                "name": name,
                "gender": gender,
                "age": age,
                "skills": skills,
                "company": company,
                "salary": salary,
                "location": {"lat": lat, "lon": lon},
                "registered": registered_date,
            }

            data.append(data_dict)

    return data


if __name__ == "__main__":
    main_dir = Path(r"csv_files")
    result = []
    for file in main_dir.iterdir():
        result += process_csv_data(file)
    save_json(result, "data.json")
