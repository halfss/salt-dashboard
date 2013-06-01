import email
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

fromAdd = 'secrete@gamewave.net'
server = 'smtp.gamewave.net'
user = 'secrete@gamewave.net'
passwd = 'qyops00&admin'

#conn = libvirt.open('qemu:///system')
#doms = conn.listDomainsID()


def sendEmail(toAdd, subject, htmlText):
    strTo = ','.join(toAdd)
    msgRoot = email.MIMEMultipart.MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = fromAdd
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = email.MIMEText.MIMEText(htmlText, 'html', 'utf-8')
    msgAlternative.attach(msgText)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(server)
        smtp.login(user, passwd)
        for i in toAdd:
            smtp.sendmail(fromAdd,i, msgRoot.as_string())
            smtp.quit()
            return True
    except Exception,e:
        print str(e)
        return False
