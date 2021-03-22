# DjangoRestfulAPI
Example of Restful Api in Django


#### about
simple api in Django-rest-framework 
implemented docker container on heroku 
For db used native for heroku posgresql setup. 

#### LINKS TO WORKING IMPLEMNTATION:

endpoints: 

* POST, GET cars:https://fathomless-wildwood-73927.herokuapp.com/cars/
* GET,DELTE car:  https://fathomless-wildwood-73927.herokuapp.com/cars/{ID}
* POST rating: https://fathomless-wildwood-73927.herokuapp.com/rate
* GET popular: https://fathomless-wildwood-73927.herokuapp.com/popular

json query examples: 

Post/cars
```
{
  "make": "Honda",
  "model":"Accord"
}
```
WRONG Post/cars 
```
{
  "make": "Honda",
  "model":"WrongModel" #cars that are not on  https://vpic.nhtsa.dot.gov/api/ will not be accepted
}
```
Post/rating
```
{
  "car_id": 1,
  "rating":"4"
}
```
#### BUILD 

1. Clone repository
2. Build image on your local machine 
3. Run image  on your local macchine 
