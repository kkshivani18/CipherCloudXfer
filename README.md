# CipherCloudXfer 🌩️
This project provides a secure, automated system for encrypting, transferring, and decrypting files between two systems using containerized services and cloud storage. It's a small demo or project for implementing docker. 

![architecture of project](https://github.com/user-attachments/assets/25ab03c7-19e9-430e-8f89-d1df94de812b)  

🛠️ Tech Stack
- Docker – Containerized sender & receiver services
- Python – Implements encryption & decryption service 
- GitHub Actions – Automates encryption, transfer and decryption 

🚀 Features
 - End-to-End Encryption – Uses AES encryption done via Fernet before transfer  
 - Containerized Architecture – Sender & receiver services run in isolated environments    
 - Automated Workflow – GitHub Actions handles file encryption, transfer, and   decryption  
 
🔧 How It Works
 - User uploads a file to the containerized sender service
 - The file is encrypted before being sent using AES via Fernet
 - Receiver service automatically decrypts the file after transfer
