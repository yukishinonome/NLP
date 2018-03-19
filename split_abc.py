def split_abc(s):
    """
    入力文を指定した文字で分割してリストにする。
    文字の指定がない場合はスペース・タブなどで分割される。
    """
    s_list = s.split()
    print(s_list)


if __name__ == '__main__':
    split_abc(input())