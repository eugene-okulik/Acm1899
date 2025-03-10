import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Путь к папке с логами")
parser.add_argument("--text", help="Текст для поиска в логах")
parser.add_argument("--first-only", action="store_true", help="Выводить только первое совпадение в файле")
args = parser.parse_args()
my_path = args.path

files = []
for root, _, filenames in os.walk(my_path):
    print()
    for filename in filenames:
        files.append(os.path.join(root, filename))

for file_path in files:
    flag = False
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            if args.text in line:
                words = line.split()
                try:
                    index = words.index(args.text)
                    before = " ".join(words[max(0, index - 5):index])
                    after = " ".join(words[index + 1:index + 6])
                    match = f"{before} *{words[index]}* {after}"
                except ValueError:
                    continue
                print(f"File: {file_path}")
                print(f"String {line_num}: {match}")
                if args.first_only:
                    flag = True
                    break
    if flag:
        break
