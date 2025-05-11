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

## 📁 Project Structure

```
aws-translate-polly-api/
│
├── lambda/
│   └── lambda_function.py        # Main Lambda function
│
├── events/
│   └── sample-event.json         # Example API Gateway event
│
├── screenshots/
│   └── *.png                     # Upload screenshots here
│
└── README.md                     # This file
```

---

## 📦 Sample Request

```http
POST /speak
Content-Type: application/json

{
  "text": "I love AI.",
  "language": "fr"
}
```

---

## ✅ Sample Response

```json
{
  "translated_text": "J'adore l'IA.",
  "audio_url": "https://translate-polly-giles-2025.s3.eu-west-1.amazonaws.com/xxxx.mp3"
}
```

---

## 🧪 Testing Tools

- Postman or any frontend HTML form
- S3 public link opens the mp3 directly
- Translate supports many language codes (e.g., `es`, `fr`, `de`, `it`, `pt`, etc.)

---

## 🖼️ Screenshots

_Add screenshots of your Lambda config, S3 setup, and API Gateway route here._

---

## 👨‍💻 Author

Giles Woodford — AWS Serverless Portfolio Project
