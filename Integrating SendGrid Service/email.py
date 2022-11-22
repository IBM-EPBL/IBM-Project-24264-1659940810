from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

email = "xxx@gmail.com"
username = "xxx"

message = Mail(from_email='customercareregcj7@gmail.com', to_emails=email, subject='Customer Care Registry - Account Creation',
               html_content='Hello '+username + ',\n\n' + """\n\nThank you for registering as a customer with Customer Care Registry Application. """)

sg = SendGridAPIClient('')
response = sg.send(message)
