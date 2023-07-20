from flask import Flask, render_template, jsonify, request
from email.message import EmailMessage


import smtplib
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/opt')
def opt():
    return render_template("opt.html")


@app.route("/vad")
def vad():
    return render_template("vad.html")


@app.route("/api/forma/", methods=['POST', "GET"])
def post_api_form():
    data = request.get_data()
    print(data)
    # данные для отправки письма
    sender_email = 'sale@amlayn.ru'
    sender_password = 'SVzxPegQnGyCjL2HQH97'
    receiver_email = 'sale@amlayn.ru'
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    subject = 'Заявка на ВЭД - ОПТ'
    data_str = data.decode('utf-8') 
    data_dict = json.loads(data_str)
    body = f'Имя - {data_dict["name"]}\nПочта - {data_dict["mail"]}\nНомер телефона - {data_dict["tel"]}'
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)
    server.sendmail(sender_email, receiver_email, msg.as_bytes())

    server.quit()
    return jsonify({"status": True})
    


if __name__ == "__main__":
    app.run(debug=True)

