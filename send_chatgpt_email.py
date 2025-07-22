# -*- coding: utf-8 -*-
import smtplib
import openai
from email.message import EmailMessage
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
gmail_user = os.getenv("GMAIL_USER")
gmail_password = os.getenv("GMAIL_APP_PASSWORD")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "����� ������ �˻� ������Դϴ�."},
        {"role": "user", "content": "������ �ΰ����� ���� �ֿ� ���� 3������ �������"}
    ]
)
result_text = response.choices[0].message["content"]

msg = EmailMessage()
msg["Subject"] = "������ ChatGPT ���� ���"
msg["From"] = gmail_user
msg["To"] = "�޴»��@gmail.com"
msg.set_content(result_text)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(gmail_user, gmail_password)
    smtp.send_message(msg)
