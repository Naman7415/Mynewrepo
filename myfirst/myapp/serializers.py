from rest_framework import serializers
from .models import *

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tenant1Model
        fields=['id', 'name', 'email', 'rollnumber']
        
        
class TenantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tenant2Model
        fields = ['id', 'tenant', 'data_field1', 'data_field2']  # Add fields as needed

        
        

#     def create(self, validated_data):
#         # Ensure that the newly created TenantData instance is associated with the current tenant
#         validated_data['tenant'] = self.context['request'].user.tenant
#         return super().create(validated_data)


# from rest_framework import serializers
# from .models import MyUser

# class TenantModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TenantModel
#         fields = ['id', 'name', 'password', 'username']



# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ['id', 'name', 'password', 'username']