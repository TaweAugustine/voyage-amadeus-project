
from django.shortcuts import render
from rest_framework import viewsets
from .models import Favorites
from .serializers import FavoritesSerializer

from rest_framework import status

from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View, CreateView,FormView,DetailView,ListView #We can use FormModel instead of CreateView

from .models import *
from django.contrib.auth.models import User
from authentication.models import CustomUser


from django.db.models import Q 

from django.core.paginator import Paginator


from django.conf import settings 

# from amadeus import amadeus
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from amadeus import Client, ResponseError
# from ..voyage import  AMADEUS_API_KEY,AMADEUS_API_SECRET


from amadeus import Location


AMADEUS_API_KEY = '4n91NAQupMl1kJkA9c7Jm3yDauA3gdVS'
AMADEUS_API_SECRET = 'wquLrYXvNp1ESTGL'

amadeus = Client(
    client_id = AMADEUS_API_KEY,
    client_secret = AMADEUS_API_SECRET
)

class FavoritesViewSet(viewsets.ModelViewSet):
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()

    http_method_names = ['GET','PUT','PATCH','DELETE']



class TravelInspiration(APIView):

    def get(self, request, format=None):
        try:
            data = request.GET

            origin_code = str(data.get('originLocationCode'))
            dest_code = str(data.get('destinationLocationCode'))
            depart_date = str(data.get('departureDate'))

            print("Data origin====>>#####",str(origin_code))
            #     all_travel_list = amadeus.reference_data.recommended_locations.get(
            #         cityCodes=dest_code,
            #         destinationCountryCodes=origin_code
            #    )
            all_travel_list = amadeus.reference_data.recommended_locations.get(
                cityCodes=origin_code,
                travelerCountryCode=dest_code
           )
            print("Les travels ===========#####>", all_travel_list.data ,"LEN ==>",len(all_travel_list.data))
            data_liste:dict = dict()
            # # data_liste.update(all_travel_list.data)
            # for travel in all_travel_list:
            #     data_liste.update({
            #      'a' : travel
            #     }
            #     )
            data_liste = all_travel_list.data

            for tr in data_liste:

                print("Object format =======+++>",tr)
                # travel = tr
                # favorite = Favorites(
                #     type_travel = data_liste, 
                #     subType = data_liste.subType,
                #     name = data_liste.name,
                #     detailedName = data_liste.detailedName, 
                #     id = data_liste.id, self = data_liste.self, 
                #     timeZoneOffset =data_liste.timeZoneOffset, 
                #     iataCode = data_liste.iataCode
                # )
                # favorite.geoCode = data_liste.geoCode, 
                # favorite.address = data_liste.address, 
                # favorite.analytics = data_liste.analytics

                # if request.user :
                #     user = request.user
                #     favorite.users.add(user)

                # favorite.save()
                

                # Favorites.objects.create(
                #     type_travel =data_liste.type, 
                #     subType = data_liste.subType,
                #     name = data_liste.name,
                #     detailedName = data_liste.detailedName, 
                #     id = data_liste.id, self = data_liste.self, 
                #     timeZoneOffset =data_liste.timeZoneOffset, 
                #     iataCode = data_liste.iataCode,
                #     geoCode = data_liste.geoCode, 
                # address = data_liste.address, 
                # analytics = data_liste.analytics
                # )
             
            # print("Favorite Created===============>",favorite)

        except Exception as e:
            print(e)
            all_travel_list = amadeus.reference_data.recommended_locations.get(
                cityCodes="PAR",
                travelerCountryCode="FR"
           )
            print("Les travels ex===========#####>", all_travel_list.data)
            return Response(data={"message":"Something was wrong"},status=status.HTTP_400_BAD_REQUEST)
        
        return  Response(data=all_travel_list.data,status=status.HTTP_200_OK)



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

