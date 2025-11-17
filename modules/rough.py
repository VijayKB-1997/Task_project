lst = '''PRETTY_NAME="Ubuntu 24.04.2 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.2 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo'''
os_info = {}
lines = lst.splitlines()
for line in lines:
   key, value = line.split('=')
   if key not in os_info:
      os_info[key] = value#.strip('""')
print(f'Name : {os_info['NAME']}\nVersion : {os_info["VERSION_ID"]}')
