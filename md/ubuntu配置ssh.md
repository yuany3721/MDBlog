---
title: 'Ubuntu配置ssh和sftp'
date: Tue, 28 Sep 2021 14:22:21 +0000
draft: false
tags: ['ftp', 'Linux', 'ssh', 'ubuntu', 'ubuntu 20.04']
---

安装
--

**ssh是客户端，sshd才是服务端**```
\# 查看是否已经安装
dpkg -l | grep ssh
# 安装openssh server
sudo apt install openssh-server
```

修改端口
----

```
\# 修改端口
sudo vi /etc/ssh/sshd\_config
# 修改Port后的参数
# 重启ssh
sudo service ssh restart
```

远程连接
----

```
ssh -p 修改后的端口 用户名@ip地址
```

配置sftp
------

```
\# 使用系统自带的internal-sftp服务
sudo vi /etc/ssh/sshd\_config
# 修改以下字段
Subsystem sftp internal-sftp
# 限定用户
Match Group sftp
# 更改登录后默认路径
ChrootDirectory /
```