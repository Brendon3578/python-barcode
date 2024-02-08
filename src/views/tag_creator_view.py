from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsibility for interacting with HTTP
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # body = http_request.body
        # product_code = body["product_code"]

        # business logic
        print('validated and created')
        print(http_request)

        # http return
        return HttpResponse(status_code=200, body={"barcode_status": "created"})
