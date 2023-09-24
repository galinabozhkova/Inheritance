from shop.product import Product


class ProductRepository():
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for el in self.products:
            if el.name == product_name:
                return el

    def remove(self, product_name):
        for el in self.products:
            if el.name == product_name:
                self.products.remove(el)

    def __repr__(self):
        result = '\n'.join(f"{el.name}: {el.quantity}" for el in self.products)
        return result
