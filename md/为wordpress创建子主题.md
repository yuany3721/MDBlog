---
title: '为WordPress创建子主题'
date: Thu, 16 Sep 2021 08:33:54 +0000
draft: false
tags: ['WordPress', '子主题']
---

子主题
---

*   父主题是一个完整的主题，其中包括所有必需的 WordPress 模板文件和主题工作所需的文件资源。所有主题（不包括子主题）都可以被认为是父主题。
*   子主题可以继承父主题所有功能和外观，但可用于对主题的任何部分进行修改。自定义子主题与父主题的文件是分开的，升级父主题时不会影响对站点所做的修改。

**如果需要进行大量的样式、功能修改，则不推荐使用子主题**

创建子主题
-----

找到`wp-content/themes`，记住父主题的**文件夹名称（注意不是主题名）**，这里以kratos为例。

*   在temes目录下新建文件夹并进入，文件夹即为子主题路径。```
    mkdir kratos-yuany3721
    cd kratos-yuany3721
    ```
*   新建style.css文件并进行配置```
    vi style.css
    
    # 配置如下
    /\*
     Theme Name:   kratos-yuany3721
     Theme URI:    http://example.com
     Description:  kratos-yuany3721
     Author:       yuany3721
     Author URI:   http://example.com
     Template:     kratos
     Version:      0.0.1
     License:      GNU General Public License v2 or later
     License URI:  http://www.gnu.org/licenses/gpl-2.0.html
     Tags:         light, dark, two-columns, right-sidebar, responsive-layout, accessibility-ready
     Text Domain:  yyyy
    \*/
    ```其中，Theme Name需要对themes目录内主题唯一，Template后写的是父主题的**文件夹名称**，其余各内容均非必填项。
*   新建functions.php并进行配置。回到父主题查看functions.php：
    *   如果存在get\_template函数，例如get\_template\_directory()或者get\_template\_directory\_uri()，则如下配置functions.php```
        <?php
        add\_action( 'wp\_enqueue\_scripts', 'my\_theme\_enqueue\_styles' );
        function my\_theme\_enqueue\_styles() {
            wp\_enqueue\_style( 'child-style', get\_stylesheet\_uri(),
                array( 'parenthandle' ), 
                wp\_get\_theme()->get('Version') // this only works if you have Version in the style header
            );
        }
        
        ```
    *   如果存在get\_stylesheet函数，例如get\_stylesheet\_directory()或get\_stylesheet\_directory\_uri()，则如下配置functions.php```
        <?php
        add\_action( 'wp\_enqueue\_scripts', 'my\_theme\_enqueue\_styles' );
        function my\_theme\_enqueue\_styles() {
            $parenthandle = 'parent-style'; // This is 'twentyfifteen-style' for the Twenty Fifteen theme.
            $theme = wp\_get\_theme();
            wp\_enqueue\_style( $parenthandle, get\_template\_directory\_uri() . '/style.css', 
                array(),  // if the parent theme code has a dependency, copy it to here
                $theme->parent()->get('Version')
            );
            wp\_enqueue\_style( 'child-style', get\_stylesheet\_uri(),
                array( $parenthandle ),
                $theme->get('Version') // this only works if you have Version in the style header
            );
        }
        
        ```
    *   以本文kratos为例，配置如下：```
        <?php
        function my\_theme\_enqueue\_styles() {
            wp\_enqueue\_style( 'child-style', get\_template\_directory\_uri().'/style.css' );
        }
        add\_action( 'wp\_enqueue\_scripts', 'my\_theme\_enqueue\_styles');
        ```
*   回到WordPress主题中查看，如果配置无误就会出现一个新的子主题，点击启用即可