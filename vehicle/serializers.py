from rest_framework import serializers

from vehicle.models import Car, Moto, Milage


class MilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = '__all__'


class CarMilageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = ('year', 'milage', 'id')

class CarSerializer(serializers.ModelSerializer):
    last_milage = serializers.IntegerField(source='milage_set.last.milage', default=0, read_only=True)
    milage = CarMilageSerializer(many=True, read_only=True, source='milage_set')

    class Meta:
        model = Car
        fields = '__all__'
        # fields = ('title', 'description',)


class MotoSerializer(serializers.ModelSerializer):
    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        milage = instance.milage.all().last()
        if milage:
            return milage.milage
        return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer(many=False)

    class Meta:
        model = Milage
        fields = ('year', 'milage', 'id', 'moto')


class MotoCreateSerializer(serializers.ModelSerializer):
    milage = MotoMilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def create(self, validated_data):
        milage = validated_data.pop('milage')
        moto_instance = Moto.objects.create(**validated_data)
        for m in milage:
            Milage.objects.create(moto=moto_instance, **m)
        return moto_instance