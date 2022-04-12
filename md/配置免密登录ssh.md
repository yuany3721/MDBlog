---
title: '配置免密登录ssh'
date: Wed, 29 Sep 2021 10:42:27 +0000
draft: false
tags: ['Linux', 'RSA', 'ssh', 'ubuntu', 'ubuntu 20.04', 'windows', 'Windows']
---

*   本机A，需要连接的远程主机B

1.  A中进入.ssh文件夹内`ssh-keygen -t rsa` Windows的.ssh在C:\\User\\Username\\.ssh Ubuntu、Centos的.ssh在~\\.ssh(/home/username/.ssh)
2.  如果有ssh-copy-id则执行以下代码，否则到3 `ssh-copy-id -i YourIdRsa.pub Busername@Bhostaddress`
3.  将id\_rsa.pub不管用拷贝、ftp还是什么办法扔到B机器上 `cat id_rsa.pub >> ~/.ssh/authorized_keys`
4.  检查ssh是否开启RSA免密登录```
    vi /etc/ssh/sshd\_config
    # 需要正确配置以下选项（在openssh中均为默认）
    RSAAuthentication yes
    PubkeyAuthentication yes
    AuthorizedKeysFile      .ssh/authorized\_keys
    ```

*   Windows Terminal新建远程连接tab```
    ssh -p 1234 Busername@Bhostaddress
    ```