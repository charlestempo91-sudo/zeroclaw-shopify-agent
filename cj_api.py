import requests

class CJAPI:
    def __init__(self, affiliate_id, api_key):
        self.base_url = "https://api.cj.com/v2"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.affiliate_id = affiliate_id

    def get_products(self):
        """获取CJ产品列表"""
        params = {"advertiserId": self.affiliate_id}
        response = requests.get(f"{self.base_url}/products", headers=self.headers, params=params)
        return response.json().get("products", [])

    def place_order(self, order_data):
        """在CJ创建订单"""
        payload = {
            "order": {
                "advertiserId": self.affiliate_id,
                "items": [
                    {
                        "sku": item["sku"],
                        "quantity": item["quantity"]
                    } for item in order_data["line_items"]
                ],
                "shipping": {
                    "name": order_data["shipping_address"]["name"],
                    "address1": order_data["shipping_address"]["address1"],
                    "city": order_data["shipping_address"]["city"],
                    "state": order_data["shipping_address"]["province"],
                    "zip": order_data["shipping_address"]["zip"],
                    "country": order_data["shipping_address"]["country_code"]
                }
            }
        }
        response = requests.post(f"{self.base_url}/orders", headers=self.headers, json=payload)
        return response.json().get("orderId")
