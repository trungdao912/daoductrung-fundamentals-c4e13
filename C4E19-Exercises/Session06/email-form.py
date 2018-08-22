from gmail import GMail
from gmail import Message
from random import choice
import datetime
from threading import Timer

def auto_email():
    html_content = """
    <p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
    <p style="text-align: center;">Độc lập - Tự do - Hạnh Ph&uacute;c</p>
    <p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
    <p style="text-align: left;">Em ch&agrave;o thầy,</p>
    <p style="text-align: left;">&nbsp;</p>
    <p style="text-align: left;">T&ecirc;n em l&agrave; Đ&agrave;o Đức Trung, h&ocirc;m nay em xin nghi học do {{sickness}}</p>
    <p style="text-align: left;">&nbsp;</p>
    <p style="text-align: left;">Em xin cảm ơn</p>
    <p style="text-align: left;">Trung Đ&agrave;o</p>
    <p style="text-align: left;">&nbsp;</p>
    """
    reasons = ["thon", "tieu chay", "sot"]
    reason = choice(reasons)
    html_to_send = html_content.replace("{{sickness}}", reason)

    gmail = GMail('trungdao.ftu@gmail.com','english1996')
    msg = Message('TEST', 
        to = 'meomeo311@gmail.com', 
        html = html_to_send)
    return gmail.send(msg)

now = datetime.datetime.now()
run_at = datetime.datetime.strptime("2018/07/17 7:00:00", "%Y/%m/%d %H:%M:%S")
delta_t = run_at - now

t = Timer(delta_t, auto_email)
t.start()