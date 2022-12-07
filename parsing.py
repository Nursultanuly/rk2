file = input("Имя файла: ")
with open(file) as f:
    print('Данные о файле:')
    print(len(list(filter(lambda x: x.isalpha(), f.read()))), 'буквы ')
    f.seek(0)
    print(len(f.read().split()), 'слов')
    f.seek(0)
    print(len(list(f.readlines())), 'строки')

