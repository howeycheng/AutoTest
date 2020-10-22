create database cases_manager;
use cases_manager;

/*
 table : cases
 */
CREATE TABLE cases
(
    id           int(11)          NOT NULL,
    scene_id     int(11)          DEFAULT NULL,
    project_id   int(10) unsigned NOT NULL,
    group_name   char(50)         NOT NULL,
    name         varchar(400)     NOT NULL,
    case_id      varchar(50)      DEFAULT NULL,
    description  text,
    created_user varchar(50)      DEFAULT NULL,
    created_date date             DEFAULT NULL,
    parent_id    int(10) unsigned NOT NULL,
    level        int(10) unsigned DEFAULT '0',
    tier         varchar(60)      DEFAULT '000',
    run_state    int(11)          DEFAULT '0',
    order_id     int(10) unsigned DEFAULT '0',
    PRIMARY KEY (id, project_id) USING BTREE,
    KEY casesIndex (case_id) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : cases_components
 */
CREATE TABLE cases_components
(
    project_id      int(11)  NOT NULL,
    component_name  char(50) NOT NULL,
    component_clazz char(50) NOT NULL,
    component_type  int(11)     DEFAULT NULL,
    case_id         varchar(50) DEFAULT NULL,
    order_id        int(11)     DEFAULT NULL,
    description     text,
    PRIMARY KEY (project_id, component_name, case_id) USING BTREE,
    KEY casesComponentsIndex (project_id, component_name, case_id) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : cases_parameters
 */
/* CREATE TABLE cases_parameters
(
    project_id  int(10) unsigned NOT NULL,
    type        int(11)          NOT NULL,
    component   char(150)        NOT NULL,
    value       text,
    description text,
    state       int(11)     DEFAULT NULL,
    case_id     varchar(50)      NOT NULL,
    sequence    smallint(4) DEFAULT '0',
    PRIMARY KEY (project_id, case_id, component) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT; */

/*
 table : sets
 */
CREATE TABLE sets
(
    id           int(11)          NOT NULL AUTO_INCREMENT,
    project_id   int(11) unsigned NOT NULL,
    group_name   varchar(50)      NOT NULL,
    set_name     varchar(50)      NOT NULL,
    set_id       varchar(50) DEFAULT NULL,
    description  text,
    created_user varchar(50) DEFAULT NULL,
    created_date date        DEFAULT NULL,
    parent_id    int(11)     DEFAULT '0',
    level        int(11)     DEFAULT '0',
    PRIMARY KEY (id) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 0
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : cases_in_set
 */
CREATE TABLE cases_in_set
(
    project_id  int(11) unsigned NOT NULL,
    name        varchar(400)     NOT NULL,
    case_id     varchar(50) DEFAULT NULL,
    order_id    int(11)     DEFAULT NULL,
    description text,
    case_state  int(11)     DEFAULT NULL,
    set_id      varchar(50)      NOT NULL
#     PRIMARY KEY (project_id, case_id, set_id) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : components
 */
CREATE TABLE components
(
    id           int(11)          NOT NULL DEFAULT '0',
    project_id   int(11)          NOT NULL DEFAULT '0',
    runner_id    int(11)                   DEFAULT NULL,
    root_name    varchar(50)               DEFAULT NULL,
    group_name   varchar(100)              DEFAULT NULL,
    module_name  varchar(100)              DEFAULT NULL,
    description  text,
    script_name  varchar(200)              DEFAULT NULL,
    data_name    varchar(50)               DEFAULT NULL,
    created_user varchar(50)               DEFAULT NULL,
    created_date varchar(50)               DEFAULT NULL,
    parent_id    int(11)          NOT NULL DEFAULT '0',
    level        int(10) unsigned NOT NULL DEFAULT '0',
    type         int(10) unsigned NOT NULL,
    tier         varchar(60)               DEFAULT '',
    PRIMARY KEY (id, project_id) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : requirement
 */
CREATE TABLE requirement
(
    id        int(11) NOT NULL DEFAULT '0',
    project_id   int(11) NOT NULL DEFAULT '-1',
    name         varchar(400)     DEFAULT NULL,
    parent_id    int(11)          DEFAULT NULL,
    level        int(11)          DEFAULT NULL,
    description  text,
    created_user varchar(50)      DEFAULT NULL,
    created_date datetime         DEFAULT NULL,
    rq_order_id  int(11)          DEFAULT '0',
    tier         varchar(60)      DEFAULT NULL,
    PRIMARY KEY (id, project_id) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : parameter_rules
 */
CREATE TABLE parameter_rules
(
    id             int(11) unsigned NOT NULL AUTO_INCREMENT,
    project_id        int(11)          NOT NULL DEFAULT '0',
    fk_com_id         int(11)                   DEFAULT NULL,
    target_field      varchar(50)               DEFAULT NULL,
    condition_field   varchar(50)               DEFAULT NULL,
    con_value         varchar(50)               DEFAULT NULL,
    con_value_index   int(11)                   DEFAULT NULL,
    check_field       varchar(50)               DEFAULT NULL,
    res_value         varchar(50)               DEFAULT NULL,
    res_value_index   int(11)                   DEFAULT NULL,
    read_only_marking varchar(20)               DEFAULT NULL,
    check_name        varchar(30)               DEFAULT NULL,
    description       varchar(500)              DEFAULT NULL,
    parameter_value   text,
    PRIMARY KEY (id) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 1
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : req_scene
 */
CREATE TABLE req_scene
(
    id             int(11) NOT NULL,
    project_id        int(11) NOT NULL DEFAULT '0',
    req_id         int(11)          DEFAULT NULL,
    scene_name        varchar(100)     DEFAULT NULL,
    scene_description varchar(400)     DEFAULT NULL,
    created_user      varchar(50)      DEFAULT NULL,
    created_date      date             DEFAULT NULL,
    PRIMARY KEY (id, project_id) USING BTREE
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : scene_set
 */
CREATE TABLE scene_set
(
    id             int(11) NOT NULL AUTO_INCREMENT,
    project_id     int(11)     DEFAULT NULL,
    scene_id    int(11)     DEFAULT NULL,
    component_name varchar(50) DEFAULT '',
    com_id      int(11)     DEFAULT NULL,
    type           int(11)     DEFAULT NULL,
    order_id       int(11)     DEFAULT NULL,
    description    text,
    created_user   varchar(50) DEFAULT '',
    created_date   date        DEFAULT NULL,
    PRIMARY KEY (id) USING BTREE
) ENGINE = InnoDB
  AUTO_INCREMENT = 0
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*
 table : scene_set_io
 */
CREATE TABLE scene_set_io
(
    project_id  int(11)      NOT NULL,
    scene_id int(11)      NOT NULL,
    type        int(11)      NOT NULL,
    name        varchar(150) NOT NULL,
    assign      varchar(150) DEFAULT NULL,
    value       text,
    description varchar(200) DEFAULT NULL,
    sequence    smallint(4)  DEFAULT '0'
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*用例出入参*/
CREATE TABLE case_set_io (
  project_id int(10) unsigned NOT NULL,
  type int(11) NOT NULL,
  name char(150) NOT NULL,
  assign varchar(150) NOT NULL DEFAULT '',
  value text,
  description text,
  state int(11) DEFAULT NULL,
  case_id varchar(50) NOT NULL,
  sequence smallint(4) DEFAULT '0',
  PRIMARY KEY (project_id,case_id,name,assign) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

/*用例值传递、值校验*/
CREATE TABLE case_set_io_outparam (
  project_id int(10) unsigned NOT NULL,
  type int(11) NOT NULL,
  name char(150) NOT NULL,
  assign varchar(150) NOT NULL DEFAULT '',
  value text,
  description text,
  state int(11) DEFAULT NULL,
  case_id varchar(50) NOT NULL,
  sequence smallint(4) DEFAULT '0',
  PRIMARY KEY (project_id,case_id,type,name,assign) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

/*测试集和场景关联表*/
CREATE TABLE set_req(
    id        int(10) NOT NULL,
    parent_id int(10) NOT NULL,
    name      varchar(400) NOT NULL,
    set_id    varchar(50) NOT NULL,
    tier      varchar(60) DEFAULT NULL,
    PRIMARY KEY (id,set_id) USING BTREE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

CREATE TABLE run
(
    project_id int(10)  NOT NULL,
    run_id     char(50) DEFAULT NULL,
    run_name   char(50) NOT NULL,
    runner     char(50) DEFAULT NULL,
    set_id     char(50) DEFAULT NULL,
    start      datetime DEFAULT NULL,
    finish     datetime DEFAULT NULL,
    status     int(11)  DEFAULT NULL,
    PRIMARY KEY (project_id, run_id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;


/*日志列表*/
CREATE TABLE run_set (
  project_id int(10) NOT NULL,
  case_name char(200) NOT NULL,
  case_clazz char(200) NOT NULL,
  case_type int(11) DEFAULT NULL,
  case_id varchar(50) DEFAULT NULL,
  order_id int(11) DEFAULT NULL,
  case_state int(11) DEFAULT NULL,
  set_id varchar(50) DEFAULT NULL,
  run_id char(50) DEFAULT NULL,
  flag int(10) unsigned DEFAULT '0',
  KEY runSetIndex2 (PROJECT_ID,run_id,set_id)
)  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

/*日志出入参数表*/
CREATE TABLE run_set_io (
  project_id int(10) NOT NULL,
  component_name char(200) NOT NULL,
  value text,
  description text,
  status int(11) DEFAULT NULL,
  case_id varchar(50) DEFAULT NULL,
  run_id char(50) DEFAULT NULL,
  order_id smallint(6) DEFAULT NULL,
  KEY runSetIoIndex (PROJECT_ID,run_id,case_id)
) ENGINE = InnoDB
  AUTO_INCREMENT = 0
  DEFAULT CHARSET = utf8
  ROW_FORMAT = COMPACT;

  alter table set_req add index set_id_parent_id (set_id,parent_id);
  alter table case_set_io_outparam add index case_id_type (case_id,type);
  alter table run_set_io add index run_id_case_id (run_id,case_id);