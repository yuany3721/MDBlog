---
title: 'docker安装gitlab'
date: Sat, 19 Feb 2022 16:51:09 +0000
draft: false
tags: ['docker', 'docker', 'gitlab']
---

*   安装

```
sudo docker pull gitlab/gitlab-ce

sudo docker run -d \\
--publish 1118:80 \\
--publish 1119:22 \\
--name texlab \\
--restart always \\
-v /home/yuany3721/mnt/gitlab/config:/etc/gitlab \\
-v /home/yuany3721/mnt/gitlab/logs:/var/log/gitlab \\
-v /home/yuany3721/mnt/gitlab/data:/var/opt/gitlab \\
--shm-size 256m \\
gitlab/gitlab-ce
```修改配置文件```
cd /home/yuany3721/mnt/gitlab/config
sudo vi gitlab.rb

## 找到external\_url并修改为
external\_url 'http://texlab.yuany3721.top'

## 找到gitlab\_rails\['gitlab\_shell\_ssh\_port'\]并修改为
gitlab\_rails\['gitlab\_shell\_ssh\_port'\] = 1119
```初始root的密码在`/home/yuany3721/mnt/gitlab/config/initial_root_password`里

*   配置邮件

```
\# 修改gitlab.rb
gitlab\_rails\['smtp\_enable'\] = true
gitlab\_rails\['smtp\_address'\] = "smtp.qq.com"
gitlab\_rails\['smtp\_port'\] = 465
gitlab\_rails\['smtp\_user\_name'\] = "XXXX@qq.com"
gitlab\_rails\['smtp\_password'\] = "123456"  # qq授权码
gitlab\_rails\['smtp\_domain'\] = "smtp.qq.com"
gitlab\_rails\['smtp\_authentication'\] = "login"
gitlab\_rails\['smtp\_enable\_starttls\_auto'\] = true
gitlab\_rails\['smtp\_tls'\] = true

gitlab\_rails\['gitlab\_email\_from'\] = "XXXX@qq.com"    #和smtp\_user\_name一致，并且一定要有双引号
gitlab\_rails\['gitlab\_email\_enabled'\] = true
```