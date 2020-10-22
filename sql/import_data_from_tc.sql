/*
用于从TC项目库导出数据到CM
*/

insert into cases_manager.cases (id, scene_id, project_id, group_name, name, case_id, description, created_user,
                                 created_date, parent_id, level, tier, run_state, order_id)
select pk_id,
       fk_scene_id,
       PROJECT_ID,
       GROUP_NAME,
       NAME,
       TABLE_NAME,
       DESCRIPTION,
       created_User,
       created_Date,
       parent_id,
       level,
       tier,
       run_state,
       Case_order_Id
from testcenter_24.allcase;

/*
 cases_components
 */
insert into cases_manager.cases_components(project_id, component_name, component_clazz, component_type, case_id,
                                           order_id, description)
SELECT PROJECT_ID, CASE_NAME, CASE_CLAZZ, CASE_TYPE, TABLE_NAME, WL_ACTION, DESCRIPTION
from testcenter_24.allcase_set;

/*
 cases_in_set
 */
insert into cases_manager.cases_in_set(project_id, name, case_id, order_id, description, case_state, set_id)
SELECT PROJECT_ID, CASE_CLAZZ, TABLE_NAME, WL_ACTION, DESCRIPTION, CASE_STATE, SET_NAME
from testcenter_24.allset_set;

/*
 cases_parameters
 */
-- insert into cases_manager.cases_parameters(project_id, type, component, value, description, state, case_id, sequence)
-- SELECT PROJECT_ID,
--        TYPE,
--        NAME,
--        value,
--        DESCRIPTION,
--        STATE,
--        SET_NAME,
--        sequence
-- from testcenter_24.allcase_set_io;

/*
 components
 */
insert into cases_manager.components(id, project_id, runner_id, root_name, group_name, module_name, description,
                                     script_name, data_name, created_user, created_date, parent_id, level, type, tier)
SELECT pk_id,
       PROJECT_ID,
       RUNNERID,
       ROOTNAME,
       GROUPNAME,
       MODULENAME,
       DESCRIPTION,
       SCRIPTNAME,
       DATANAME,
       created_user,
       created_date,
       parent_id,
       level,
       type,
       tier
from testcenter_24.component;

/*
parameter_rules
 */
insert into cases_manager.parameter_rules(id, project_id, fk_com_id, target_field, condition_field, con_value,
                                          con_value_index, check_field, res_value, res_value_index, read_only_marking,
                                          check_name, description, parameter_value)
SELECT pk_id,
       project_id,
       fk_com_id,
       target_field,
       condition_field,
       con_value,
       con_value_index,
       check_field,
       res_value,
       res_value_index,
       read_only_marking,
       check_name,
       description,
       paramvalue
from testcenter_24.tc_constraints_rule;

insert into cases_manager.req_scene(id, project_id, req_id, scene_name, scene_description, created_user,
                                    created_date)
SELECT pk_id,
       project_id,
       fk_req_id,
       scene_Name,
       scene_Desc,
       created_User,
       created_Date
from testcenter_24.tc_req_scene;

/*
requirement
 */
insert into cases_manager.requirement(id, project_id, name, parent_id, level, description, created_user,
                                      created_date, rq_order_id, tier)
SELECT RQID,
       PROJECT_ID,
       NAME,
       PARENT_ID,
       LEVEL,
       DESCRIPTION,
       created_user,
       created_date,
       RQ_ORDER_ID,
       tier
from testcenter_24.requirement;

/*
scene_set
 */
insert into cases_manager.scene_set(project_id, scene_id, component_name, com_id, type, order_id, description,
                                    created_user, created_date)
SELECT PROJECT_ID,
       FK_SCENE_ID,
       CASE_NAME,
       FK_COM_ID,
       CASE_TYPE,
       WL_ACTION,
       DESCRIPTION,
       CREATED_USER,
       CREATED_DATE
from testcenter_24.tc_scene_set;

/*
 scene_set_io
 */
insert into cases_manager.scene_set_io(project_id, scene_id, type, name, assign, value, description, sequence)
SELECT project_id,
       fk_scene_id,
       type,
       name,
       assign,
       value,
       description,
       sequence
from testcenter_24.tc_scene_set_io;

/*
sets
 */
insert into cases_manager.sets(id, project_id, group_name, set_name, set_id, description, created_user, created_date,
                               parent_id, level)
SELECT PK_ID,
       PROJECT_ID,
       GROUP_NAME,
       NAME,
       TABLE_NAME,
       DESCRIPTION,
       created_user,
       created_date,
       parent_id,
       level
