import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailManage:
    def send_email(self):
        smtpserver = 'smtp.qq.com'
        smtp_port = 465  # 必须使用 465 端口 + SMTP_SSL
        username = '3471814599@qq.com'
        password = 'oclfxybqfnoicjgc'  # 确保是最新的授权码
        receiver = '1395635971@qq.com'

        message = MIMEMultipart('related')
        message['From'] = username
        message['To'] = receiver
        message['Subject'] = '测试'

        # 添加附件
        with open(r'F:\interfacetest\report.html', 'rb') as f:
            fujian = MIMEText(f.read(), 'html', 'utf-8')
        message.attach(fujian)

        try:
            with smtplib.SMTP_SSL(smtpserver, smtp_port) as smtp:
                smtp.login(username, password)
                smtp.sendmail(username, [receiver], message.as_string())
            print("邮件发送成功！")
        except Exception as e:
            print(f"邮件发送失败: {e}")

if __name__ == '__main__':
    EmailManage().send_email()