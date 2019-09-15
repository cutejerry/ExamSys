from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Subject(models.Model):
#    exam_id = models.ForeignKey("Exam", null = True, blank = True)
    number = models.CharField(max_length=512, null = True, blank = False)
    content_txt = models.TextField(null = True, blank = False)
    answer_idx = models.PositiveSmallIntegerField(default=1)
    options1 = models.TextField(max_length=1024, null = True, blank = True)
    options2 = models.TextField(max_length=1024, null = True, blank = True)
    options3 = models.TextField(max_length=1024, null = True, blank = True)
    options4 = models.TextField(max_length=1024, null = True, blank = True)
    options5 = models.TextField(max_length=1024, null = True, blank = True)
    content_img = models.ImageField(upload_to="images", null=True, blank=True)
    content_video = models.URLField(null=True, blank=True)
    options6 = models.TextField(max_length=1024, null = True, blank = True)
    options7 = models.TextField(max_length=1024, null = True, blank = True)
    options8 = models.TextField(max_length=1024, null = True, blank = True)
    type = models.CharField(max_length=512, null = True, blank = True)
    period = models.PositiveSmallIntegerField(null = True, blank = True, default=1)
    theme =  models.CharField(max_length=512, null = True, blank = True)
    point1 = models.CharField(max_length=512, null = True, blank = True)
    point2 = models.CharField(max_length=512, null = True, blank = True)
    point3 = models.CharField(max_length=512, null = True, blank = True)
    logic = models.CharField(max_length=512, null = True, blank = True)
    difficult = models.PositiveSmallIntegerField(null = True, blank = True, default=1)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.number

class Exam(models.Model):
    name = models.CharField(max_length=128, unique=True)
    subjects_set = models.ManyToManyField("Subject")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name