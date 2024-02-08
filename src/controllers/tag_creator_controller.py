from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    def create(self, product_code: str) -> Dict:
        tag_path = self.__create_tag(product_code)
        formatted_response = self.__format_response(tag_path)
        return formatted_response

    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        tag_path = barcode_handler.create_barcode(product_code)
        return tag_path

    def __format_response(self, tag_path: str) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{tag_path}.png'
            }
        }
