# 参考文献
# 日本語WordNet: http://compling.hss.ntu.edu.sg/wnja/
# python3コード: http://sucrose.hatenablog.com/entry/20120305/p1
# 日本語WordNetを事前にダウンロードしておく必要がある


import sqlite3
from collections import namedtuple


def getWords(lemma):
    cur = conn.execute("select * from word where lemma=?", (lemma,))
    return [Word(*row) for row in cur]

def getSenses(word):
    cur = conn.execute("select * from sense where wordid=?", (word.wordid,))
    return [Sense(*row) for row in cur]

def getSynset(synset):
    cur = conn.execute("select * from synset where synset=?", (synset,))
    return Synset(*cur.fetchone())

def getWordsFromSynset(synset, lang):
    cur = conn.execute("select word.* from sense, word where synset=? and word.lang=? and sense.wordid = word.wordid;", (synset,lang))
    return [Word(*row) for row in cur]

def getWordsFromSenses(sense, lang="jpn"):
    synonym = {}
    for s in sense:
        lemmas = []
        syns = getWordsFromSynset(s.synset, lang)
        for sy in syns:
            lemmas.append(sy.lemma)
        synonym[getSynset(s.synset).name] = lemmas
    return synonym

def getSynonym(word):
    synonym = {}
    words = getWords(word)
    if words:
        for w in words:
            sense = getSenses(w)
            s = getWordsFromSenses(sense)
            synonym = dict(list(synonym.items()) + list(s.items()))
    return synonym

def synonymlist(word):
    synonym = list(getSynonym(word).values())
    synonym2 = []
    for s_list in synonym:
        for s in s_list:
            synonym2.append(s)
    synonym2 = list(set(synonym2))
    return synonym2

if __name__ == '__main__':
    conn = sqlite3.connect("wnjpn.db", check_same_thread = False)
    Word = namedtuple('Word', 'wordid lang lemma pron pos')
    Sense = namedtuple('Sense', 'synset wordid lang rank lexid freq src')
    Synset = namedtuple('Synset', 'synset pos name src')
    print(synonymlist(input("類義語検索：")))