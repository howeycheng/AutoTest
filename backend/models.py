# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from mptt.models import MPTTModel


class Requirement(models.Model):
    rqid = models.IntegerField(db_column='RQID', blank=True, null=True)  # Field name made lowercase.
    project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=400, blank=True, null=True)  # Field name made lowercase.
    covered = models.IntegerField(db_column='COVERED', blank=True, null=True)  # Field name made lowercase.
    author = models.TextField(db_column='AUTHOR', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    review = models.IntegerField(db_column='REVIEW', blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    level = models.IntegerField(db_column='LEVEL', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    theme = models.TextField(db_column='THEME', blank=True, null=True)  # Field name made lowercase.
    accessory = models.TextField(db_column='ACCESSORY', blank=True, null=True)  # Field name made lowercase.
    rq_remark = models.CharField(db_column='RQ_Remark', max_length=300, blank=True,
                                 null=True)  # Field name made lowercase.
    req_rbt = models.TextField(db_column='req_RBT', blank=True, null=True)  # Field name made lowercase.
    test_item = models.TextField(db_column='test_Item', blank=True, null=True)  # Field name made lowercase.
    created_user = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    rq_last_mender = models.TextField(db_column='RQ_LAST_MENDER', blank=True, null=True)  # Field name made lowercase.
    rq_last_modifieddate = models.DateTimeField(db_column='RQ_LAST_ModifiedDate', blank=True,
                                                null=True)  # Field name made lowercase.
    rq_order_id = models.IntegerField(db_column='RQ_ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    tier = models.TextField(blank=True, null=True)
    rq_lock_type = models.IntegerField(db_column='RQ_LOCK_Type', blank=True, null=True)  # Field name made lowercase.
    rq_lock_remark = models.TextField(db_column='RQ_LOCK_REMARK', blank=True, null=True)  # Field name made lowercase.
    rq_lock_locktime = models.DateTimeField(db_column='RQ_LOCK_LOCKTIME', blank=True,
                                            null=True)  # Field name made lowercase.
    rq_lock_user = models.TextField(db_column='RQ_LOCK_USER', blank=True, null=True)  # Field name made lowercase.
    default1 = models.TextField(blank=True, null=True)
    default2 = models.TextField(blank=True, null=True)
    default3 = models.TextField(blank=True, null=True)
    default4 = models.TextField(blank=True, null=True)
    default5 = models.TextField(blank=True, null=True)
    default6 = models.TextField(blank=True, null=True)
    default7 = models.TextField(blank=True, null=True)
    default8 = models.TextField(blank=True, null=True)
    default9 = models.TextField(blank=True, null=True)
    default10 = models.TextField(blank=True, null=True)
    rq_other_req_id = models.PositiveIntegerField(db_column='RQ_OTHER_REQ_ID', blank=True,
                                                  null=True)  # Field name made lowercase.
    rq_state = models.PositiveIntegerField(db_column='RQ_STATE', blank=True, null=True)  # Field name made lowercase.
    rq_child_no = models.PositiveIntegerField(db_column='RQ_CHILD_NO', blank=True,
                                              null=True)  # Field name made lowercase.
    principal_user = models.TextField(db_column='principal_User', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'requirement'


class TcReqScene(models.Model):
    pk_id = models.IntegerField(blank=True, null=True)
    project_id = models.IntegerField(blank=True, null=True)
    fk_req_id = models.IntegerField(blank=True, null=True)
    scene_name = models.TextField(db_column='scene_Name', blank=True, null=True)  # Field name made lowercase.
    scene_desc = models.CharField(db_column='scene_Desc', max_length=400, blank=True,
                                  null=True)  # Field name made lowercase.
    scene_rbt = models.TextField(db_column='scene_RBT', blank=True, null=True)  # Field name made lowercase.
    scene_complexity = models.TextField(db_column='scene_Complexity', blank=True,
                                        null=True)  # Field name made lowercase.
    source_type = models.IntegerField(blank=True, null=True)
    target_source = models.TextField(db_column='target_Source', blank=True, null=True)  # Field name made lowercase.
    file_name = models.TextField(blank=True, null=True)
    master = models.TextField(blank=True, null=True)
    created_user = models.TextField(db_column='created_User', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateField(db_column='created_Date', blank=True, null=True)  # Field name made lowercase.
    auditing_state = models.IntegerField(db_column='AUDITING_STATE', blank=True,
                                         null=True)  # Field name made lowercase.
    precondition = models.TextField(blank=True, null=True)
    sceneimg = models.TextField(blank=True, null=True)
    scenevks = models.TextField(blank=True, null=True)
    default1 = models.TextField(blank=True, null=True)
    default2 = models.TextField(blank=True, null=True)
    default3 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tc_req_scene'
