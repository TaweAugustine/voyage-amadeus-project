
from django.shortcuts import render
from rest_framework import viewsets
from .models import Favorites

from .serialisers import FavoritesSerializer
from rest_framework import status

from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View, CreateView,FormView,DetailView,ListView #We can use FormModel instead of CreateView

from .models import *
from django.contrib.auth.models import User
from authentication.models import CustomUser


from django.db.models import Q 

from django.core.paginator import Paginator

from dotenv import load_dotenv
import os

# Charge les variables d'environnement depuis le fichier .env

load_dotenv()

from django.conf import settings 

# from amadeus import amadeus
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from amadeus import Client, ResponseError
# from ..voyage import  AMADEUS_API_KEY,AMADEUS_API_SECRET


from amadeus import Location


amadeus = Client(
    client_id = os.getenv('AMADEUS_API_KEY',"4n91NAQupMl1kJkA9c7Jm3yDauA3gdVS"),
    client_secret = os.getenv('AMADEUS_API_SECRET','wquLrYXvNp1ESTGL')
)


class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()

    #http_method_names = ['GET','PUT','PATCH','DELETE']

#http://127.0.0.1:8000/api/travel-inspiration/?originLocationCode=PAR&destinationLocationCode=FR

class TravelInspiration(APIView):

    def get(self, request, format=None):
        try:
            data = request.GET

            origin_code = str(data.get('originLocationCode'))
            dest_code = str(data.get('destinationLocationCode'))
            depart_date = str(data.get('departureDate'))

            all_travel_list = amadeus.reference_data.recommended_locations.get(
                cityCodes=origin_code,
                travelerCountryCode=dest_code
            )

            data_liste = all_travel_list.data

            for travel in all_travel_list.data:
                favorite = Favorites(
                type_travel=travel['type'],
                    subType=travel['subtype'],
                    name=travel['name'],
                    detailedName=travel['detailedName'],
                    id=travel['id'],
                    self=travel['self'],
                    timeZoneOffset=travel['timeZoneOffset'],
                    iataCode=travel['iataCode'],
                    geoCode=travel['geoCode'],
                    address=travel['address'],
                    analytics=travel['analytics'],
                )

                if request.user:
                    user = request.user
                    favorite.users.add(user)

                favorite.save()
                print("Favorite created : ",favorite)
                #return Response({"message": "Favorites created successfully."}, status=status.HTTP_201_CREATED)


        except Exception as e:
            print(e)
            all_travel_list = amadeus.reference_data.recommended_locations.get(
                cityCodes=origin_code,
                destinationCountryCodes=dest_code
            )

        return Response({"message": "Favorites created successfully."}, status=status.HTTP_201_CREATED)


class TravelInspirationDetail(APIView):
    def get(self, request,pk=None,format=None):
        try:
            travel = amadeus.reference_data.recommended_locations.get(
                cityCodes=str(pk)
                )
            print("Les travels ===========#####>", travel.data,"Code : ",pk)
        except Exception as e:
            print(e)
            print("Code : ",pk)

            return Response(data={"message":"Something was wrong"},status=status.HTTP_400_BAD_REQUEST)

        
        return  Response(data=travel.data,status=status.HTTP_200_OK)


class TravelInspirationSearch(APIView):
    def get(self, request,keyword=None,format=None):
        try:
            search_travel =   amadeus.reference_data.locations.get(
                keyword=str(keyword),
                subType=Location.ANY
            )
            print("Les travels ===========#####>", search_travel.data,"keyword : ",keyword)
        except Exception as e:
            print(e)
            print("keyword : ",keyword)

            return Response(data={"message":"Something was wrong for keyword"},status=status.HTTP_400_BAD_REQUEST)
        
        return  Response(data=search_travel.data,status=status.HTTP_200_OK)

