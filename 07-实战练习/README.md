> 笔记来源：[尚硅谷Web前端HTML5&CSS3初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[TOC]

# 实战练习

## 1. 京东图片列表

![image-20210522222054290](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522222055.png)

### 开发准备

![image-20210522232556134](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522232557.png)

本来我们是想直接右键`图片另存为`的，但是发现并没有该选项，应该是京东对图片做了一定的限制

不过，这不妨碍我们获取这些图片，当然你也可以采用截图的方式获取，这里我们采用另外一种方式

![image-20210522232511516](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522232512.png)

通过F12可以看到，`img`元素的`src`属性，我们将三张图片的这些地址copy出来，直接在地址栏进行访问

```http
//img14.360buyimg.com/babel/s380x300_jfs/t1/168591/2/9328/64891/603ddb1aE93567699/3e4e717eeac051b2.jpg.webp
//img12.360buyimg.com/babel/s380x300_jfs/t1/152314/13/19839/57522/603e118dE941f0ce9/fdff58457adbef3e.jpg.webp
//img10.360buyimg.com/babel/s380x300_jfs/t1/154848/7/7426/82296/5fc072eeE20809200/34dca267e049d035.jpg.webp
```

这里就可以进行`图片另存为`了，当然你也可以直接在`src`上填写这些地址

![image-20210522233119008](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522233122.png)

不过，细心的同学会发现，这张图片的格式是`jpg.webp`后缀结尾的

因为我是在谷歌浏览器中访问的，而谷歌浏览器有自己的特有的一种图片格式webp（这个我们在第三节-字符实体与语义标签中介绍过）

当然这个格式不是谷歌自己进行转换的，而应该是京东做了不同浏览器之间的适配，即不同的浏览器传递不同格式的图片

**Q：怎么验证这种说法呢？**

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522235941.jpg)

A：我们可以打开非Chrome内核的浏览器，使用F12查看`img`的`src`地址就会发现不一样的地方了

这里我用微软自带的IE浏览器（<mark>温馨提示：微软官宣定于2022年6月15日完全停止对IE的支持</mark>）

![image-20210522234320111](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522234321.png)

对比就可以发现，无非就是在Chrome浏览器里后缀名多了一个`.webp`而已

```html
<!-- IE中的src地址 -->
//img14.360buyimg.com/babel/s380x300_jfs/t1/168591/2/9328/64891/603ddb1aE93567699/3e4e717eeac051b2.jpg
<!-- Chrome中的src地址 -->
//img14.360buyimg.com/babel/s380x300_jfs/t1/168591/2/9328/64891/603ddb1aE93567699/3e4e717eeac051b2.jpg.webp
```

知道这个原理，我们除了可以直接在`图片另存为`保存为`jpg`格式，其实还可以直接修改url地址

最后，我们将下载的图片放入`assets`（自定义目录）工程目录下即可

### 布局剖析

我们使用F12进行调试，可以看到京东图片列表的具体元素及属性

![image-20210522223411308](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522223412.png)

![image-20210522231503230](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522231554.png)

- 整体使用一个`li`元素包裹，里面又套了一层div`元素，宽高比：190:470
- 每张图片使用一个`img`元素，同时分别用`a`元素包裹，宽高比：190:150
- 三张图片高度和为150\*3=450 < 470，注意到图片之间存在2\*10px的外边距

这样，整个京东的图片列表的整体布局就非常清晰了

![525344c2d5628535e09f7f7087ef76c6a7ef6363](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522224823.gif)

但是，我们不会那么去实现代码。因为`li`元素应该包裹在`ul`元素或者`ol`元素中，而这里并没有遵循css中的语义标签使用规范

我们先看一下这么写会有什么问题

```html
<link rel="stylesheet" href="assets/reset.css">
<!-- ul包裹li -->
<ul>
    <li>ul li</li>
    <li>ul li</li>
    <li>ul li</li>
</ul>
<!-- div包裹li -->
<div>
    <li>div li</li>
    <li>div li</li>
    <li>div li</li>
