> 笔记来源：[尚硅谷Web前端HTML5&CSS3初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[TOC]

# 变形：平移与旋转

变形就是指通过css来改变元素的形状或位置

变形不会影响到页面的布局

`transform`用来设置元素的变形效果

## 1、平移

- `translateX()` 沿着由方向平移
- `translateY()` 沿着y轴方向平移
- `translateZ()` 沿着z轴方向平移平移元素

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
    transition: all .3s;
}

div:hover {
    box-shadow: 0 0 10px rgba(0, 0, 0, .2);
    transform: translateY(-5px);
}
```

![浮出效果](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210623221313.gif)



## 2、Z轴平移

z轴平移，调整元素在z轴的位置，正常情况就是调整元素和人眼之间的距离，距离越大，元素离人越近

z轴平移属于立体效果（近大远小），默认情况下网页是不支持透视，如果需要看见效果必须要设置网页的视距

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
    transition: all .3s;
}

.box:hover {
    box-shadow: 0 0 10px rgba(0, 0, 0, .2);
    transform: translateZ(200px);
}
```

![透视效果](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210623222027.gif)



## 3、旋转

通过旋转可以使元素沿着x、y或z旋转指定的角度

- `rotateX()`
- `rotateY()`
- `rotateZ()`

```css
/* transform: rotateY(0.5turn); */
transform: rotateY(180deg);
```

![旋转效果](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210623224457.gif)
