from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    draft = models.BooleanField()
    published_date = models.DateField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def sort_comment_set(self):
        return self.comments.order_by('created_at')

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.message
