from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        tag_path = f'{tag}'
        tag.save(tag_path)

        return tag_path
