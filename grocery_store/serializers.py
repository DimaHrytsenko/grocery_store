from rest_framework import serializers

from grocery_store.models import Employee, Game, Feedback


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Feedback
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['computer']


class TimeFromOpenweather:
    def __init__(self, api_time):
        self.api_time = api_time


class TimeFromOpenweatherSerializer(serializers.Serializer):
    api_time = serializers.CharField(max_length=255)
