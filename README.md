🔐 DoubleLock – SSH 2FA Automation (v0.8)

DoubleLock is a lightweight automation tool that enables Google Authenticator–based Two-Factor Authentication (2FA) on Linux SSH servers with minimal user input.

The tool configures SSH and PAM, ensures correct 2FA flow, and creates backups before modifying system files.

✨ Features

🔒 Automates enabling Google Authenticator 2FA for SSH

⚙️ Automatically updates PAM + SSHD configurations

🗄️ Creates backups of:

 - /etc/ssh/sshd_config

 - /etc/pam.d/sshd

📲 Guides user through Google Authenticator setup

🚀 Stable login flow: Verification Code → Password

📁 Python-based automation (DeadLock.py)

🔧 Future expansion planned (v1.0 roadmap)

📦 Installation & Usage
1. Clone the repository
git clone https://github.com/yourusername/DoubleLock.git
cd DoubleLock

2. Run the automation script

Execute as root:

sudo python DeadLock.py


This script will:

Configure SSHD & PAM for 2FA

Create backup copies

Prepare your system for Google Authenticator setup

3. Enable Google Authenticator

Run:

google-authenticator


Select YES for all recommended prompts:

Time-based tokens

Update existing key

Prevent code reuse

Rate limiting

Backup scratch codes

4. Start or restart SSH

Start SSH:

sudo systemctl start ssh


If SSH is already running:

sudo systemctl restart ssh


Your SSH server is now protected by DoubleLock 2FA 🛡️

📝 Important Notes

auth_log_parser.py does not affect the project.
It is not implemented in this version (v0.8) but planned for future updates.

This is an early version — more automation, error handling, and
log-parsing features will be added soon.

🛠️ Roadmap (Upcoming Versions)

🔍 SSH log parsing & anomaly detection

🚫 Fail2Ban integration

📊 2FA status verification

🔄 Auto-rollback on misconfiguration

🧪 Self-test module to verify SSH 2FA

📫 Feedback & Suggestions

For feedback or feature requests, contact:

📧 sunderravi27@gmail.com

Your suggestions help improve DoubleLock!

⭐ Support

If you found this project helpful, please consider giving it a star ⭐ on GitHub!
