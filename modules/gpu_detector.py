from ssh_connect import SSHConnect
from os_detector import OSDetector

class GPUDETECTOR:

    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
    
    def detect_gpu(self):
        command = 'clear'
        try:
            ssh = SSHConnect(self.hostname,self.username,self.password)
            ssh.connect()
            get_os = OSDetector
            os_name,os_version = get_os.detect_os(ssh)
            if os_name == 'Ubuntu' or 'ubuntu':
                out , err =ssh.execute_command(command)
                print(out)
            ssh.close()
        except Exception as e:
            print(f"error occured:{e}")

if __name__ == '__main__':
    gpu = GPUDETECTOR('100.98.179.97','root','dell@123')
    gpu.detect_gpu()