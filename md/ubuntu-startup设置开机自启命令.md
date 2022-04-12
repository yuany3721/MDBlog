---
title: 'Ubuntu startup设置开机自启命令'
date: Thu, 30 Sep 2021 01:15:27 +0000
draft: false
tags: ['Linux', 'startup', 'ubuntu', 'ubuntu 20.04']
---

`Version: Ubuntu Server 20.04.3 LTS`

1.  建立自己的脚本，如`wlt.sh`
2.  修改脚本执行权限`chmod 775 wlt.sh`
3.  将脚本放入/etc/profile.d路径下即可 /etc/init.d update-rc.d wlt.sh defaults 91