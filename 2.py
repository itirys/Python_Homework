# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

print(f'Количество строк: {len(text)}')
for i in range(len(text)):
    print(f'Количество слов в строке {i+1}: {len(text[i].split())}')