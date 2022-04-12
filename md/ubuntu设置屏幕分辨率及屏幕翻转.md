---
title: 'Ubuntu设置屏幕分辨率及屏幕翻转'
date: Fri, 24 Sep 2021 12:26:05 +0000
draft: false
tags: ['Linux', 'ubuntu', 'ubuntu 18.04', '分辨率', '屏幕翻转']
---

`Version: Ubuntu 18.04.6 LTS`

1.  1.  使用xrandr查看屏幕信息```
        $ xrandr
        Screen 0: minimum 320 x 200, current 1920 x 1080, maximum 8192 x 8192
        VGA-0 connected primary 1920x1080+0+0 inverted (normal left inverted right x axis y axis) 0mm x 0mm
           1024x768      60.00  
           800x600       60.32    56.25  
           848x480       60.00  
           640x480       59.94  
           1920x1080\_60.00  59.96\* 
        HDMI-0 disconnected (normal left inverted right x axis y axis)
        # 这里的信息是修改后的内容，主要注意当前显示器名称，例如我的是VGA-0
        ```
    2.  获得分辨率详情```
        $ cvt 1920 1080
        # 1920x1080 59.96 Hz (CVT 2.07M9) hsync: 67.16 kHz; pclk: 173.00 MHz
        Modeline "1920x1080\_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
        
        # 注意输出中Modeline后的内容
        # "1920x1080\_60.00"是resolution的名称
        # 整个Modeline后所有信息是newmode所需信息
        
        ```
    3.  设置并应用分辨率```
        xrandr --newmode "1920x1080\_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
        xrandr --addmode VGA-0 "1920x1080\_60.00"
        ```
    4.  设置屏幕翻转```
        xrandr -o inverted
        # left向左旋转90° right向右旋转90° normal正常显示
        ```
    5.  设置开机自动配置```
        \# 向~/.profile中添加以上步骤中的命令
        # set display resolution
        cvt 1920 1080
        xrandr --newmode "1920x1080\_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
        xrandr --addmode VGA-0 "1920x1080\_60.00"
        # set display rotation
        xrandr -o inverted
        ```