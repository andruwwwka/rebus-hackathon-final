from rest_framework import serializers


class DeploymentListResponseSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    source = serializers.CharField()
    tenantId = serializers.CharField()
    deploymentTime = serializers.DateField()


class DeploymentCreateResponseSerializer(serializers.Serializer):
    id = serializers.CharField()
    links = serializers.ListField(child=serializers.DictField())
    name = serializers.CharField()
    source = serializers.CharField()
    tenantId = serializers.CharField()
    deploymentTime = serializers.CharField()
