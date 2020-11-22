# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mptt.models import MPTTModel


class Cases(models.Model):
    id = models.IntegerField(primary_key=True)
    scene_id = models.IntegerField(blank=True, null=True)
    project_id = models.PositiveIntegerField()
    group_name = models.CharField(max_length=50)
    name = models.CharField(max_length=400)
    case_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_user = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    parent_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField(blank=True, null=True)
    tier = models.CharField(max_length=60, blank=True, null=True)
    run_state = models.IntegerField(blank=True, null=True)
    order_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases'
        unique_together = (('id', 'project_id'),)


class CasesComponents(models.Model):
    project_id = models.IntegerField(primary_key=True)
    component_name = models.CharField(max_length=50)
    component_clazz = models.CharField(max_length=50)
    component_type = models.IntegerField(blank=True, null=True)
    case_id = models.CharField(max_length=50)
    order_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases_components'
        unique_together = (('project_id', 'component_name', 'case_id'),)


class CasesInSet(models.Model):
    project_id = models.PositiveIntegerField()
    name = models.CharField(max_length=400)
    case_id = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    case_state = models.IntegerField(blank=True, null=True)
    set_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cases_in_set'


class Components(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    runner_id = models.IntegerField(blank=True, null=True)
    root_name = models.CharField(max_length=50, blank=True, null=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    module_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    script_name = models.CharField(max_length=200, blank=True, null=True)
    data_name = models.CharField(max_length=50, blank=True, null=True)
    created_user = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.IntegerField()
    level = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    tier = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'components'
        unique_together = (('id', 'project_id'),)


class ParameterRules(models.Model):
    id = models.AutoField(primary_key=True)
    project_id = models.IntegerField()
    fk_com_id = models.IntegerField(blank=True, null=True)
    target_field = models.CharField(max_length=50, blank=True, null=True)
    condition_field = models.CharField(max_length=50, blank=True, null=True)
    con_value = models.CharField(max_length=50, blank=True, null=True)
    con_value_index = models.IntegerField(blank=True, null=True)
    check_field = models.CharField(max_length=50, blank=True, null=True)
    res_value = models.CharField(max_length=50, blank=True, null=True)
    res_value_index = models.IntegerField(blank=True, null=True)
    read_only_marking = models.CharField(max_length=20, blank=True, null=True)
    check_name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    parameter_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parameter_rules'


class ReqScene(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    req_id = models.IntegerField(blank=True, null=True)
    scene_name = models.CharField(max_length=100, blank=True, null=True)
    scene_description = models.CharField(max_length=400, blank=True, null=True)
    created_user = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'req_scene'
        unique_together = (('id', 'project_id'),)


class Requirement(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.IntegerField()
    name = models.CharField(max_length=400, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_user = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    rq_order_id = models.IntegerField(blank=True, null=True)
    tier = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requirement'
        unique_together = (('id', 'project_id'),)


class SceneSet(models.Model):
    project_id = models.IntegerField(blank=True, null=True)
    scene_id = models.IntegerField(blank=True, null=True)
    component_name = models.CharField(max_length=50, blank=True, null=True)
    com_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_user = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scene_set'


class SceneSetIo(models.Model):
    project_id = models.IntegerField()
    scene_id = models.IntegerField()
    type = models.IntegerField()
    name = models.CharField(max_length=150)
    assign = models.CharField(max_length=150, blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    sequence = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scene_set_io'


class Sets(models.Model):
    id = models.IntegerField(primary_key=True)
    project_id = models.PositiveIntegerField()
    group_name = models.CharField(max_length=50)
    set_name = models.CharField(max_length=50)
    set_id = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_user = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sets'


class CaseSetIo(models.Model):
    project_id = models.PositiveIntegerField(primary_key=True)
    type = models.IntegerField()
    name = models.CharField(max_length=150)
    assign = models.CharField(max_length=150)
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    case_id = models.CharField(max_length=50)
    sequence = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_set_io'
        unique_together = (('project_id', 'case_id', 'name', 'assign'),)


class SetReq(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    name = models.CharField(max_length=400)
    set_id = models.CharField(max_length=50)
    tier = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'set_req'
        unique_together = (('id', 'set_id'),)


class CaseSetIoOutparam(models.Model):
    project_id = models.PositiveIntegerField(primary_key=True)
    type = models.IntegerField()
    name = models.CharField(max_length=150)
    assign = models.CharField(max_length=150)
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    case_id = models.CharField(max_length=50)
    sequence = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_set_io_outparam'
        unique_together = (('project_id', 'case_id', 'type', 'name', 'assign'),)


class Run(models.Model):
    project_id = models.IntegerField()
    run_id = models.CharField(max_length=50)
    run_name = models.CharField(max_length=50)
    runner = models.CharField(max_length=50, blank=True, null=True)
    set_id = models.CharField(max_length=50, blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    finish = models.DateTimeField(blank=True, null=True)
    finish_nums = models.IntegerField()
    nums = models.IntegerField()
    runner_result = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'run'
        unique_together = (('project_id', 'run_id'),)


class RunSet(models.Model):
    project_id = models.IntegerField()
    case_name = models.CharField(max_length=200)
    case_clazz = models.CharField(max_length=200)
    case_type = models.IntegerField(blank=True, null=True)
    case_id = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    case_state = models.IntegerField(blank=True, null=True)
    set_id = models.CharField(max_length=50, blank=True, null=True)
    run_id = models.CharField(max_length=50, blank=True, null=True)
    runner_result = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'run_set'


class RunSetIo(models.Model):
    project_id = models.IntegerField()
    component_name = models.CharField(max_length=200)
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    runner_result = models.IntegerField(blank=True, null=True)
    case_id = models.CharField(max_length=50, blank=True, null=True)
    run_id = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'run_set_io'
