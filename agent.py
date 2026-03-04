from shopify_api import ShopifyAPI
from cj_api import CJAPI
import config

class ZeroClawAgent:
    def __init__(self):
        # 初始化Shopify和CJ的API客户端
        self.shopify = ShopifyAPI(
            store_url=config.SHOPIFY_STORE_URL,
            api_key=config.SHOPIFY_API_KEY,
            password=config.SHOPIFY_PASSWORD
        )
        self.cj = CJAPI(
            affiliate_id=config.CJ_AFFILIATE_ID,
            api_key=config.CJ_API_KEY
        )

    def sync_products_from_cj_to_shopify(self):
        """从CJ同步产品到Shopify"""
        print("开始从CJ同步产品...")
        cj_products = self.cj.get_products()
        for product in cj_products:
            self.shopify.create_or_update_product(product)
        print("产品同步完成。")

    def process_new_shopify_orders(self):
        """处理Shopify的新订单，自动在CJ下单"""
        print("开始处理新订单...")
        shopify_orders = self.shopify.get_new_orders()
        for order in shopify_orders:
            cj_order_id = self.cj.place_order(order)
            self.shopify.update_order_note(order['id'], f"CJ订单ID: {cj_order_id}")
        print("订单处理完成。")

if __name__ == "__main__":
    agent = ZeroClawAgent()
    # 先同步产品
    agent.sync_products_from_cj_to_shopify()
    # 再处理订单
    agent.process_new_shopify_orders()
