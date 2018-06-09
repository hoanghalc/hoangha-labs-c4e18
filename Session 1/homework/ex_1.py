from gmail import GMail 
from gmail import Message
from random import choice
import datetime

html_content = """ <p style="text-align: center;">Cộng ho&agrave; x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập- Tự do- Hạnh ph&uacute;c</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: justify; padding-left: 30px;"><strong>K&iacute;nh gửi:&nbsp;</strong>thầy gi&aacute;o Huỳnh Tuấn Anh</p>
<p style="text-align: justify; padding-left: 30px;">T&ecirc;n em l&agrave; Ho&agrave;ng Mạnh H&agrave;, học sinh lớp Code for Everyone 18. H&ocirc;m nay ng&agrave;y 07/03/2018, do h&ocirc;m nay em [!!!] n&ecirc;n ko đi học được. Em xin ph&eacute;p nghỉ học buổi h&ocirc;m nay v&agrave; hứa sẽ b&ugrave;ng b&agrave;i tập về nh&agrave;. Em xin cảm ơn!</p>
<p style="text-align: center;">&nbsp;</p>
<p>&nbsp;</p>
"""

reasons = ['chán','ốm','lười','thích thì nghỉ thôi']
rand = choice(reasons)
html_content_update = html_content.replace("[!!!]",rand)

gmail = GMail('hoangha.techkids@gmail.com','hoanghalc96')
msg = Message('Don xin nghi hoc', 
                to = 'hoangha.techkids@gmail.com',
                html = html_content_update)

now = datetime.datetime.now()
time_to_send = now.hour

while time_to_send > 7:
    gmail.send(msg) 