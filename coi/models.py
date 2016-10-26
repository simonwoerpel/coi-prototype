from django.db import models


class Record(models.Model):
    author_name = models.CharField(max_length=255)
    author_affiliation = models.CharField(max_length=2000, blank=True, null=True)
    paper_date = models.DateField()
    paper_title = models.CharField(max_length=2000)
    conflict = models.TextField()
