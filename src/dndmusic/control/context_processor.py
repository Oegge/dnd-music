def custom_context(request):
    navigation_items = {
        "navigation_items": [
            {"name": "Home", "url": "/"},
            {"name": "Playlists", "url": "/playlists/overview"},
            {"name": "Contact", "url": "/contact"},
        ]
    }
    return navigation_items
