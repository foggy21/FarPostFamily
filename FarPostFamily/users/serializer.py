# Импортируем необходимые библиотеки
from rest_framework import serializers
from .models import User, Interest, Specialization

# Создаем сериализатор для модели Interest
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['name']

# Создаем сериализатор для модели Specialization
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['name']

# Создаем сериализатор для модели User
class UserSerializer(serializers.ModelSerializer):
    # Добавляем вложенные сериализаторы для связанных моделей
    interest = InterestSerializer(many=True)
    specialization = SpecializationSerializer()
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'password', 'image_url', 'name', 'age', 'gender', 'interest', 'specialization']
    
    def get_image_url(self, obj):
        # Получаем текущий запрос
        request = self.context.get('request')
        # Строим абсолютный URL из относительного пути
        image = request.build_absolute_uri(obj.image.url)
        # Возвращаем URL изображения
        return image
