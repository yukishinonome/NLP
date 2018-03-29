s = input()
sort_s = sorted(s)
print(sort_s)

# str型の文字列を直接sorted()に入れると
# str型の文字列を１文字ずつに分割したlist型として認識して
# それをソートしたlist型を取得できる。