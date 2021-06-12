> 笔记来源：[尚硅谷Web前端HTML5&CSS3初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[TOC]

# 背景

## 1. PS的基本设置

> 工欲善其事，必先利其器

在介绍背景之前，首先需要做好准备工作：安装PS与基本设置

这里就不详细介绍PS的安装了，因为网上一抓一大把，主要介绍PS的基本设置

**左侧工具栏**

调成2列，更方便使用

![image-20210612131932089](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612131934.png)

**右侧工具栏**

不需要的视图统统关掉

![image-20210612132102709](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612132103.png)

**修改单位为像素**

由于一般默认的单位是厘米，所以这里需要修改

在历史记录、颜色或色板附近`右键`，打开选项卡，选择`界面选项`

![image-20210612132552271](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612200936.png)

打开`单位与标尺`，修改`单位`中的`标尺`与`文字`为`像素`

![image-20210612132904635](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612132906.png)



## 2. 背景

- `background-color` 设置背景颜色
- `background-image` 设置背景图片
  - 如果背景图片大小小于元素，则背景图片会自动在元素中平铺将元素铺满
  - 如果背景图片大小大于元素，则背景图片一部分会无法完全显示
  - 如果背景图片大小等于元素，则背景图片会直接正常显示
- `background-repeat` 设置背景图片的重复方式
  - `repeat` 默认值，背景图片沿着x轴和y轴双方向重复
  - `repeat-x` 背景图片沿着x轴方向重复
  - `repeat-y` 背景图片沿着y轴方向重复
  - `no-repeat` 背景图片不重复
- `background-position` 设置背景图片的位置
  - 通过`top` `left` `right` `bottom` `center`几个表示方位的词来设置背景图片的位置：使用方位词时必须要同时指定两个值，如果只写一个则第二个默认就是`center`
  - 通过偏移量来指定背景图片的位置：水平方向偏移量、垂直方向变量
- `background-clip` 设置背景的范围
  - `border-box` 默认值，背景会出现在边框的下边
  - `padding-box` 背景不会出现在边框，只出现在内容区和内边距
  - `content-box` 背景只会出现在内容区
- `background-origin` 背景图片的偏移量计算的原点
  - `border-box` 背景图片的变量从边框处开始计算
  - `padding-box` 默认值，`background-position`从内边距处开始计算
  - `content-box` 背景图片的偏移量从内容区处计算
- `background-size` 设置背景图片的大小
  - 第一个值表示宽度，第二个值表示高度；如果只写一个，则第二个值默认是`auto`
  - `cover` 图片的比例不变，将元素铺满
  - `contain` 图片比例不变，将图片在元素中完整显示
- `background-attachment` 背景图片是否跟随元素移动
  - `scroll` 默认值，背景图片会跟随元素移动
  - `fixed` 背景会固定在页面中，不会随元素移动

可以同时设置背景图片和背景颜色，这样背景颜色将会成为图片的背景色

**示例1**

```css
.box1 {
    height: 500px;
    width: 500px;
    overflow: auto;
    border: 20px red double;
    padding: 10px;
    /* 背景色 */
    background-color: darksalmon;
    /* 背景图 */
    background-image: url('/assets/背景.png');
    /* 背景图重复方式 */
    background-repeat: no-repeat;
    /* 背景图偏移位置 */
    background-position: 0 0;
    /* 背景图偏移量计算的原点 */
    background-origin: content-box;
    /* 背景范围 */
    background-clip: content-box;
    /* 背景图片大小 */
    background-size: contain;
}

.box2 {
    width: 100px;
    height: 1000px;
    background-color: orange;
    background-image: url("assets/背景2.jpg");
    background-repeat: no-repeat;
    background-position: 50px 50px;
    /* 背景图片是否跟随移动 */
    background-attachment: fixed;
}
```

![动画](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612155107.gif)

`backgound` 背景相关的简写属性，所有背景相关的样式都可以通过该样式来设置并且该样式没有顺序要求，也没有哪个属性是必须写的

**注意**

- `background-size`必须写在`background-position`的后边，并且使用/隔开`background-position/background-size` 
- `background-origin background-clip` 两个样式，`orgin`要在`clip`的前边

**示例2**

```css
.box1 {
    height: 500px;
    width: 500px;
    border: 10px red double;
    padding: 10px;
    background: #bfa url("assets/dlam.png") no-repeat 100px 100px/200px padding-box content-box;
}
```

![image-20210612155539118](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612155540.png)



## 练习1：线性渐变效果的背景图

![image-20210612160713058](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612160714.png)

如果我们仔细挂那可能，会发现很多网站导航条的背景色并不是单一的某种颜色，而是有一个渐变的效果

不过到目前为止，我们还没有学习`线性渐变`的内容，不过凭上面所学的知识同样可以实现

**切图**

首先，我们需要通过PS软件进行`切图`

1. 按住`Alt`同时滚动鼠标滑轮，可以对图片大小进行缩放；调整至合适大小，再选择`矩形块`工具，截取一个宽度为1px大小的图片

![image-20210612164205624](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612164207.png)

2. 然后选择`图像`-`裁剪`，就可以得到一个我们需要的一个背景图片

![image-20210612164423702](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612164425.png)

![image-20210612164544430](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612164545.png)

3. 最后，选择`文件`-`存储为Web所用格式`

![image-20210612164611999](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612164612.png)

4. 我这里选择的是PNG的格式，你可以对比几种格式，看看最终的图片大小折中选择，最好选择存储位置即可

![image-20210612164704402](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612164705.png)

5. 得到我们需要的背景图片之后，就可以引入到`css`样式中了

**代码**

```css
height: 60px;
width: 1500px;
background: url("assets/背景3.png") repeat-x;
```

**效果**

![image-20210612163950079](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612163954.png)



## 练习2：按钮点击效果

**代码**

```html
<style>
    a:link {
        /* 因为本身是行内元素，变成块元素更方便设置宽高 */
        display: block;
        width: 93px;
        height: 29px;
        background: url("assets/背景/练习2-背景/link.png");
    }

    a:hover {
        background: url("assets/背景/练习2-背景/hover.png");
    }

    a:active {
        background: url("assets/背景/练习2-背景/active.png");
    }
</style>

<a href="javascript:;"></a>
```

**效果**

![动画](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210612200530.gif)

