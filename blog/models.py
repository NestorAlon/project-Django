from django.db import models  # --- 1

class Article(models.Model):  # Definición del modelo Article
    title = models.CharField(max_length=255)
    content = models.TextField()
    check_box = models.BooleanField(null=True)
    multiple_check_box = models.CharField(max_length=255, null=True)
    pulldown = models.CharField(max_length=255, null=True)
    radio = models.CharField(max_length=255, null=True)