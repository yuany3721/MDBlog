---
title: 'Ubuntu安装docker'
date: Sat, 19 Feb 2022 12:14:37 +0000
draft: false
tags: ['docker', 'Linux', 'ubuntu', 'ubuntu 20.04']
---

```
\# 安装
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
# 验证
sudo docker run hello-world
# 开机自启守护进程
sudo systemctl enable docker
```