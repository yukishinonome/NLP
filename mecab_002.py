import MeCab


def mecab_002(s):
    """
    入力文に対して分かち書きを行う。
    mecab-ipadic-neologdを使うことでより多い単語に対応できる。
    """
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -Owakati')
    m_str = m.parse(s)
    print(m_str)
    

if __name__ == '__main__':
    mecab_002(input())