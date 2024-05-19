def custom_context(request):
    navigation_items = {
        "navigation_items": [
            {"name": "Home", "url": "/"},
            {"name": "About", "url": "/about/"},
            {"name": "Contact", "url": "/contact/"},
        ]
    }
    return navigation_items
