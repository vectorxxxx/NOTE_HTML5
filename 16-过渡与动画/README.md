> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# 过渡与动画

## 1、过渡

**过渡（transition）**

- 通过过渡可以指定一个属性发生变化时的切换方式
- 通过过渡可以创建一些非常好的效果，提升用户的体验

**属性值**

`transition-property`：指定要执行过渡的属性

- 多个属性间使用`,`隔开；
- 如果所有属性都需要过渡，则使用`all`关键字；
- 大部分属性都支持过渡效果；
- 注意过渡时必须是从一个有效数值向另外一个有效数值进行过渡；

`transition-duration`：指定过渡效果的持续时间

- 时间单位：s 和 ms（1s=1000ms）

`transition-delay`：过渡效果的延迟，等待一段时间后在执行过渡

`transition-timing-function`：过渡的时序函数

- `linear`匀速运动
- `ease` 默认值，慢速开始，先加速后减速
- `ease-in` 加速运动
- `ease-out` 减速运动
- `ease-in-out` 先加速后减速
- `cubic-bezier()`来指定时序函数 [https://cubic-bezier.com](https://cubic-bezier.com)
- `steps()`分步执行过渡效果，可以设置第二个值：
  - `end`，在时间结束时执行过渡（默认值）
  - `start`，在时间开始时执行过渡

`transition`：可以同时设置过渡相关的所有属性

- 只有一个要求，如果要写延迟，则两个时间中第一个是持续时间，第二个是延迟时间

**示例**

```css
/* transition: margin-left 2s 1s; */
transition-property: margin-left;
transition-duration: 2s;
transition-delay: 1s;
```

![transition](https://img-blog.csdnimg.cn/img_convert/7480db3e978d72b04b48e47351b2712a.gif)

**几种过渡效果对比**

`linear`匀速运动

```css
transition-timing-function: linear;
```

![linear](https://img-blog.csdnimg.cn/img_convert/db1e5c02804cfa5d8cfc03e84f465cc0.gif)

`ease` 默认值，慢速开始，先加速后减速

```css
transition-timing-function: ease;
```

![ease](https://img-blog.csdnimg.cn/img_convert/cc12a68d322c7f04647408b28e1a355b.gif)

`ease-in` 加速运动

```css
transition-timing-function: ease-in;
```

![ease-in](https://img-blog.csdnimg.cn/img_convert/e7e99280e1108793f8e0f681587c50fd.gif)

`ease-out` 减速运动

```css
transition-timing-function: ease-out;
```

![ease-out](https://img-blog.csdnimg.cn/img_convert/2c408e4fbec59ccbcf324b308d893ad9.gif)

`ease-in-out` 先加速后减速

```css
transition-timing-function: ease-in-out;
```

![ease-in-out](https://img-blog.csdnimg.cn/img_convert/a34bb617b70c57b8bdcdbba930315b82.gif)

`cubic-bezier()`来指定时序函数

```css
transition-timing-function: cubic-bezier(0.17, 1.79, 0.68, -0.69);
```

![cubic-bezier](https://img-blog.csdnimg.cn/img_convert/95be9a5c0834580690f63674754a5a5d.gif)

`steps()`分步执行过渡效果

```css
/* transition-timing-function: steps(2, end); */
transition-timing-function: steps(2);
```

![steps-end](https://img-blog.csdnimg.cn/img_convert/fad621042638ade6ffc1ca8ed7291524.gif)

```css
transition-timing-function: steps(2, start);
```

![steps-start](https://img-blog.csdnimg.cn/img_convert/eafa6e6574b7570eea4cbbd26bafe377.gif)

## 2、动画

动画和过渡类似，都是可以实现一些动态的效果，不同的是

- 过渡需要在某个属性发生变化时才会触发
- 动画可以自动触发动态效果

设置动画效果，必须先要设置一个**关键帧**，关键帧设置了动画执行每一个步骤

```css
@keyframes test {
  from {
    margin-left: 0;
  }

  to {
    margin-left: 900px;
  }
}
```

`animation-name` 指定动画的关键帧名称

`animation-duration`：指定动画效果的持续时间

`animation-delay`：动画效果的延迟，等待一段时间后在执行动画

`animation-timing-function`：动画的时序函数

`animation-iteration-count` 动画执行的次数

- `infinite` 无限执行

`animation-direction` 指定动画运行的方向

- `normal` 从`from`向`to`运行，每次都是这样，默认值
- `reverse` 从`to`向`from`运行，每次都是这样
- `alternate` 从`from`向`to`运行，重复执行动画时反向执行
- `alternate-reverse` 从`to`向`from`运行，重复执行动画时反向执行

`animation-play-state` 设置动画的执行状态

- `running` 动画执行，默认值
- `paused` 动画暂停

`animation-fill-mode` 动画的填充模式

- `none` 动画执行完毕，元素回到原来位置，默认值
- `forwards` 动画执行完毕，元素会停止在动画结束的位置
- `backwards` 动画延时等待时，元素就会处于开始位置
- `both` 结合了`forwards`和`backwards`

**示例**

```css
/* animation-name: test;
animation-duration: 2s;
animation-delay: 2s;
animation-timing-function: linear;
animation-iteration-count: infinite;
animation-direction: alternate;
animation-fill-mode: both; */

animation: test 2s 2s linear infinite alternate both;
```

![animation](https://img-blog.csdnimg.cn/img_convert/c81fb42fc5c22a36a108077fb3c388c7.gif)

## 3、实战

### 米兔

```css
.box {
  height: 271px;
  width: 132px;
  background-image: url("/assets/米兔/bigtap-mitu-queue-big.png");
  margin: 100px auto;
  transition: background-position 1s steps(4);
}

.box:hover {
  background-position: -528px 0;
}
```

![米兔](https://img-blog.csdnimg.cn/img_convert/cfcff3ec2765beff571c95c8af08b20d.gif)

### 奔跑的少年

```css
.box {
  height: 256px;
  width: calc(1536px / 6);
  background-image: url("/assets/奔跑的少年/bg2.png");
  margin: 100px auto;
  animation: run 1s steps(6) infinite;
}

/* 关键帧 */
@keyframes run {
  from {
    background-position: 0 0;
  }

  to {
    background-position: -1536px 0;
  }
}
```

![奔跑的少年](https://img-blog.csdnimg.cn/img_convert/c78e2ab5980c340bc4ee76e3229c8292.gif)

### 弹力球

```css
.outer {
  width: 100%;
  height: 700px;
  border-bottom: 10px solid #000;
  /* 外边距重叠，开启BFC */
  overflow: hidden;
}

.ball {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background-color: gray;
  animation: bounce 6s ease-in;
}

@keyframes bounce {
  from {
    margin-top: 0;
  }

  5%,
  15%,
  25%,
  35%,
  45%,
  55%,
  65%,
  75%,
  85%,
  95%,
  98%,
  to {
    margin-top: 600px;
    animation-timing-function: ease-out;
  }

  10%,
  20%,
  30%,
  40%,
  50%,
  60%,
  70%,
  80%,
  90% {
    animation-timing-function: ease-in;
  }

  10% {
    margin-top: 60px;
  }

  20% {
    margin-top: 120px;
  }

  30% {
    margin-top: 180px;
  }

  40% {
    margin-top: 240px;
  }

  50% {
    margin-top: 300px;
  }

  60% {
    margin-top: 360px;
  }

  70% {
    margin-top: 420px;
  }

  80% {
    margin-top: 480px;
  }

  90% {
    margin-top: 540px;
  }

  96% {
    margin-top: 580px;
  }

  99% {
    margin-top: 590px;
  }
}
```

![弹力球](https://img-blog.csdnimg.cn/img_convert/52d7d87ae591a78eba76a51b14903865.gif)

### 酷炫球

```css
div {
  float: left;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  animation: bounce 0.5s infinite ease-in alternate;
}

.ball1 {
  background-color: red;
  animation-delay: 0.1s;
}

.ball2 {
  background-color: yellow;
  animation-delay: 0.2s;
}

.ball3 {
  background-color: green;
  animation-delay: 0.3s;
}

.ball4 {
  background-color: blue;
  animation-delay: 0.4s;
}

.ball5 {
  background-color: pink;
  animation-delay: 0.5s;
}

.ball6 {
  background-color: orange;
  animation-delay: 0.6s;
}

.ball7 {
  background-color: fuchsia;
  animation-delay: 0.7s;
}

.ball8 {
  background-color: gray;
  animation-delay: 0.8s;
}

.ball9 {
  background-color: darkcyan;
  animation-delay: 0.9s;
}

.ball10 {
  background-color: indigo;
  animation-delay: 1s;
}

.ball11 {
  background-color: black;
  animation-delay: 1.1s;
}

.ball12 {
  background-color: darkcyan;
  animation-delay: 1.2s;
}

.ball13 {
  background-color: darkkhaki;
  animation-delay: 1.3s;
}

.ball14 {
  background-color: brown;
  animation-delay: 1.4s;
}

.ball15 {
  background-color: mediumpurple;
  animation-delay: 1.5s;
}

@keyframes bounce {
  from {
    margin-top: 0;
  }

  to {
    margin-top: 500px;
  }
}
```

![酷炫球](https://img-blog.csdnimg.cn/img_convert/d50aebb593aefa2d94e62fcbaf49f37c.gif)
