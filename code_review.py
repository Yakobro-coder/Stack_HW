import email
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"


class SendingMail:

    def __init__(self):
        self.login = 'login@gmail.com'
        self.password = 'qwerty'
        self.subject = 'Subject'
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.message = 'Message'
        self.header = None

        self.send_message()

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        ms.ehlo()  # identify ourselves to smtp gmail client
        ms.starttls()  # secure our email with tls encryption
        ms.ehlo()  # re-identify ourselves as an encrypted connection

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())

        ms.quit()

    def recieve(self):
        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()

        return email_message


if __name__ == '__main__':
    sender = SendingMail()
    sender.send_message()
    sender.recieve()