</div>
```

**效果**

![image-20210522231742596](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522231743.png)

由于使用了reset样式，浏览器的默认样式被我们去除了。但是使用`ul`包裹的`li`元素和使用`div`包裹的`li`元素存在明显的区别：

- 使用`ul`包裹的`li`元素是没有默认样式的
- 使用`div`包裹的`li`元素前仍然存在黑点

我想是因为京东在这里实现了自己的样式替换，所以为了避免重复reset默认样式，我们采用正常的列表标签

### 结构搭建

```html
<ul>
    <li><a href="javascript:;"><img src="assets/1.jpg"></a></li>
    <li><a href="javascript:;"><img src="assets/2.jpg"></a></li>
    <li><a href="javascript:;"><img src="assets/3.jpg"></a></li>
</ul>
```

到这里我们基本骨架已经有了，不过因为没有写css样式，图片几乎占据了整个浏览器页面

![image-20210523001408717](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523001409.png)

### 样式添加

#### 方式1

还记得上面分析对布局结构的分析吗？

我们首先调整整体的宽高比和单个图片的宽高比

```css
ul {
    width: 190px;
    height: 470px;
}

ul>li img{
    /* 
		这里其实只调整高度即可，因为我们下载的图片宽高比跟F12中调试的是一致的
		而且一般情况下，不会固定或修改图片在网页中显示的宽高比
		因为如果我们随意调整css中的宽高比，会导致图片变形 
    	这里任意只调整高度或宽度，图片可以保持原比例大小
    */
    /* width: 190px; */
    height: 150px;
}
```

![image-20210523001149274](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523001150.png)

当然这只是其中写法，我们还可以换个思路，退一步来思考

#### 方式2

我们呢不去限制图片的宽或高，而是对超出`ul`元素部分（溢出部分）进行隐藏

```css
ul {
    width: 190px;
    height: 470px;
    overflow: hidden;
}
```

![image-20210523003056834](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523003058.png)

但是因为图片本身的大小还没有做限制，所以图片保持了原来的图片比例和大小

![image-20210523003305715](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523003306.png)

> 小剧场：
>
> 我们发现下载下来的图片分辨率大小为380*300，宽和高都刚好是浏览器中图片宽高的2倍
>
> 这只是巧合么？
>
> 不！这是京东为了高分辨率设备而做的适配，保证在一些高清屏下也能够保持清晰

那我们再对图片添加固定的宽或高不就行了？

不！我们直接指定宽或高的话，`overflow`属性不就显得多此一举嘛

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523003727.gif)

我们给img元素设定一个`100%`的`width`属性

```css
ul>li img {
    /* height: 150px; */
    width: 100%;
}
```

**Q：为什么不能用`auto`呢？**

A：我们前一节-盒模型中讲过，水平布局必须要满足一个等式，不满足即存在<mark>过渡约束</mark>，会做自动调整

而`ul`元素是块元素，块元素什么特点？独占一行啊！

图片宽度为380px，浏览器宽度为1920px（我本机中最大化浏览器的宽度）

现在的等式为`0 + 0 + 0 + 380px + 0 + 0 + 0 = 1920px`

这七个值中没有`auto`的情况，所以浏览器会自动调整`margin-right`值以使等式满足

`0 + 0 + 0 + 380px + 0 + 0 + (1920-380)px = 1920px`

![image-20210523005504380](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523005506.png)

所以如果使用`auto`属性值，整个过程中图片的`width`不会发生变化，展现出来的效果就依然是裁剪的样式

**Q：为什么`100%`可以呢？**

A：我们知道`100%`是会按照父元素计算的，`img`的父元素是`a`，a`的`父元素是`li`，`li`的父元素是`ul`

也就是说，由于我们没有给`a`和`li`单独设置样式，因此`img`最终会根据`ul`的宽度计算

而如果只调整图片的宽或高，图片是会保持原比例进行缩放的

所以这个时候就相当于给`img`设置了一个`width=190px`的属性值

### 细节完善

#### 背景色

通过颜色拾取器，识别背景色（我这里使用的是[FastStone Capture](https://faststone-capture.en.softonic.com/)中自带的`Screen Color Picker`）

```css
ul{
    ...
    /* 添加背景色 */
    background-color: #F4F4F4;
}
```

#### 外边距

根据布局剖析结果，我们给每个`li`元素添加一个10px的下边距

```css
ul>li {
    margin-bottom: 10px;
}
/* 
	但是上述写法有些问题，最后一张图片也有10px的外边距，有可能会影响到页面布局 
	所以我们可以指定最后一个没有外边距，可以使用之前讲到的伪类选择器
*/
ul>li:not(:last-child){
    margin-bottom: 10px;
}
```

**Q：为什么是给`li`元素添加呢？**

A：我们在调整布局结构的时候，特别是设置外边距，一般是设置块元素的，而不建议去调整行内元素或行内块元素

### 最终效果

![image-20210523012552494](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523012557.png)

### 核心代码

```html
<link rel="stylesheet" href="css/reset.css">
<style>
    ul {
        /* 宽高 */
        width: 190px;
        height: 470px;
        /* 处理溢出部分，这块不写效果也是一样的 */
        overflow: hidden;
        /* 设置背景色 */
        background-color: #F4F4F4;
    }

    ul>li:not(:last-child) {
        /* 设置下外边距 */
        margin-bottom: 10px;
    }

    ul>li img {
        /* 设定图片宽度 */
        width: 100%;
    }
