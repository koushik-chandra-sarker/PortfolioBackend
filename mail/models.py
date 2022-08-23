from django.db import models, transaction

# Create your models here.
from django.utils.html import format_html


class MailInfo(models.Model):
    subject = models.CharField(max_length=200, verbose_name='Title', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)
    active = models.BooleanField(default=False)
    host = models.CharField(max_length=50, default='smtp.gmail.com',
                            help_text='default host is "smtp.gmail.com". if you want to '
                                      'change it then give your host, otherwise leave it ')
    port = models.IntegerField(default=587, help_text='default port is "587". if you want to change it then give your'
                                                      ' port no, otherwise leave it')
    tls = models.BooleanField(default=False)
    ssl = models.BooleanField(default=False)
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=200,
                                help_text=format_html(f'<p><b>For Gmail: You need to follow those steps:</b></p><br>'
                                                      f'<p>1. Enable less secure app for your gmail from this link'
                                                      f' https://myaccount.google.com/lesssecureapps </p> <br>'
                                                      f'<p>2. Enable 2-Step Verification from your gmail account.'
                                                      f'</p> <br>'
                                                      f'<p>3. Generate an App passwords from your gmail account and'
                                                      f' upload here. https://myaccount.google.com/apppasswords</p> <br>'))

    def __str__(self):
        return self.mail

    def save(self, *args, **kwargs):
        if not self.active:
            return super(MailInfo, self).save(*args, **kwargs)
        with transaction.atomic():
            MailInfo.objects.filter(active=True).update(active=False)
            return super(MailInfo, self).save(*args, **kwargs)
