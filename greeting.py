import datetime


def greeting():
    """
    時間帯に合った挨拶を出力する。
    """
    todaydetail = datetime.datetime.today()
    if 4 <= todaydetail.hour <= 10:
        print("おはようございます")
    elif 11 <= todaydetail.hour <= 17:
        print("こんにちは")
    else:
        print("こんばんは")


if __name__ == '__main__':
    greeting()