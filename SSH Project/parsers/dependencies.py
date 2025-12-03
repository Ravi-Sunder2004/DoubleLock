import subprocess

def install_dependencies():
    check = subprocess.run(['which', 'google-authenticator'], capture_output=True)

    if check.returncode != 0:
        install = subprocess.run(['sudo', 'apt', 'install', '-y', 'libpam-google-authenticator'])
        
        if install.returncode == 0:
            print("Google Authenticator successfully installed.")
        else:
            print("Error: installation failed.")
    else:
        print("Google Authenticator is already installed.")
