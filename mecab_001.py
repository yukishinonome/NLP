import MeCab


def mecab_001(s):
    """
    入力文に対して形態素解析を行う。
    mecab-ipadic-neologdを使うことでより多い単語に対応できる。
    """
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    m_str = m.parse(s)
    print(m_str)
    

if __name__ == '__main__':
    mecab_001(input())