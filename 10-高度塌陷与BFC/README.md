> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# 高度塌陷与 BFC

## 1. 高度塌陷

在浮动布局中，父元素的高度默认是被子元素撑开的

当子元素浮动后，其会完全脱离文档流，子元素从文档流中脱离将会无法撑起父元素的高度，导致父元素的高度丢失

父元素高度丢失以后，其下的元素会自动上移，导致页面的布局混乱

![动画2021-41](https://img-blog.csdnimg.cn/img_convert/79ace51ec70494c5917ac3d27ff5329b.gif)

所以高度塌陷是浮动布局中比较常见的一个问题，这个问题我们必须要进行处理！

![img](https://img-blog.csdnimg.cn/img_convert/11a161357960e3308e5d889ca6c60eba.png)

别急，我们接着往下看

## 2. BFC

BFC（Block Formatting Context）块级格式化环境

- BFC 是一个 CSS 中的一个<mark>隐含的属性</mark>，可以为一个元素开启 BFC
- 开启 BFC 该元素会变成一个<mark>独立的布局区域</mark>

元素开启 BFC 后的特点：

- <mark>不会被浮动元素覆盖</mark>
- <mark>父子元素外边距不会重叠</mark>
- <mark>可以包含浮动的元素</mark>

![img](https://img-blog.csdnimg.cn/img_convert/428820832a6f375b1cda617fde8453b8.png)

可以通过一些特殊方式来开启元素的 BFC：

- 设置为<mark>浮动（不推荐）</mark>：很明显下方元素被覆盖了，总不能让所有元素都浮动吧

  ![动画2021-40](https://img-blog.csdnimg.cn/img_convert/a38cbf9ed8239821e3a9467190cbf1fa.gif)

- 设置为<mark>行内块元素（不推荐）</mark>：不再独占一行，宽度变了，同时与下方元素产生了一点空隙

  ![动画2021-39](https://img-blog.csdnimg.cn/img_convert/7558d16d4432a5069baf896fc023505f.gif)

- 设置<mark>`overflow`为非`visible`值</mark>：既没有覆盖元素，也保持了独占一方的特性（保持了宽度），与下方元素也保持了最初的间隙

  常用的方式为元素设置`overflow:hidden`（`overflow:auto`也是 ok 的） 开启其 BFC， 以使其可以包含浮动元素

  `overflow:scroll` 会有滚动条，可能并不需要的，所以不太推荐

  ![动画2021-38](https://img-blog.csdnimg.cn/img_convert/ca62f230f7f5767c0888734ed36ead36.gif)

  不过，这种方式也存在一定问题，如下，`overflow`并没有完全清除 div2 布局上受到的影响

  ![动画2021-34](https://img-blog.csdnimg.cn/img_convert/3c81ef620cbd90f54bc1023f38967e8b.gif)

**总结**

- 可以通过变成浮动元素，来防止自身被浮动元素覆盖（有点“以毒攻毒”那味了）
- 可以设置行内块，来防止自身及其他元素被浮动元素覆盖（如果说浮动是“独善其身”，那行内块就有点“兼济天下”的意思）
- 可以设置`overflow`属性，包含浮动元素（既“独善其身”，又“兼济天下”，但仍有缺陷）

![img](https://img-blog.csdnimg.cn/img_convert/b4e408068ab82a6ecab73a1fbc25f9b5.png)

![img](https://img-blog.csdnimg.cn/img_convert/6d2288432ad5b7031581962a1d9afbdd.png)

我们可以打开`Zeal`手册（《02-前端开发准备》有介绍），查看关于 BFC 的说明文档

![image-20210526210723927](https://img-blog.csdnimg.cn/img_convert/a4df090e5a9a297c2c7b07e1b5251306.png)

打开`Block formatting context`模块后，可以看到有很多开启 BFC 的方式

![image-20210526210843339](https://img-blog.csdnimg.cn/img_convert/715774f89f4902f61e44de7a23f8f1d7.png)

我这里大概翻译了一下，并整理了一份表格，应该看起来更直观一点（有些概念因为还没有学习，翻译和理解有误的地方还望谅解）

| 元素或属性                                                                                                                                                               | 说明                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| `<html>`                                                                                                                                                                 | 文档根元素                                                                       |
| <mark>`float: left`</mark><br/><mark>`float: right`</mark>                                                                                                               | 浮动元素（`float`不为`none`）                                                    |
| <mark>`position: absolut`</mark><br/><mark>`position: fixed`</mark>                                                                                                      | 绝对定位元素                                                                     |
| <mark>`display: inline-block`</mark>                                                                                                                                     | 行内块元素                                                                       |
| `display: table-cell`                                                                                                                                                    | 表格单元，默认值                                                                 |
| `display: table-caption`                                                                                                                                                 | 表格标题，默认值                                                                 |
| `display: table`<br/>`display: table-row`<br/>`display: table-row-group`<br/>`display: table-header-group`<br/>`display: table-footer-group`<br/>`display: inline-table` | 匿名的表格单元，分别是 HTML 表格、表行、表体、表头和表脚的默认值                 |
| <mark>`overflow: hidden`</mark><br/><mark>`overflow: scroll`</mark><br/><mark>`overflow: auto`</mark>                                                                    | `overflow`不为`visible`和`clip`的块元素                                          |
| `display: flow-root`                                                                                                                                                     |                                                                                  |
| `contain: layout`<br/>`contain: content`<br/>`contain: paint`                                                                                                            |                                                                                  |
| `display: flex`<br/>`display: inline-flex`的直接子元素                                                                                                                   | Flex 项，如果它们本身既不是`flex`，也不是`grid`或`table`容器                     |
| `display: grid`<br/>`display: inline-grid`的直接子元素                                                                                                                   | Grid 项，如果它们本身既不是`flex`，也不是`grid`或`table`容器                     |
| `column-count`不为`auto`<br/>`column-width`不为`auto`                                                                                                                    | Multicol 容器，包含`column-count: 1`                                             |
| `column-span: all`                                                                                                                                                       | 应该总是创建一个新的格式化上下文，即使`column-span: all`元素不在 multicol 容器中 |

但是，注意不管哪种方式，多多少少都会有些隐患、缺陷或者说“副作用”

![image-20210526231648421](https://img-blog.csdnimg.cn/img_convert/54a3b91bf3738e16dc8d60c506924d20.png)

## 3. clear

我们这里设计三个兄弟元素，对前两个元素进行`float`的浮动属性设置，看下效果

![动画2021-36](https://img-blog.csdnimg.cn/img_convert/6285eef0e0e5defcaef2925ec2b85696.gif)

由于 box1 的浮动，导致 box3 位置上移也就是 box3 受到了 box1 浮动的影响，位置发生了改变（注意，这里文字并没有被覆盖，《09-浮动》一节说过浮动的特点，其中第 7 点就是“文字环绕”的问题）

![img](https://img-blog.csdnimg.cn/img_convert/29f0b07925ee64e09181cca348316db7.png)

如果我们不希望某个元素因为其他元素浮动的影响而改变位置，可以通过`clear`属性来清除浮动元素对当前元素所产生的影响

`clear`作用：<mark>清除浮动元素对当前元素所产生的影响（本质是为元素添加一个`margin-top`属性，值由浏览器自动计算）</mark>

可选值：

- `left` 清除左侧浮动元素对当前元素的影响
- `right ` 清除右侧浮动元素对当前元素的影响
- `both` 清除两侧中影响较大一侧元素的影响（注意，这里不是同时清除两侧的影响）

![动画2021-37](https://img-blog.csdnimg.cn/img_convert/7b3a3be80af3b924c768f14d1feef532.gif)

## 4. after

我们学习了上面知识后，了解了高度塌陷问题的解决方式，其中主要有

- 通过`overflow: hidden`等可以为元素开启 BFC

  ![动画2021-35](https://img-blog.csdnimg.cn/img_convert/2a64a7f4d7361b89342ad40eabb82710.gif)

- 通过`clear: both`等可以清除浮动对元素产生的影响

  ![动画2021-33](https://img-blog.csdnimg.cn/img_convert/296eed7a83250499d08f2fbaa1b3291f.gif)

同时也了解到，这两种方式都有一定的弊端和隐患。那有没有一种更好的方式去解决高度塌陷的问题呢？

答案当然是：有！

![image-20210526233234635](https://img-blog.csdnimg.cn/img_convert/9d32694d81d9cc615113bfd6de3b2a45.png)

我们直接上效果图

![动画2021-32](https://img-blog.csdnimg.cn/img_convert/ac9d8de28e765aa3612db88e0e3665ab.gif)

**Q1：这里使用了一个伪元素选择器`::after`，那有人会问了，跟在 box2 下直接定义一个 box3 有什么区别呢？**

A：我们知道，网页的结构思想是：结构+表现+行为。在 box2 下直接定义一个 box3，属于结构；而使用伪元素选择器，属于表现

而高度塌陷问题属于表现问题，定义 box3 的目的是为了撑起 box1 的内容，属于表现，而不是结构，所以在 css 中定义`::after`更符合网页的编程思想

**Q2：为什么需要使用`display: block`呢？**

A：因为默认情况下，`::after`伪元素是一个行内元素，如果不转为块元素，将仍然撑不起 box1 的高度

![image-20210526235431125](https://img-blog.csdnimg.cn/img_convert/38df19f0100616bfd366757a2df68018.png)

## 5. clearfix

我们在前面《06-盒模型》一节中说过垂直布局中边距重叠的问题：相邻的垂直方向外边距会发生重叠现象

![动画2021-30](https://img-blog.csdnimg.cn/img_convert/ba545f805064146c3744634c3a18d6cc.gif)

如上图所示，子元素设置了一个`margin-top`之后，父元素跟随子元素一起进行了移动

即我们之前说的<q>父子元素间相邻外边距，子元素会传递给父元素（上外边距）</q>

聪明的小伙伴已经想到了，用刚才说的伪元素选择器啊

![img](https://img-blog.csdnimg.cn/img_convert/ce282bce62e362e18faf2d65c90b08b3.gif)

好，我们先来看下效果

![动画2021-29](https://img-blog.csdnimg.cn/img_convert/d03986dc25481fafe66233a5c5470ef6.gif)

貌似是没有任何变化，到底是什么地方不对呢？

![img](https://img-blog.csdnimg.cn/img_convert/09fd881a8713a5541ab547fa10bcea10.png)

我们再来回顾下使用`after`伪元素的心路历程：

- 使用无内容的 box3 撑起 box1 ==》表现代替结构（`::after`代替 box3）
- `clear`清除浮动对元素产生的影响（还记得`clear`的原理么？）

![img](https://img-blog.csdnimg.cn/img_convert/9bd752f3fdd37c33a292b5fccd1f2b8f.png)

其实就是给元素设置了一个`margin-top`属性，不过这个在开发者工具中是看不到的

既然如此，就相当于在 box2 下面添加一个 box3，然后给 box3 设置一个`margin-top`属性

到此为止，

∵ <q>相邻的垂直方向外边距</q> 这个条件仍然满足

∴ <q>会发生重叠现象</q>这个结论也依然成立

具体点就是，<q>父子元素间相邻外边距，子元素会传递给父元素（上外边距）</q>，表现为 box1 和 box2 同步往下移动

那我们应该怎么做才能解决这个问题？ ~~凭你们朴素的情感，应该怎么判？~~ 当然就是让上述条件不满足呗！

怎么能够不满足？当然是让两个元素垂直外边距不相邻啊！

好，多说无益，我们直接上代码看效果！

![动画2021-28](https://img-blog.csdnimg.cn/img_convert/87eab6edc155de046c6841b0586ba336.gif)

我们用了`before`伪元素选择器，目的当然是让 box1 和 box2 的外边距不相邻，但是好像并没有效果

我们再换成`display: inline-block`属性看看

![动画2021-27](https://img-blog.csdnimg.cn/img_convert/b5a137926b68526aff7ad926c032fe98.gif)

好像是解决了父元素布局的问题，但是子元素怎么还往下跑了一段距离？ ~~是谁给的勇气？~~

因为`inline-block`兼顾行内元素和块元素的特点，既可以设置宽高也不独占一行

在没有设置宽高时，会存在一个默认高度，所以`inline-block`仍然行不通

还有一个属性，`display: table`

![动画2021-26](https://img-blog.csdnimg.cn/img_convert/7999d34a5a577908d59299abb852fe35.gif)

Bingo！实现了我们最终想要的效果

**Q1：为什么没有使用 clear 属性？**

A：不是说了吗？`clear`是为了清除浮动对布局的影响，我们现在没有浮动的元素啊，我们要讨论的也不是浮动的问题

**Q2：display 不是还有一个`none`属性么，为什么不用呢？**

A：`none`属性是不占据位置，但是也不能让元素相邻的外边距分离啊

**Q3：为什么`table`值就可以呢？**

A：这个问题问的非常好，算是问到点上了！我们上面在讲开启 BFC 的一些方法的时候，也提到了该属性。而且，应该牢记的是，元素开启 BFC 后的其中一个特点就是 <q><mark>父子元素外边距不会重叠</mark></q>。当然，这里也需要合理选择伪元素选择器，使其外边距不相邻才行

另外，总结一下：

- 高度塌陷问题，一般用`::after`
- 外边距重叠问题，一般用`::before`

不知道到这里，大家能不能想明白这两件事情

![img](https://img-blog.csdnimg.cn/img_convert/ca42dae38fd9f042dc0fb3640a1489a9.png)

那么问题来了，有没有一个两全其美的办法，既可以解决高度塌陷，又可以解决外边距重叠呢？

![img](https://img-blog.csdnimg.cn/img_convert/0819d9f0a70423ba3116ab56c728cda3.png)

当然有！`clearfix` 这个样式就可以同时解决高度塌陷和外边距重叠的问题

当你在遇到这些问题时，直接使用`clearfix`这个类即可，他就可以帮你轻松搞定 css 中的两大难题

```css
.clearfix::before,
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

其中`.clearfix::before`是为了解决外边距重叠问题

```css
.clearfix::before {
  content: "";
  display: table;
}
```

`.clearfix::after`是为了解决高度塌陷问题

```css
.clearfix::after {
  content: "";
  display: table;
  clear: both;
}
```

两者合在一起，就可以完美地解决高度塌陷和外边距重叠这两大“世纪难题”了

![image-20210528030932616](https://img-blog.csdnimg.cn/img_convert/f93beec8c02faaf177b44418a7edcb24.png)
