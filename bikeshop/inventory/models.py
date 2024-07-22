from django.db import models

class Bike(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Sale(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    date_of_sale = models.DateField()

    def __str__(self):
        return f"{self.quantity_sold} x {self.bike.name} sold to {self.customer.name}"

