from django.db import models

class SafariPackage(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    days = models.PositiveIntegerField()
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to="safaris/", blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    safari = models.ForeignKey(SafariPackage, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.safari.name}"