</style>

<ul>
    <li><a href="javascript:;"><img src="assets/1.jpg"></a></li>
    <li><a href="javascript:;"><img src="assets/2.jpg"></a></li>
    <li><a href="javascript:;"><img src="assets/3.jpg"></a></li>
</ul>
```



## 2. 京东左侧导航条

![image-20210522222118478](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522222119.png)

### 开发准备

我们需要的就是这些文字，事先复制下来

```html
家用电器
手机 / 运营商 / 数码
电脑 / 办公
家居 / 家具 / 家装 / 厨具
男装 / 女装 / 童装 / 内衣
美妆 / 个护清洁 / 宠物
女鞋 / 箱包 / 钟表 / 珠宝
男鞋 / 运动 / 户外
房产 / 汽车 / 汽车用品
母婴 / 玩具乐器
食品 / 酒类 / 生鲜 / 特产
艺术 / 礼品鲜花 / 农资绿植
医药保健 / 计生情趣
图书 / 文娱 / 教育 / 电子书
机票 / 酒店 / 旅游 / 生活
理财 / 众筹 / 白条 / 保险
安装 / 维修 / 清洗 / 二手
工业品
```

### 布局剖析

![image-20210523122622621](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523122623.png)

- 整体使用`ul`和`li`元素，宽高比=190px:470px，其中上下存在10px的内边距（影响盒子大小）和10px的外边距（影响盒子布局）

![image-20210523122736533](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523122737.png)

- `li`中每个元素也比较简单，用`a`包裹文字，用`span`包裹斜杠
- 每个`li`元素的宽高比=190px:25px，其中左边存在18px的内边距（注意右边是不存在的）

![image-20210523123641389](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523123643.png)

- a元素没有什么大的布局，`span`元素左右存在2px的内边距

### 结构搭建

```html
<ul>
    <li>
        <a href="javascript:;">家用电器</a>
    </li>
    <li>
        <a href="javascript:;">手机</a>
        <span>/</span>
        <a href="javascript:;">运营商</a>
        <span>/</span>
        <a href="javascript:;">数码</a>
    </li>
    <li>
        <a href="javascript:;">电脑</a>
        <span>/</span>
        <a href="javascript:;">办公</a>
    </li>
    <li>
        <a href="javascript:;">家居</a>
        <span>/</span>
        <a href="javascript:;">家具</a>
        <span>/</span>
        <a href="javascript:;">家装</a>
        <span>/</span>
        <a href="javascript:;">厨具</a>
    </li>
    <li>
        <a href="javascript:;">男装</a>
        <span>/</span>
        <a href="javascript:;">女装</a>
        <span>/</span>
        <a href="javascript:;">童装</a>
        <span>/</span>
        <a href="javascript:;">内衣</a>
    </li>
    <li>
        <a href="javascript:;">美妆</a>
        <span>/</span>
        <a href="javascript:;">个护清洁</a>
        <span>/</span>
        <a href="javascript:;">宠物</a>
    </li>
    <li>
        <a href="javascript:;">女鞋</a>
        <span>/</span>
        <a href="javascript:;">箱包</a>
        <span>/</span>
        <a href="javascript:;">钟表</a>
        <span>/</span>
        <a href="javascript:;">珠宝</a>
    </li>
    <li>
        <a href="javascript:;">男鞋</a>
        <span>/</span>
        <a href="javascript:;">运动</a>
        <span>/</span>
        <a href="javascript:;">户外</a>
    </li>
    <li>
        <a href="javascript:;">房产</a>
        <span>/</span>
        <a href="javascript:;">汽车</a>
        <span>/</span>
        <a href="javascript:;">汽车用品</a>
    </li>
    <li>
        <a href="javascript:;">母婴</a>
        <span>/</span>
        <a href="javascript:;">玩具乐器</a>
    </li>
    <li>
        <a href="javascript:;">食品</a>
        <span>/</span>
        <a href="javascript:;">酒类</a>
        <span>/</span>
        <a href="javascript:;">生鲜</a>
        <span>/</span>
        <a href="javascript:;">特产</a>
    </li>
    <li>
        <a href="javascript:;">艺术</a>
        <span>/</span>
        <a href="javascript:;">礼品鲜花</a>
        <span>/</span>
        <a href="javascript:;">农资绿植</a>
    </li>
    <li>
        <a href="javascript:;">医药保健</a>
        <span>/</span>
        <a href="javascript:;">计生情趣</a>
    </li>
    <li>
        <a href="javascript:;">图书</a>
        <span>/</span>
        <a href="javascript:;">文娱</a>
        <span>/</span>
        <a href="javascript:;">教育</a>
        <span>/</span>
        <a href="javascript:;">电子书</a>
    </li>
    <li>
        <a href="javascript:;">机票</a>
        <span>/</span>
        <a href="javascript:;">酒店</a>
        <span>/</span>
        <a href="javascript:;">旅游</a>
        <span>/</span>
        <a href="javascript:;">生活</a>
    </li>
    <li>
        <a href="javascript:;">理财</a>
        <span>/</span>
        <a href="javascript:;">众筹</a>
        <span>/</span>
        <a href="javascript:;">白条</a>
        <span>/</span>
        <a href="javascript:;">保险</a>
    </li>
    <li>
        <a href="javascript:;">安装</a>
        <span>/</span>
        <a href="javascript:;">维修</a>
        <span>/</span>
        <a href="javascript:;">清洗</a>
        <span>/</span>
        <a href="javascript:;">二手</a>
    </li>
    <li>
        <a href="javascript:;">工业品</a>
    </li>
