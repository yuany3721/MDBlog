---
title: 'Ubuntu配置mariadb'
date: Thu, 30 Sep 2021 03:20:57 +0000
draft: false
tags: ['Linux', 'mariadb', 'ubuntu', 'ubuntu 20.04']
---

安装
--

`sudo apt install mariadb-server`

配置
--

```
\# 启动 状态 重启
sudo service mysql start
service mysql status
sudo service mysql restart
# 初始化配置
sudo mysql\_secure\_installation
# 修改配置
sudo vi mariadb.cnf
# 端口号
Port 1234
# 允许远程连接登录
bind-address = 0.0.0.0
```

修改用户
----

```
\# 修改用户host
update user set host = '%' where user = 'root';
# 允许密码登录
update user set plugin='mysql\_native\_password' where user='root';
update user set password=password('password') where user='root';
# 修改密码
ALTER user 'root'@'localhost' IDENTIFIED BY 'passward';
# 用户授权
grant all privileges on \*.\* to 'user'@'host' identified by 'password' with grant option;
# 添加权限（和已有权限合并，不会覆盖已有权限）
GRANT Insert ON 'your database'.\* TO 'user'@'host';
# 删除权限
REVOKE Delete ON 'your database'.\* FROM 'user'@'host';
# 查看权限
show grants for 'user'@'localhost';
# 回收权限
revoke create on \*.\* from 'user@localhost';
# 删除用户
drop user 'user'@'localhost';
# 重命名用户
rename user 'user'@'%' to 'user1'@'%';
```权限列表： ![](https://wp.yuany3721.top/wp-content/uploads/2021/09/Pasted-7.png)

解决ERROR 1698 (28000)
--------------------

```
sudo vi mysqld.cnf
# 加入以下字段
\[mysqld\]
skip-grant-tables
# 重启mysql服务
sudo service mysql restart
# 直接enter进mysql
mysql -u root -p
```Ubuntu的日志在`/var/log/mysql````
use mysql
update user set authentication\_string=password("password"),plugin='mysql\_native\_password' where user='root';
flush privileges;
quit
```