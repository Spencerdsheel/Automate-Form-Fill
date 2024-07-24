## Automate-Form-Fill" 
# Python (Selenium) Assignment

## Overview
This project automates the submission of a Google form using Selenium, captures a screenshot of the confirmation page, and sends the screenshot via email using Django.

## Requirements
- Python 3.x
- Selenium
- WebDriver Manager
- Django

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd selenium_assignment
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure email settings**:
    Update the email settings in `selenium_assignment/settings.py` with your SMTP server details.

4. **Submit the form and capture the screenshot**:
    ```sh
    python form_submitter.py
    ```

5. **Send the email**:
    ```sh
    python manage.py send_email
    ```

## File Structure
- `form_submitter.py`: Script to submit the form and capture the screenshot.
- `emailer/`: Django app to send the email.
- `emailer/management/commands/send_email.py`: Django management command to send the email.

## Screenshot
![Confirmation Page](confirmation_page.png)
