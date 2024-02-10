from barcode import Code128
from barcode.writer import ImageWriter

class BarcodeHandler:
    '''
    Barcode Handler for use extern barcode library, created with facade Design Pattern
    '''
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        folder_output = 'output'
        path_from_tag = f'{folder_output}/{tag}'
        tag.save(path_from_tag)

        return path_from_tag
