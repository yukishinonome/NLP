s = "abc"
s_list = ["d", "e", "f"]

for s1, s2 in zip(s, s_list):
    print(s1, s2)


# str型の文字列とlist型をzipに入れると
# str型は１文字に分割されてlist型として扱われるので
# エラーは発生しない。