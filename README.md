# 📬 Automatic Invoice and Boleto Email Sender

Automatically send invoices and boletos via email as soon as they're saved in a client-specific folder.

---

## 🚀 Features

- 📂 Real-time folder monitoring per client
- ✅ File validation (PDFs)
- 📧 Automatic email sending with attachments
- 🔐 Environment-based configuration (.env)
- 🧱 Modular and scalable structure

---

## 🧠 Prerequisites

- Python 3.10+
- An email account with SMTP support (e.g., Gmail with app password)
- VSCode or preferred code editor

---

## 📁 Project Structure

```text
auto-invoice-mailer/
├── app/                  # Core application logic
│   ├── mailer.py         # Email sending logic
│   └── utils.py          # File and client utilities
├── clients/              # Folders by client containing documents
├── logs/                 # System logs (future)
├── config/               # Optional config files (future)
├── main.py               # Main script that runs the monitor
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment configuration
├── .gitignore
└── README.md
```

## ⚙️ How to Run

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/auto-invoice-mailer.git
   cd auto-invoice-mailer
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate # Linux/macOS
   .venv\Scripts\activate # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env file with your email credentials**:

   ```bash
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password
   CLIENTS_FOLDER=clients/
   ```

5. **Run the project**:

   ```bash
   python main.py
   ```

## 🔐 Security

Your actual .env file is ignored via .gitignore and should never be committed.
Always use email app passwords, never your main email password.
Do not include real client data in a public repository.

## 🧪 Example Workflow

You save a boleto.pdf inside clients/ClientName/.
The system automatically detects the new file.
An email is sent to the appropriate recipient with the file as an attachment.

## 🛠️ Tech Stack

- Python 3.10+
- watchdog
- smtplib
- email.message
- dotenv support for environment variables

## 📄 License

This project is licensed under the Apache License. See the LICENSE file for details.

## 👨‍💻 Author

Made with dedication by **Lucas**.  
If you like this project, feel free to ⭐ the repo and contribute!

📬 Contributions, issues, and suggestions are welcome.  
Open a pull request or start a discussion — let's build something great together!

[![GitHub](https://img.shields.io/badge/GitHub-Lucas--Gelenski-181717?style=flat&logo=github)](https://github.com/Gelenski)
