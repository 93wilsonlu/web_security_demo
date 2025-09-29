"""
簡單的 Flask XSS 靶機（單檔）
說明：
 - /       : 顯示搜尋表單
 - /search : 接收 GET 參數 q，會在頁面上原樣回顯（刻意存在反射/儲存型 XSS 的示範點）

注意：本程式為教學用途，請務必在內網/隔離環境執行，勿公開部署。
"""

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# 範例產品資料
PRODUCTS = [
    {"id": 1, "name": "USB-C Hub", "desc": "7-port USB hub with 4K HDMI output", "price": 1299, "rating": 4.5, "reviews": 234},
    {"id": 2, "name": "Mechanical Keyboard", "desc": "Cherry MX Blue switch, RGB backlit", "price": 2890, "rating": 4.8, "reviews": 567},
    {"id": 3, "name": "Wireless Mouse", "desc": "Ergonomic design, 2.4GHz wireless", "price": 890, "rating": 4.3, "reviews": 189},
    {"id": 4, "name": "Webcam", "desc": "1080p 60fps with auto-focus", "price": 1590, "rating": 4.6, "reviews": 423},
    {"id": 5, "name": "27-inch Monitor", "desc": "IPS 144Hz gaming monitor", "price": 8999, "rating": 4.7, "reviews": 892},
    {"id": 6, "name": "Portable SSD 1TB", "desc": "NVMe USB-C ultra-fast storage", "price": 3299, "rating": 4.9, "reviews": 1234},
    {"id": 7, "name": "Noise Cancelling Headphones", "desc": "Over-ear Bluetooth with ANC", "price": 4599, "rating": 4.4, "reviews": 678},
    {"id": 8, "name": "Laptop Stand", "desc": "Aluminum adjustable foldable stand", "price": 799, "rating": 4.2, "reviews": 345},
    {"id": 9, "name": "USB Microphone", "desc": "Professional streaming microphone", "price": 2199, "rating": 4.6, "reviews": 456},
    {"id": 10, "name": "Smartphone Gimbal", "desc": "3-axis stabilizer for mobile filming", "price": 3599, "rating": 4.3, "reviews": 234},
    {"id": 11, "name": "Wi-Fi 6 Router", "desc": "Dual-band MU-MIMO mesh router", "price": 5999, "rating": 4.5, "reviews": 789},
    {"id": 12, "name": "Bluetooth Speaker", "desc": "Portable waterproof speaker", "price": 1899, "rating": 4.4, "reviews": 567},
    {"id": 13, "name": "Action Camera", "desc": "4K ultra HD with image stabilization", "price": 6999, "rating": 4.7, "reviews": 890},
    {"id": 14, "name": "3D Mouse", "desc": "Professional CAD and 3D design mouse", "price": 4299, "rating": 4.1, "reviews": 123},
    {"id": 15, "name": "RGB Desk Lamp", "desc": "Adjustable color temperature LED lamp", "price": 1699, "rating": 4.3, "reviews": 345},
    {"id": 16, "name": "Power Bank 20000mAh", "desc": "Quick Charge & Power Delivery support", "price": 999, "rating": 4.5, "reviews": 678},
]

INDEX_HTML = """

"""


@app.route('/')
def index():
    # 預設沒有搜尋
    return render_template('index.html', q="", products=PRODUCTS, q_escaped="")


@app.route('/search')
def search():
    # 取得 GET 參數 q
    q = request.args.get('q', '')

    # 簡單的篩選（用於示範）
    matched = []
    if q:
        q_lower = q.lower()
        for p in PRODUCTS:
            if q_lower in p['name'].lower() or q_lower in p['desc'].lower():
                matched.append(p)
    else:
        matched = PRODUCTS

    # 注意：我們故意在 template 裡面使用 |safe 回顯 q，模擬未經處理的輸入回顯導致 XSS。
    #       教學時可讓學生嘗試輸入 <script>alert(1)</script> 或 <img src=x onerror=...>

    return render_template('index.html', q=q, products=matched, q_escaped=q)


if __name__ == '__main__':
    # 開發模式（只用於教學環境），不要在公開伺服器啟動 debug 模式
    app.run(host='0.0.0.0', port=10009, debug=True)
