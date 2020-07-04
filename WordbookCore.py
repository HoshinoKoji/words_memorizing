import time
import json

def GET_WORDBOOK_FROM_FILE(filename):
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = json.loads(f.read())
    wordbook = Wordbook(content['name'], content['create_time'])
    for word in content['words']:
        wordbook.addWord(word)

    return wordbook

class Wordbook:
    def __init__(self, name, create_time = None):
        self.__name = name
        self.__create_time = create_time if create_time else time.time()
        self.__words = []
        self.currentID = 0

    def getName(self):
        return self.__name

    def getTime(self):
        return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(self.__create_time))))
    
    def save(self):
        content = json.dumps({
            'name': self.__name,
            'create_time': self.__create_time,
            'words': [word for word in self.__words]
        })
        with open(f'./.data/{self.__name}.wordbook', 'w', encoding = 'utf-8') as f:
            f.write(content)

    def addWord(self, word):
        self.__words.append(word)
        self.currentID += 1
        self.save()

    def getWords(self):
        return self.__words[:]
    
    def deleteWord(self, word_id):
        new_word_list = []
        if isinstance(word_id, str):
            for word in self.__words:
                if word['id'] != word_id:
                    new_word_list.append(word)
        elif isinstance(word_id, list):
            for word in self.__words:
                if word['id'] not in word_id:
                    new_word_list.append(word)

        self.__words = new_word_list
        self.save()