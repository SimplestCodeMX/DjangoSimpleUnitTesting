from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class Mailing:

    def __init__(self, default_mail):
        self.default_mail = default_mail

    def send_with_sendgrid(self, from_email, to_emails, subject, html_content):

        message = Mail(
            from_email=from_email,
            to_emails=list(set(to_emails)),
            subject=subject,
            html_content=html_content
        )

        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)

    def send_html_mail(self, subject, template_name, context, to_mail_list):
        try:
            self.send_with_sendgrid(
                from_email=self.default_mail,
                to_emails=to_mail_list,
                subject=subject,
                html_content=render_to_string(template_name, context)
            )
        except Exception as e:
            send_mail(
                f'Error -{e}- enviando email {subject}, es muy probable que el email no sea correcto',
                message=f'Error:{e}',
                from_email=self.default_mail,
                recipient_list=[self.default_mail],
                fail_silently=False
            )



