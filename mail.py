import smtplib
import ssl
from email.mime.text import MIMEText

MEETING_INVITATION = """
Sorry for the inconvenience. It was a wrong trigger. There is no meeting scheduled.
"""


class Mail:

	def __init__(self, smtp, port, sender, passwd, receivers, email_body):
		self.smtp = smtp
		self.port = port
		self.sender = sender
		self.passwd = passwd
		self.receivers = receivers
		self.message = MIMEText("{}".format(email_body))

	def send_email(self):
		# self.message['Subject'] = "Errors found in logs"
		# self.message['From'] = self.sender
		# self.message['To'] = ', '.join(self.receivers)
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(self.smtp, self.port, context=context) as server:
			server.login(self.sender, self.passwd)
			# print(help(server.sendmail))
			server.sendmail(self.sender, self.receivers,
			                self.message.as_string())


if __name__ == '__main__':
	import os
	batch_emails = [
	]
	notification_email = Mail(smtp="smtp.gmail.com",
	                          port=465,
	                          sender=os.environ.get("sender"),
	                          passwd=os.environ.get("sender_password"),
	                          receivers=batch_emails,
	                          email_body=MEETING_INVITATION)
	# email_body="You guys received the invites?")
	notification_email.send_email()
