from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Profile, Unite  # Adjust this import based on your actual model locations

class StationNameBackend(BaseBackend):
    def authenticate(self, request, unitename=None, password=None, **kwargs):
        try:
            # Assuming `unite` has a field `name` that stores the station name
            unite = Unite.objects.get(unite_name=unitename)
            profiles = Profile.objects.filter(unite=unite)
            for profile in profiles:
                user = profile.user

                if user.check_password(password):
                    return user
        except (Unite.DoesNotExist, Profile.DoesNotExist, User.DoesNotExist):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None