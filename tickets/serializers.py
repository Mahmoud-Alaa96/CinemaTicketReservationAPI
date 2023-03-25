from rest_framework import serializers
from .models import Guest, Movie, Reservation, post

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ReservationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"

class GuestSerializers(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ["pk","reservation","name","mobile"]


class postSerializers(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = "__all__"





