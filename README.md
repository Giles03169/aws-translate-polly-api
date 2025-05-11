# AWS Translate + Polly API

This project demonstrates how to build a serverless translation + speech synthesis service using AWS Translate, Polly, S3, Lambda, and API Gateway.

---

## 🚀 Features

- Text translation using **Amazon Translate**
- Voice synthesis using **Amazon Polly**
- Public audio link hosted in **S3**
- CORS-enabled **API Gateway** endpoint
- Fully serverless and scalable

---


## 📦 Sample Request

{
  "text": "AWS now lets me speak in french, love Giles.",
  "language": "fr"
}

---

## ✅ Sample Response

```json
{"translated_text": "AWS me permet d\u00e9sormais de parler en fran\u00e7ais, j'adore Giles.", "audio_url": "https://translate-polly-giles-2025.s3.eu-west-1.amazonaws.com/d2323052-9a74-4700-9e3e-3f6fe2b708ee.mp3"}
```

---

## 🧪 Testing Tools

- Postman or any frontend HTML form
- S3 public link opens the mp3 directly
- Translate supports many language codes (e.g., `es`, `fr`, `de`, `it`, `pt`, etc.)

---



---

## 👨‍💻 Author

Giles 
