import MeCab


def mecab_003():
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    word_list = []

    # ファイルから文章を読み込んで処理できる形に変換する
    with open(input("分析したいファイルの名前："), 'r') as f:
        read_data = f.read()
        m_str = m.parse(read_data)
        m_list = m_str.split('\n')
        for word in m_list:
            # 文章から名詞のみ抽出
            if '名詞' in word and '非自立' not in word and '代名詞' not in word:
                w_list = word.split()
                word_list.append(w_list[0])
        print(word_list)


if __name__ == '__main__':
    mecab_003()