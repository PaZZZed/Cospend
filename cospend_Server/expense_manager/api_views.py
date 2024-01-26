from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from .models import UserProfile

# @require_http_methods(["POST"])
def get_user_public_keys(request):
    try:
        print(request.GET)
        user_ids = request.POST.getlist('user_ids')
        user_profiles = UserProfile.objects.filter(user_id__in=user_ids)
        public_keys = {profile.user_id: profile.public_key for profile in user_profiles}
        return JsonResponse(public_keys)
    except (ValueError, ObjectDoesNotExist):
        return HttpResponseBadRequest("Invalid request")
