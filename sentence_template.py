class SentenceTemplate():

    def __init__(self, sentence):
        self.sentence = sentence

    def evaluate(self, **kwargs):
        for key in kwargs:
            key.split('.')
            if key[0] == 'c':

        while '{' in self.sentence:
            return self.sentence.format(**kwargs)

if __name__ == '__main__':
    print '{c1} was a famous hero'.format(c1='John')

    print SentenceTemplate('{c1} was a famous hero',).evaluate(c1='John');