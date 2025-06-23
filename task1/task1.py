

def total_salary(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = [float(el.strip().split(',')[1]) for el in file.readlines()]

            total = sum(salaries)
            return total, total / len(salaries)
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        return None, None



total, average = total_salary("task1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
total, average = total_salary("task1/non_existing.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
total, average = total_salary("task1/salary_file_malformed.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

