from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservation,post
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import GuestSerializers, MovieSerializers, ReservationsSerializers, postSerializers
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics, mixins, viewsets

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly


#1 without REST and no model query FBV
def noRestNoModel(request):
    Guests =[
        {"id":1,
         "name":"NoName",
         "mobile":122334321},
         { "id":2,
         "name":"NoName",
         "mobile":122334321}]
    return JsonResponse ({"Guests":Guests})

#2 model data default djanog without rest
def noRestFromModel(request):
    data = Guest.objects.all()
    response =  {"Guests":list(data.values("name", "mobile"))}
    return JsonResponse(response)

# List == GET
# Create == POST
# pk query == GET 
# Update == PUT
# Delete destroy == DELETE

#3 Function based views 
#3.1 GET POST
@api_view(["GET","POST"])
def FBV_list(request):
    if request.method =="GET":
        guest = Guest.objects.all()
        serializer = GuestSerializers(guest, many=True)
        return Response(serializer.data)
    
    #POST
    elif request.method =="POST":
        serializer = GuestSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

#3.Delete GET POST
@api_view(["GET","PUT","DELETE"])
def FBV_pk(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = GuestSerializers(guest)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = GuestSerializers(guest, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        guest.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
       

#4 Class based views
#4.1
class CBV_List(APIView):
    #GET
    def get(self, request):
        guest = Guest.objects.all()
        serializer = GuestSerializers(guest, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GuestSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

#4.1
class CBV_pk(APIView):
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializers(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializers(guest, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     

#5 Mixins 
#5.1 mixins list

class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    

#5.2 

class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    
    def get(self, request,pk):
        return self.retrieve(request)
    
    def put(self, request,pk):
        return self.update(request)
    
    def delete(self, request,pk):
        return self.destroy(request)

    
#6.1
class generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    authentication_classes  = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

#6.2

class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    authentication_classes = [TokenAuthentication]
   # permission_classes = [IsAuthenticated]

#7 viewsets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializers
    

    
class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ["movie"]

class viewsets_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializers

#8 
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(
        hall = request.data['hall'],
        Movie = request.data['movie']

    )
    serializer = MovieSerializers(movies, many= True)
    return Response(serializer.data)

#9
@api_view(['POST'])
def new_reservations(request):
       
    movie = Movie.objects.get(
    hall = request.data['hall'],
    movie = request.data['movie'],
    )
   
    guest = Guest()
    guest.name = request.data["name"]
    guest.mobile = request.data["mobile"]
    guest.save()

    reservation = Reservation()
    reservation.guest = guest
    reservation.movie = movie
    reservation.save()
    
    return Response(status = status.HTTP_201_CREATED)

#10
class Post_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = post.objects.all()
    serializer_class = postSerializers














