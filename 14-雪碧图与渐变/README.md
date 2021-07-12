> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# 雪碧图与渐变

## 1. 雪碧图

解决图片闪烁的问题：

可以将多个小图片统一保存到一个大图片中，然后通过调整`background-position`来显示响应的图片

这样图片会同时加载到网页中就可以有效的避免出现闪烁的问题

这个技术在网页中应用十分广泛，被称为`CSS-Sprite`，这种图我们称为雪碧图

雪碧图的使用步骤：

1. 先确定要使用的图标
2. 测量图标的大小
3. 根据测量结果创建一个元素
4. 将雪碧图设置为元素的背景图片
5. 设置一个偏移量以显示正确的图片

雪碧图的特点：

- 一次性将多个图片加载进页面，降低请求的次数，加快访问速度，提升用户的体验

**示例 1**

![image-20210612230816217](https://img-blog.csdnimg.cn/img_convert/e8a34378504abff5538d7d362a1d9c3c.png)

```css
a:link {
  display: block;
  width: 93px;
  height: 29px;
  background: url("assets/背景/练习2-背景/btn.png");
  /* 默认值，可以不设置 */
  background-position: 0 0;
}

a:hover {
  /* 设置水平方向的一个偏移量；注意是向左移动，所以是负值 */
  background-position: -93px 0;
}

a:active {
  /* 设置水平方向的一个偏移量；注意是向左移动，所以是负值 */
  background-position: calc(-93px * 2) 0;
}
```

![动画](https://img-blog.csdnimg.cn/img_convert/4bef45919d901b3dddf40a364bd89037.gif)

我们对比以下之前练习中的效果，第一次加载进来的时候会有明显的闪烁

![动画](https://img-blog.csdnimg.cn/img_convert/48cf54374d1d7827bc18d2e13c3d52b7.gif)

**示例 2**

![image-20210612230929739](https://img-blog.csdnimg.cn/img_convert/42c16d9512e844b8d273e8feda0cad1a.png)

```css
.box1 {
  width: 109px;
  height: 33px;
  background: url("assets/背景/练习3-雪碧图/amazon-sprite_.png");
  /* 设置水平和垂直方向的一个偏移量；注意移动方向 */
  background-position: -10px -10px;
}

.box2 {
  width: 42px;
  height: 30px;
  background: url("assets/背景/练习3-雪碧图/amazon-sprite_.png");
  /* 设置水平和垂直方向的一个偏移量；注意移动方向 */
  background-position: -58px -338px;
}
```

![image-20210612231316806](https://img-blog.csdnimg.cn/img_convert/fbd314d9c0c3da0c4a6deb1b7e3320f1.png)

## 2. 线性渐变

通过渐变可以设置一些复杂的背景颜色，可以实现从一个颜色向其他颜色过渡的效果

！！渐变是图片，需要通过`background-image`来设置

线性渐变，颜色沿着一条直线发生变化 `linear-gradient()`

```css
# 红色在开头，黄色在结尾，中间是过渡区域
background-image: linear-gradient(red, yellow);
```

![image-20210612205407103](https://img-blog.csdnimg.cn/img_convert/47123ca0139073c1a8a2f61395408167.png)

线性渐变的开头，我们可以指定一个渐变的方向

- `to left`
- `to right`
- `to bottom`
- `to top`
- `deg` deg 表示度数
- `turn` 表示圈

```css
background-image: linear-gradient(to left, red, yellow);
background-image: linear-gradient(to right, red, yellow);
background-image: linear-gradient(to top, red, yellow);
background-image: linear-gradient(to bottom, red, yellow);
```

上面基本的 4 个方向的渐变很好理解，我们就不再做过多的一一解释了

我们来看度数的渐变效果

```css
background-image: linear-gradient(45deg, red, yellow);
```

![image-20210612210437495](https://img-blog.csdnimg.cn/img_convert/64164ca16b1fc085883520eccd349ec1.png)

会发现它是从左下角往右上角去进行渐变的，为什么呢？

我们小时候肯定都用过量角器

![image-20210612210854253](https://img-blog.csdnimg.cn/img_convert/6ad862f51623cae580cd5d395af6e930.png)

是不是恍然大悟，我们以原点作为起始点，有角度的那条边去做渐变，再把四象限的概念和矩形内部的四个角对应起来

**<mark>总结</mark>**：线性渐变的边上的某一点为起点，以一定角度渐变的；渐变方向的颜色是线性变化的，而其垂线方向的颜色是一致的

然后看下圈数的表示方法

```css
background-image: linear-gradient(0.4turn, red, yellow);
```

因为圈数和角度之间可以相互转换，所以这里就不再进行赘述了

另外，渐变可以同时指定多个颜色，多个颜色默认情况下平均分布，也可以手动指定渐变的分布情况

`repeating-linear-gradient()` 可以平铺的线性渐变

```css
background-image: repeating-linear-gradient(red, yellow);
```

![image-20210612205909079](https://img-blog.csdnimg.cn/img_convert/1ec54cc28b7ec1ffa1dd355206a85eb1.png)

默认情况下，跟`linear-gradient(red, yellow)`效果一样，我们稍作改动

```css
background-image: repeating-linear-gradient(red 0px, yellow 50px);
```

![image-20210612210015129](https://img-blog.csdnimg.cn/img_convert/3e39b9b284335266b3f626529b6aaa79.png)

由于我们设置的`div`宽高为`200px`，所以会有 4 次重复的渐变效果

所以默认情况下，下列几种写法是一致的，效果相同

```css
background-image: linear-gradient(red, yellow);
background-image: repeating-linear-gradient(red, yellow);
/* 因为我们设置的div盒子的宽高为200px，所以这里[height]=200px */
background-image: repeating-linear-gradient(red 0, yellow [height]);
```

## 3. 径向渐变

`radial-gradient()` 径向渐变（放射性的效果）

```css
background-image: radial-gradient(red, yellow);
```

默认情况下，径向渐变的形状根据元素的形状来计算的

- 正方形 --> 圆形

  ![image-20210612215139463](https://img-blog.csdnimg.cn/img_convert/ef3c9f5ed8c21677749b93d2e1d93917.png)

- 长方形 --> 椭圆形

  ![image-20210612215228775](https://img-blog.csdnimg.cn/img_convert/222148cc7e1047bd50ec3dd165ff6fae.png)

默认情况下，`circle`和`ellipse`是自动适配盒子的，我们也可以手动指定径向渐变的形状

**形状**

- `circle` 圆形
- `ellipse`椭圆

```css
background-image: radial-gradient(circle, red, yellow);
```

![image-20210612220320304](https://img-blog.csdnimg.cn/img_convert/f52c0364605c0ad9a20763de0a82db5f.png)

也可以指定渐变的位置

**位置**

- `top`
- `right`
- `left`
- `center`
- `bottom`

```css
background-image: radial-gradient(at left, red, yellow);
```

![image-20210612220417179](https://img-blog.csdnimg.cn/img_convert/e67d258061cdf5263312fbbda747964b.png)

当然，除了上述值，还可以指定像素

**大小**

- `closest-side` 近边
- `farthest-side` 远边
- `closest-corner` 近角
- `farthest-corner` 远角

```css
background-image: radial-gradient(100px 60px, red, yellow);
```

![image-20210612220547137](https://img-blog.csdnimg.cn/img_convert/8bd62e310a802d483b1a4c499db507b1.png)

同时对其形状/大小和位置进行指定

`radial-gradient(形状/大小 at 位置, 颜色 位置, 颜色 位置, 颜色 位置)`

```css
background-image: radial-gradient(circle at 50px 100px, red 50px, yellow 100px);
```

![image-20210612221359657](https://img-blog.csdnimg.cn/img_convert/2d952552e1a55ae04a6c358f99f191d1.png)

总结一下

**形状**

- `circle` 圆形
- `ellipse`椭圆

**大小**

- `closest-side` 近边
- `farthest-side` 远边
- `closest-corner` 近角
- `farthest-corner` 远角

**位置**

- `top`
- `right`
- `left`
- `center`
- `bottom`

类似于线性渐变，径向渐变也有对应的`repeat`属性

```css
background-image: repeating-radial-gradient(
  circle at 50px 100px,
  red 50px,
  yellow 100px
);
```

![image-20210612221604176](https://img-blog.csdnimg.cn/img_convert/9c41690bc864e959e50ebc0fd5fdf36c.png)

**<mark>总结</mark>**：径向渐变的渐变方向以圆心为起点，往四周扩散的；同一半径上的颜色是渐变的，同一圆周上的颜色是一致的
