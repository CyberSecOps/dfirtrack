from dfirtrack_main import models as dfirtrack_main_models
from dfirtrack_api.serializers import dfirtrack_main_fk
from dfirtrack_api.serializers.dfirtrack_artifacts_fk import ArtifactFkSerializer
from rest_framework import serializers


class AnalysisstatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Analysisstatus
        # attributes made available for api
        fields = (
            'analysisstatus_id',
            'analysisstatus_name',
        )

class CaseSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # redefine representation
    def to_representation(self, instance):

        # get serializers of foreignkey relationsships
        self.fields['tag'] =  dfirtrack_main_fk.TagFkSerializer(many=True, read_only=True)

        # get existing to_representation
        representation = super(CaseSerializer, self).to_representation(instance)

        # change mandatory time strings
        representation['case_create_time'] = instance.case_create_time.strftime('%Y-%m-%dT%H:%M')

        return representation

    class Meta:
        model = dfirtrack_main_models.Case
        # attributes made available for api
        fields = (
            'case_id',
            'case_name',
            'tag',
            'case_is_incident',
            'case_created_by_user_id',
            'case_create_time',
        )

class CaseprioritySerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Casepriority
        # attributes made available for api
        fields = (
            'casepriority_id',
            'casepriority_name',
        )

class CasestatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Casestatus
        # attributes made available for api
        fields = (
            'casestatus_id',
            'casestatus_name',
        )

class CasetypeSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Casetype
        # attributes made available for api
        fields = (
            'casetype_id',
            'casetype_name',
        )

class CompanySerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['division'] =  dfirtrack_main_fk.DivisionFkSerializer(read_only=True)
        return super(CompanySerializer, self).to_representation(instance)

    class Meta:
        model = dfirtrack_main_models.Company
        # attributes made available for api
        fields = (
            'company_id',
            'company_name',
            'division',
        )

class ContactSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Contact
        # attributes made available for api
        fields = (
            'contact_id',
            'contact_name',
            'contact_email',
            'contact_phone',
        )

class DivisionSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Division
        # attributes made available for api
        fields = (
            'division_id',
            'division_name',
        )

class DnsnameSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['domain'] =  dfirtrack_main_fk.DomainFkSerializer(read_only=True)
        return super(DnsnameSerializer, self).to_representation(instance)

    class Meta:
        model = dfirtrack_main_models.Dnsname
        # attributes made available for api
        fields = (
            'dnsname_id',
            'dnsname_name',
            'domain',
        )

class DomainSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Domain
        # attributes made available for api
        fields = (
            'domain_id',
            'domain_name',
        )

class DomainuserSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['domain'] =  dfirtrack_main_fk.DomainFkSerializer(read_only=True)
        return super(DomainuserSerializer, self).to_representation(instance)

    class Meta:
        model = dfirtrack_main_models.Domainuser
        # attributes made available for api
        fields = (
            'domainuser_id',
            'domainuser_name',
            'domain',
            'domainuser_is_domainadmin',
        )

class IpSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Ip
        # attributes made available for api
        fields = (
            'ip_id',
            'ip_ip',
        )

class LocationSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Location
        # attributes made available for api
        fields = (
            'location_id',
            'location_name',
        )

class OsSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Os
        # attributes made available for api
        fields = (
            'os_id',
            'os_name',
        )

class OsarchSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Osarch
        # attributes made available for api
        fields = (
            'osarch_id',
            'osarch_name',
        )

class ReasonSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Reason
        # attributes made available for api
        fields = (
            'reason_id',
            'reason_name',
        )

class RecommendationSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Recommendation
        # attributes made available for api
        fields = (
            'recommendation_id',
            'recommendation_name',
        )

class ServiceproviderSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Serviceprovider
        # attributes made available for api
        fields = (
            'serviceprovider_id',
            'serviceprovider_name',
        )

class SystemSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # redefine representation
    def to_representation(self, instance):

        # get serializers of foreignkey relationsships
        self.fields['analysisstatus'] =  dfirtrack_main_fk.AnalysisstatusFkSerializer(many=False, read_only=True)
        self.fields['case'] =  dfirtrack_main_fk.CaseFkSerializer(many=True, read_only=True)
        self.fields['company'] =  dfirtrack_main_fk.CompanyFkSerializer(many=True, read_only=True)
        self.fields['contact'] =  dfirtrack_main_fk.ContactFkSerializer(many=False, read_only=True)
        self.fields['dnsname'] =  dfirtrack_main_fk.DnsnameFkSerializer(many=False, read_only=True)
        self.fields['domain'] =  dfirtrack_main_fk.DomainFkSerializer(many=False, read_only=True)
        self.fields['host_system'] =  dfirtrack_main_fk.HostSystemFkSerializer(many=False, read_only=True)
        self.fields['ip'] =  dfirtrack_main_fk.IpFkSerializer(many=True, read_only=True)
        self.fields['location'] =  dfirtrack_main_fk.LocationFkSerializer(many=False, read_only=True)
        self.fields['os'] =  dfirtrack_main_fk.OsFkSerializer(many=False, read_only=True)
        self.fields['osarch'] =  dfirtrack_main_fk.OsarchFkSerializer(many=False, read_only=True)
        self.fields['reason'] =  dfirtrack_main_fk.ReasonFkSerializer(many=False, read_only=True)
        self.fields['recommendation'] =  dfirtrack_main_fk.RecommendationFkSerializer(many=False, read_only=True)
        self.fields['serviceprovider'] =  dfirtrack_main_fk.ServiceproviderFkSerializer(many=False, read_only=True)
        self.fields['systemstatus'] =  dfirtrack_main_fk.SystemstatusFkSerializer(many=False, read_only=True)
        self.fields['systemtype'] =  dfirtrack_main_fk.SystemtypeFkSerializer(many=False, read_only=True)
        self.fields['tag'] =  dfirtrack_main_fk.TagFkSerializer(many=True, read_only=True)

        # get existing to_representation
        representation = super(SystemSerializer, self).to_representation(instance)

        # change mandatory time strings
        representation['system_create_time'] = instance.system_create_time.strftime('%Y-%m-%dT%H:%M')
        representation['system_modify_time'] = instance.system_modify_time.strftime('%Y-%m-%dT%H:%M')

        # change optional time strings
        # TODO: change after model rebuild
        #if instance.system_install_time:
        #    representation['system_install_time'] = instance.system_install_time.strftime('%Y-%m-%dT%H:%M')
        if instance.system_lastbooted_time:
            representation['system_lastbooted_time'] = instance.system_lastbooted_time.strftime('%Y-%m-%dT%H:%M')
        if instance.system_deprecated_time:
            representation['system_deprecated_time'] = instance.system_deprecated_time.strftime('%Y-%m-%dT%H:%M')

        return representation

    class Meta:
        model = dfirtrack_main_models.System
        # attributes made available for api in a sorted fashion
        fields = (
            'system_id',
            'system_uuid',
            'system_name',
            'domain',
            'dnsname',
            'systemstatus',
            'analysisstatus',
            'reason',
            'recommendation',
            'systemtype',
            'ip',
            'os',
            'osarch',
            # TODO: change after model rebuild
            #'system_install_time',
            'system_lastbooted_time',
            'system_deprecated_time',
            'system_is_vm',
            'host_system',
            'company',
            'location',
            'serviceprovider',
            'contact',
            'tag',
            'case',
            'system_create_time',
            'system_created_by_user_id',
            'system_modify_time',
            'system_modified_by_user_id',
            'system_export_markdown',
            'system_export_spreadsheet',
        )

class SystemstatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Systemstatus
        # attributes made available for api
        fields = (
            'systemstatus_id',
            'systemstatus_name',
        )

class SystemtypeSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Systemtype
        # attributes made available for api
        fields = (
            'systemtype_id',
            'systemtype_name',
        )

class SystemuserSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # redefine representation
    def to_representation(self, instance):

        # get serializers of foreignkey relationsships
        self.fields['system'] =  dfirtrack_main_fk.SystemFkSerializer(read_only=True)

        # get existing to_representation
        representation = super(SystemuserSerializer, self).to_representation(instance)

        # change optional time strings
        if instance.systemuser_lastlogon_time:
            representation['systemuser_lastlogon_time'] = instance.systemuser_lastlogon_time.strftime('%Y-%m-%dT%H:%M')

        return representation

    class Meta:
        model = dfirtrack_main_models.Systemuser
        # attributes made available for api
        fields = (
            'systemuser_id',
            'systemuser_name',
            'system',
            'systemuser_lastlogon_time',
            'systemuser_is_systemadmin',
        )

class TagSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # get serializers of foreignkey relationsships
    def to_representation(self, instance):
        self.fields['tagcolor'] =  dfirtrack_main_fk.TagcolorFkSerializer(read_only=True)
        return super(TagSerializer, self).to_representation(instance)

    class Meta:
        model = dfirtrack_main_models.Tag
        # attributes made available for api
        fields = (
            'tag_id',
            'tag_name',
            'tagcolor',
        )

class TagcolorSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Tagcolor
        # attributes made available for api
        fields = (
            'tagcolor_id',
            'tagcolor_name',
        )

class TaskSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    # redefine representation
    def to_representation(self, instance):

        # get serializers of foreignkey relationsships
        self.fields['artifact'] =  ArtifactFkSerializer(many=False, read_only=True)
        self.fields['case'] =  dfirtrack_main_fk.CaseFkSerializer(many=False, read_only=True)
        self.fields['parent_task'] =  dfirtrack_main_fk.ParentTaskFkSerializer(many=False, read_only=True)
        self.fields['system'] =  dfirtrack_main_fk.SystemFkSerializer(many=False, read_only=True)
        self.fields['tag'] =  dfirtrack_main_fk.TagFkSerializer(many=True, read_only=True)
        self.fields['taskname'] =  dfirtrack_main_fk.TasknameFkSerializer(many=False, read_only=True)
        self.fields['taskpriority'] =  dfirtrack_main_fk.TaskpriorityFkSerializer(many=False, read_only=True)
        self.fields['taskstatus'] =  dfirtrack_main_fk.TaskstatusFkSerializer(many=False, read_only=True)

        # get existing to_representation
        representation = super(TaskSerializer, self).to_representation(instance)

        # change mandatory time strings
        representation['task_create_time'] = instance.task_create_time.strftime('%Y-%m-%dT%H:%M')
        representation['task_modify_time'] = instance.task_modify_time.strftime('%Y-%m-%dT%H:%M')

        # change optional time strings
        if instance.task_scheduled_time:
            representation['task_scheduled_time'] = instance.task_scheduled_time.strftime('%Y-%m-%dT%H:%M')
        if instance.task_started_time:
            representation['task_started_time'] = instance.task_started_time.strftime('%Y-%m-%dT%H:%M')
        if instance.task_finished_time:
            representation['task_finished_time'] = instance.task_finished_time.strftime('%Y-%m-%dT%H:%M')
        if instance.task_due_time:
            representation['task_due_time'] = instance.task_due_time.strftime('%Y-%m-%dT%H:%M')

        return representation

    class Meta:
        model = dfirtrack_main_models.Task
        # attributes made available for api
        fields = (
            'task_id',
            'parent_task',
            'taskname',
            'taskpriority',
            'taskstatus',
            'artifact',
            'case',
            'system',
            'task_assigned_to_user_id',
            'tag',
            'task_scheduled_time',
            'task_started_time',
            'task_finished_time',
            'task_due_time',
            'task_create_time',
            'task_modify_time',
            'task_created_by_user_id',
            'task_modified_by_user_id',
        )

class TasknameSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Taskname
        # attributes made available for api
        fields = (
            'taskname_id',
            'taskname_name',
        )

class TaskprioritySerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Taskpriority
        # attributes made available for api
        fields = (
            'taskpriority_id',
            'taskpriority_name',
        )

class TaskstatusSerializer(serializers.ModelSerializer):
    """ create serializer for model instance """

    class Meta:
        model = dfirtrack_main_models.Taskstatus
        # attributes made available for api
        fields = (
            'taskstatus_id',
            'taskstatus_name',
        )
