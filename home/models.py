from django.db import models

# Create your models here.
class contact(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class quiz_question(models.Model):
    question_id = models.IntegerField()
    question = models.TextField()
    question_image = models.ImageField(upload_to="",default="")

    option_1 = models.TextField()
    option_1_image = models.ImageField(upload_to="",default="")

    option_2 = models.TextField()
    option_2_image = models.ImageField(upload_to="",default="")

    option_3 = models.TextField()
    option_3_image = models.ImageField(upload_to="",default="")

    option_4 = models.TextField()
    option_4_image = models.ImageField(upload_to="",default="")
    
    answer = models.TextField()

    def __str__(self):
        return str(self.question_id)
    
class quiz_submissions(models.Model):
    username = models.CharField(max_length=255)
    remain = models.TextField()
    my_ans = models.TextField()
    score = models.IntegerField()

    def __str__(self):
        return self.username

class admin_access(models.Model):
    control = models.CharField(max_length=255)
    value = models.BooleanField()

    def __str__(self):
        return self.control