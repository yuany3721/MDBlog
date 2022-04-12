---
title: 'PGP'
date: Mon, 27 Sep 2021 09:29:48 +0000
draft: false
tags: ['PGP', '密码学', '邮件加密']
---

#
-

为了保护电子邮件及文件的保密性，Phil Zimmermann提出了Pretty Good Privacy 加密标准，得到了广泛的应用。 PGP（Pretty Good Privacy）是一个基于RSA公钥加密体系的邮件加密软件。 PGP加密技术的创始人是美国的Phil Zimmermann。他创造性地把RSA公钥体系和传统加密体系的结合起来，并且在数字签名和密钥认证管理机制上有巧妙的设计，因此PGP成为目前几乎最流行的公钥加密软件包。 由于RSA算法计算量极大，在速度上不适合加密大量数据，所以PGP实际上用来加密的不是RSA本身，而是采用传统加密算法IDEA，IDEA加解密的速度比RSA快得多。

*   PGP随机生成一个密钥，用IDEA算法对明文加密，然后用RSA算法对密钥加密。收件人同样是用RSA解出随机密钥，再用IEDA解出原文。这样的链式加密既有RSA算法的保密性(Privacy)和认证性(Authentication)，又保持了IDEA算法速度快的优势。
*   PGP提供五种服务：鉴别，机密性，压缩，兼容电子邮件，分段

PGP最初在Windows实现，直到PGP Desktop9.0一直为免费共享软件，后来PGP被Symantec收购，成为了收费软件。 OpenPGP (http://www.openpgp.org/index.shtml)是源自PGP 标准的免费开源实现，目前是世界上应用最广泛的电子邮件加密标准。OpenPGP由IETF 的OpenPGP 工作组提出，其标准定义在RFC 4880。在Windows和Linux(Unix)下均有免费开源的版本。 GunPG(The GNU Privacy Guard)是OpenPGP的最典型实现，目前支持Windows 、 Linux 、 MacOS 等 流 行 操 作 系 统 。