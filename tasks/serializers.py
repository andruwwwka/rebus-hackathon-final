from rest_framework import serializers


class TaskListGetParametersSerializer(serializers.Serializer):
    assignee = serializers.CharField(required=True)


class TaskResponseSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    assignee = serializers.CharField()
    owner = serializers.CharField()
    created = serializers.CharField()
    due = serializers.CharField()
    followUp = serializers.CharField()
    delegationState = serializers.CharField()
    description = serializers.CharField()
    executionId = serializers.CharField()
    parentTaskId = serializers.CharField()
    priority = serializers.IntegerField()
    processDefinitionId = serializers.CharField()
    processInstanceId = serializers.CharField()
    caseExecutionId = serializers.CharField()
    caseDefinitionId = serializers.CharField()
    caseInstanceId = serializers.CharField()
    taskDefinitionKey = serializers.CharField()
    formKey = serializers.CharField()
