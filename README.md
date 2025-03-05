---

# **AWS Lambda Image Resizer 🚀**  

## 📌 Overview  
This project is an **AWS Lambda function** that **automatically resizes images** when uploaded to an **S3 bucket**. The resized image is then stored in another **S3 bucket**, and an **SNS notification** is sent to subscribers.  

## 🛠 Tech Stack  
- **AWS Lambda (Python 3.9)**  
- **Amazon S3** (Storage)  
- **Amazon SNS** (Notifications)  
- **IAM Roles & Policies**  
- **boto3** (AWS SDK for Python)  
- **Pillow** (Python Imaging Library)  

---

## 📂 Project Structure  
```
aws-lambda-image-resizer/
│── lambda_function.py   # Main Lambda function  
│── README.md            # Project documentation  
│── requirements.txt     # Python dependencies  
│── .gitignore           # Files to ignore in Git  
```

---

## 📥 Installation  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/ritikops/aws-lambda-image-resizer.git
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## 📌 AWS Setup Guide  

### **1️⃣ Create S3 Buckets**  
- **Source Bucket:** `source-images-bucket`  
- **Destination Bucket:** `resized-images-bucket`  

### **2️⃣ Create an IAM Role for Lambda**  
Attach the following permissions:  
✅ `AmazonS3FullAccess`  
✅ `AWSLambdaBasicExecutionRole`  
✅ `SNS Publish` permissions  

### **3️⃣ Deploy the Lambda Function**  
- Upload `lambda_function.py`  
- Set the runtime to **Python 3.9**  
- Add an **S3 Trigger** for `source-images-bucket`  

### **4️⃣ Create an SNS Topic**  
- Topic Name: `ImageResizeNotification`  
- Subscribe via **Email or SMS**  

---

## 📝 License  
This project is licensed under the **MIT License**.  

---

## 📌 Additional Files  

### **`.gitignore`**  
```gitignore
__pycache__/
*.pyc
.env
```

### **`requirements.txt`**  
```txt
boto3
Pillow
```

---
