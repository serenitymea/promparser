import csv
import json
import os
import pandas as pd

def savetoc(data, filepath):
    """Сохраняет список словарей в csv файл"""
    if not data:
        print("нет данных")
        return
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"данные сохранены в {filepath}")

def savetoj(data, filepath):
    """Сохраняет список словарей в json файл"""
    if not data:
        print("нет данных")
        return

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"данные сохранены в {filepath}")

def savetoe(data, filepath):
    """Сохраняет список словарей в excel файл"""
    if not data:
        print("нет данных")
        return

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    df = pd.DataFrame(data)
    df.to_excel(filepath, index=False)

    print(f"данные сохранены в {filepath}")
