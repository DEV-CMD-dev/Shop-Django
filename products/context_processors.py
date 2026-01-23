def favorites_processor(request):
    return {
        'favorite_ids': request.session.get('favorites', [])
    }
