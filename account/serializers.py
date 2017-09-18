from rest_framework import serializers
from account.models import User, Skill, Team, Project, Task


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('title','content','assigner','assignee','project')
        read_only_fields = ('assigner',)


class SkillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skill
        fields = ('name','user')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name','team','members')


class TeamSerializer(serializers.ModelSerializer):
    project_set = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = Team
        fields = ('name','lead','members','project_set')


class UserSerializer(serializers.ModelSerializer):
    skill_set = SkillSerializer(many=True)
    team_set = TeamSerializer(many=True ,read_only=True)
    project_set = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = User
        fields = ('username','password','first_name','empid','age','teamlead','skill_set','team_set','project_set')

    def create(self, validated_data):
        skills_data = validated_data.pop('skill_set')
        user = User.objects.create_user(**validated_data)
        for skill_data in skills_data:
            Skill.objects.create(user=user,**skill_data)
        return user


