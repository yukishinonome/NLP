import datetime


def current_time():
    """
    現在時刻を表示する。
    """
    todaydetail = datetime.datetime.today()
    print("現在時刻は{}:{}です。".format(todaydetail.strftime('%H'), todaydetail.strftime('%M')))


if __name__ == '__main__':
    current_time()