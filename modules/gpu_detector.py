from ssh_connect import SSHConnect
from os_detector import OSDetector

class GPUDETECTOR:

    def __init__(self,hostname,username,password):
        self.hostname = hostname
        self.username = username
        self.password = password
    
    def detect_gpu(self):
        pass