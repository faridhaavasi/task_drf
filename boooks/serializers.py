from rest_framework import serializers
from .models import books
'''
class bookserializer(serializers.Serializer):
    name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    auther = serializers.CharField()
    serial_number = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return books.objects.create(
            name=validated_data['name'],
            title=validated_data['title'],
            description=validated_data['description'],
            auther=validated_data['auther'],
            serial_number=validated_data['serial_number'],
            price=validated_data['price']
            )

'''
class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = '__all__'

