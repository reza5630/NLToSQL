from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

class NER:
    nerDict = {}

    # constructor
    def __init__(self):
        pass

    def ner_pass(self,sentence):

        ne_tree = ne_chunk(pos_tag(word_tokenize(sentence)))

        #print(ne_tree)

        for i in ne_tree:
            try:
                pp = [x[0] for x in i]
                pp = ' '.join(map(str, pp))
                if i.label() in self.nerDict:
                    self.nerDict[i.label()].append(pp)
                else:
                    self.nerDict[i.label()] = [pp]
            except AttributeError:
                pass

        for key,value in self.nerDict.items():
            for i in value:
                sentence = sentence.replace(i,key,1)

        return sentence


    def ner_pass2(self,sentence):
        for key,value in self.nerDict.items():
            for i in value:
                sentence = sentence.replace(key,i,1)
        return sentence