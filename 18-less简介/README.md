> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# less 简介

`less`是一门`css`的预处理语言

- `less`是一个 css 的增强版，通过`less`可以编写更少的代码实现更强大的样式
- 在`less`中添加了许多的新特性：像对变量的支持、对`mixin`的支持...
- `less`的语法大体上和`css`语法一致，但是`less`中增添了许多对`css`的扩展，所以浏览器无法直接执行`less`代码，要执行必须向将`less`转换为`css`，然后再由浏览器执行

## 1、安装插件

在`vscode`中搜索`less`，点击`安装`

![image-20210626203546217](https://img-blog.csdnimg.cn/img_convert/7649e0d4d1ad3f9179fecb8642287ad0.png)

## 2、编写 less

**html 代码**

使用快捷方式创建`html`代码

![image-20210626204018016](https://img-blog.csdnimg.cn/img_convert/f992f8225262f1355df4628586602a87.png)

`回车`生成`html`代码

```html
<div class="box1"></div>
<div class="box2"></div>
<div class="box3"></div>
```

**less 代码**

创建`style.less`文件，编写`less`代码

```less
body {
  --height: calc(200px / 2);
  --width: 100px;
  div {
    height: var(--height);
    width: var(--width);
  }
  .box1 {
    background-color: #bfa;
  }
  .box2 {
    background-color: red;
  }
  .box3 {
    background-color: yellow;
  }
}
```

`Easy LESS`插件会帮助我们在`style.less`所在目录下面生成一个相同名称的`css`文件

![image-20210626204312658](https://img-blog.csdnimg.cn/img_convert/201068ea2c14019210172db470a04934.png)

查看生成的`style.css`代码

```css
body {
  --height: calc(200px / 2);
  --width: 100px;
}
body div {
  height: var(--height);
  width: var(--width);
}
body .box1 {
  background-color: #bfa;
}
body .box2 {
  background-color: red;
}
body .box3 {
  background-color: yellow;
}
```

我们直接在 HTML 中引入生成的`style.css`

```html
<link rel="stylesheet" href="/css/style.css" />
```

运行代码，查看效果

![image-20210626204502781](https://img-blog.csdnimg.cn/img_convert/97f40a1f8f76041202ac4ef693ad5b36.png)

## 3、less 语法

### less 注释

`less`中的单行注释，注释中的内容不会被解析到`css`中

`css`中的注释，内容会被解析到`css`文件中

```less
// `less`中的单行注释，注释中的内容不会被解析到`css`中

/*
`css`中的注释，内容会被解析到`css`文件中
*/
```

### 父子关系嵌套

在`less`中，父子关系可以直接嵌套

```less
// `less`中的单行注释，注释中的内容不会被解析到`css`中

/*
`css`中的注释，内容会被解析到`css`文件中
*/
body {
  --height: calc(200px / 2);
  --width: 100px;
  div {
    height: var(--height);
    width: var(--width);
  }
  .box1 {
    background-color: #bfa;
    .box2 {
      background-color: red;
      .box3 {
        background-color: yellow;
      }
      > .box4 {
        background-color: green;
      }
    }
  }
}
```

对应的`css`

```css
/*
`css`中的注释，内容会被解析到`css`文件中
*/
body {
  --height: calc(200px / 2);
  --width: 100px;
}
body div {
  height: var(--height);
  width: var(--width);
}
body .box1 {
  background-color: #bfa;
}
body .box1 .box2 {
  background-color: red;
}
body .box1 .box2 .box3 {
  background-color: yellow;
}
body .box1 .box2 > .box4 {
  background-color: green;
}
```

### 变量

变量，在变量中可以存储一个任意的值

并且我们可以在需要时，任意的修改变量中的值

变量的语法：`@变量名`

- 直接使用使用变量时，则以`@变量名`的形式使用即可
- 作为类名、属性名或者一部分值使用时，必须以`@{变量名}`的形式使用
- 可以在变量声明前就使用变量（可以但不建议）

```less
@b1:box1;
@b2:box2;
@b3:box3;
@size:200px;
@bc:background-color;
@bi:background-image;
@color:red;
@path:image/a/b/c;

.@{b1}{
  width: @size;
  height: $width;
  @{bc}: @color;
  @{bi}: url("@{path}/1.png");
}

.@{b2}{
  width: @size;
  height: $width;
  @{bc}: @color;
  @{bi}: url("@{path}/2.png");
}

.@{b3}{
  width: @size;
  height: $width;
  @{bc}: @color;
  @{bi}: url("@{path}/3.png");
}
```

生成的`css`代码

```css
.box1 {
  width: 200px;
  height: 200px;
  background-color: red;
  background-image: url("image / a / b / c/1.png");
}
.box2 {
  width: 200px;
  height: 200px;
  background-color: red;
  background-image: url("image / a / b / c/2.png");
}
.box3 {
  width: 200px;
  height: 200px;
  background-color: red;
  background-image: url("image / a / b / c/3.png");
}
```

<mark>注意：在`url`中使用`less`语法需要用引号包裹</mark>

### 其他

```less
.p1 {
  width: @size;
  height: $width;
  &-wrapper {
    background-color: peru;
  }
  // &:hover{
  //   background-color: blue;
  // }
  :hover {
    background-color: blue;
  }
}
.p2:extend(.p1) {
  color: @color;
}
.p3 {
  .p1();
}
.p4() {
  width: @size;
  height: $width;
}
.p5 {
  // .p4();
  .p4;
}
```

生成的`css`代码

```css
.p1,
.p2 {
  width: 200px;
  height: 200px;
}
.p1-wrapper {
  background-color: peru;
}
.p1 :hover {
  background-color: blue;
}
.p2 {
  color: red;
}
.p3 {
  width: 200px;
  height: 200px;
}
.p5 {
  width: 200px;
  height: 200px;
}
```

- `&` 拼接
- 伪元素
- `:extend()` 对当前选择器扩展指定选择器的样式（选择器分组）
- `.p1()` 直接对指定的样式进行引用，这里就相当于将`p1`的样式在这里进行了复制（`mixin` 混合）
- 使用类选择器时可以在选择器后边添加一个括号，这时我们实际上就创建了一个`mixins`混合函数

## 4、混合函数

在混合函数中可以直接设置变量，并且可以指定默认值

```less
.test(@w:200px, @h:100px, @bc:red) {
  width: @w;
  height: @h;
  background-color: @bc;
}

.p6 {
  // .test(200px, 100px, red); // 对应参数位传值
  // .test(@h:200px,@w:100px,@bc:red); // 写明对应属性，可变换顺序
  // .test();
  .test(300px);
}
```

生成的`css`代码

```css
.p6 {
  width: 300px;
  height: 100px;
  background-color: red;
}
```

### 其他

- `average`混合函数

  ```less
  .h1 {
    color: average(red, yellow);
  }
  ```

  生成的`css`代码

  ```css
  .h1 {
    color: #ff8000;
  }
  ```

- `darken`混合函数

  ```less
  body {
    background-color: darken(#bfa, 50%);
  }
  ```

  生成的`css`代码

  ```css
  body {
    background-color: #22aa00;
  }
  ```

## 5、补充

创建`all.less`文件，将我们之前编写的`less`文件通过`@import`引入进来

可以通过`import`来将其他的`less`引入到当前的`less`中

```less
@import "style.less";
@import "syntax.less";
```

查看生成的`all.css`代码，会发现其他的内容囊括了两个`less`文件的内容

所以，我们可以利用`@import`来对`less`文件进行整合，然后引入生成的`css`文件使用即可

这样，每次修改的时候直接对某个模块的`less`文件进行修改，就会非常简单

如果我们观察过之前`fontawesome`源码文件，会发现其中也有`less`代码文件

![image-20210626222450991](https://img-blog.csdnimg.cn/img_convert/71b255aafaccb595fc0341c50f6a3fa0.png)

不同的`less`文件里都有其自己的`职责`，如

- `_animated.less`中专门存放动画的混合函数
- `_variables.less`中专门存放定义的变量
- ...

但是也有个问题，通过`F12`调试时显示的也是`css`中对应的行号

![image-20210626223208492](https://img-blog.csdnimg.cn/img_convert/dcc8dac7e284d8f1f296455dd302d7a6.png)

如果我们要改，需要找一下，太麻烦了，能不能直接显示`less`中行号呢？这样我们直接定位到对应`less`中直接进行修改，维护起来也会比较方便

我们需要在`Easy LESS`插件中修改`settings.json`文件，在其中添加如下配置

```json
"less.compile": {
    "compress": true, // true => remove surplus whitespace
    "sourceMap": true, // true => generate source maps (.css.map files)
    "out": true // false => DON'T output .css files (overridable per-file, see below)
}
```

修改完毕后，会发现多生成出来一个`all.css.map`文件，说明配置生效

![image-20210626224441979](https://img-blog.csdnimg.cn/img_convert/288677124cd646d938430db12c32efbe.png)

再刷新下页面，通过`F12`会发现变成了`less`文件对应的行号

![image-20210626223858712](https://img-blog.csdnimg.cn/img_convert/781253b1659517f6dcf08697930b8e6d.png)

我们来逐一解释下配置的`less.compile`项中每一个属性的含义

- `compress` 生成的`css`文件代码会被压缩（作用相当于我们之前安装的`JS & CSS Minifier (Minify)`插件的效果）
- `sourceMap` 生成`.css.map`文件，通过`F12`可以查看了`less`文件对应行号
- `out` 生成对应`css`文件（当然是需要了）
