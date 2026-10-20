from pathlib import Path


def total_salary(path):
    file_path = Path(path)

    try:
        total = 0
        count = 0
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                try:
                    name, salary_str = cleaned_line.split(",")
                    salary = int(salary_str.strip())
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Пропущено некоректний рядок: {cleaned_line}")
                    continue

        average = total / count if count > 0 else 0.0

        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
        return total, average

    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None, None
    except Exception as e:
        print(f"Error while reading a file: {e}")
        return None, None


total, average = total_salary("task1.txt")
# Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000.0