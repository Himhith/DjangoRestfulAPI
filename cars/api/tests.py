
from rest_framework.test import APITestCase
from core.models import Car, Ratings
from api.serializers import CarSerializer, RatingSerializer,PopularSerializer
from rest_framework import status


class CarTestCase(APITestCase):
    def SetUp(self):

        Car.objects.create(
                    make="Volkswagen", model="Golf", rates_number = 0, avg_rating = 0
                )
        Car.objects.create(
                    make="Honda", model="Accord", rates_number = 0, avg_rating = 0
                )
    def test_car_create_get_delete(self):
        data = {'make': 'Honda','model': 'Accord' }
        response = self.client.post('/cars/',data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get('/cars/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete('/cars/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_car_creation_invalid_data(self):
        bad_data = {'wrong_field': 'Honda','model': 'Accord' }
        response = self.client.post('/cars/',bad_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_popular(self):
        response = self.client.get('/popular/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

