# -*- coding: utf-8 -*-
import smtplib
from openai import OpenAI
from email.message import EmailMessage
import os

# 환경 변수에서 API 키 가져오기
api_key = os.getenv("OPENAI_API_KEY")
gmail_user = os.getenv("GMAIL_USER")
gmail_password = os.getenv("GMAIL_APP_PASSWORD")

# OpenAI 클라이언트 생성
client = OpenAI(api_key=api_key)

# ChatGPT 응답 생성
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Summarize the main AI-related news headlines today."}
    ]
)

result_text = response.choices[0].message.content

# 이메일 구성
msg = EmailMessage()
msg["Subject"] = "📬 Today’s AI Summary from ChatGPT"
msg["From"] = gmail_user
msg["To"] = "sangho.ok@sktelecom.com"
msg.set_content(result_text)

# 이메일 전송
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(gmail_user, gmail_password)
    smtp.send_message(msg)