</ul>
```

![image-20210523125315312](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523125316.png)

我们引入[reset.css](https://meyerweb.com/eric/tools/css/reset/)样式来去除浏览器的默认样式

```html
<link rel="stylesheet" href="css/reset.css">
```

![image-20210523125421606](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523125422.png)

到这里，基本的骨架就有了

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523132630.gif)

**Q：那有些人会问了，我们不是引入了`reset.css`重置了浏览器的默认样式吗？为什么超链接还有样式？**

A：其实，如果仔细看reset.css的源代码，会发现`a`元素只是重置了一些基本的内外边距、边框和字体大小，并没有做完全把`a`元素的样式去除。这个下面会具体介绍

### 样式添加

根据布局剖析，我们可以直接设置整体的样式

```css
body{
    /* 这里顺便添加下背景色，通过颜色拾取器识别 */
	background-color: #F4F4F4;
}

ul {
    /* 宽高 */
    width: 190px;
    height: 450px;
    /* 内外边距 */
    padding: 10px 0;
    margin: 10px auto;
    /* 处理溢出部分 */
    overflow: hidden;
    /* 这里顺便添加下背景色，通过颜色拾取器识别 */
    background-color: #fefefe;
}

ul>li {
    /* 宽高，根据继承关系可以不写宽度 */
    height: 25px;
    /* 内外边距，这里只有一个内边距 */
    padding-left: 18px;
    /* 设置背景色：不是必须的，这里只是为了发现一些问题 */
    background-color: #bfa;
}

