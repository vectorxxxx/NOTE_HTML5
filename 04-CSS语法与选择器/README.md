> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# CSS 语法与选择器

## 1. CSS 简介

### 层叠样式表

网页实际上是一个多层的结构，通过 CSS 可以分别为网页的每一个层来设置样式，而最终我们能看到只是网页的最上边一层

总之一句话，CSS 用来设置网页中元素的样式

使用 CSS 来修改元素样式的方式大致可以分为 3 种

### 内联样式（行内样式）

在标签内部通过`style`属性来设置元素的样式

```html
<p style="color:red;font-size:60px;">内联样式（行内样式）</p>
```

问题：使用内联样式，样式只能对一个标签生效。如果希望影响到多个元素，必须在每一个元素中都复制一遍；并且当样式发生变化时，我们必须要一个一个的修改，非常的不方便。（注意：开发时绝对不要使用内联样式）

### 内部样式表

将样式编写到`head`中的`style`标签里然后通过 css 的选择器来选中元素并为其设置各种样式可以同时为多个标签设置样式，并且修改时只需要修改一处即可。内部样式表更加方便对样式进行复用

```css
<style>
p{
    color:green;
    font-size:50px;
}
</style>
```

问题：我们的内部样式表只能对一个网页起作用，它里边的样式不能跨页面进行复用

### 外部样式表

可以将 css 样式编写到一个外部的 CSS 文件中，然后通过`link`标签来引入外部的 CSS 文件

```html
<link rel="stylesheet" href="./style.css" />
```

外部样式表需要通过`link`标签进行引入，意味着只要想使用这些样式的网页都可以对其进行引用使样式，可以在不同页面之间进行<mark>复用</mark>

将样式编写到外部的 CSS 文件中，可以使用到浏览器的<mark>缓存机制，从而加快网页的加载速度</mark>，提高用户的体验。

## 2. CSS 基本语法

### 注释

#### css 中的注释

只能使用`/*`和`*/`包裹。即不管是单行注释，还是多行注释，都是以`/*`开头，以`*/`结尾

```css
/* css中的单行注释 */

/* 
css中的多行注释
css中的多行注释
css中的多行注释
*/
```

我们对比下其他几种前端语言的注释

#### html 中的注释

只能使用`<!--`和`-->`包裹。即不管是单行注释，还是多行注释，都是以`<!--`开头，以`-->`结尾

```html
<!-- html中的单行注释 -->

<!-- 
html中的多行注释
html中的多行注释
html中的多行注释
-->
```

#### JS(JavaScript)和 JQuery 中的注释

单行注释使用`//`。多行注释使用`/*`和`*/`包裹，以`<!--`开头，以`-->`结尾

```js
/* JS(JavaScript)和JQuery中的单行注释*/

/*
JS(JavaScript)和JQuery中的多行注释
JS(JavaScript)和JQuery中的多行注释
JS(JavaScript)和JQuery中的多行注释
*/
```

### 基本语法

`选择器 声明块`

#### 选择器

通过选择器可以选中页面中的指定元素

- 比如`p`的作用就是选中页面中所有的`p`元素声明块

#### 声明块

通过声明块来指定要为元素设置的样式

- 声明块由一个一个的声明组成，声明是一个名值对结构

- 一个样式名对应一个样式值，名和值之间以`:`连接，以`;`结尾

```css
h1 {
  color: green;
}
```

## 3. CSS 选择器

### 通配选择器（Universal selector）

- 作用：选中页面中的所有元素
- 语法：`*`
- 例子：`*{}`

```css
* {
  color: red;
}
```

### 元素选择器（Type selector）

也叫类型选择器、标签选择器

- 作用：根据标签名来选中指定的元素
- 语法：`elementname{}`
- 例子：`p{}` `h1{}` `div{}`

```css
p {
  color: red;
}

h1 {
  color: green;
}
```

### 类选择器（Class selector）

- 作用：根据元素的 class 属性值选中一组元素
- 语法：`.classname`
- 例子：`.blue{}`

```css
.blue {
  color: blue;
}
.size {
  font-size: 20px;
}
```

`class`是一个标签的属性，它和`id`类似，不同的是`class`

- 可以重复使用，
- 可以通过`class`属性来为元素分组，
- 可以同时为一个元素指定多个`class`属性

```html
<p class="blue size">类选择器（Class selector）</p>
```

### ID 选择器（ID selector）

- 作用：根据元素的`id`属性值选中一个元素
- 语法：`#idname{}`
- 例子：`#box{}` `#red{}`

```css
#red {
  color: red;
}
```

### 属性选择器（Attribute selector）

- 作用：根据元素的属性值选中一组元素
- 语法 1：`[属性名]` 选择含有指定属性的元素
- 语法 2：`[属性名=属性值]` 选择含有指定属性和属性值的元素
- 语法 3：`[属性名^=属性值]` 选择属性值以指定值开头的元素
- 语法 4：`[属性名$=属性值]` 选择属性值以指定值结尾的元素
- 语法 5：`[属性名*=属性值]` 选择属性值中含有某值的元素
- 例子：`p[title]{}` `p[title=e]{}` `p[title^=e]{}` `p[title$=e]{}` `p[title*=e]{}`

```css
p[title] {
  color: orange;
}
p[title="e"] {
  color: orange;
}
p[title^="e"] {
  color: orange;
}
p[title$="e"] {
  color: orange;
}
p[title*="e"] {
  color: orange;
}
```

## 4. 复合选择器

### 交集选择器

- 作用：选中同时复合多个条件的元素
- 语法：`选择器1选择器2选择器3选择器n{}`
- 注意点：交集选择器中如果有元素选择器，必须使用元素选择器开头

