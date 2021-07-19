from rest_framework import serializers

from challenge.models import Address, Company


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'street_addr',
        )


class CompanySerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'addresses',
        )
