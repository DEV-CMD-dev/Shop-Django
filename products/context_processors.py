from .models import Favorite

def favorites_processor(request):
    if request.user.is_authenticated:
        return {
            "favorite_ids": set(
                Favorite.objects.filter(user=request.user)
                .values_list("product_id", flat=True)
            )
        }
    return {"favorite_ids": set()}
