from ssh_connect import SSHConnect
import platform
import os

class OSDetector:
    @staticmethod 
    def detect_os(ssh):
        command = 'cat /etc/os-release'
        try:
            # ssh = SSHConnect(self.hostname,self.username,self.password)
            # ssh.connect()
            os_info ={}
            out,err = ssh.execute_command(command)
            if 'NAME=' in out or 'Name=' in out:
                print("Linux OS detctected..")
                lines = out.splitlines()
                for line in lines:
                    if "=" not in line:
                        continue
                    key, value = line.split("=", 1)
                    os_info[key] = value.strip().strip('"')
                OS_Name = os_info.get("NAME", "Not exist")
                OS_Version = os_info.get("VERSION_ID", "Not exist")
                print(f"Name : {OS_Name}, Version : {OS_Version}")
                return OS_Name, OS_Version   
            else:
                print("Windows OS detetcted..")
               
        except Exception as e:
            print(f"OS detection failed: {e}")

if __name__ == '__main__':
    OS = OSDetector()
    OS.detect_os()

    
    
