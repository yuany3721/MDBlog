---
title: 'Ubuntu配置阿里云ddns'
date: Wed, 29 Sep 2021 09:30:41 +0000
draft: false
tags: ['crontab', 'ddns', 'Linux', 'ubuntu', 'ubuntu 20.04']
---

1.  1.  生成阿里云access key **注意：不能使用ram子用户**
    2.  下载并配置ddns```
        curl https://github.com/NewFuture/DDNS/releases/download/v2.10.2/ddns -#SLo ddns && chmod 777 ddns
        # 自动生成config.json
        ./ddns -h
        # 配置config.json
        vi config.json
        ```
    3.  使用ddns配置```
        ./ddns -c config.json
        ```_我自己在配置时发现，如果同时解析ipv4和ipv6时，阿里云的ipv6优先级要高于ipv4，但是截至CST+8 21.09.30 ipv6连接体验仍然不尽如人意，所以可以只解析ipv4_
    4.  用crontab设置每小时自动更新ddns```
        crontab -e
        # 设置每小时的30min自动更新
        30 \* \* \* \* date >> path/to/ddns.log
        30 \* \* \* \* path/to/./ddns -c path/to/config.json >> path/to/ddns.log
        # 查看crontab设置
        crontab -l
        ```