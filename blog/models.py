from django.db import models

# Create a blog model


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_format_simple(self):
        return self.pub_date.strftime("%b %e %Y")
