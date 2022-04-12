---
title: 'nginx+php上传文件配置'
date: Sat, 25 Sep 2021 04:30:48 +0000
draft: false
tags: ['502', 'nginx', 'nginx', 'PHP', 'php', '文件上传']
---

*   设置php.ini 主要把包括的选项有：`post_max_size`、`upload_max_filesize`、`memory_limit`、`max_execution_time`等
*   设置nginx.conf 主要是`client_max_body_size`，注意设置`sendfile on`
*   nginx一定程度上避免502```
    location / {
        ......
        proxy\_connect\_timeout 300;
        proxy\_send\_timeout 300;
        proxy\_read\_timeout 300;
    }
    ```