import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template


def send_message(receiver_name, receiver_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 465
    sender_email = "guralnikelias390@gmail.com"
    from_email = "Elias Newsletter <" + sender_email + ">"
    password = "jyrk krnj hxcr qfoy"

    data = {
        "name": receiver_name,
        "email": receiver_email
    }

    receiver_email = data['email']

    html_content = """\
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .container {
                width: 600px;
                margin: auto;
                padding: 20px;
                font-family: Arial, sans-serif;
                border: 1px solid #ddd;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            }
            h2 {
                color: #2c3e50;
            }
            p {
                font-size: 16px;
                color: #444;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 10px;
                text-decoration: none;
                color: white;
                background-color: #3498db;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Welcome to Our Newsletter – Exciting News Awaits!</h2>
            <p>Hello {{name}},</p>
            <p>Thank you for joining our newsletter! We're thrilled to have you on board.<br />
    
                Here's what you can expect: <br />
                ✔️ Exclusive updates before anyone else<br />
                ✔️ Special offers and discounts<br />
                ✔️ Tips, insights, and exciting news<br />
                
                Stay tuned for our next update—something special is coming your way soon!</p>
            <h3>💡 Follow us on social media to stay even more up to date:</h3>
            <a href="https://www.linkedin.com/in/eliasguralnik/">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn Profile" width="50">
            </a>
    
            <a href="https://github.com/EliasX55">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Profile" width="50">
            </a>
            <p>Best regards, Elias</p>
    
            <a href="https://eliasguralnik.netlify.app" class="button">Visit my website</a>
        </div>
    </body>
    </html>
    """

    template = Template(html_content)
    rendered_html = template.render(data)

    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = receiver_email
    message["Subject"] = "Newsletter from Elias"
    message.attach(MIMEText(rendered_html, "html"))

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("E-Mail wurde erfolgreich gesendet!")