from testcenter_24.allset;

/*
用例出入参
*/
insert into cases_manager.case_set_io(project_id, type, name, assign, value, description, state, case_id, sequence)
select PROJECT_ID,
       TYPE,
       NAME,
       ASSIGN,
       value,
       DESCRIPTION,
       STATE,
       SET_NAME,
       sequence
from testcenter_24.allcase_set_io;

/*用例值传递*/
insert into cases_manager.case_set_io_outparam (project_id, type, name, assign, value, description, state, case_id,
                                                sequence)
select PROJECT_ID,
       TYPE,
       NAME,
       ASSIGN,
       value,
       DESCRIPTION,
       STATE,
       SET_NAME,
       sequence
from testcenter_24.allcase_set_io_outparam;

/*获取测试集和场景关系*/
use testcenter_24;
drop procedure if exists getSetReq;
create procedure getSetReq()
begin
    # 存储测试集个数
    declare setCount int;
    declare tierCount int;
    drop table if exists set_req;
    # 创建测试集与场景关联表，根据set_id标识，每个测试集下包含的场景
    create table set_req
    (
        id        int(10),
        parent_id int(10),
        name      varchar(400),
        set_id    varchar(50),
        tier      varchar(60)
    );
    drop table if exists temp_sets;
    create temporary table temp_sets
    select SET_NAME as set_id from allset_set group by SET_NAME;
    # 查询测试集个数，针对每个测试集，查找其所有用例对应的父节点场景
    select count(distinct SET_NAME) into setCount from allset_set;
    select setCount;
    set @i = 0;
    set @set_name = '';
    repeat
        prepare s from 'select set_id into @set_name from temp_sets limit 1 offset ?';
        execute s using @i;
        deallocate prepare s;
        set @i = @i + 1;
        select @set_name;
        prepare s from 'create temporary table temp_tier select distinct allcase.tier as tier,allcase.parent_id as parent_id
        from allcase
            join allset_set on allcase.TABLE_NAME = allset_set.TABLE_NAME
        where allset_set.SET_NAME = ?';
        drop table if exists temp_tier;
        execute s using @set_name;
        deallocate prepare s;
        select * from temp_tier;
        select count(*) into tierCount from temp_tier;
        set @j = 0;
        set @parent_id = null;
        repeat
            prepare s from 'select parent_id into @parent_id from temp_tier limit 1 offset ?';
            execute s using @j;
            deallocate prepare s;
            # 递归遍历查找
            while @parent_id != ''
                do
                    set @id_count = 0;
                    select count(*) into @id_count from set_req where id = @parent_id and set_id = @set_name;
                    # 去重
                    if @id_count = 0 then
                        insert into set_req(id, parent_id, name, set_id,tier)
                        select pk_id, parent_id, NAME, @set_name,tier
                        from allcase
                        where pk_id = @parent_id;
                    end if;
                    select parent_id into @parent_id from allcase where pk_id = @parent_id;
                end while;
            set @j = @j + 1;
        until @j >= tierCount end repeat;
    until @i >= setCount end repeat;
    drop table temp_sets;
end;

call getSetReq();

insert into cases_manager.set_req select * from testcenter_24.set_req;

insert into cases_manager.run_set (project_id, case_name, case_id, set_id, run_id, status) SELECT PROJECT_ID,CASE_CLAZZ,TABLE_NAME,SET_NAME,RUNNAME,FLAG from testcenter_24.allrun_set;

insert into cases_manager.run (project_id, run_id, run_name, runner, set_id, start, finish, status)
SELECT PROJECT_ID,
       RUNTIMETABLE,
       RUNNAME,
       RUNNER,
       SETNAME,
       START,
       FINISH,
       STATE
from testcenter_24.allrun;

insert into cases_manager.run_set (project_id, case_name, case_clazz, case_type, case_id, order_id, case_state, set_id,
                                   run_id, flag)
SELECT PROJECT_ID,
       CASE_NAME,
       CASE_CLAZZ,
       CASE_TYPE,
       TABLE_NAME,
       WL_ACTION,
       CASE_STATE,
       SET_NAME,
       RUNNAME,
       FLAG
from testcenter_24.allrun_set

insert into cases_manager.run_set_io (project_id, component_name, value, description, status, case_id, run_id,
                                      order_id)
SELECT PROJECT_ID,
       NAME,
       value,
       DESCRIPTION,
       STATE,
       SET_NAME,
       RUNNAME,
       sequence
from testcenter_24.allrun_set_io;
