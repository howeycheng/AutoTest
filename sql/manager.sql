CREATE TABLE project (
  project_id int(10) NOT NULL AUTO_INCREMENT,
  name varchar(128) DEFAULT NULL,
  description mediumtext,
  create_user varchar(32) DEFAULT NULL,
  PRIMARY KEY (project_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

CREATE TABLE project_user (
  project_id int(10) unsigned NOT NULL DEFAULT '0',
  user_id int(10) unsigned NOT NULL DEFAULT '0',
  access_level smallint(6) NOT NULL DEFAULT '10',
  is_book_mail int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (project_id,user_id) USING BTREE,
  KEY idx_project_user (user_id) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8


