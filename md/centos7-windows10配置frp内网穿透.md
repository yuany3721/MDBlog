---
title: 'Centos7 / Windows10配置frp+远程桌面'
date: Sun, 29 Aug 2021 12:57:28 +0000
draft: false
tags: ['centos', 'frp', 'Linux', 'windows', 'Windows', '远程桌面']
---

`Version: Centos 7.3 Windows10 21H1`

#
-

frp由客户端(frpc)和服务端(frps)组成，服务端通常部署在具有公网 IP 的机器上，客户端通常部署在需要穿透的内网服务所在的机器上。 内网服务由于没有公网IP，不能被非局域网内的其他用户访问。用户通过访问服务端的 frps，由frp负责根据请求的端口或其他信息将请求路由到对应的内网机器，从而实现通信。 在 frp 中一个代理对应一个需要暴露的内网服务。一个客户端支持同时配置多个代理。 [官方文档](https://gofrp.org/docs)

代理类型
----

类型

描述

tcp

单纯的 TCP 端口映射，服务端会根据不同的端口路由到不同的内网服务。

udp

单纯的 UDP 端口映射，服务端会根据不同的端口路由到不同的内网服务。

http

针对 HTTP 应用定制了一些额外的功能，例如修改 Host Header，增加鉴权。

https

针对 HTTPS 应用定制了一些额外的功能。

stcp

安全的 TCP 内网代理，需要在被访问者和访问者的机器上都部署 frpc，不需要在服务端暴露端口。

sudp

安全的 UDP 内网代理，需要在被访问者和访问者的机器上都部署 frpc，不需要在服务端暴露端口。

xtcp

点对点内网穿透代理，功能同 stcp，但是流量不需要经过服务器中转。

tcpmux

支持服务端 TCP 端口的多路复用，通过同一个端口访问不同的内网服务。

配置Centos服务端
-----------

```
# 下载Latest Release
wget https://github.com/fatedier/frp/releases/LatestRelease/frp.tar.gz
# 解压
tar -zxf frp.tar.gz
# 进入解压后的文件夹
cd frp
# 配置服务端配置文件
vi frps.ini
``````
; 配置基本内容
[common]
bind_port = 7000
; frp自带的frps控制台
dashboard_port = 7001
dashboard_user = xxxx
dashboard_pwd = xxxx
``````
# 启动frps 
./frps -c frps.ini
```

配置Windows客户端
------------

下载Latest Release for Windows amd64并解压 编辑frpc.ini```
[common]
server_addr = 1.2.3.4
server_port = 7000  ; frpc中的

[remote_desktop]
type = tcp
local_ip = 127.0.0.1
local_port = 3389 ; Windows远程桌面的默认端口
remote_port = 8011
```进入cmd，`./frpc.exe -c frpc.ini`这时使用另一台电脑运行mstsc，连接1.2.3.4:8011并输入凭据即可顺利登录到Windows远程桌面 - 检查可能的问题：

1.  Windows未开启远程桌面
2.  Windows未开启远程访问权限（系统--远程设置--允许远程连接至此电脑）
3.  远程桌面的其他设置（系统--远程桌面）
4.  查看设置的端口是否被占用，对应端口防火墙是否打开，frpc是否与frps端口对应（bind\_port是frp提供服务的端口，local\_port是客户端需要访问的服务所在端口，remote\_port是访问客户端服务的服务端端口）

设置Window10的frpc开机自启
-------------------

新建run.bat```
# 使用绝对路径
D:\frp_0.37.0\./frpc.exe -c D:\frp_0.37.0\frpc.ini > D:\frp_0.37.0\frpc.log
```新建frpc.vbs```
set ws=WScript.CreateObject(WScript.Shell) 
ws.Run run.bat,0
' 这里的run.bat也需要用绝对路径
```将frpc.vbs放到`C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`里即可

关于xtcp
------

*   开防火墙udp

```
firewall-cmd --permanent --add-port=7002/udp --zone=public
firewall-cmd --reload
```

*   修改frps.ini

```
[common]
bind_port = 7000
bind_udp_port = 7001
dashboard_port = 7001
dashboard_user = xxxx
dashboard_pwd = xxxx
```

*   配置frpc1（需要被访问的服务所在主机）的frpc.ini

```
[common]
server_addr = 1.2.3.4
server_port = 7000

[remote_desktop]
type = tcp
local_ip = 127.0.0.1
local_port = 3389
remote_port = 8011

[xtcp_remote_desktop]
type = xtcp
sk = abcdefg
local_ip = 127.0.0.1
local_port = 3389
```

*   配置frpc2（访问服务的主机）的frpc.ini

```
[common]
server_addr = 1.2.3.4
server_port = 7000

[xtcp_visitor]
type = xtcp
role = visitor
server_name = xtcp_remote_desktop  ; 与上面的对应
sk = abcdefg
bind_addr = 127.0.0.1
bind_port = 1234
```

*   启动两个frpc，都正常注册，访问127.0.0.1:1234进行连接时两个frpc同时报错：

```
[xtcp_remote_desktop] get sid from visitor error: read udp 192.168.1.101:57484: i/o timeout
[xtcp_visitor] get sid from visitor error: read udp 192.168.1.104:60475->103.98.240.96:42221: i/o timeout
```_截至Aug 30 2021 GMT+08，[GitHub issue](https://github.com/fatedier/frp/issues)中对此问题的回答仍然是与运营商NAT机制有关，无法稳定穿透，请尝试stcp_\## 用nginx伪装端口 nginx的stream没有server\_name选项，所以即使拿域名伪装后面也会带一个端口号 _以及安装nginx的时候并没有`--with-stream`，所以懒得弄了= =_