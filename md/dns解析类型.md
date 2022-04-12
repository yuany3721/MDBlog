---
title: 'DNS解析类型'
date: Mon, 30 Aug 2021 07:36:08 +0000
draft: false
tags: ['DNS', '计算机网络']
---

1.  A（Address）记录 将域名指向 IP 地址（Ipv4）
2.  MX（Mail Exchange）记录 邮件交换记录，用于电子邮件系统发邮件时根据收信人的地址后缀来定位邮件服务器
3.  CNAME（Canonical Name）记录 通常称别名解析，可实现将域名指向另一个域名或IP地址
4.  URL（Uniform Resource Locator）转发 网址转发，如果没有一个独立的IP地址或者有一个域名B，想在访问A域名时访问到B域名的内容，这时就可以通过URL转发来实现。URL转发可以转发到某一个目录或某一个文件上，而CName不可以
5.  NS（Name Server）记录 域名服务器记录，用来指定该域名由哪个DNS服务器来进行解析
6.  AAAA记录 将域名指向 Ipv6 地址
7.  TXT记录 文本记录
8.  PTR值（Pointer） 用于将一个IP地址映射到对应的域名，也可以看成是A记录的反向解析
9.  SRV记录 服务定位器，记录了哪台服务器提供了何种服务
10.  CAA（Certificate Authority Authorization）记录 认证机构授权，限定了特定域名颁发的证书和CA（证书颁发机构）之间的联系