def abc():
    """
    文の基本的な操作
    """
    a = "今日はいい天気ですね。"
    print("a : {}".format(a))
    print("a[1] : {}".format(a[1]))
    print("a[-1] : {}".format(a[-1]))
    print("a[:2] : {}".format(a[:2]))
    print("a[-4:] : {}".format(a[-4:]))
    print("a[::2] : {}".format(a[::2]))
    print("list(a) : {}".format(list(a)))
    print()
    b = ["今日", "天気", "です"]
    print("b : {}".format(b))
    print("b[1] : {}".format(b[1]))    
    print("b[-1] : {}".format(b[-1]))
    print("''.join(b) : {}".format(''.join(b)))
    print()
    c = {'x': "今日", 'y': "天気", 'z': "です"}
    print("c : {}".format(c))
    print("c['x'] : {}".format(c['x']))
    print("c.keys() : {}".format(c.keys()))
    print("c.values() : {}".format(c.values()))
    print("c.items() : {}".format(c.items()))


if __name__ == '__main__':
    abc()