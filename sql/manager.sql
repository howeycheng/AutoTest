CREATE TABLE project (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(50) DEFAULT NULL,
  status smallint(6) DEFAULT NULL,
  enabled tinyint(4) DEFAULT NULL,
  view_state smallint(6) DEFAULT NULL,
  access_min smallint(6) DEFAULT NULL,
  description varchar(2000) DEFAULT NULL,
  createDate datetime DEFAULT '2008-12-01 00:00:00',
  workflow int(11) DEFAULT '1',
  pro_code varchar(50) DEFAULT NULL,
  pro_info varchar(100) DEFAULT NULL,
  pro_type int(10) unsigned DEFAULT NULL,
  pro_scope int(10) unsigned DEFAULT NULL,
  pro_parent_system int(10) unsigned DEFAULT NULL,
  pro_pm varchar(50) DEFAULT NULL,
  pro_pm_phone varchar(50) DEFAULT NULL,
  pro_test_type int(10) unsigned DEFAULT NULL,
  pro_planBeginTime varchar(50) DEFAULT NULL,
  pro_planEndTime varchar(50) DEFAULT NULL,
  pro_testResouce varchar(50) DEFAULT NULL,
  pro_testManager varchar(50) DEFAULT NULL,
  pro_tm_phone varchar(50) DEFAULT NULL,
  pro_beginTime varchar(50) DEFAULT NULL,
  pro_endTime varchar(50) DEFAULT NULL,
  pro_person_number int(10) unsigned DEFAULT NULL,
  pro_req_code varchar(50) DEFAULT NULL,
  manager int(11) DEFAULT '0',
  PRIMARY KEY (id) USING BTREE,
  UNIQUE KEY idx_project_name (name) USING BTREE,
  KEY idx_project_id (id) USING BTREE,
  KEY idx_project_view (view_state) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8

CREATE TABLE project_user (
  project_id int(10) unsigned NOT NULL DEFAULT '0',
  user_id int(10) unsigned NOT NULL DEFAULT '0',
  access_level smallint(6) NOT NULL DEFAULT '10',
  is_book_mail int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (project_id,user_id) USING BTREE,
  KEY idx_project_user (user_id) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8


