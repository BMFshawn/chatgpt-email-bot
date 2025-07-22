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
        {"role": "system", "content": "당신은 유용한 검색 도우미입니다."},
        {"role": "user", "content": "오늘의 인공지능 관련 주요 뉴스 3가지를 요약해줘"}
    ]
)
result_text = response.choices[0].message["content"]

msg = EmailMessage()
msg["Subject"] = "오늘의 ChatGPT 뉴스 요약"
msg["From"] = gmail_user
msg["To"] = "받는사람@gmail.com"
msg.set_content(result_text)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(gmail_user, gmail_password)
    smtp.send_message(msg)