```css
div.red {
  font-size: 30px;
}

.a.b.c {
  color: blue;
}
```

### 并集选择器（选择器分组）

- 作用：同时选择多个选择器对应的元素
- 语法：`选择器1,选择器2,选择器3,选择器n{}`
- 例子：`#b1,.p1,h1,span,div.red{}`

```css
h1,
span {
  color: green;
}
```

## 5. 关系选择器

- <mark>父元素</mark>：直接包含子元素的元素叫做父元素
- <mark>子元素</mark>：直接被父元素包含的元素是子元素
- <mark>祖先元素</mark>：直接或间接包含后代元素的元素叫做祖先元素；一个元素的父元素也是它的祖先元素
- <mark>后代元素</mark>：直接或间接被祖先元素包含的元素叫做后代元素；子元素也是后代元素
- <mark>兄弟元素</mark>：拥有相同父元素的元素是兄弟元素

### 子元素选择器（Child combinator）

- 作用：选中指定父元素的指定子元素
- 语法：`父元素 > 子元素`
- 例子：`A > B`

```css
div.box > p > span {
  color: orange;
}
```

### 后代元素选择器（Descendant combinator）

- 作用：选中指定元素内的指定后代元素
- 语法：`祖先 后代`
- 例子：`A B`

```css
div span {
  color: skyblue;
}
```

### 兄弟元素选择器（Sibling combinator）

- 作用：选择下一个兄弟
- 语法：`前一个 + 下一个` `前一个 + 下一组`
- 例子 1：`A1 + A2`（Adjacent sibling combinator）
- 例子 2： `A1 ~ An`（General sibling combinator）

```css
p + span {
  color: red;
}

p ~ span {
  color: red;
}
```

## 6. 伪类选择器

伪类（不存在的类，特殊的类）

伪类用来描述一个元素的特殊状态，比如：第一个子元素、被点击的元素、鼠标移入的元素.…

伪类一般情况下都是使用`:`开头

- <mark>`:first-child`</mark> 第一个子元素
- <mark>`:last-child`</mark> 最后一个子元素
- <mark>`:nth-child()`</mark> 选中第 n 个子元素
  - n：第 n 个，n 的范围 0 到正无穷
  - 2n 或 even：选中偶数位的元素
  - 2n+1 或 odd：选中奇数位的元素

以上这些伪类都是根据所有的子元素进行排序的

- <mark>`:first-of-type`</mark> 同类型中的第一个子元素
- <mark>`:last-of-type`</mark> 同类型中的最后一个子元素
- <mark>`:nth-of-type()`</mark> 选中同类型中的第 n 个子元素

这几个伪类的功能和上述的类似，不同点是他们是在同类型元素中进行排序的

- <mark>`:not()`</mark>否定伪类，将符合条件的元素从选择器中去除

```css
/* ul下所有li，黑色 */
ul > li {
  color: black;
}

/* ul下第偶数个li，黄色 */
ul > li:nth-child(2n) {
  color: yellow;
}

/* ul下第奇数个li，绿色 */
ul > li:nth-child(odd) {
  color: green;
}

/* ul下第一个li，红色 */
ul > li:first-child {
  color: red;
}

/* ul下最后一个li，黄色 */
ul > li:last-child {
  color: orange;
}
```

![image-20210516162703966](https://img-blog.csdnimg.cn/img_convert/3373666820269df4830e7827c7b9623b.png)

- <mark>`:link`</mark> 未访问的链接
- <mark>`:visited`</mark> 已访问的链接
  - 由于隐私的原因，所以`visited`这个伪类只能修改链接的颜色
- <mark>`:hover`</mark> 鼠标悬停的链接
- <mark>`:active`</mark> 鼠标点击的链接

```css
/* unvisited link */
a:link {
  color: red;
}

/* visited link */
a:visited {
  color: yellow;
}

/* mouse over link */
a:hover {
  color: green;
}

/* selected link */
a:active {
  color: blue;
}
```

![动画2021-5-8](https://img-blog.csdnimg.cn/img_convert/afda6908ddd6c7e9cab45751aabbcb5c.gif)

## 7. 伪元素选择器

伪元素，表示页面中一些特殊的并不真实的存在的元素（特殊的位置）

伪元素使用`::`开头

- <mark>`::first-letter`</mark> 表示第一个字母
- <mark>`::first-line`</mark> 表示第一行
- <mark>`::selection`</mark> 表示选中的内容
- <mark>`::before`</mark> 元素的开始
- <mark>`::after`</mark> 元素的最后
- <mark>`::before`和`::after`</mark> 必须结合`content`属性来使用

```css
/* 段落首字母设置大小为30px */
p::first-letter {
  font-size: 30px;
}

/* 段落第一行设置为黄色背景 */
p::first-line {
  background-color: yellow;
}

/* 段落选中的部分变绿色 */
p::selection {
  background-color: green；;
}

/* div前加上内容 */
div::before {
  content: "BEFORE";
  color: red;
}

/* div后加上内容 */
div::after {
  content: "AFTER";
  color: blue;
}
```

![动画2021-5-7](https://img-blog.csdnimg.cn/img_convert/d00bc5df427763fc326a624449e0eec2.gif)

## 8. CSS Dinner 游戏

官方地址：[CSS Diner - Where we feast on CSS Selectors!](https://flukeout.github.io/)

CSS Dinner 是一个帮助初学者快速熟悉 css 各种选择器的网页游戏

![](https://img-blog.csdnimg.cn/img_convert/3655328d85f103c4981afb3105ca3538.png)
