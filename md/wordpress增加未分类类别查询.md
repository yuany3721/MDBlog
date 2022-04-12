---
title: 'WordPress增加未分类类别查询'
date: Fri, 10 Sep 2021 02:40:12 +0000
draft: false
tags: ['WordPress', 'WordPress', '分类目录']
---

在主题编辑器中找到分类目录页面，添加如下代码：```
<h2><a href="<?php echo home\_url()?>/archives/category/uncategorized">未分类</a></h2>
```