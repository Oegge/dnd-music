def custom_context(request):
    navigation_items = {
        "navigation_items": [
            {"name": "Home", "url": "/"},
            {"name": "Playlists", "url": "/playlists/overview"},
            {"name": "Contact", "url": "/contact"},
            {"name": "All Songs", "url": "/songs/play"},
        ]
    }
    return navigation_items
