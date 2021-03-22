from core.models import Car
from api.serializers import CarSerializer, RatingSerializer,PopularSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from django.http import Http404


@api_view(['GET', 'POST'])
def car_list(request):
    """
     Lists all cars in databse, or creates a new one.
    """

    if request.method == 'GET':
        try:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        except:
            return Response( status=status.HTTP_204_NO_CONTENT)



    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            #check if fits
            model = request.data['make']
            url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{model}?format=json'
            try:
                response = requests.get(url)
                data = json.loads(response.text)
                data = data["Results"]
                on_list = False
                for element in data:
                    if element['Model_Name'] == request.data['model']:
                        on_list = True
                        break
                if not on_list:
                    raise Http404
            except Http404 as err:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def rate(request):
    if request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            id = request.data['car_id']
            car = Car.objects.get(pk=id)
            if not car.avg_rating:
                car.avg_rating = 0
            if not car.rates_number:
                car.rates_number = 0
            rating = float(car.avg_rating)
            added_rating = float(request.data['rating'])
            car.avg_rating = (rating * car.rates_number + added_rating) / (car.rates_number + 1)
            car.rates_number = car.rates_number + 1
            car.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def popular(request):
    """
    Retrive desceding list of cars by popularity.
    """
    if request.method == 'GET':
        try:
            car = Car.objects.all().order_by('-rates_number')
        except Car.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PopularSerializer(car,many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)
