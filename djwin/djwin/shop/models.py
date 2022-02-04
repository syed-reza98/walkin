from django.db import models

# Create your models here.


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_description = models.TextField()
    hotel_image = models.ImageField(upload_to = "hotel/")
    hotel_address = models.TextField(default="N/A")
    hotel_star = models.PositiveIntegerField()
    roomQuantity = models.PositiveIntegerField()

    def __str__(self):
        return self.hotel_name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_title = models.CharField(max_length=100)
    room_image = models.ImageField(upload_to = "rooms/")
    room_capacity = models.PositiveIntegerField()
    room_avaibility = models.BooleanField(default=True)
    room_description = models.TextField()
    room_price = models.PositiveIntegerField()
    room_discount_price = models.PositiveIntegerField()
    available_date = models.CharField(max_length=150)

    def __str__(self):
        return self.room_title
