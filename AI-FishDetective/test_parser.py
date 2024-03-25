import os
import pandas as pd
import torch
import csv
from myparser import check_directory_and_run_model  # Импортируем функцию из myparser.py

# Остальной код автотеста остается без изменений

def create_test_file(directory):
    test_subdirectory = os.path.join(directory, 'ParsFile')
    os.makedirs(test_subdirectory, exist_ok=True)
    test_file_path = os.path.join(test_subdirectory, 'test_file.csv')
    with open(test_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Accounting report 04.20.2024", "Good Morning, Ivan Ivanovich!"])
        writer.writerow(["Accounting report 04.20.2024", "I am providing you with an accounting report dated 04/20/2024"])
        writer.writerow(["Accounting report 04.20.2024", "Sincerely, Mark Markovich!"])
    return test_file_path

def run_autotests():
    try:
        # Создаем тестовый файл в поддиректории 'ParsFile'
        test_directory = 'test_data'
        test_file_path = create_test_file(test_directory)

        # Проверяем работу функции check_directory_and_run_model
        predictions = check_directory_and_run_model(test_directory)

        # Проверяем, что функция возвращает предсказания модели
        assert predictions is not None, "Функция не вернула предсказания модели."

        # Удаляем тестовый файл и поддиректорию
        os.remove(test_file_path)
        os.rmdir(os.path.join(test_directory, 'ParsFile'))
        os.rmdir(test_directory)

        print("Функция check_directory_and_run_model работает правильно.")
    except Exception as e:
        print(f"Ошибка при выполнении автотестов: {str(e)}")

if __name__ == "__main__":
    run_autotests()
