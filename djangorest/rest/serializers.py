from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # or fields = '__all__'
        fields = ('name', 'age', 'created_at', 'updated_at')
