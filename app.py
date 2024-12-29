from flask import Flask, render_template, request, redirect, url_for, flash
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For flashing messages

# Your email details
EMAIL_SENDER = "kavungalvinesh@gmail.com"
EMAIL_PASSWORD = "juhcwdkvudxnjszl"  # Use App Password if using Gmail

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        email_receiver = request.form['email']
        subject = request.form['subject']
        body = request.form['body']
        
        try:
            # Email sending logic
            em = EmailMessage()
            em['From'] = EMAIL_SENDER
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
                smtp.sendmail(EMAIL_SENDER, email_receiver, em.as_string())
            
            flash("Email sent successfully!", "success")
            return redirect(url_for('done'))

        except Exception as e:
            flash(f"Failed to send email: {e}", "danger")
            return redirect(url_for('send_email'))
    
    return render_template('email_form.html')

@app.route('/done')
def done():
    return render_template('Done.html')

if __name__ == "__main__":
    app.run(debug=True)
