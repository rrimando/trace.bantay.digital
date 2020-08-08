from rest_framework.serializers import ModelSerializer
from wyvernjobs.models import WyvernJobs


class WyvernJobsSerializer(ModelSerializer):

    # job_site                  = models.ForeignKey(WyvernSite, on_delete=models.CASCADE)
    # job_title                     = models.CharField(max_length=255)
    # job_description               = models.TextField(null=True, blank=True)
    # job_subtitle                  = models.CharField(max_length=255, null=True, blank=True)
    # job_slug                      = models.CharField(max_length=255, null=True, blank=True)
    # job_image                     = models.ImageField(upload_to=get_file_path, null=True, blank=True) # TODO - Pull from config
    # job_status                    = models.IntegerField(choices=choices(Status))
    # job_posted_by                 = models.ForeignKey(User, on_delete=models.CASCADE)
    # job_type                      = models.CharField(max_length=50, choices=job_type, default='aggro') # Pull from config
    # job_notifications_recipients  = models.CharField(max_length=255, null=True, blank=True)
    # date_created                  = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        fields = (
            "id",
            "job_site",
            "job_title",
            "job_type",
            "job_description",
            "job_subtitle",
            "job_slug",
            "job_status",
            "job_hours",
            "job_experience_required",
            "job_location",
        )
        model = WyvernJobs

    def create(self, validated_data):
        job = WyvernJobs.objects.create(**validated_data)
        job.save()

        return job
