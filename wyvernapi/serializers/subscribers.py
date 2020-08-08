from rest_framework.serializers import ModelSerializer
from wyvernsubscriptions.models import WyvernSubscribers


class WyvernSubscriptionsSerializer(ModelSerializer):

    # subscriber      = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # sub_site        = models.ForeignKey(WyvernSite, on_delete=models.CASCADE, null=True, blank=True)
    # sub_firstname   = models.CharField(max_length=255, null=True, blank=True)
    # sub_lastname    = models.CharField(max_length=255, null=True, blank=True)
    # sub_fullname    = models.CharField(max_length=255, null=True, blank=True)
    # site_status     = models.IntegerField(choices=choices(Status))
    # sub_date        = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        fields = (
            "id",
            "sub_firstname",
            "sub_lastname",
            "sub_fullname",
            "sub_email",
            "sub_status",
            "sub_date",
        )
        model = WyvernSubscribers

    def create(self, validated_data):
        sub = WyvernSubscribers.objects.create(**validated_data)
        sub.save()

        return sub
