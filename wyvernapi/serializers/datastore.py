from rest_framework.serializers import ModelSerializer
from wyverndatastorage.models import WyvernDataStore
from wyvernsite.models import WyvernSite


class WyvernDataStoreSerializer(ModelSerializer):
    class Meta:
        fields = (
            "id",
            "data_store_identity",
            "data_store_content",
            "data_store_tags",
        )  # , 'data_store_site')
        model = WyvernDataStore
        validators = []

    def create(self, validated_data):

        data = WyvernDataStore.objects.create(**validated_data)
        data.save()

        return data


class WyvernDataStoredSerializer(ModelSerializer):
    class Meta:
        model = WyvernDataStore
        fields = (
            "id",
            "data_store_identity",
            "data_store_timestamp",
            "data_store_content",
        )  # , 'data_store_site')
