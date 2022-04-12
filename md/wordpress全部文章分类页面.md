---
title: 'WordPress全部文章分类页面'
date: Tue, 31 Aug 2021 16:48:56 +0000
draft: false
tags: ['PHP', 'WordPress', 'WordPress', '分类目录']
---

1.  复制一个page.php为catlist.php```
    cd usr/wordpress # 自己的WordPress目录 
    find . -name page.php # 找到自己主题对应的路径 
    cd YourThemePath 
    cp page.php catlist.php
    ```
2.  在catlist.php最前添加代码```
    <?php
    /\*
    Template Name: Category
    \*/
    ?>
    ```
3.  在catlist.php中找到`<?php the_content();?>`并在其后添加如下代码```
    <?php
      //获得顶级分类
      $taxonomies=get\_terms('category',array('hide\_empty'=>false,'parent'=>'0',));
      if(!empty($taxonomies)){
          foreach($taxonomies as $category){
              if($category->name != '未分类'){?>
                  <h2><a href=<?php echo get\_category\_link($category->term\_id)?>><?php echo $category->name?></a></h2>
                  <?php
                  echo   '<ul>';
                  //获取二级分类
                  $cats=get\_terms('category',array('hide\_empty'=>false,'parent'=>$category->term\_id,));
                  if(!empty($cats)){
                      foreach($cats as $cat){?>
                          <h3><a href=<?php echo get\_category\_link($cat->term\_id)?>><?php echo $cat->name?></a></h3>
                          <?php
                          echo   '<ul>';
                          //获取三级分类
                          $terms = get\_terms('category',array('hide\_empty'=>false,'parent'=>$cat->term\_id,));
                          if(!empty($terms)) {
                              foreach($terms as $term){?>
                                  <h4><a href=<?php echo get\_category\_link($term->term\_id)?>><?php echo $term->name?></a></h4>
                              <?php
                              }
                          }
                          echo '</ul>';
                      }
                  }
                  echo '</ul>';
              }
          }
      }
      ?>
    <h2><a href="<?php echo home\_url()?>/archives/category/uncategorized">未分类</a></h2>
      <style>
          h2>a,
          h3>a,
          h4>a {
              color: black;
          }
          h2 {
              margin-top: 2em;
              font-size: 28px;
          }
          h3 {
              font-size: 22px;
          }
          h4 {
              font-size: 18px;
          }
      </style>
    ```
4.  保存模板，新建空白页面，页面模板选第二步Template Name后的名字，这里是Category
5.  保存并发布，在菜单添加该页面即可