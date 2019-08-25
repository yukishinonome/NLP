import email
from email.header import decode_header
import quopri
import base64
import glob

def get_mail_contents(filename):
    """
    メールコンテンツの取得
    """
    # バイナリ形式を読み込むためにモードに「b」をつける必要がある
    with open(filename, 'rb') as email_file:
        email_message = email.message_from_bytes(email_file.read())

        num = 0
        # print("\n---Content---")

        for part in email_message.walk():
            # print(f"type: {part.get_content_type():<22} charset: {part.get_content_charset()}")
            charset = part.get_content_charset()
            payload = part.get_payload(decode=True)

            # 本文の取得を試みる
            try:
                if payload:
                    # 本文ではないデータを省く
                    if num == 0:
                        num += 1
                        continue

                    # メールはいろんなエンコード方式のものが届く。
                    # 全てのメールのコンテンツをデコードするには
                    # 様々な文字コードやエンコード方式に対応する必要があるが、
                    # 今回は日本語のメールだけ取得したいので意図的に限定している。
                    # 「 iso-2022-jp 」は日本語用のエンコード方式
                    if charset != "iso-2022-jp" and charset != "shift_jis" and charset != "utf-8":
                        continue

                    # タイトルを取得する関数の呼び出し
                    # get_mail_subject(email_message)

                    if "base64" in part:
                        b = base64.b64decode(payload)
                    elif "quoted-printable" in part:
                        b = quopri.decodestring(payload, header=False)
                    else:
                        b = payload

                    # オプションのignoreはデコードできない文字を無視する
                    if charset == "iso-2022-jp":
                        msg = b.decode("iso-2022-jp", "ignore")
                    elif charset == "shift_jis":
                        msg = b.decode("shift_jis", "ignore")
                    else:
                        msg = b.decode("utf-8", "ignore")

                    # 文字列最後の不要な改行を削除
                    while msg[-1] == "\n":
                        msg = msg[:-1]

                    # メールの本文を表示
                    print(msg)
                    print("\n\n-------------------------------------------------\n\n")

                else:
                    pass
            except:
                pass


def get_mail_subject(email_message):
    """
    メールタイトルの取得
    """
    for fragment, encoding in decode_header(email_message.get('Subject')):
        print("---Subject---")
        # shift_jisはunknown-8bitと表記されることがある
        if encoding == 'unknown-8bit':
            print(fragment.decode('shift_jis', "ignore"))
        elif encoding:
            print(fragment.decode(encoding))
        else:
            print(fragment)


if __name__ == '__main__':
    """
    mailフォルダにあるメールファイルを読み込んでタイトルや本文をデコードして取得
    """
    for filename in glob.glob("mail/*"):
        # print(filename)
        get_mail_contents(filename)