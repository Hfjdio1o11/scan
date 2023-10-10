import paramiko

def check_vps_status(ip, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password, timeout=5)
        stdin, stdout, stderr = client.exec_command('uptime')
        output = stdout.read().decode().strip()
        print(f"\033[1;32mVPS {ip} is up and running. Uptime: {output}")
        client.close()
    except paramiko.AuthenticationException:
        print(f"\033[1;31mFailed to connect to {ip}: Authentication failed")
    except paramiko.SSHException as e:
        print(f"\033[1;31mFailed to connect to {ip}: {str(e)}")
    except paramiko.SSHException as e:
        print(f"\033[1;31mFailed to connect to {ip}: {str(e)}")

# Đọc danh sách địa chỉ IP từ tệp ip.txt
ip_list = []

with open('ip.txt', 'r') as file:
    for line in file:
        ip_list.append(line.strip())

# Thông tin đăng nhập SSH của các VPS
username = "root"   # Thay thế bằng tên người dùng SSH của bạn
password = "root"   # Thay thế bằng mật khẩu SSH của bạn

# Kiểm tra trạng thái của từng VPS
for ip in ip_list:
    check_vps_status(ip, username, password)