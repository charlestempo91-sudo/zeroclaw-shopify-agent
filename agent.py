from flask import Flask, request, jsonify
import requests
import hashlib
import time
import config

app = Flask(__name__)

def cj_create_order(shopify_order):
    """将 Shopify 订单自动同步到 CJ Dropshipping 发货"""
    timestamp = str(int(time.time()))
    sign_str = f"{config.CJ_API_KEY}{timestamp}{config.CJ_SECRET_KEY}"
    sign = hashlib.md5(sign_str.encode()).hexdigest().upper()

    order_data = {
        "store_id": config.CJ_STORE_ID,
        "order_id": str(shopify_order["id"]),
        "recipient_name": shopify_order["shipping_address"]["name"],
        "recipient_phone": shopify_order["shipping_address"].get("phone", ""),
        "recipient_email": shopify_order["email"],
        "recipient_country": shopify_order["shipping_address"]["country"],
        "recipient_state": shopify_order["shipping_address"]["province"],
        "recipient_city": shopify_order["shipping_address"]["city"],
        "recipient_address1": shopify_order["shipping_address"]["address1"],
        "recipient_address2": shopify_order["shipping_address"].get("address2", ""),
        "recipient_zip": shopify_order["shipping_address"]["zip"],
        "items": [
            {
                "sku": item["sku"],
                "quantity": item["quantity"],
                "price": item["price"]
            } for item in shopify_order["line_items"]
        ]
    }

    url = "https://developers.cjdropshipping.com/api/v2/orders"
    headers = {
        "Content-Type": "application/json",
        "CJ-Api-Key": config.CJ_API_KEY,
        "CJ-Timestamp": timestamp,
        "CJ-Sign": sign
    }

    response = requests.post(url, json=order_data, headers=headers)
    return response.json()

@app.route('/webhook/shopify/orders', methods=['POST'])
def handle_shopify_order():
    """处理 Shopify 订单创建 Webhook"""
    order = request.get_json()
    print(f"✅ 收到新订单 - ID: {order['id']}")
    print(f"💰 订单金额: ${order['total_price']}")
    print(f"📧 客户邮箱: {order['email']}")

    # 自动同步到 CJ 发货
    cj_response = cj_create_order(order)
    print(f"📦 CJ 发货响应: {cj_response}")

    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
