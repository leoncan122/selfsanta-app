from fastapi import Request

def call_api_gateway(request: Request):
    portal_id = request.path_params["portal_id"]

    if portal_id == "user":
        raise RedirectUserPortalException()
    elif portal_id == "purchase":
        raise RedirectPurchasePortalException()
    elif portal_id == "product":
        raise RedirectProductLinksException()

class RedirectUserPortalException(Exception):
    pass

class RedirectPurchasePortalException(Exception):
    pass   

class RedirectProductLinksException(Exception):
    pass
