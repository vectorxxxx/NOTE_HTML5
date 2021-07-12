> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# 背景

## 1. PS 的基本设置

> 工欲善其事，必先利其器

在介绍背景之前，首先需要做好准备工作：安装 PS 与基本设置

这里就不详细介绍 PS 的安装了，因为网上一抓一大把，主要介绍 PS 的基本设置

**左侧工具栏**

调成 2 列，更方便使用

![image-20210612131932089](https://img-blog.csdnimg.cn/img_convert/7d73fd6a596ea0e47e70748496a8bf40.png)

**右侧工具栏**

不需要的视图统统关掉

![image-20210612132102709](https://img-blog.csdnimg.cn/img_convert/727d4922a4b6e4dd43795672ded474ea.png)

**修改单位为像素**

由于一般默认的单位是厘米，所以这里需要修改

在历史记录、颜色或色板附近`右键`，打开选项卡，选择`界面选项`

![image-20210612132552271](https://img-blog.csdnimg.cn/img_convert/bce39fddd0e9beb31e0653283a6a9bd0.png)

打开`单位与标尺`，修改`单位`中的`标尺`与`文字`为`像素`

![image-20210612132904635](https://img-blog.csdnimg.cn/img_convert/c112282537409ae4e3d29fe0a9c20c33.png)

## 2. 背景

- `background-color` 设置背景颜色
- `background-image` 设置背景图片
  - 如果背景图片大小小于元素，则背景图片会自动在元素中平铺将元素铺满
  - 如果背景图片大小大于元素，则背景图片一部分会无法完全显示
  - 如果背景图片大小等于元素，则背景图片会直接正常显示
- `background-repeat` 设置背景图片的重复方式
  - `repeat` 默认值，背景图片沿着 x 轴和 y 轴双方向重复
  - `repeat-x` 背景图片沿着 x 轴方向重复
  - `repeat-y` 背景图片沿着 y 轴方向重复
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

**示例 1**

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
  background-image: url("/assets/背景.png");
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

![动画](https://img-blog.csdnimg.cn/img_convert/9f806f08854b47c21d02d5c23ed805a7.gif)

`backgound` 背景相关的简写属性，所有背景相关的样式都可以通过该样式来设置并且该样式没有顺序要求，也没有哪个属性是必须写的

**注意**

- `background-size`必须写在`background-position`的后边，并且使用/隔开`background-position/background-size`
- `background-origin background-clip` 两个样式，`orgin`要在`clip`的前边

**示例 2**

```css
.box1 {
  height: 500px;
  width: 500px;
  border: 10px red double;
  padding: 10px;
  background: #bfa url("assets/dlam.png") no-repeat 100px 100px/200px
    padding-box content-box;
}
```

![image-20210612155539118](https://img-blog.csdnimg.cn/img_convert/e469a4b629a9d0a42bacbf69b4a88ca2.png)

## 练习 1：线性渐变效果的背景图

![image-20210612160713058](https://img-blog.csdnimg.cn/img_convert/12dbf45389452852cdb04ac7b87e5946.png)

如果我们仔细挂那可能，会发现很多网站导航条的背景色并不是单一的某种颜色，而是有一个渐变的效果

不过到目前为止，我们还没有学习`线性渐变`的内容，不过凭上面所学的知识同样可以实现

**切图**

首先，我们需要通过 PS 软件进行`切图`

1. 按住`Alt`同时滚动鼠标滑轮，可以对图片大小进行缩放；调整至合适大小，再选择`矩形块`工具，截取一个宽度为 1px 大小的图片

![image-20210612164205624](https://img-blog.csdnimg.cn/img_convert/9cf933089851d88ab149afbd2a09ffca.png)

2. 然后选择`图像`-`裁剪`，就可以得到一个我们需要的一个背景图片

![image-20210612164423702](https://img-blog.csdnimg.cn/img_convert/99c888010d9f623899d7c21059dd1f60.png)

![image-20210612164544430](https://img-blog.csdnimg.cn/img_convert/ea1f3a686a6f538d0bd7b221952ec4a7.png)

3. 最后，选择`文件`-`存储为Web所用格式`

![image-20210612164611999](https://img-blog.csdnimg.cn/img_convert/db062cd60f46f94d2829f9601866ae99.png)

4. 我这里选择的是 PNG 的格式，你可以对比几种格式，看看最终的图片大小折中选择，最好选择存储位置即可

![image-20210612164704402](https://img-blog.csdnimg.cn/img_convert/1e51da62eaaa95c55273289aba15decd.png)

5. 得到我们需要的背景图片之后，就可以引入到`css`样式中了

**代码**

```css
height: 60px;
width: 1500px;
background: url("assets/背景3.png") repeat-x;
```

**效果**

![image-20210612163950079](https://img-blog.csdnimg.cn/img_convert/eb584be8969046de24bbf44e29a30a22.png)

## 练习 2：按钮点击效果

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

![动画](https://img-blog.csdnimg.cn/img_convert/2f9fc038af13642f79b96a76a02b710f.gif)
