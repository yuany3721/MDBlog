---
title: 'Ubuntu防火墙操作'
date: Tue, 28 Sep 2021 14:14:49 +0000
draft: false
tags: ['Linux', 'ubuntu', 'ubuntu 20.04', '防火墙']
---

```
\# 启用防火墙
sudo ufw enable
# 查看防火墙状态
sufo ufw status
# 默认拒绝连接
sudo ufw default deny
# 开启端口
sudo ufw allow 1234
# 开启指定协议的端口
sudo ufw allow 8001/tcp
# 删除规则
sudo ufw delete allow 1234
sudo ufw delete allow 8081/tcp
# 重新加载配置
sudo ufw reload
```