> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# 变形：平移、旋转与缩放

变形就是指通过 css 来改变元素的形状或位置

变形不会影响到页面的布局

`transform`用来设置元素的变形效果

## 1、平移

- `translateX()` 沿着由方向平移
- `translateY()` 沿着 y 轴方向平移
- `translateZ()` 沿着 z 轴方向平移平移元素

百分比是相对于自身计算的

**几种水平垂直双方向居中的方式对比**

1. 绝对定位的方式

   ```css
   /* 这种居中方式，只适用于元素的大小确定 */
   position: absolute;
   top: 0;
   left: 0;
   bottom: 0;
   right: 0;
   margin: auto;
   ```

2. `table-cell`的方式

   ```css
   /* table-cell的方式具有一定局限性 */
   display: table-cell;
   vertical-align: middle;
   text-align: center;
   ```

3. `transform`的方式

   ```css
   /* transform变形平移的方式 */
   position: absolute;
   left: 50%;
   top: 50%;
   transform: translateX(-50%) translateY(-50%);
   ```

### 浮出效果

```css
div {
  float: left;
  width: 200px;
  height: 300px;
  background-color: silver;
  margin: 100px 50px auto 50px;
  transition: all 0.3s;
}

div:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  transform: translateY(-5px);
}
```

![浮出效果](https://img-blog.csdnimg.cn/img_convert/241b88c09dcb68952c07cc88a7d68f26.gif)

## 2、Z 轴平移

z 轴平移，调整元素在 z 轴的位置，正常情况就是调整元素和人眼之间的距离，距离越大，元素离人越近

z 轴平移属于立体效果（近大远小），默认情况下网页是不支持透视，如果需要看见效果必须要设置网页的视距

### 透视效果

```css
html {
  background-color: rgb(71, 44, 32);
  perspective: 800px;
}

.box {
  width: 200px;
  height: 300px;
  background-color: silver;
  margin: 100px auto;
  transition: all 0.3s;
}

.box:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  transform: translateZ(200px);
}
```

![透视效果](https://img-blog.csdnimg.cn/img_convert/7a257398286736e1e216f16e808ad651.gif)

## 3、旋转

通过旋转可以使元素沿着 x、y 或 z 旋转指定的角度

- `rotateX()`
- `rotateY()`
- `rotateZ()`

```css
/* transform: rotateY(0.5turn); */
transform: rotateY(180deg);
```

![旋转效果](https://img-blog.csdnimg.cn/img_convert/d68844170ec937f3d811eff8d6e5200e.gif)

## 4、缩放

对元素进行缩放的函数

- `scalex()` 水平方向缩放
- `scaleY()` 垂直方向缩放
- `scale()` 双方向的缩放

```css
.box {
  height: 200px;
  width: 200px;
  background-color: #bfa;
  margin: 200px auto;
  transition: 2s;
}

.box:hover {
  /* transform: scaleX(2); */
  /* transform: scaleY(2); */
  transform: scale(2);
  /* 变形的原点 */
  transform-origin: 0 0;
}
```

![变形原点](https://img-blog.csdnimg.cn/img_convert/b24a8805bd538d5a520c0e68b7e52e5a.gif)

## 5、实战

### 鸭子表

**html 代码**

```html
<div class="clock">
  <div class="hour-wrapper">
    <div class="hour"></div>
  </div>
  <div class="minute-wrapper">
    <div class="minute"></div>
  </div>
  <div class="second-wrapper">
    <div class="second"></div>
  </div>
</div>
```

**css 代码**

```css
.clock {
  width: 500px;
  height: 500px;
  background-image: url("assets/鸭子表/clock.png");
  background-image: url("assets/鸭子表/clock_duck.jpg");
  background-size: cover;
  margin: 100px auto;
  position: relative;
}

.clock > div {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
}

.clock > div > div {
  height: 50%;
  margin: 0 auto;
}

/* 时针 */
.hour-wrapper {
  height: 60%;
  width: 60%;
  animation: clock-run 720s infinite;
}

.hour {
  width: 8px;
  background-color: black;
}

/* 分针 */
.minute-wrapper {
  height: 75%;
  width: 75%;
  animation: clock-run 60s steps(60) infinite;
}

.minute {
  width: 4px;
  background-color: black;
}

/* 秒针 */
.second-wrapper {
  height: 90%;
  width: 90%;
  animation: clock-run 1s steps(60) infinite;
}

.second {
  width: 2px;
  background-color: red;
}

@keyframes clock-run {
  from {
    transform: rotateZ(0);
  }

  to {
    transform: rotateZ(360deg);
  }
}
```

![鸭子表](https://img-blog.csdnimg.cn/img_convert/4fb02c061aeac2234f492f24026a0ea7.gif)

### 复仇者联盟

html 代码

```html
<div class="cube">
  <div class="surface1"></div>
  <div class="surface2"></div>
  <div class="surface3"></div>
  <div class="surface4"></div>
  <div class="surface5"></div>
  <div class="surface6"></div>
</div>
```

css 代码

```css
html {
  perspective: 800px;
}

.cube {
  height: 200px;
  width: 200px;
  margin: 200px auto;
  position: relative;
  /* 设置3d变形效果 */
  transform-style: preserve-3d;
  animation: cube-rotate 12s infinite linear;
}

.cube div {
  height: 200px;
  width: 200px;
  background-size: cover;
  position: absolute;
  top: 0;
  left: 0;
  /* 为元素设置透明效果 */
  opacity: 0.85;
}

.surface1 {
  background-image: url("/assets/复仇者联盟/1.jpg");
  transform: translateX(-100px) rotateY(90deg);
}

.surface2 {
  background-image: url("/assets/复仇者联盟/2.jpg");
  transform: translateX(100px) rotateY(90deg);
}

.surface3 {
  background-image: url("/assets/复仇者联盟/3.jpg");
  transform: translateY(-100px) rotateX(90deg);
}

.surface4 {
  background-image: url("/assets/复仇者联盟/4.jpg");
  transform: translateY(100px) rotateX(90deg);
}

.surface5 {
  background-image: url("/assets/复仇者联盟/5.jpg");
  transform: translateZ(-100px);
}

.surface6 {
  background-image: url("/assets/复仇者联盟/6.jpg");
  transform: translateZ(100px);
}

@keyframes cube-rotate {
  from {
    transform: rotateX(0) rotateY(0) rotateZ(0);
  }

  to {
    transform: rotateX(1turn) rotateY(2turn) rotateZ(3turn);
  }
}
```

![复仇者联盟](https://img-blog.csdnimg.cn/img_convert/a00ee8c59dd8e4bf7ac14286be0ccd3d.gif)
