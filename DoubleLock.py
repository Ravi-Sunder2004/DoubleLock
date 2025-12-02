from parsers.dependencies import install_dependencies
from src.pam_totp import configure_pam_totp
from src.server_sshconf import configure_sshd

def main():
    print("=== SSH HARDENING PROJECT START ===\n")

    print("[1/3] Installing dependencies…")
    install_dependencies()
    print("✔ Done.\n")

    print("[2/3] Configuring PAM (TOTP)…")
    configure_pam_totp()
    print("✔ Done.\n")

    print("[3/3] Configuring SSHD…")
    configure_sshd()
    print("✔ Done.\n")

    print("\n All tasks completed successfully!")

if __name__ == "__main__":
    main()
