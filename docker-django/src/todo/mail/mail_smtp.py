import base64
import smtplib
import ssl
import sys
from email.mime.text import MIMEText
from email.utils import formatdate

#実行方法
#第１引数：メールアドレス


args = sys.argv

"""
(1) MIMEメッセージを作成する
"""
main_text = "これが本文です"
charset = "utf-8"
if charset == "utf-8":
    msg = MIMEText(main_text, "plain", charset)
elif charset == "iso-2022-jp":
    msg = MIMEText(base64.b64encode(main_text.encode(charset, "ignore")), "plain", charset)


"""
(2) MIMEメッセージに必要なヘッダを付ける
* Gmailで送信する場合
  - Gmailの設定で「セキュリティの低いアプリの許可」を有効にする必要あり
  - https://myaccount.google.com/u/1/lesssecureapps?pageId=none
"""
msg.replace_header("Content-Transfer-Encoding", "base64")
msg["Subject"] = "これが件名です"
msg["From"] = "shimo@shimo-campus.com" # "Alice <alice@gmail.com>"
msg["To"] = args[1]
msg["Cc"] = ""
msg["Bcc"] = ""
msg["Date"] = formatdate(None,True)


"""
(3) SMTPクライアントインスタンスを作成する
* yahoo!メールで送信する場合
  host: "smtp.mail.yahoo.co.jp"
  nego_combo: ("no-encrypt", 25) or ("no-encrypt", 587) or
              ("ssl", 465)
* Gmailで送信する場合
  host: "smtp.gmail.com"
  nego_combo: ("starttls", 587) or ("starttls", 25) or
              ("ssl", 465)

host = "smtp.gmail.com"
"""
host = "shimo-campus.com"
nego_combo = ("starttls", 587) # ("通信方式", port番号)

if nego_combo[0] == "no-encrypt":
    smtpclient = smtplib.SMTP(host, nego_combo[1], timeout=10)
elif nego_combo[0] == "starttls":
    smtpclient = smtplib.SMTP(host, nego_combo[1], timeout=10)
    smtpclient.ehlo()
    # smtpclient.starttls()
    # smtpclient.ehlo()
elif nego_combo[0] == "ssl":
    context = ssl.create_default_context()
    smtpclient = smtplib.SMTP_SSL(host, nego_combo[1], timeout=10, context=context)
smtpclient.set_debuglevel(2) # サーバとの通信のやり取りを出力してくれる


"""
(4) サーバーにログインする
"""
username = "shimo@shimo-campus.com"
password = "saslShimo515norI"
smtpclient.login(username, password)


"""
(5) メールを送信する
"""
smtpclient.send_message(msg)
smtpclient.quit()

