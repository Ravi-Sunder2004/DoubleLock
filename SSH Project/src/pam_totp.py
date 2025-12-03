import shutil
import os

config_path = '/etc/pam.d/sshd'
backup_path = '/etc/pam.d/sshd.bak'

def configure_pam_totp():
    shutil.copy(config_path, backup_path)

    if os.path.exists(backup_path) and os.path.getsize(backup_path) > 0:
        print("PAM backup created.")
    else:
        print("Backup failed.")
        exit(1)

    with open(config_path, 'r') as file:
        lines = file.readlines()

    setting_line = "auth required pam_google_authenticator.so nullok \n"

    def update_pam(lines):
        for line in lines:
            if "pam_google_authenticator.so" in line and not line.strip().startswith("#"):
                print("Google Authenticator already enabled in PAM.")
                return lines

        updated = []
        inserted = False

        for line in lines:
            if not inserted and "@include common-auth" in line:
                updated.append(setting_line)
                inserted = True
            updated.append(line)

        if not inserted:
            updated.insert(0, setting_line)

        print("Google Authenticator PAM entry added.")
        return updated

    updated_lines = update_pam(lines)

    with open(config_path, "w") as file:
        file.writelines(updated_lines)

    print("PAM file updated successfully.")
