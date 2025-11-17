from ssh_connect import SSHConnect
import platform
import os

class OSDetector:
    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
        
    def detect_os(self):
        command = 'cat /etc/os-release'
        try:
            ssh = SSHConnect(self.hostname,self.username,self.password)
            ssh.connect()
            os_info ={}
            out,err= ssh.execute_command(command)
            if 'Linux' or 'linux' in out:
                print("Linux OS detctected..")
                #print(out)
                lines = out.splitlines()
                for line in lines:
                    key, value = line.split('=')
                    if key not in os_info.keys():
                         os_info[key] = value.strip('""')
                print(f'Name : {os_info['NAME']}, Version : {os_info["VERSION_ID"]}')
                OS_Name = os_info['NAME']
                OS_Version = os_info["VERSION_ID"]
                return OS_Name, OS_Version
            else:
                print("Windows OS detetcted..")
            ssh.close()
        except Exception as e:
            print(f"OS detection failed: {e}")
        

if __name__ == '__main__':
    OS = OSDetector('100.98.241.146','root','dell@123')
    OS.detect_os()

    
    
