import subprocess
import smtplib
import socket
import os
from email.mime.text import MIMEText
import datetime

to = '<youremail@gmail.com>'
gmail_user = '<raspiemail@gmail.com>'
gmail_password = '<raspiemail-password>'
smtp_uri = 'smtp.gmail.com'
smtp_port = 587

current_ip_filepath = '/home/pi/.current_ip'

def notify_ip_changes(new_ip):
  smtpserver = smtplib.SMTP(smtp_uri, smtp_port)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo
  smtpserver.login(gmail_user, gmail_password)
  today = datetime.date.today()

  msg = MIMEText('New IP assigned.\n Visit the RasPiServer dashboard http://%s' % new_ip)
  msg['Subject'] = "RasPI @ " + new_ip + " started up on %s" % today.strftime('%b %d %Y')
  msg['From'] = gmail_user
  msg['To'] = to
  smtpserver.sendmail(gmail_user, [to], msg.as_string())
  smtpserver.quit()


def get_current_ip():
  proc = subprocess.Popen('ip route list', shell=True, stdout = subprocess.PIPE)
  data = proc.communicate()
  split_data = data[0].split()
  ip = split_data[split_data.index('src')+1]
  return ip

def load_ip():
  if not os.path.isfile(current_ip_filepath):
    return ''
  else:
    with open(current_ip_filepath, 'r') as f:
      return f.readline().rstrip('\n')

def store_ip(ip):
  with open(current_ip_filepath, 'w') as f:
    f.write(ip)


previous_ip = load_ip()
new_ip = get_current_ip()

if new_ip and previous_ip != new_ip:
  print('IP Address has changed from (%s) to (%s)' % (previous_ip, new_ip))
  store_ip(new_ip)
  notify_ip_changes(new_ip)
else:
  print('IP Address detected: (%s)' % new_ip)

