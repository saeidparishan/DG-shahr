from django.db import models


class Todoitem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_time = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}-{}'.format(self.pk, self.title)
