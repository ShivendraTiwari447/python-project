from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # We'll hash the password

    def __str__(self):
        return self.username
    


#     # from django.db import models

# # class Event(models.Model):
# #     title = models.CharField(max_length=100)
# #     description = models.TextField()
# #     date = models.DateField()

# #     def __str__(self):
# #         return self.title
    







