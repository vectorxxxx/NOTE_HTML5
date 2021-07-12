> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# 字符实体与语义标签

## 1. 字符实体

有些时候，在 HTML 中不能直接书写一些特殊符号，如：

- 多个连续的空格（在网页中编写的多个空格默认情况会自动被浏览器解析为一个空格）
- 比如字母两侧的大于小于号（可能会被认为是标签并解析）

如果我们需要在网页中书写这些特殊的符号，则需要使用 html 中的实体（转义字符）实体的语法：`&实体的名字;`，如：

| 实体名称              | 显示结果 | 描述     |
| :-------------------- | :------- | -------- |
| <mark>`&nbsp;`</mark> | ` `      | 空格     |
| <mark>`&gt;`</mark>   | >        | 大于号   |
| <mark>`&lt;`</mark>   | <        | 小于号   |
| <mark>`&amp;`</mark>  | &        | 与       |
| `&copy;`              | ©        | 版权     |
| `&reg;`               | ®        | 注册商标 |
| `&trade;`             | ™        | 商标     |
| `&times;`             | ×        | 乘号     |
| `&divide;`            | ÷        | 除号     |
| `&iquest;`            | ¿        | 倒问号   |

更多的字符实体，可参考：[HTML 字符实体](https://www.w3school.com.cn/html/html_entities.asp)、[HTML ISO-8859-1 参考手册](https://www.w3school.com.cn/charsets/ref_html_8859.asp)

## 2. meta 标签

以京东网站为例，右键单击，选择`查看网页源代码`

![image-20210514225741114](https://img-blog.csdnimg.cn/img_convert/855d9e0cd0c8ed56c78869e22744fc8d.png)

```html
<meta charset="utf8" version="1" />
<meta
  name="viewport"
  content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes"
/>
<meta
  name="description"
  content="京东JD.COM-专业的综合网上购物商城,销售家电、数码通讯、电脑、家居百货、服装服饰、母婴、图书、食品等数万个品牌优质商品.便捷、诚信的服务，为您提供愉悦的网上购物体验!"
/>
<meta
  name="Keywords"
  content="网上购物,网上商城,手机,笔记本,电脑,MP3,CD,VCD,DV,相机,数码,配件,手表,存储卡,京东"
/>
```

meta 主要用于设置网页中的一些元数据，元数据并不是给用户看的

- <mark>charset</mark> ：指定网页的字符集

- <mark>name</mark> ：指定的数据的名称

  - <mark>keywords</mark>：表示网站的关键字，可以同时指定多个关键字，关键字间使用`,`隔开

  - <mark>description</mark>：表示网站的描述信息

    ![image-20210514230338273](https://img-blog.csdnimg.cn/img_convert/3730201c7f36c90a23f8683d8e8b1cc4.png)

- <mark>content</mark> ：指定的数据的内容，会作为搜索结果的超链接上的文字显示

打开 Zeal 手册（前端开发准备中做过介绍）

![image-20210514230900103](https://img-blog.csdnimg.cn/img_convert/69244610084684cb6f8d3fc544a7dd03.png)

发现除了`charset`、`name`、`content`之外，还有一个叫<mark>`http-equiv`</mark>的属性

```html
If the http-equiv attribute is set, the <meta /> element is a pragma directive,
providing information equivalent to what can be given by a similarly-named HTTP
header.
```

如果设置了`http-equiv`属性，`<meta>`元素就是一个 pragma 指令，提供的信息相当于一个类似名称的 HTTP 头所能提供的信息。

点击`http-equiv`的链接，查看其更详细信息。

![image-20210514231126506](https://img-blog.csdnimg.cn/img_convert/03688356f8a9847bfe15f80fe5405bd0.png)

- `content-security-policy`：允许页面作者为当前页面定义一个<mark>内容策略</mark>。内容策略主要指定允许的服务器来源和脚本端点，这有助于防范跨站脚本攻击。
- `content-type`：声明文档的<mark>MIME 类型和字符编码</mark>。如果指定，content 属性必须有 "`text/html; charset=utf-8` "的值。这相当于一个指定了 charset 属性的`<meta>`元素，并对文档中的位置有同样的限制。注意：只能在使用`text/html`的文档中使用，不能在使用 XML MIME 类型的文档中使用。
- `default-style`：设置默认的 CSS 样式表集的名称。
- `x-ua-compatible`： 如果指定，内容属性必须有 "`IE=edge `"的值。用户代理被要求忽略这个 pragma。
- <mark>`refresh`</mark>：该指令指定页面重新加载及重定向的方式
  - 直到页面应该被重新加载的秒数--只有当 content 属性包含一个正整数时。
  - 直到页面重定向到另一个页面的秒数--只有当内容属性包含一个正整数，后面跟着字符串'`;url=`'，以及一个有效的 URL。

其中我们直接将 Examples 中的示例代码加入 Demo.html 中

```html
<meta charset="utf-8" />
<!-- Redirect page after 3 seconds -->
<meta http-equiv="refresh" content="3;url=https://www.mozilla.org" />
```

对`refresh`进行测试，发现过了 3 秒钟之后自动跳转到了指定的网站

![sxx2l-rwqq5](https://img-blog.csdnimg.cn/img_convert/fbaddeed5f4a1ad02d91e063200140bf.gif)

## 3. 语义标签

在网页中 HTML 专门用来负责网页的结构所以在使用 html 标签时，应该关注的是标签的语义，而不是它的样式

这里先介绍几个基本的语义标签，还有些常用的标签放在后面具体讲解

|                             | 标签                                                                                                                                        | 作用   | 描述                                                                                                                                                                                                                  |
| --------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ | :----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 块元素<br/>Block Element    | <mark>`<h1>`</mark><br/><mark>`<h2>`</mark><br/><mark>`<h3>`</mark><br/><mark>`<h4>`</mark><br/><mark>`<h5>`</mark><br/><mark>`<h6>`</mark> | 标题   | 一共有六级标题<br/>从`h1` ~ `h6`重要性递减，`h1`最重要，`h6`最不重要<br/>h1 在网页中的重要性仅次于`title`标签<br/>一般情况下一个页面中只会有一个`h1`<br/>一般情况下标题标签只会使用到`h1` ～ `h3`，`h4` ～ `h6`很少用 |
|                             | `<hgroup>`                                                                                                                                  | 标题组 | 多层次的标题。它将一组`<h1>` ～ `<h6>`元素分组                                                                                                                                                                        |
|                             | <mark>`<p>`</mark>                                                                                                                          | 段落   | 页面中的一个段落。由空行或第一行缩进将相邻的文本块分开                                                                                                                                                                |
|                             | `<blockquote>`                                                                                                                              | 短引文 | 用缩进表示所包含文本。<br/>可以用`cite`属性表示引文来源，用`<cite>`元素表示来源的文本表述                                                                                                                             |
| 行内元素<br/>Inline Element | `<q>`                                                                                                                                       | 长引文 | 用一个简短的内联引号包围文本。<br/>大多数浏览器通过在文本周围加上引号来实现。<br/>该元素用于不需要段落分隔的短引文；                                                                                                  |
|                             | <mark>`<br>`</mark>                                                                                                                         | 换行   |                                                                                                                                                                                                                       |
|                             | `<em>`                                                                                                                                      | 强调   | 表示强调作用。`<em>`元素可以嵌套，每一级嵌套表示更高的强调程度<br/><mark>`<i>`</mark>元素效果与它相同，不过`<i>`不属于语义标签                                                                                        |
|                             | `<strong>`                                                                                                                                  | 重要   | 表示重要性、严肃性或紧迫性。浏览器通常以粗体字呈现内容<br/><mark>`<b>`</mark>元素效果与它相同，不过`<b>`不属于语义标签                                                                                                |

**举例**

```html
<h1>Beetles</h1>
<h2>External morphology</h2>
<h3>Head</h3>
<h4>Mouthparts</h4>
<h3>Thorax</h3>
<h4>Prothorax</h4>
<h4>Pterothorax</h4>
```

**效果**

![image-20210515212349676](https://img-blog.csdnimg.cn/img_convert/f1b33334fe6d180469fa616c3c083196.png)

HTML5 提供的新语义元素有

| 标签                    | 作用                         | 描述                                                                                               |
| :---------------------- | :--------------------------- | -------------------------------------------------------------------------------------------------- |
| <mark>`<header>`</mark> | 页眉                         | 介绍性的内容                                                                                       |
| <mark>`<footer>`</mark> | 页脚                         | 通常包含有关作者的信息、版权或文件链接                                                             |
| <mark>`<nav>`</mark>    | 导航链接                     | 可以是当前文档内的，也可以是到其他文档的。常见例子是菜单、目录和索引                               |
| <mark>`<main>`</mark>   | 文档主内容                   | 中心主题直接相关或扩展的内容                                                                       |
| `<article>`             | 文章                         | 自成一体，独立分发，可重复使用                                                                     |
| `<section>`             | 文档中的节                   | 没有一个更具体的语义元素来代表                                                                     |
| <mark>`<aside>`</mark>  | 页面内容以外的内容           | 其内容与文档的主要内容只有间接的关系。经常以边栏或呼出框的形式出现                                 |
| <mark>`<mark>`</mark>   | 重要或强调的文本             | 为参考或记事目的而被标记或突出的文本，表明其相关性和重要性                                         |
| `<summary>`             | `<details>` 标题             | 为`<details>`指定一个摘要、标题或图例。点击`<summary>`可以切换`<details>`打开和关闭                |
| `<details>`             | 用户能够查看或隐藏的额外细节 | 其中的信息只有被切换到 "打开 "状态时才可见。必须使用`<summary>`提供一个摘要或标签                  |
| `<figure>`              | 自包含内容                   | 独立的内容，用`<figcaption>`元素指定一个可选的标题。比如图示、图表、照片、代码清单等               |
| `<figcaption>`          | `<figure>` 的标题            | 描述其父元素<figure>其余内容的标题或图例                                                           |
| `<time>`                | 定义日期/时间                | 可能包括`datetime`属性，将日期翻译成机器可读的格式，以便获得更好的搜索引擎结果或自定义功能。如提醒 |

这些新语义标签在视觉效果上基本上没有什么区别

## 4. 块元素与行内元素

### 块元素（block element）

- 在网页中一般通过块元素来对页面进行布局

### 行内元素（inline element）

- 行内元素主要用来包裹文字
- 一般情况下会在块元素中放行内元素，而不会在行内元素中放块元素
  - 如`<p>`元素中不能放任何的块元素，不过

## 5. 内容修正

浏览器在解析网页时，会自动对网页中不符合规范的内容进行修正，比如：

- 标签写在了根元素的外部
- `<p>`元素中嵌套了块元素
- 根元素中出现了除`head`和`body`以外的子元素

这个通过浏览器中的`查看网页源代码`并不能看到效果，但是使用 F12 进行`开发者调试`时是能够看到上述几种情况被修正的结果。

不过虽然浏览器能够对不规范的页面内容进行修正，还是不建议编写不规范的代码，因为这对后期代码维护或团队代码协作将是非常不好的后果和体验。

## 6. 布局标签

**结构化语义标签**

- `header`表示网页的头部（页眉）
- `main`表示网页的主体部分（一个页面中只会有一个 main）
- `footer`表示网页的底部（页脚）
- `nav`表示网页中的导航
- `aside`和主体相关的其他内容（侧边栏）
- `article`表示一个独立的文章
- `section`表示一个独立的区块，上边的标签都不能表示时使用 section

![HTML5 语义元素](https://img-blog.csdnimg.cn/img_convert/62350db5fc5eae4fd6366e0bbb2aa645.png)

- `div` 块元素，没有任何的语义，就用来表示一个区块。目前来讲，div 还是主要的布局元素
- `span` 行内元素，没有任何的语义，一般用于在网页中`选中文字`

## 7. 列表

在 html 中可以创建列表，html 列表一共有三种：

- 有序列表，使用`ol`标签来创建有序列表，使用`li`表示列表项

  ```html
  <ol>
    <li>Mix flour, baking powder, sugar, and salt.</li>
    <li>In another bowl, mix eggs, milk, and oil.</li>
    <li>Stir both mixtures together.</li>
    <li>Fill muffin tray 3/4 full.</li>
    <li>Bake for 20 minutes.</li>
  </ol>
  ```

  ![image-20210515212835770](https://img-blog.csdnimg.cn/img_convert/915dad2f463cb462375242c8d04768ca.png)

- 无序列表，使用`ul`标签来创建无序列表，使用`li`表示列表项

  ```html
  <ul>
    <li>Milk</li>
    <li>
      Cheese
      <ul>
        <li>
          Blue cheese
          <ul>
            <li>Sweet blue cheese</li>
            <li>Sour blue cheese</li>
          </ul>
        </li>
        <li>Feta</li>
      </ul>
    </li>
  </ul>
  ```

  ![image-20210515213301387](https://img-blog.csdnimg.cn/img_convert/1e16701ac02ef44c0dca2129a0eaa417.png)

  可以看出，列表元素之间是可以互相嵌套的

- 定义列表，使用`dl`标签来创建定义列表，使用`dt`表示定义的内容，使用`dd`来对内容进行解释说明

  ```html
  <dl>
    <dt>Beast of Bodmin</dt>
    <dd>A large feline inhabiting Bodmin Moor.</dd>

    <dt>Morgawr</dt>
    <dd>A sea serpent.</dd>

    <dt>Owlman</dt>
    <dd>A giant owl-like creature.</dd>
  </dl>
  ```

  ![image-20210515212936773](https://img-blog.csdnimg.cn/img_convert/80de044f3bf4c7b61a381ff842cd2645.png)

## 8. 超链接

超链接可以让我们从一个页面跳转到其他页面，或者是当前页面的其他的位置

使用`a`标签来定义超链接，`href`属性指定跳转的目标路径，值可以是一个外部网站的地址，也可以写一个内部页面的地址

超链接是也是一个行内元素，在`a`标签中可以嵌套除它自身外的任何元素

### 外部地址

- <q>Linking to an absolute URL</q>：链接一个绝对路径
- <q>Linking to an email address</q>：链接一个 email 地址
- <q>Linking to telephone numbers</q>：链接电话号码
- <q>Using the download attribute to save a `<canvas>` as a PNG</q>：下载图片

```html
<ul>
  <li><a href="https://www.baidu.com">Website</a></li>
  <li><a href="mailto:example@outlook.com">Email</a></li>
  <li><a href="tel:+123456789">Phone</a></li>
</ul>
```

**效果**

![动画2021-5-15](https://img-blog.csdnimg.cn/img_convert/b1b0efbb5dc40fdaca6e6ea45510846f.gif)

### 内部地址

当我们需要跳转一个服务器内部的页面时，一般我们都会使用相对路径，会以`./`或`../`开头

- `./` 表示当前文件所在目录，可以省略不写
- `../`表示当前文件所在目录的上一级目录

```html
<a href="./test1.html">超链接1</a><br />
<a href="../test2.html">超链接2</a><br />
<a href="./test3/test3.html">超链接3</a><br />
<a href="../test4/test4.html">超链接4</a>
```

**效果**

![动画2021-5-11](https://img-blog.csdnimg.cn/img_convert/612bdcda740f7f6ffa49b1618c5bdfdc.gif)

### 新建页面

`target`属性，用来指定超链接打开的位置可选值：

- `_self`在当前页面中打开超链接，默认值
- `_blank`在新建页面中打开超链接

```html
<a href="./test1.html">超链接1——默认</a><br />
<a href="./test1.html" target="_self">超链接1——当前页面</a><br />
<a href="./test1.html" target="_blank">超链接1——新建页面</a><br />
```

![动画2021-5-10](https://img-blog.csdnimg.cn/img_convert/4cac9b988ae5b78fd1db1ab1fea2078b.gif)

### 锚点跳转

可以使用`javascript:void(0);`来作为`href`的属性，此时点击这个超链接什么也不会发生

可以将`#`作为超链接的路径的占位符使用。

可以直接将超链接的`href`属性设置为`#`，这样点击超链接以后页面不会发生跳转，而是转到当前页面的顶部的位置

可以跳转到页面的指定位置（锚点），只需将`href`属性设置`#目标元素的id属性值`（唯一不重复）

```html
<p>汉皇重色思倾国，御宇多年求不得。</p>
<p>杨家有女初长成，养在深闺人未识。</p>
<p>天生丽质难自弃，一朝选在君王侧。</p>
<p><a id="Anchor1" href="#Anchor2"> 回眸一笑百媚生，六宫粉黛无颜色。</a></p>
<p>春寒赐浴华清池，温泉水滑洗凝脂。</p>
<p>侍儿扶起娇无力，始是新承恩泽时。</p>
<p>云鬓花颜金步摇，芙蓉帐暖度春宵。</p>
<p>春宵苦短日高起，从此君王不早朝。</p>
<p>承欢侍宴无闲暇，春从春游夜专夜。</p>
<p><a id="Anchor2" href="#Anchor3"> 后宫佳丽三千人，三千宠爱在一身。</a></p>
<p>金屋妆成娇侍夜，玉楼宴罢醉和春。</p>
<p>姊妹弟兄皆列土，可怜光彩生门户。</p>
<p>遂令天下父母心，不重生男重生女。</p>
<p>骊宫高处入青云，仙乐风飘处处闻。</p>
<p>缓歌慢舞凝丝竹，尽日君王看不足。</p>
<p>渔阳鼙鼓动地来，惊破霓裳羽衣曲。</p>
<p>九重城阙烟尘生，千乘万骑西南行。</p>
<p>翠华摇摇行复止，西出都门百余里。</p>
<p>六军不发无奈何，宛转蛾眉马前死。</p>
<p>花钿委地无人收，翠翘金雀玉搔头。</p>
<p>君王掩面救不得，回看血泪相和流。</p>
<p>黄埃散漫风萧索，云栈萦纡登剑阁。</p>
<p>峨嵋山下少人行，旌旗无光日色薄。</p>
<p>蜀江水碧蜀山青，圣主朝朝暮暮情。</p>
<p>行宫见月伤心色，夜雨闻铃肠断声。</p>
<p>天旋地转回龙驭，到此踌躇不能去。</p>
<p>马嵬坡下泥土中，不见玉颜空死处。</p>
<p>君臣相顾尽沾衣，东望都门信马归。</p>
<p>归来池苑皆依旧，太液芙蓉未央柳。</p>
<p>芙蓉如面柳如眉，对此如何不泪垂。</p>
<p>春风桃李花开夜，秋雨梧桐叶落时。</p>
<p>西宫南苑多秋草，落叶满阶红不扫。</p>
<p>梨园弟子白发新，椒房阿监青娥老。</p>
<p>夕殿萤飞思悄然，孤灯挑尽未成眠。</p>
<p><a id="Anchor3" href="#Anchor4"> 迟迟钟鼓初长夜，耿耿星河欲曙天。 </a></p>
<p>鸳鸯瓦冷霜华重，翡翠衾寒谁与共。</p>
<p>悠悠生死别经年，魂魄不曾来入梦。</p>
<p>临邛道士鸿都客，能以精诚致魂魄。</p>
<p>为感君王辗转思，遂教方士殷勤觅。</p>
<p>排空驭气奔如电，升天入地求之遍。</p>
<p>上穷碧落下黄泉，两处茫茫皆不见。</p>
<p>忽闻海上有仙山，山在虚无缥渺间。</p>
<p>楼阁玲珑五云起，其中绰约多仙子。</p>
<p>中有一人字太真，雪肤花貌参差是。</p>
<p>金阙西厢叩玉扃，转教小玉报双成。</p>
<p>闻道汉家天子使，九华帐里梦魂惊。</p>
<p>揽衣推枕起徘徊，珠箔银屏迤逦开。</p>
<p>云鬓半偏新睡觉，花冠不整下堂来。</p>
<p><a id="Anchor4" href="#Anchor5"> 风吹仙袂飘飖举，犹似霓裳羽衣舞。 </a></p>
<p>玉容寂寞泪阑干，梨花一枝春带雨。</p>
<p>含情凝睇谢君王，一别音容两渺茫。</p>
<p>昭阳殿里恩爱绝，蓬莱宫中日月长。</p>
<p>回头下望人寰处，不见长安见尘雾。</p>
<p>惟将旧物表深情，钿合金钗寄将去。</p>
<p>钗留一股合一扇，钗擘黄金合分钿。</p>
<p>但令心似金钿坚，天上人间会相见。</p>
<p>临别殷勤重寄词，词中有誓两心知。</p>
<p>七月七日长生殿，夜半无人私语时。</p>
<p><a id="Anchor5" href="#Anchor6"> 在天愿作比翼鸟，在地愿为连理枝。 </a></p>
<p>天长地久有时尽，此恨绵绵无绝期。</p>

<!-- Heading to link to -->
<a href="#">回到顶部</a>
```

**效果**

![动画2021-5-14](https://img-blog.csdnimg.cn/img_convert/e522bb59afcc1c08e24081f0f8fe0304.gif)

## 9. 图片

图片标签用于向当前页面中引入一个外部图片

`img`标签是一个自结束标签，这种元素属于替换元素（块和行内元素之间，具有两种元素的特点）

**属性**

- `src`：属性指定的是外部图片的路径（路径规则和超链接是一样的）
- `alt`：图片的描述，这个描述默认情况下不会显示，有些浏览器会在图片无法加载时显示，搜索引擎会根据 alt 中的内容来识别图片
- `width`：图片的宽度（单位是像素）
- `height` ：图片的高度（单位是像素）
- 宽度和高度中如果只修改了一个，则另一个会等比例缩放

**注意**

- 一般情况在 pc 端，不建议修改图片的大小，需要多大的图片就裁多大
- 但是在移动端，经常需要对图片进行缩放（大图缩小）

**举例**

```html
<img
  src="https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002416.png"
  alt="蒂姆·伯纳斯·李爵士，万维网的发明人"
/>
<img
  src="https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514233853.gif"
  alt="结构、表现、行为"
/>
```

**效果**

![image-20210515233449533](https://img-blog.csdnimg.cn/img_convert/f5833d8d3eda58ef6dd16955604238a7.png)

### 图片格式

#### jpeg（jpg）

- 支持的颜色比较丰富
- 不支持透明效果
- 不支持动图
- 一般用来显示照片

#### gif

- 支持的颜色比较单一
- 支持简单透明
- 支持动图

#### png

- 支持的颜色丰富
- 支持复杂透明
- 不支持动图
- 专为网页而生

#### webp

- 这种格式是谷歌新推出的专门用来表示网页中的图片的一种格式
- 具备其他图片格式的所有优点，而且文件还特别的小
- 缺点：兼容性不好

#### base64

- 将图片使用 base64 编码，这样可以将图片转换为字符，通过字符的形式来引入图片

  ```html
  <img
    width="300"
    src="data:image/png;base64,AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAxVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zda/P9qhPz/mKr9/7bC/f/Fz/7/ydL+/8HM/v+tu/3/jaH9/156/P8zV/z/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/z9h/P+gsP3/8fP+/////////////////////////////////////////////////+ru/v+Zqv3/PV/8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P9lgPz/6+/+///////////////////////////////////////////////////////////////////////s7/7/Y378/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/aoT8//r6/v///////////////////////v7+/+Po/v/R2f7/y9T+/9rg/v/3+f7////////////////////////////j6P7/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/0Zm/P/w8/7/////////////////5+v+/4ab/f9AYvz/MVX8/zFV/P8xVfz/MVX8/zVY/P9kf/z/tsP9//39/v////////////T2/v8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/sL79/////////////////87W/v8/Yfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/ZYD8//L0/v//////n7D9/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/0Bh/P/6+/7////////////v8v7/QmP8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/TWz8/3GJ/P8yVvz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/e5L8/////////////////5qr/f8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P+mtv3/////////////////XHn8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/7/L/f////////////////87Xfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/ydL+////////////+/v+/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P/Ezv7////////////9/f7/M1b8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/7G//f////////////////9HZ/z/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/kqX9/////////////////22H/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P9kf/z/////////////////pbX9/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zRX/P/v8v7////////////s7/7/Nln8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/6Ky/f////////////////+Inf3/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/RWb8//f4/v////////////H0/v9Kafz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/PV/8/1Jw/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/kKT9/////////////////9vh/v9DZPz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/1Fv/P/m6/7//v7+/3aO/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8zVvz/xM79/////////////////+fr/v9viPz/MVX8/zFV/P8xVfz/MVX8/zRX/P+Emf3/8/X+////////////xc/+/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P87Xfz/ztf+///////////////////////i5/7/sL79/5+w/f+ywP3/6u3+//////////////////////+uvP3/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P83Wvz/sL79//7+/v//////////////////////////////////////////////////////3OL+/0Vl/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/aYP8/9Pb/v//////////////////////////////////////9fb+/5yu/f84W/z/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/1d0/P+Spf3/t8T9/8fR/v/Dzv7/qrn9/3uS/P88Xvz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/MVX8/zFV/P8xVfz/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA="
  />
  ```

  图片格式的选择

- 图片效果一样的，选文件小的
- 图片效果不一样的，选图片效果好的
- 尽可能的兼顾和平衡图片效果和文件大小

## 10. 内联格式

内联框架`iframe`，用于向当前页面中引入一个其他页面，

- `src`指定要引入的网页的路径
- `frameborder`指定内联框架的边框

**举例**

```html
<iframe
  src="https://www.qq.com"
  width="800"
  height="600"
  frameborder="0"
></iframe>
```

**效果**

![image-20210516001417802](https://img-blog.csdnimg.cn/img_convert/eb3a46bfa5df9d15306c7cc3b9cb81a8.png)

## 11. 音视频

### 音频

`audio`标签用来向页面中引入一个外部的音频文件

音视频文件引入时，默认情况下不允许用户自己控制播放停止

**属性**：

- `controls`是否允许用户控制播放
- `autoplay`音频文件是否自动播放
  - 如果设置了`autoplay`，则音乐在打开页面时会自动播放
  - 但是目前来讲大部分浏览器都不会自动对音乐进行播放
- `loop`音乐是否循环播放

```html
<audio src="./source/audio.mp3" controls autoplay loop></audio>
```

![image-20210516002915651](https://img-blog.csdnimg.cn/img_convert/9ef64b24a0e8cd8e43ebd8b261919ca6.png)

### source

除了通过`src`属性来指定外部文件的路径以外，还可以通过`<source>`元素来指定文件的路径

```html
<audio controls autoplay loop>
  对不起，您的浏览器不支持播放音频！请升级浏览器！
  <source src="./source/audio.mp3" />
  <source src="./source/audio.ogg" />
</audio>
```

IE11 下，能够正常播放

![image-20210516004453236](https://img-blog.csdnimg.cn/img_convert/b5e863093973646c1e3bbbce16baaba0.png)

IE8 下，出现我们自定义的提示信息

![image-20210516005054543](https://img-blog.csdnimg.cn/img_convert/f11c3ab9ce3128eed193328a5256b8dc.png)

### embed

IE8 下不支持`audio`元素，但是可以使用 `<embed>` 元素在文档中的指定位置嵌入外部内容。

这个内容是由外部应用程序或其他互动内容的来源提供的，如浏览器插件。

```html
<embed src="./source/audio.mp3" />
```

![image-20210516005207428](https://img-blog.csdnimg.cn/img_convert/5f54ccbb70bced3e23e549d4e2fbe2b6.png)

### 视频

使用`video`标签来向网页中引入一个视频，使用方式和`audio`基本上是一样的

```html
<video controls>
  <source
    src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm"
    type="video/webm"
  />
  <source
    src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
    type="video/mp4"
  />
  <embed
    src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4"
    type="video/mp4"
  />
</video>
```

IE11 下，能够正常播放

![image-20210516012905334](https://img-blog.csdnimg.cn/img_convert/29e4c96daec4c5db577ac0a4ce5ce1b8.png)

IE8 下，也能正常播放

![image-20210516010618514](https://img-blog.csdnimg.cn/img_convert/20d0e02a6af2a2497a6ccb45657f5d8d.png)

### 其他

通过`iframe`和`embed`的方式引入视频。以某艺为例，提供了视频链接的 HTML 代码和通用代码

![image-20210516011905816](https://img-blog.csdnimg.cn/img_convert/f2001068e8a632e4191bb7372e1eade2.png)

![image-20210516011837229](https://img-blog.csdnimg.cn/img_convert/faf8c2e1c98d340dd5140f4428316a03.png)

```html
<iframe
  src="http://open.iqiyi.com/developer/player_js/coopPlayerIndex.html?vid=0c53ddd55f262c6d416afa9d1f49dc55&tvId=1008748400&accessToken=2.ef9c39d6c7f1d5b44768e38e5243157d&appKey=8c634248790d4343bcae1f66129c1010&appId=1368&height=100%&width=100%"
  frameborder="0"
  allowfullscreen="true"
  width="100%"
  height="100%"
></iframe>
```

不过，`embed`需要 flash 的支持

```html
<embed
       src="//player.video.iqiyi.com/0c53ddd55f262c6d416afa9d1f49dc55/0/0/v_19rrcuh1jw.swf-albumId=1008748400-tvId=1008748400-isPurchase=0-cnId=undefined"
       allowFullScreen="true" quality="high" width="480" height="350" align="middle" allowScriptAccess="always"
       type="application/x-shockwave-flash"></embed>
```
