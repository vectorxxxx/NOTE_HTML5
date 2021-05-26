> 笔记来源：[尚硅谷Web前端HTML5&CSS3初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[TOC]

# 高度塌陷与BFC

## 1. 高度塌陷

在浮动布局中，父元素的高度默认是被子元素撑开的

当子元素浮动后，其会完全脱离文档流，子元素从文档流中脱离将会无法撑起父元素的高度，导致父元素的高度丢失

父元素高度丢失以后，其下的元素会自动上移，导致页面的布局混乱

![动画2021-41](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526231243.gif)

所以高度塌陷是浮动布局中比较常见的一个问题，这个问题我们必须要进行处理！

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526232333.jpg)

别急，我们接着往下看



## 2. BFC

BFC（Block Formatting Context）块级格式化环境

- BFC是一个CSS中的一个<mark>隐含的属性</mark>，可以为一个元素开启BFC
- 开启BFC该元素会变成一个<mark>独立的布局区域</mark>

元素开启BFC后的特点：

- <mark>不会被浮动元素覆盖</mark>
- <mark>父子元素外边距不会重叠</mark>
- <mark>可以包含浮动的元素</mark>

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526232518.jpg)

可以通过一些特殊方式来开启元素的BFC：

- 设置为<mark>浮动（不推荐）</mark>：很明显下方元素被覆盖了，总不能让所有元素都浮动吧

  ![动画2021-40](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526202924.gif)

- 设置为<mark>行内块元素（不推荐）</mark>：不再独占一行，宽度变了，同时与下方元素产生了一点空隙

  ![动画2021-39](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526203053.gif)

- 设置<mark>`overflow`为非`visible`值</mark>：既没有覆盖元素，也保持了独占一方的特性（保持了宽度），与下方元素也保持了最初的间隙

  常用的方式为元素设置`overflow:hidden`（`overflow:auto`也是ok的） 开启其BFC， 以使其可以包含浮动元素

  `overflow:scroll` 会有滚动条，可能并不需要的，所以不太推荐

  ![动画2021-38](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526203245.gif)
  
  不过，这种方式也存在一定问题，如下，`overflow`并没有完全清除div2布局上受到的影响
  
  ![动画2021-34](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526230525.gif)

**总结**

- 可以通过变成浮动元素，来防止自身被浮动元素覆盖（有点“以毒攻毒”那味了）
- 可以设置行内块，来防止自身及其他元素被浮动元素覆盖（如果说浮动是“独善其身”，那行内块就有点“兼济天下”的意思）
- 可以设置`overflow`属性，包含浮动元素（既“独善其身”，又“兼济天下”，但仍有缺陷）

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526232615.jpg)

![img](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526232716.jpg)

我们可以打开`Zeal`手册（《02-前端开发准备》有介绍），查看关于BFC的说明文档

![image-20210526210723927](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526210727.png)

打开`Block formatting context`模块后，可以看到有很多开启BFC的方式

![image-20210526210843339](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526210844.png)

我这里大概翻译了一下，并整理了一份表格，应该看起来更直观一点（有些概念因为还没有学习，翻译和理解有误的地方还望谅解）

| 元素或属性                                                   | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `<html>`                                                     | 文档根元素                                                   |
| <mark>`float: left`</mark><br/><mark>`float: right`</mark>   | 浮动元素（`float`不为`none`）                                |
| <mark>`position: absolut`</mark><br/><mark>`position: fixed`</mark> | 绝对定位元素                                                 |
| <mark>`display: inline-block`</mark>                         | 行内块元素                                                   |
| `display: table-cell`                                        | 表格单元，默认值                                             |
| `display: table-caption`                                     | 表格标题，默认值                                             |
| `display: table`<br/>`display: table-row`<br/>`display: table-row-group`<br/>`display: table-header-group`<br/>`display: table-footer-group`<br/>`display: inline-table` | 匿名的表格单元，分别是HTML表格、表行、表体、表头和表脚的默认值 |
| <mark>`overflow: hidden`</mark><br/><mark>`overflow: scroll`</mark><br/><mark>`overflow: auto`</mark> | `overflow`不为`visible`和`clip`的块元素                      |
| `display: flow-root`                                         |                                                              |
| `contain: layout`<br/>`contain: content`<br/>`contain: paint` |                                                              |
| `display: flex`<br/>`display: inline-flex`的直接子元素       | Flex项，如果它们本身既不是`flex`，也不是`grid`或`table`容器  |
| `display: grid`<br/>`display: inline-grid`的直接子元素       | Grid项，如果它们本身既不是`flex`，也不是`grid`或`table`容器  |
| `column-count`不为`auto`<br/>`column-width`不为`auto`        | Multicol容器，包含`column-count: 1`                          |
| `column-span: all`                                           | 应该总是创建一个新的格式化上下文，即使`column-span: all`元素不在multicol容器中 |

但是，注意不管哪种方式，多多少少都会有些隐患、缺陷或者说“副作用”

![image-20210526231648421](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526231649.png)



## 3. clear

我们这里设计三个兄弟元素，对前两个元素进行`float`的浮动属性设置，看下效果

![动画2021-36](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526221756.gif)

由于box1的浮动，导致box3位置上移也就是box3受到了box1浮动的影响，位置发生了改变（注意，这里文字并没有被覆盖，《09-浮动》一节说过浮动的特点，其中第7点就是“文字环绕”的问题）

![img](file:///C:\Users\Archimedes\Documents\Tencent Files\1402758731\Image\C2C\D946B8F36926DBC3A1C6CE68BFE8E716.jpg)

如果我们不希望某个元素因为其他元素浮动的影响而改变位置，可以通过`clear`属性来清除浮动元素对当前元素所产生的影响

`clear`作用：<mark>清除浮动元素对当前元素所产生的影响（本质是为元素添加一个`margin-top`属性，值由浏览器自动计算）</mark>

可选值：

- `left` 清除左侧浮动元素对当前元素的影响
- `right ` 清除右侧浮动元素对当前元素的影响
- `both` 清除两侧中影响较大一侧元素的影响（注意，这里不是同时清除两侧的影响）

![动画2021-37](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526221424.gif)



## 4. after伪元素

我们学习了上面知识后，了解了高度塌陷问题的解决方式，其中主要有

- 通过`overflow: hidden`等可以为元素开启BFC

  ![动画2021-35](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526233456.gif)

- 通过`clear: both`等可以清除浮动对元素产生的影响

  ![动画2021-33](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526233449.gif)

同时也了解到，这两种方式都有一定的弊端和隐患。那有没有一种更好的方式去解决高度塌陷的问题呢？

答案当然是：有！

![image-20210526233234635](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526233235.png)

我们直接上效果图

![动画2021-32](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526233904.gif)

**Q1：这里使用了一个伪元素选择器`::after`，那有人会问了，跟在box2下直接定义一个box3有什么区别呢？**

A：我们知道，网页的结构思想是：结构+表现+行为。在box2下直接定义一个box3，属于结构；而使用伪元素选择器，属于表现

而定义box3的目的是为了撑起box1的内容，属于表现，而不是结构，所以在css中定义`::after`更符合网页的编程思想

**Q2：为什么需要使用`display: block`呢？**

A：因为默认情况下，`::after`伪元素是一个行内元素，如果不转为块元素，将仍然撑不起box1的高度

![image-20210526235431125](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526235432.png)



## 补充：小技巧

1. 在vscode中，我们可以使用css选择器组合，快速生成div代码块

   ![image-20210526220551778](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210526220759.png)

2. 使用`alt + shift + ↑`或`alt + shift + ↓`快捷键，快速复制多行代码
