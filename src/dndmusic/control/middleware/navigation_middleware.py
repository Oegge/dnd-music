class NavigationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    
        response = self.get_response(request)
        print(response)
        if hasattr(response, 'context_data'):
            navigation_items = [
                {"name": "Home", "url": "/"},
                {"name": "About", "url": "/about/"},
                {"name": "Contact", "url": "/contact/"}
            ]
            response.context_data["navigation_items"] = navigation_items
            print("triggerd")
            

        return response
