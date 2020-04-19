from django.db import models
from django.urls import reverse


class Catagories (models.Model):
    catagories_name = models.CharField(max_length=20,primary_key=True)


    def __str__(self):
        return self.catagories_name

    def get_absolute_url(self):
        return reverse("task_group:cdetail",kwargs={'pk':self.pk})



class Task(models.Model):
    Catagories = models.ForeignKey(Catagories,related_name='Task',on_delete=models.CASCADE )
    title = models.CharField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
   # dead_line = models.DateTimeField()
    done = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_date"]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("task_group:tdetail",kwargs={'pk':self.pk})


