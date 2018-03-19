def conditional_branch(abc):
    """
    入力文に特定の文字が含まれている場合に条件にあった文を出力する。
    注意：入力文が複数の条件を満たす場合は最初に記述された条件が適用される。
         例：入力文：bac ---> 出力文：aが含まれています。
    """
    if 'a' in abc:
        print("aが含まれています。")
    elif 'b' in abc:
        print("bが含まれています。")
    elif 'c' in abc:
        print("cが含まれています。") 
    else:
        print("aもbもcも含まれていません。")


if __name__ == '__main__':
    conditional_branch(input())