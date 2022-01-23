from rest_framework.serializers import ModelSerializer
from wyvernuser.models import User


class WyvernUserSerializer(ModelSerializer):
    class Meta:
        # fields = ('id', 'job_site', 'job_title', 'job_type', 'job_description', 'job_subtitle', 'job_slug', 'job_status')
        model = User
