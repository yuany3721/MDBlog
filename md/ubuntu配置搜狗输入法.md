---
title: 'Ubuntu配置搜狗输入法'
date: Mon, 27 Sep 2021 06:32:52 +0000
draft: false
tags: ['Linux', 'ubuntu', 'ubuntu 20.04', '搜狗输入法']
---

`Version: Ubuntu 20.04.3 LTS`

1.  下载deb包 [官网地址](https://pinyin.sogou.com/linux/)
2.  ```
    sudo dpkg -i sogoupinyin\_版本号\_amd64.deb
    # 如果提示缺少依赖
    sudo apt -f install
    ```
3.  设置系统语言 Settings --> Region & Language --> Manage Installed Languages 将 Keyboard input method system设置为fcitx
4.  注销重新登录用户，使用Ctrl+Space即可切换为搜狗输入法