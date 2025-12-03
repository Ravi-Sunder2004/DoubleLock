import subprocess
import shutil
import os
import re

config_path = '/etc/ssh/sshd_config'
backup_path = '/etc/ssh/sshd_config.bak'

def configure_sshd():
    shutil.copy(config_path, backup_path)

    if os.path.exists(backup_path) and os.path.getsize(backup_path) > 0:
        print("Backup of SSH configuration created.")
    else:
        print("Backup creation failed.")
        exit(1)

    with open(config_path, 'r') as file:
        lines = file.readlines()

    settings = {
        'KbdInteractiveAuthentication': 'yes',
        'PasswordAuthentication': 'yes',
        'PermitRootLogin': 'yes',
        'ChallengeResponseAuthentication': 'yes',
        'AuthenticationMethods': 'keyboard-interactive password',
        'UsePam': 'yes'
    }

    def update_settings(lines, settings):
        updated_lines = []
        found_settings = set()

        for line in lines:
            stripped_line = line.strip()

            if stripped_line.startswith('#') or not stripped_line:
                updated_lines.append(line)
                continue

            matched = False
            for key, value in settings.items():
                if re.match(f'^{key}\\s+', stripped_line, re.IGNORECASE):
                    updated_lines.append(f"{key} {value}\n")
                    found_settings.add(key)
                    matched = True
                    break

            if not matched:
                updated_lines.append(line)

        for key, value in settings.items():
            if key not in found_settings:
                updated_lines.append(f"{key} {value}\n")

        return updated_lines

    updated_lines = update_settings(lines, settings)

    with open(config_path, 'w') as file:
        file.writelines(updated_lines)
        print(f"SSH configuration updated at {config_path}")

    def reload_ssh_service():
        commands = [
            ["systemctl", "reload", "ssh"],
            ["systemctl", "reload", "sshd"],
            ["service", "ssh", "reload"],
            ["service", "sshd", "reload"]
        ]
        for cmd in commands:
            reload = subprocess.run(cmd)
            if reload.returncode == 0:
                print("SSHD service reloaded successfully.")
                return True
        print("Failed to reload SSHD service. Reload manually.")

    test_run = subprocess.run(['sshd', '-t'], capture_output=True, text=True)
    if test_run.returncode == 0:
        print("SSHD configuration test passed.")
        reload_ssh_service()
    else:
        print("SSHD configuration test failed:")
        print(test_run.stderr)
        shutil.copy(backup_path, config_path)
        print(f"Restored original config from {backup_path}")
