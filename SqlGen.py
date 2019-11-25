from nltk.parse.corenlp import CoreNLPDependencyParser
import pandas as pd
import SentenceSimilarity as sm
import ner

class SqlGen:
    parsed = ""
    tokenized=""
    dep_parser = ""
    text =""
    data =""
    attributes =""
    conditions = []

    #constructor
    def __init__(self,sentence):
        self.prop= {"depparse.extradependencies": "NONE","depparse.keepPunct":"false"}
        self.dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
        self.text = ner.NER().ner_pass(sentence)
        self.parsed , = self.dep_parser.raw_parse(self.text, properties=self.prop)


    def getData(self,type='None'):

        if  type == 'pandas1' or type == 'pandas2' or type== 'pandas3':
            x = self.parsed
            if x.contains_address(0):
                x.remove_by_address(0)
            x = x.nodes
            df = pd.DataFrame([(v['address'], v['word'], v['lemma'], v['ctag'], v['tag'], v['feats'], v['head'], v['deps'], v['rel'])for v in x.values()],columns=['position', 'word', 'lemma', 'ctag', 'tag', 'feat', 'head', 'deps', 'rel']).set_index('position')
            self.data = df
            if type == 'pandas1':
                #all columns are included
                return df
            elif type == 'pandas2':
                # removed some columns from pandas1, only the columns specified in the list are included
                return df[['lemma', 'tag', 'head', 'rel']]
            else:
                # removed all colums except dependents
                return df[['deps']]

        else:
            return self.parsed.to_conll(4)

    def getAction(self,df):
        try:
            mainVerb = df.query("tag == 'VB'  & head == 0").to_dict()
            return mainVerb['lemma']
        except IndexError:
            return

    def getAttributes(self,df):
        #x = df.query(" (rel == 'dobj'  & head == %s) |(rel == 'conj:and'  & head ==  %s)" %(1,1)).to_dict()
        x = df.query("  (rel == 'dobj' & head == %s) |(rel == 'acl:relcl') |(rel == 'conj:and' & head ==  %s) |(rel == 'appos' )" %(1,1)).to_dict()
        self.attributes = (x['lemma'])
        self.rel = (x['rel'])
        return x

    def getValueNodes(self,index):
        pos = self.data.query("(rel == 'acl:relcl' )").to_dict()['word']
        if pos:
            pos = list(pos.keys())[0]
            x = self.data.query(" (rel == 'nmod:poss')|(rel == 'nmod:at')|(rel == 'dobj' & index > %s) | (rel == 'nmod:for')| (rel == 'nmod:as') | (rel == 'nmod:in')" %(pos)).to_dict()
            self.conditions = x['word']
            return x
        else:
            x = self.data.query(" (rel == 'nmod:poss')|(rel == 'nmod:at') | (rel == 'nmod:for')| (rel == 'nmod:as') | (rel == 'nmod:in')" % (
                    pos)).to_dict()
            self.conditions = x['word']
            return x

    def findAssociation(self,attributes):
        att = []
        for keys in attributes:
            x = self.data.query(" (~tag.str.contains('DT')& ~rel.str.contains('ref')& ~rel.str.contains('cc')& ~rel.str.contains('case') & ~rel.str.contains('punct')) &(head == %s)" % (keys)).to_dict()
            #temp = [(attributes[keys])]
            if self.rel[keys] == "acl:relcl":
                temp = {attributes[keys]:'acl:relcl'}
            else:
                temp = {attributes[keys]: 'main'}
            for keys in x['lemma']:
                try:
                    if(x['lemma'][keys] not in attributes.values() and x['lemma'][keys] not in self.conditions.values()):
                        temp[x['lemma'][keys]]= x['rel'][keys]
                except AttributeError:
                    pass
            att.append(temp)
        return att





query = input("What is your query? ")


if query != "":
    Sql = SqlGen(query)
    data = Sql.getData("pandas1")
    print(Sql.getData("pandas2"))
    print(Sql.getData("pandas3"))


    print("******************************Action****************************")
    print(Sql.getAction(data))
    print("******************************End of Action ****************************")
    print("******************************Attributes are ****************************")
    Sql.getAttributes(data)
    print(Sql.attributes)
    print("******************************End of Attributes ****************************")
    print("******************************ValueNodes are ****************************")
    Sql.getValueNodes(data)
    print(Sql.conditions)
    print("******************************End of ValueNodes ****************************")
    att = Sql.findAssociation(Sql.attributes)

    attr = []
    table = []

    print("**** Attributes are*****")
    print(att)
    for i in att:
        x,y,z = sm.getSimilarAttribute(i)
        print(x,y,z)
        if y not in attr and y is not "":
            attr.append(y)
        if x not in table and x != "not available":
            table.append(x)

    query = "Select " + ' , '.join(map(str, attr))+" from " + ' , '.join(map(str, table))
    print(query)

    print("Similarity : ",z)

    try:
        where = sm.whereSim(list(Sql.conditions.values()),table)
    except AttributeError:
        pass

    try:
        if where:
            query = query + where
            query = ner.NER().ner_pass2(query)
    except:
        NameError

    print(query)



