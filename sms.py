import email, smtplib, ssl
from providers import PROVIDERS

def send_sms( number, message, provider,
    sender_cred, subject="None", smtp_server="smtp.gmail.com",
    smtp_port=465):
    
    sender_email, email_password = sender_cred
    receiver_email = number+"@"+PROVIDERS[provider]["sms"]

    email_message = "Subject:"+subject+"\nTo:"+receiver_email+"\n"+message

    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_cred, receiver_email, email_message)

def main():
    number = "7049967447"
    message = "what is up?"
    provider = "Verizon"

    sender = ("foreverygame.11@gmail.com", "ksggtbqwxrdbsfje")

    send_sms(number, message, provider, sender)

if __name__ == "__main__":
    main()

