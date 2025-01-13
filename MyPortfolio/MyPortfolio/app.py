from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'razaqsoftware@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'mianwali@1'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'razaqsoftware@gmail.com'  # Replace with your email

mail = Mail(app)

@app.route('/')
def index():
    return render_template('portfolio.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send email
        msg = Message('New Contact Message', recipients=['your_email@gmail.com'])  # Replace with your email
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        return 'Message sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)
