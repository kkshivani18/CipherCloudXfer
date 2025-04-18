# CipherCloudXfer 🌩️
This project provides a secure, automated system for encrypting, transferring, and decrypting files between two systems using containerized services and cloud storage. It's a small demo or project for implementing docker. 

🛠️ Tech Stack
- Docker – Containerized sender & receiver services
- Python – Implements encryption & decryption service 
- GitHub Actions – Automates encryption, transfer, and decryption 

🚀 Features
 - End-to-End Encryption – Uses AES/GPG encryption before transfer  
 - Containerized Architecture – Sender & receiver services run in isolated environments    
 - Automated Workflow – GitHub Actions handles file encryption, transfer, and   decryption  
 
🔧 How It Works
 - User uploads a file to the containerized sender service
 - The file is encrypted before being sent using AES/GPG
 - Receiver service automatically decrypts the file after transfer
