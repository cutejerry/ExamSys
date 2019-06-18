from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Subject(models.Model):
#    exam_id = models.ForeignKey("Exam", null = True, blank = True)
    degree = models.PositiveSmallIntegerField(verbose_name = "Degree: 0-easy;5-normal;10-hard")
    type = models.CharField(choices=(("1", "ADD"),("2", "SUB"),("3", "MUL"),("4", "DIV"),("0", "others")), max_length = 1, default = "0")
    content_txt = models.TextField(null = True, blank = False)
    answer_idx = models.PositiveSmallIntegerField()
    options1 = models.CharField(max_length=512, null = True, blank = True)
    options2 = models.CharField(max_length=512, null = True, blank = True)
    options3 = models.CharField(max_length=512, null = True, blank = True)
    options4 = models.CharField(max_length=512, null = True, blank = True)
    content_img = models.ImageField(upload_to="images", null=True, blank=True)
    content_video = models.URLField(null=True, blank=True)
    options5 = models.CharField(max_length=512, null = True, blank = True)
    options6 = models.CharField(max_length=512, null = True, blank = True)
    options7 = models.CharField(max_length=512, null = True, blank = True)
    options8 = models.CharField(max_length=512, null = True, blank = True)
    attr1 = models.PositiveSmallIntegerField(default=0)
    attr2 = models.PositiveSmallIntegerField(default=0)
    attr3 = models.PositiveSmallIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "ID: " + str(self.id)

class Exam(models.Model):
    name = models.CharField(max_length=128, unique=True)
    subjects_set = models.ManyToManyField("Subject")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name