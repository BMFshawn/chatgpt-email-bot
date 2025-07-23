# -*- coding: utf-8 -*-
import os
import smtplib
from email.message import EmailMessage
from openai import OpenAI

def main():
    # 1) 환경 변수 읽기
    api_key        = os.getenv("OPENAI_API_KEY")
    gmail_user     = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")
    prompt         = os.getenv(
        "CHATGPT_PROMPT",
        "Please summarize the top 3 AI news items of today."
    )
    email_to       = os.getenv("EMAIL_RECIPIENT", gmail_user)

    # 2) 필수 환경 변수 체크
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY")
    if not gmail_user or not gmail_password:
        raise ValueError("Missing GMAIL_USER or GMAIL_APP_PASSWORD")

    # 3) OpenAI 클라이언트 생성
    client = OpenAI(api_key=api_key)

    # 4) ChatGPT 호출
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",  "content": "You are a helpful assistant."},
            {"role": "user",    "content": prompt}
        ]
    )
    summary = response.choices[0].message.content

    # 5) 이메일 구성
    msg = EmailMessage()
    msg["Subject"] = "📬 ChatGPT AI Summary"
    msg["From"]    = gmail_user
    msg["To"]      = email_to
    msg.set_content(summary)

    # 6) SMTP로 발송
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    main()
