from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
import os

class Command(BaseCommand):
    help = 'Send email with attachment'

    def handle(self, *args, **kwargs):
        subject = 'Python (Selenium) Assignment - Spencer Dsheel'
        
        body = (    
            "Project Overview\n\n"
            "This project automates the submission of a Google form using Selenium, "
            "captures a screenshot of the confirmation page, and sends the screenshot via email using Django. "
            "The project demonstrates proficiency in web automation, form submission, web scraping, and email functionality integration within a Django framework.\n\n"
            "Tasks Completed:\n"
            "- Form Submission Using Selenium\n"
            "- Screenshot Capture of Confirmation Page\n"
            "- Emailing the Screenshot via Django\n\n"
            "Implementation:\n"
            "1. Form Submission Using Selenium\n"
            "- Utilized Selenium WebDriver for browser automation.\n"
            "- Employed webdriver_manager to manage ChromeDriver installation.\n"
            "- Navigated to the provided Google form URL.\n\n"
            "2. Screenshot Capture of Confirmation Page\n"
            "- Used Selenium's save_screenshot method to capture and save the screenshot in PNG format\n\n"
            "3. Emailing the Screenshot via Django\n"
            "- Configured Django project to use SMTP for sending emails.\n"
            "- Created a Django management command to handle email sending.\n\n"
            "GitHub link: https://github.com/Spencerdsheel/Automate-Form-Fill"
            "The link contain the source code of the project\n\n"
            "Please find attached the screenshot of the confirmation page.\n"
        )
        
        from_email = 'spencerdsheel749@gmail.com'
        to_emails = ['tech@themedius.ai']
        cc_emails = ['hr@themedius.ai']
        attachment_path = 'D:/AI project/AutomateFormFill/selenium_assignment/screenshots/confirmation_page.png'

        email = EmailMessage(subject, body, from_email, to_emails, cc=cc_emails)
        email.attach_file(attachment_path)
        email.send()

        self.stdout.write(self.style.SUCESS('Email sent successfully'))