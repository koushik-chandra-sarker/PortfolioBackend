from django.core import mail
from django.core.mail.backends.smtp import EmailBackend

from mail.models import MailInfo


def sendEmail(body, mailTo=None):
    try:
        con = mail.get_connection()
        mail_setting = MailInfo.objects.get(active=True)
        host = mail_setting.host
        host_user = mail_setting.mail
        host_pass = mail_setting.password
        host_port = mail_setting.port
        mail_obj = EmailBackend(
            host=host,
            port=host_port,
            username=host_user,
            password=host_pass,
            use_tls=mail_setting.tls,
            use_ssl=mail_setting.ssl,
        )
        mail_obj.open()
        msg = mail.EmailMessage(
            subject=mail_setting.subject,
            body=f'Please complete your account ({mailTo}) by confirming your email address.: {body}',
            from_email=host_user,
            to=[mailTo],
            connection=con,
        )
        mail_obj.send_messages([msg])
        mail_obj.close()
        return True

    except Exception as _error:
        print('Error in sending mail >> {}'.format(_error))
        return False
