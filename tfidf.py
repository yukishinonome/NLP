import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf():
    """
    TF-IDFで文章から特徴的な（重要度の高い）単語を抽出する。
    """
    m = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    word_list = []
    word_list2 = []
    word_list3 = []
    word_list4 = []

    # ファイルから文章を読み込んで処理できる形に変換する
    with open(input("分析したいファイルの名前："), 'r') as f:
        read_data = f.read()
        m_str = m.parse(read_data)
        m_list = m_str.split('\n')
        for word in m_list:
            # 文章から名詞のみ抽出
            if ('名詞' in word and '非自立' not in word and '代名詞' not in word) or \
                ('。' in word or '！' in word or '？' in word or '」' in word):
                if '。' in word or '！' in word or '？' in word or '」' in word:
                    if word_list != []:
                        word_list2.append(word_list)
                        word_list = []
                else:
                    w_list = word.split()
                    word_list.append(w_list[0])
        for words in word_list2:
            word_list3.append(' '.join(words))

    num = input("TF-IDF値が高い単語の出力数：")
    num = int(num)
    vectorizer = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b')
    vecs = vectorizer.fit_transform(word_list3)
    tfidf = {}
    for i in range(len(vectorizer.get_feature_names())):
        # tfidf値は文ごとに求まるので同じ単語であっても文ごとに数値がやや異なる。
        # sum()は同じ単語のtfidf値を合計して処理するので、単語の出現数が多いほど値が大きくなる。
        # max()は複数の文で同じ単語に対して求めた値の中で最大の値を使用するので文ごとのtfidf値に近い。
        tfidf[vectorizer.get_feature_names()[i]] = sum(vecs.toarray()[:, i])
        # tfidf[vectorizer.get_feature_names()[i]] = max(vecs.toarray()[:, i])
    tfidf = sorted(tfidf.items(), key=lambda x: -x[1])
    for i, (k, v) in enumerate(tfidf):
        if i == num:
            break
        # print(k, v)
        word_list4.append(k)
    print(word_list4)


if __name__ == '__main__':
    tfidf()