ul>li span{
    /* 内外边距*/
    padding: 0 2px;
}
```

![image-20210523140516172](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523140517.png)

到这里整体样式就添加完毕，但我们发现有点问题

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523132756.jpg)

别急！我们继续进行细节上的样式调整和优化

### 细节完善

要求效果

![image-20210523132256575](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523132258.png)

目前的效果

![image-20210523140554678](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523140555.png)



两个主要问题

1. 要求效果文字居中显示，而我们的文字偏左上角，底部有一定间距
2. 文字存在换行和重叠现象

![image-20210523132906972](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523132907.png)

我们一个一个处理

#### 文字调整

只需要给`li`元素添加一行属性

```css
line-height: 25px;
```

![image-20210523140647964](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523140652.png)

文字虽然在一行上了，但是依然有重叠问题啊，需要怎么处理呢？

要知道文字有几个属性：

- 文字大小
- 文字颜色
- 文字样式

我们通过F12看下这些属性

![image-20210523133630664](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523133631.png)

废话少说，直接写代码

```css
font-size: 14px;
color: #333;
```

我们这里先不写`text-decoration`属性，看下效果

![image-20210523141842151](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523141843.png)

写上`text-decoration`属性，再看下效果

```css
text-decoration: none;
```

![image-20210523141815499](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523141816.png)

这里可以看到文字下划线消失了，因为我们使用的`a`标签包裹文字，而超链接具有一定的文字样式（就是蓝色字体带下划线），所以`text-decoration`属性就是调整文字样式的

到这里，我们的重叠问题还是没有解决

![image-20210523135440547](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523135441.png)

~~稳住，我们能赢！~~ 我们再对比下要求的效果和我们现在的效果

![](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523151457.png)

![](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523151508.png)

看出来区别了吗？（当然重点不是我们的背景色，这无关紧要）

我们是把`/`符号用`span`包裹起来的，但是我们的`/`符号似乎又大又粗

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523140143.jpg)

#### 符号调整

![image-20210523140848453](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523140849.png)

废话少说，上代码

```css
ul>li span {
    padding: 0 2px;
    /* 调整符号字体大小 */
    font-size: 12px;
}
```

![image-20210523141939215](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523141940.png)

不过到这里，还是存在问题，我把`span`元素的内边距去除才可以 ~~（这里我没搞清楚为什么，知道的小伙伴可以评论或私信我哦；不过对比各个元素的盒子模型没什么区别，而且字体样式我也调整了；而且总感觉`/`符号之间间隙大了一点，这里存疑先不管了，我们继续往下）~~

![image-20210523143316453](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523143317.png)

#### 悬浮样式

![image-20210523144223948](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523144224.png)

我们注意到，当鼠标悬浮在某一行时，其背景颜色会有变化；同时，悬浮在某一个超链接上时，字体颜色变红

这里要用到一个伪类选择器`:hover`，我们还是直接上代码

```css
ul>li {
    height: 25px;
    padding-left: 18px;
    /* background-color: #bfa; 同时注释掉之前的一个辅助我们查看问题的背景色 */
    line-height: 25px;
}
/* 悬浮在某一行时，其背景颜色会有变化 */
ul>li:hover {
    background-color: #D9D9D9;
}
/* 悬浮在某一个超链接上时，字体颜色变红 */
ul>li a:hover {
    color: #C81724;
}
```

![image-20210523144614855](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523144615.png)

至此，我们的`京东左侧导航栏`的前端样式就基本完成了

### 最终效果

![动画2021-50](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523145041.gif)

### 核心代码

```html
<link rel="stylesheet" href="css/reset.css">
<style>
    body {
        /* body背景色，通过颜色拾取器识别 */
        background-color: #F4F4F4;
    }

    ul {
        /* 整体宽高 */
        width: 190px;
        height: 450px;
        /* 整体内外边距 */
        padding: 10px 0;
        margin: 10px auto;
        /* 处理溢出部分 */
        overflow: hidden;
        /* 整体背景色，通过颜色拾取器识别 */
        background-color: #FEFEFE;
    }

    ul>li {
        /* 每行宽高 */
        height: 25px;
        padding-left: 18px;
        /* 每行行高 */
        line-height: 25px;
    }

    ul>li:hover {
        /* 悬浮背景色 */
        background-color: #D9D9D9;
    }

    ul>li a {
        /* 字体大小、颜色、样式 */
        font-size: 14px;
        color: #333;
        text-decoration: none;
    }

    ul>li a:hover {
        /* 悬浮字体颜色 */
        color: #C81724;
    }

    ul>li span {
        /* 内边距，应该是有的，但是有点问题 */
        /* padding: 0 2px; */
        font-size: 12px;
    }
