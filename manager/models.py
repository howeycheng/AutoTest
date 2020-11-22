from django.db import models


# Create your models here.


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_user = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectUser(models.Model):
    project_id = models.PositiveIntegerField(primary_key=True)
    user_id = models.PositiveIntegerField()
    access_level = models.SmallIntegerField()
    is_book_mail = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'project_user'
        unique_together = (('project_id', 'user_id'),)
