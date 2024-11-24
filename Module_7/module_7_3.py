'''Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count'''
import os
class WordsFinder:
    def __init__(self, *file_name:list[str], my_str=""):
        self.file_name = file_name
        self.my_str = my_str


    # def add_file_name(self, *file_name):
    #     self.file_name
    def get_all_words(self, *file_name:str, my_str:str=''):
        all_words ={str:tuple}
        # print(os.path.dirname(os.path.abspath(__file__)))
        for name in file_name:
            with open (name, 'r',encoding='utf-8') as f:
                my_str.split(f.readline())
                all_words.append(f.name:(my_str[0],my_str[1]))
                print (my_str)
                # all_words.append({f.name:my_str})
            print (all_words)
            f.close()


    def find(self,word):
        pass
        # for name in file_name:



    def count(self,word):
        pass

print (os.getcwd())
os.chdir('H:\\Users\\aadim\\New_Project\\StudentProject\\Module_7\\Материал для 7_3')
first=WordsFinder(os.getcwd() + '\\test_file.txt')
# H:\Users\aadim\New_Project\StudentProject\Module_7\Материал для 7_3
# first.get_all_words('H:\\Users\\aadim\\New_Project\\StudentProject\\Module_7\\Материал для 7_3\\test_file.txt')

first.get_all_words(os.getcwd() + '\\test_file.txt')