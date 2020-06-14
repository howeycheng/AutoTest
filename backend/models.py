# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mptt.models import MPTTModel


# class Requirement(models.Model):
#     rqid = models.IntegerField(db_column='RQID', blank=True, null=True)  # Field name made lowercase.
#     project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
#     covered = models.IntegerField(db_column='COVERED', blank=True, null=True)  # Field name made lowercase.
#     author = models.TextField(db_column='AUTHOR', blank=True, null=True)  # Field name made lowercase.
#     priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
#     type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
#     review = models.IntegerField(db_column='REVIEW', blank=True, null=True)  # Field name made lowercase.
#     parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
#     level = models.IntegerField(db_column='LEVEL', blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
#     theme = models.TextField(db_column='THEME', blank=True, null=True)  # Field name made lowercase.
#     accessory = models.TextField(db_column='ACCESSORY', blank=True, null=True)  # Field name made lowercase.
#     rq_remark = models.CharField(db_column='RQ_Remark', max_length=300, blank=True,
#                                  null=True)  # Field name made lowercase.
#     req_rbt = models.TextField(db_column='req_RBT', blank=True, null=True)  # Field name made lowercase.
#     test_item = models.TextField(db_column='test_Item', blank=True, null=True)  # Field name made lowercase.
#     created_user = models.TextField(blank=True, null=True)
#     created_date = models.DateTimeField(blank=True, null=True)
#     rq_last_mender = models.TextField(db_column='RQ_LAST_MENDER', blank=True, null=True)  # Field name made lowercase.
#     rq_last_modifieddate = models.DateTimeField(db_column='RQ_LAST_ModifiedDate', blank=True,
#                                                 null=True)  # Field name made lowercase.
#     rq_order_id = models.IntegerField(db_column='RQ_ORDER_ID', blank=True, null=True)  # Field name made lowercase.
#     tier = models.TextField(blank=True, null=True)
#     rq_lock_type = models.IntegerField(db_column='RQ_LOCK_Type', blank=True, null=True)  # Field name made lowercase.
#     rq_lock_remark = models.TextField(db_column='RQ_LOCK_REMARK', blank=True, null=True)  # Field name made lowercase.
#     rq_lock_locktime = models.DateTimeField(db_column='RQ_LOCK_LOCKTIME', blank=True,
#                                             null=True)  # Field name made lowercase.
#     rq_lock_user = models.TextField(db_column='RQ_LOCK_USER', blank=True, null=True)  # Field name made lowercase.
#     default1 = models.TextField(blank=True, null=True)
#     default2 = models.TextField(blank=True, null=True)
#     default3 = models.TextField(blank=True, null=True)
#     default4 = models.TextField(blank=True, null=True)
#     default5 = models.TextField(blank=True, null=True)
#     default6 = models.TextField(blank=True, null=True)
#     default7 = models.TextField(blank=True, null=True)
#     default8 = models.TextField(blank=True, null=True)
#     default9 = models.TextField(blank=True, null=True)
#     default10 = models.TextField(blank=True, null=True)
#     rq_other_req_id = models.PositiveIntegerField(db_column='RQ_OTHER_REQ_ID', blank=True,
#                                                   null=True)  # Field name made lowercase.
#     rq_state = models.PositiveIntegerField(db_column='RQ_STATE', blank=True, null=True)  # Field name made lowercase.
#     rq_child_no = models.PositiveIntegerField(db_column='RQ_CHILD_NO', blank=True,
#                                               null=True)  # Field name made lowercase.
#     principal_user = models.TextField(db_column='principal_User', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'requirement'
#
#
# class TcReqScene(models.Model):
#     pk_id = models.IntegerField(blank=True, null=True)
#     project_id = models.IntegerField(blank=True, null=True)
#     fk_req_id = models.IntegerField(blank=True, null=True)
#     scene_name = models.TextField(db_column='scene_Name', blank=True, null=True)  # Field name made lowercase.
#     scene_desc = models.CharField(db_column='scene_Desc', max_length=400, blank=True,
#                                   null=True)  # Field name made lowercase.
#     scene_rbt = models.TextField(db_column='scene_RBT', blank=True, null=True)  # Field name made lowercase.
#     scene_complexity = models.TextField(db_column='scene_Complexity', blank=True,
#                                         null=True)  # Field name made lowercase.
#     source_type = models.IntegerField(blank=True, null=True)
#     target_source = models.TextField(db_column='target_Source', blank=True, null=True)  # Field name made lowercase.
#     file_name = models.TextField(blank=True, null=True)
#     master = models.TextField(blank=True, null=True)
#     created_user = models.TextField(db_column='created_User', blank=True, null=True)  # Field name made lowercase.
#     created_date = models.DateField(db_column='created_Date', blank=True, null=True)  # Field name made lowercase.
#     auditing_state = models.IntegerField(db_column='AUDITING_STATE', blank=True,
#                                          null=True)  # Field name made lowercase.
#     precondition = models.TextField(blank=True, null=True)
#     sceneimg = models.TextField(blank=True, null=True)
#     scenevks = models.TextField(blank=True, null=True)
#     default1 = models.TextField(blank=True, null=True)
#     default2 = models.TextField(blank=True, null=True)
#     default3 = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tc_req_scene'
#
#
# class Allcase(models.Model):
#     pk_id = models.IntegerField(blank=True, null=True)
#     fk_scene_id = models.IntegerField(blank=True, null=True)
#     project_id = models.PositiveIntegerField(db_column='PROJECT_ID', blank=True,
#                                              null=True)  # Field name made lowercase.
#
#     rqid = models.IntegerField(db_column='RQID', blank=True, null=True)  # Field name made lowercase.
#     group_name = models.CharField(db_column='GROUP_NAME', max_length=50, blank=True,
#                                   null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
#     table_name = models.TextField(db_column='TABLE_NAME', blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
#     auditing_state = models.CharField(db_column='AUDITING_STATE', max_length=1, blank=True,
#                                       null=True)  # Field name madelowercase.
#     precondition = models.TextField(blank=True, null=True)
#     is_invalidation = models.IntegerField(db_column='is_Invalidation', blank=True,
#                                           null=True)  # Field name made lowercase.
#     case_rbt = models.TextField(db_column='case_RBT', blank=True, null=True)  # Field name made lowercase.
#     created_user = models.TextField(db_column='created_User', blank=True, null=True)  # Field name made lowercase.
#     created_date = models.DateField(db_column='created_Date', blank=True, null=True)  # Field name made lowercase.
#     default1 = models.TextField(db_column='DEFAULT1', blank=True, null=True)  # Field name made lowercase.
#     default2 = models.TextField(db_column='DEFAULT2', blank=True, null=True)  # Field name made lowercase.
#     default3 = models.TextField(db_column='DEFAULT3', blank=True, null=True)  # Field name made lowercase.
#     parent_id = models.PositiveIntegerField(blank=True, null=True)
#     level = models.PositiveIntegerField(blank=True, null=True)
#     tier = models.TextField(blank=True, null=True)
#     run_state = models.IntegerField(blank=True, null=True)
#     case_req_impact = models.IntegerField(db_column='Case_Req_Impact', blank=True,
#                                           null=True)  # Field name made lowercase.
#     case_order_id = models.PositiveIntegerField(db_column='Case_order_Id', blank=True,
#                                                 null=True)  # Field name made lowercase.
#     attribute_1 = models.TextField(blank=True, null=True)
#     attribute_2 = models.TextField(blank=True, null=True)
#     attribute_3 = models.TextField(blank=True, null=True)
#     attribute_4 = models.TextField(blank=True, null=True)
#     attribute_5 = models.TextField(blank=True, null=True)
#     attribute_6 = models.TextField(blank=True, null=True)
#     attribute_7 = models.TextField(blank=True, null=True)
#     attribute_8 = models.TextField(blank=True, null=True)
#     attribute_9 = models.TextField(blank=True, null=True)
#     attribute_10 = models.TextField(blank=True, null=True)
#     attribute_11 = models.TextField(blank=True, null=True)
#     attribute_12 = models.TextField(blank=True, null=True)
#     attribute_13 = models.TextField(blank=True, null=True)
#     attribute_14 = models.TextField(blank=True, null=True)
#     attribute_15 = models.TextField(blank=True, null=True)
#     attribute_16 = models.TextField(blank=True, null=True)
#     attribute_17 = models.TextField(blank=True, null=True)
#     attribute_18 = models.TextField(blank=True, null=True)
#     attribute_19 = models.TextField(blank=True, null=True)
#     attribute_20 = models.TextField(blank=True, null=True)
#     attribute_21 = models.TextField(blank=True, null=True)
#     attribute_22 = models.TextField(blank=True, null=True)
#     attribute_23 = models.TextField(blank=True, null=True)
#     attribute_24 = models.TextField(blank=True, null=True)
#     attribute_25 = models.TextField(blank=True, null=True)
#     attribute_26 = models.TextField(blank=True, null=True)
#     attribute_27 = models.TextField(blank=True, null=True)
#     attribute_28 = models.TextField(blank=True, null=True)
#     attribute_29 = models.TextField(blank=True, null=True)
#     attribute_30 = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'allcase'
#
#
# class AllcaseSet(models.Model):
#     project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
#     case_name = models.CharField(db_column='CASE_NAME', max_length=50, blank=True,
#                                  null=True)  # Field name made lowercase.
#     case_clazz = models.CharField(db_column='CASE_CLAZZ', max_length=50, blank=True,
#                                   null=True)  # Field name made lowercase.
#     case_type = models.IntegerField(db_column='CASE_TYPE', blank=True, null=True)  # Field name made lowercase.
#     case_role = models.CharField(db_column='CASE_ROLE', max_length=50, blank=True,
#                                  null=True)  # Field name made lowercase.
#     case_data = models.CharField(db_column='CASE_DATA', max_length=50, blank=True,
#                                  null=True)  # Field name made lowercase.
#     table_name = models.TextField(db_column='TABLE_NAME', blank=True, null=True)  # Field name made lowercase.
#     wl_action = models.IntegerField(db_column='WL_ACTION', blank=True, null=True)  # Field name made lowercase.
#     wl_case = models.CharField(db_column='WL_CASE', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
#     case_state = models.IntegerField(db_column='CASE_STATE', blank=True, null=True)  # Field name made lowercase.
#     set_name = models.TextField(db_column='SET_NAME', blank=True, null=True)  # Field name made lowercase.
#     flag = models.PositiveIntegerField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.
#     fk_com_id = models.PositiveIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'allcase_set'
#
#
# class AllcaseSetIo(models.Model):
#     project_id = models.PositiveIntegerField(db_column='PROJECT_ID', blank=True,
#                                              null=True)  # Field name made lowercase.
#
#     type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     assign = models.TextField(db_column='ASSIGN', blank=True, null=True)  # Field name made lowercase.
#     value = models.TextField(blank=True, null=True)
#     description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
#     state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
#     set_name = models.TextField(db_column='SET_NAME', blank=True, null=True)  # Field name made lowercase.
#     sequence = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'allcase_set_io'
#
#
# class AllcaseSetIoOutparam(models.Model):
#     project_id = models.PositiveIntegerField(db_column='PROJECT_ID', blank=True,
#                                              null=True)  # Field name made lowercase.
#
#     type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(db_column='NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     assign = models.TextField(db_column='ASSIGN', blank=True, null=True)  # Field name made lowercase.
#     value = models.TextField(blank=True, null=True)
#     description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
#     state = models.IntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
#     set_name = models.TextField(db_column='SET_NAME', blank=True, null=True)  # Field name made lowercase.
#     sequence = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'allcase_set_io_outparam'
#
#
# class TcSceneSet(models.Model):
#     pk_id = models.IntegerField(db_column='PK_ID', blank=True, null=True)  # Field name made lowercase.
#     project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
#     fk_scene_id = models.IntegerField(db_column='FK_SCENE_ID', blank=True, null=True)  # Field name made lowercase.
#     case_name = models.TextField(db_column='CASE_NAME', blank=True, null=True)  # Field name made lowercase.
#     fk_com_id = models.IntegerField(db_column='FK_COM_ID', blank=True, null=True)  # Field name made lowercase.
#     case_type = models.IntegerField(db_column='CASE_TYPE', blank=True, null=True)  # Field name made lowercase.
#     case_role = models.TextField(db_column='CASE_ROLE', blank=True, null=True)  # Field name made lowercase.
#     wl_action = models.IntegerField(db_column='WL_ACTION', blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
#     created_user = models.TextField(db_column='CREATED_USER', blank=True, null=True)  # Field name made lowercase.
#     created_date = models.DateField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'tc_scene_set'
#
#
# class Component(models.Model):
#     pk_id = models.IntegerField(blank=True, null=True)
#     project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
#     runnerid = models.IntegerField(db_column='RUNNERID', blank=True, null=True)  # Field name made lowercase.
#     rootname = models.TextField(db_column='ROOTNAME', blank=True, null=True)  # Field name made lowercase.
#     groupname = models.TextField(db_column='GROUPNAME', blank=True, null=True)  # Field name made lowercase.
#     modulename = models.TextField(db_column='MODULENAME', blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
#     scriptname = models.TextField(db_column='SCRIPTNAME', blank=True, null=True)  # Field name made lowercase.
#     dataname = models.TextField(db_column='DATANAME', blank=True, null=True)  # Field name made lowercase.
#     version = models.TextField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.
#     created_user = models.TextField(blank=True, null=True)
#     created_date = models.TextField(blank=True, null=True)
#     default1 = models.TextField(blank=True, null=True)
#     default2 = models.TextField(blank=True, null=True)
#     default3 = models.TextField(blank=True, null=True)
#     default4 = models.TextField(blank=True, null=True)
#     default5 = models.TextField(blank=True, null=True)
#     extend_com_id = models.IntegerField(db_column='extend_com_Id', blank=True, null=True)  # Field name made lowercase.
#     parent_id = models.IntegerField(blank=True, null=True)
#     level = models.PositiveIntegerField(blank=True, null=True)
#     type = models.PositiveIntegerField(blank=True, null=True)
#     tier = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'component'
#
#
# class TcConstraintsRule(models.Model):
#     pk_id = models.PositiveIntegerField(blank=True, null=True)
#     project_id = models.IntegerField(blank=True, null=True)
#     fk_com_id = models.IntegerField(blank=True, null=True)
#     target_field = models.TextField(blank=True, null=True)
#     condition_field = models.TextField(blank=True, null=True)
#     con_value = models.TextField(blank=True, null=True)
#     con_value_index = models.IntegerField(blank=True, null=True)
#     check_field = models.TextField(blank=True, null=True)
#     res_value = models.TextField(blank=True, null=True)
#     res_value_index = models.IntegerField(blank=True, null=True)
#     read_only_marking = models.TextField(blank=True, null=True)
#     hascondition = models.IntegerField(db_column='hasCondition', blank=True, null=True)  # Field name made lowercase.
#     default1 = models.TextField(blank=True, null=True)
#     default2 = models.TextField(blank=True, null=True)
#     default3 = models.TextField(blank=True, null=True)
#     default4 = models.TextField(blank=True, null=True)
#     default5 = models.TextField(blank=True, null=True)
#     check_name = models.TextField(blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     paramvalue = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tc_constraints_rule'
#
#
# class TcSceneSetIo(models.Model):
#     project_id = models.IntegerField(blank=True, null=True)
#     fk_scene_id = models.IntegerField(blank=True, null=True)
#     type = models.IntegerField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     assign = models.TextField(blank=True, null=True)
#     value = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     sequence = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tc_scene_set_io'
#
#
# class Allset(models.Model):
#     pk_id = models.IntegerField(db_column='PK_ID', blank=True, null=True)  # Field name made lowercase.
#     project_id = models.PositiveIntegerField(db_column='PROJECT_ID', blank=True,
#                                              null=True)  # Field name made lowercase.
#     group_name = models.TextField(db_column='GROUP_NAME', blank=True, null=True)  # Field name made lowercase.
#     name = models.TextField(db_column='NAME', blank=True, null=True)  # Field name made lowercase.
#     table_name = models.TextField(db_column='TABLE_NAME', blank=True, null=True)  # Field name made lowercase.
#     data_name = models.CharField(db_column='DATA_NAME', max_length=255, blank=True,
#                                  null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='DESCRIPTION', max_length=4369, blank=True,
#                                    null=True)  # Field name made lowercase.
#     created_user = models.TextField(blank=True, null=True)
#     created_date = models.DateField(blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     level = models.IntegerField(blank=True, null=True)
#     default1 = models.TextField(blank=True, null=True)
#     default2 = models.TextField(blank=True, null=True)
#     default3 = models.CharField(max_length=300, blank=True, null=True)
#     default4 = models.CharField(max_length=300, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'allset'
#
#
# class AllsetSet(models.Model):
#     project_id = models.PositiveIntegerField(db_column='PROJECT_ID', blank=True,
#                                              null=True)  # Field name made lowercase.
#     case_name = models.CharField(db_column='CASE_NAME', max_length=150, blank=True,
#                                  null=True)  # Field name made lowercase.
#     case_clazz = models.CharField(db_column='CASE_CLAZZ', max_length=1200, blank=True,
#                                   null=True)  # Field name made lowercase.
#     case_type = models.IntegerField(db_column='CASE_TYPE', blank=True, null=True)  # Field name made lowercase.
#     case_role = models.CharField(db_column='CASE_ROLE', max_length=150, blank=True,
#                                  null=True)  # Field name made lowercase.
#     case_data = models.CharField(db_column='CASE_DATA', max_length=150, blank=True,
#                                  null=True)  # Field name made lowercase.
#     table_name = models.ForeignKey(Allcase,on_delete=models.CASCADE,db_column='TABLE_NAME', blank=True, null=True)  # Field name made lowercase.
#     wl_action = models.IntegerField(db_column='WL_ACTION', blank=True, null=True)  # Field name made lowercase.
#     wl_case = models.CharField(db_column='WL_CASE', max_length=150, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(db_column='VERSION', max_length=60, blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(db_column='DESCRIPTION', max_length=4369, blank=True,
#                                    null=True)  # Field name made lowercase.
#     case_state = models.IntegerField(db_column='CASE_STATE', blank=True, null=True)  # Field name made lowercase.
#     set_name = models.TextField(db_column='SET_NAME', blank=True, null=True)  # Field name made lowercase.
#     flag = models.PositiveIntegerField(db_column='FLAG', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'allset_set'


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


class CasesParameters(models.Model):
    project_id = models.PositiveIntegerField(primary_key=True)
    type = models.IntegerField()
    component = models.CharField(max_length=150)
    value = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    case_id = models.CharField(max_length=50)
    sequence = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cases_parameters'
        unique_together = (('project_id', 'case_id', 'component'),)


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

