from itertools import count


class WordsFinder:
    res = {}
    def __init__(self, *file_names):
        self.file_names = file_names
    def get_all_words(self):
        all_words = {}
        for filename in self.file_names:
            with open(filename, "r", encoding='utf-8') as file:
                data = file.read()
                data = data.lower()
                for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    data = data.replace(char, " ")
                all_words[filename] = data.split()
        return all_words

    def find(self, word):
        res = {}
        word = word.lower()
        all_words = self.get_all_words()
        for filename, text in all_words.items():
            if text.count(word) > 0:
                res[filename] = text.index(word) + 1
            else:
                res[filename] = - 1
        return res

    def count(self, word):
        res = {}
        word = word.lower()
        all_words = self.get_all_words()
        for filename, text in all_words.items():
           res[filename] = text.count(word)
        return res

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
