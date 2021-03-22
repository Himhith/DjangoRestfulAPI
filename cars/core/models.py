from django.db import models


# validators
def validate_range_one_to_five(rating):
    if rating < 1 or rating > 5:
        raise ValueError(
            ('Rating can be between 1 and 5 only!')
        )


def validate_popularity_not_negative(popularity):
    if popularity < 0:
        raise ValueError(
            ('Cannot set negative popularity!')
        )


# implementation of car model
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    rates_number = models.IntegerField(blank=True, null=True, validators=[validate_popularity_not_negative], default=0)
    avg_rating = models.DecimalField(decimal_places=1,max_digits=2,blank=True,null=True, validators=[validate_range_one_to_five],default=None)
    def __str__(self):
        return f'{self.make} {self.model}'


class Ratings(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    car_id = car.primary_key
    rating = models.DecimalField(decimal_places=1, max_digits=2, blank=True, null=True,
                                 validators=[validate_range_one_to_five], default=None)