</style>
```

### 存疑问题

通过一番折腾和研究，终于发现问题的关键所在

因为在编写HTML代码时，每个`li`元素中的`a`的`span`标签都是换行的

而HTML中会将多个空格合并成一个，所以`a`的`span`之间都多了一个空格

有几种解决这个问题的方式

- 一是调整HTML中每个`li`元素中的代码，使之在一行上

- 二是给ul元素或li元素设置一个`font-size: 0`的属性值

- 三是通过js去除多余的换行字符（目前还没有学习到，所以不用这种方式，而且较麻烦）

我这里采用第二种方式

```css
ul>li {
    height: 25px;
    padding-left: 18px;
    line-height: 25px;
    /* 设置font-size */
    font-size: 0;
}

ul>li span {
    /* 设置内边距 */
    padding: 0 2px;
    font-size: 12px;
}
```

![image-20210523151126137](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523151126.png)

到这里，我们往往会忍不住赞叹一下自己：<q>Nice !</q>

![525344c2d5628535e09f7f7087ef76c6a7ef6363](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523151809.gif)

## 3. 网易新闻列表

![image-20210522222441076](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210522222442.png)

有了上面的实战步骤，对于网易新闻列表，我们就不进行那么详细的剖析了，直接上代码

### 结构搭建

```html
<div class="news_money">
    <div class="news_title">
        <h2 class="title"><a href="#">财经</a></h2>
    </div>
    <div class="news_img">
        <a href="#">
            <img width="300" height="150" alt="楼市＂加息潮＂来了?" src="assets/news.png">
            <div class="bg">
                <h3>楼市"加息潮"来了?</h3>
            </div>
        </a>
    </div>
    <ul class="news_list">
        <li>
            <a href="#">太疯狂！1000万芯片投资 "换来"7个涨停</a>
        </li>
        <li>
            <a href="#">重磅定调！打击比特币挖矿和交易行为</a>
        </li>
        <li>
            <a href="#">拜登愿将基建规模砍去6000亿美元</a>
        </li>
        <li>
            <a href="#">呷哺呷哺高管大换血 经营模式要变？</a>
        </li>
    </ul>
</div>
```

![image-20210523155443007](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523155444.png)

### 样式添加

```css
/* ====================整体==================== */
.news_money {
    /* 整体布局 */
    width: 300px;
    height: 324px;
    margin: 35px auto;
}

a {
    /* 去除超链接样式 */
    text-decoration: none;
}

/* ====================标题==================== */
.news_title {
    height: 40px;
    border-top: 1px #ddeedd solid;
}

.news_title .title {
    /* 标题整体布局 */
    width: 32px;
    height: 24px;
    line-height: 24px;
    padding-top: 6px;
    border-top: 1px #f34540 solid;
    margin-top: -1px;

}

.news_title a {
    /* 标题字体样式 */
    font-size: 16px;
    font-weight: bold;
    color: #404040;
}

.news_title a:hover {
    /* 标题悬浮样式 */
    color: red;
}

/* ====================图片==================== */
.new_img {
    height: 150px;
}

.news_img:hover {
    /* 
    	图片悬浮样式
    	这部分知识还没有学习到，所以只是做了一个简单的放大效果
    	但现在的效果其实是不对的，标题文字也被放大了
    */
    transform: scale(2);
}

/* 图片标题 */
.news_img .img_title {
    /* 图片标题整体布局 */
    height: 40px;
    line-height: 40px;
    margin-top: -40px;
    padding-left: 30px;
}

.news_img a {
    /* 图片标题字体样式 */
    color: #fff;
    font-weight: bold;
}

/* ====================新闻列表==================== */
.news_list {
    height: 120px;
    margin-top: 12px;
}

.news_list li {
    /* 新闻列表整体布局 */
    width: 285px;
    height: 30px;
    line-height: 30px;
    padding-left: 15px;
}

.news_list a {
    /* 新闻列表字体样式 */
    font-size: 14px;
    color: #666;
}

.news_list a:hover {
    /* 新闻列表悬浮样式 */
    color: red;
}
```

![动画2021-48](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210523181316.gif)