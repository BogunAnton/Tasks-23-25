import random

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class AnagramFinder(metaclass=SingletonMeta):
    def __init__(self):
        self.full_text = ""
        self.text_entered = False
        self.algorithm_executed = False

    def is_int(self, choice):
        try:
            if isinstance(choice, int):
                return True
            if choice is None:
                return False
            if not choice.isdecimal():
                return False
            int(choice)
            return True
        except (Exception, ValueError, TypeError):
            return False

    def self_input_text(self):
        print("Введите текст (для завершения ввода введите пустую строку):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        self.full_text = " ".join(lines)
        self.text_entered = True
        print("Вы ввели следующий текст:")
        print(self.full_text)

    def random_input_text(self, min_length=10, max_length=1000):
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' + ' ' * 7
        length = random.randint(min_length, max_length)
        self.full_text = ''.join(random.choice(letters) for _ in range(length))
        self.text_entered = True
        print("Сгенерированный случайный текст:")
        print(self.full_text)

    def find_anagrams(self):
        words = self.full_text.split()
        anagrams = {}
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        result = [group for group in anagrams.values() if len(group) > 1]
        self.algorithm_executed = True
        print("Алгоритм выполнен")
        return result

    def display_results(self, anagrams):
        if len(anagrams) == 0:
            print("Анаграмм в тексте нет!!!")
        else:
            for group in anagrams:
                print("Анаграммы:", group)

def show_menu():
    anagrams = []
    while True:
        anagram_finder = AnagramFinder()
        print("Выберите пункт меню:\n"
              "1. Ввод исходного текста, вручную или сгенерированного случайным образом\n"
              "2. Выполнение алгоритма по поиску анаграмм в исходном тексте\n"
              "3. Вывод результата алгоритма\n"
              "0. Выход из цикла")
        choice = input()
        if anagram_finder.is_int(choice):
            choice = int(choice)
        if choice == 1:
            option = input("Выберите опцию 1-2:\n" "1. Ввести текст самостоятельно\n" "2. Сгенерировать случайный текст\n")
            if anagram_finder.is_int(option):
                option = int(option)
            if option == 1:
                anagram_finder.self_input_text()
            elif option == 2:
                anagram_finder.random_input_text()
            else:
                print('error')
        elif choice == 2:
            if anagram_finder.text_entered:
                anagrams = anagram_finder.find_anagrams()
            else:
                print("Сначала введите текст!")
        elif choice == 3:
            anagram_finder.display_results(anagrams)
        elif choice == 0:
            break
        else:
            print("Неверный выбор, попробуйте еще раз")

if __name__ == '__main__':
    show_menu()
#Hi