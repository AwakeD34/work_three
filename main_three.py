import os

# Получаем список файлов в папке
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]

# Создаем словарь, где ключ - имя файла, а значение - количество строк в файле
file_info = {}
for file in files:
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            file_info[file] = len(f.readlines())
    except UnicodeDecodeError:
        with open(file, 'r', encoding='latin-1', errors='ignore') as f:
            file_info[file] = len(f.readlines())

# Сортируем файлы по количеству строк
sorted_files = sorted(file_info, key=file_info.get)

# Создаем итоговый файл
with open('result.txt', 'w', encoding='utf-8', errors='ignore') as result_file:
    for file in sorted_files:
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                result_file.write(f'{file}\n')
                result_file.write(f'{len(content.splitlines())}\n')
                result_file.write(content)
                result_file.write('\n\n')
        except UnicodeDecodeError:
            with open(file, 'r', encoding='latin-1', errors='ignore') as f:
                content = f.read()
                result_file.write(f'{file}\n')
                result_file.write(f'{len(content.splitlines())}\n')
                result_file.write(content)
                result_file.write('\n\n')