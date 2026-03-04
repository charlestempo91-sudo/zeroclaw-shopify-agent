import requests

class ShopifyAPI:
    def __init__(self, store_url, api_key, password):
        self.base_url = f"https://{api_key}:{password}@{store_url}/admin/api/2024-01"

    def create_or_update_product(self, product_data):
        """创建或更新Shopify产品"""
        payload = {
            "product": {
                "title": product_data["title"],
                "body_html": product_data["description"],
                "variants": [
                    {
                        "price": product_data["price"],
                        "sku": product_data["sku"]
                    }
                ],
                "images": [{"src": product_data["image_url"]}]
            }
        }
        response = requests.post(f"{self.base_url}/products.json", json=payload)
        return response.json()

    def get_new_orders(self, status="open"):
        """获取新订单"""
        response = requests.get(f"{self.base_url}/orders.json?status={status}")
        return response.json().get("orders", [])

    def update_order_note(self, order_id, note):
        """更新订单备注"""
        payload = {"order": {"note": note}}
        response = requests.put(f"{self.base_url}/orders/{order_id}.json", json=payload)
        return response.json()
