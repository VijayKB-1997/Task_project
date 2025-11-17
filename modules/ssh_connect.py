import paramiko 
import time


class SSHConnect:
    def __init__(self,hostname,username,password,port: int = 22):
        self.hostname = hostname 
        self.username = username
        self.password = password 
        self.port = port
        self.ssh = None
    
    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            print(f"Connecting to {self.hostname}..")
            time.sleep(3)
            #self.ssh.connect(self.hostname,self.username,self.password)
            self.ssh.connect(
                hostname=self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
                # timeout=5,
                # banner_timeout=5,
                # auth_timeout=5
            )
            print(f"Connected to {self.hostname}")
            
        except paramiko.AuthenticationException:
            print("Authentication failed, please check your credentials.")
        except paramiko.SSHException as e:
            print(f"SSH connection failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def execute_command(self,command):
        try:
            stdin,stdout,stderr= self.ssh.exec_command(command)
            out =stdout.read().decode().strip()
            err =stderr.read().decode().strip()
            # if out:
            #     print(out)
            # else:
            #     print(err)   
            return out, err
        
        except UnicodeDecodeError as e:
            print(f"Output decode issue: {e}")
            return None, str(e)
        except Exception as e:
            print(f"Unexpected error while executing '{command}': {e}")
            return None, str(e)
    
    def close(self):
        self.ssh.close()
        
        print(f"Disconnected from {self.hostname}!")

if __name__ == "__main__":
    ssh = SSHConnect('100.98.241.146','root','dell@123')
    ssh.connect()
    ssh.execute_command('ls')
    ssh.close()
