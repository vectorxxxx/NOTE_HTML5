> 笔记来源：[尚硅谷Web前端HTML5&CSS3初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[TOC]

# 前端简介

## 1. 软件的分类

### 1.1. 系统软件

- Windows
- Linux
- macOS

![image-20210512233610483](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210512233615.png)

### 1.2. 应用软件

- Office
- QQ

![image-20210512233641461](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002412.png)

### 1.3. 游戏软件

- 绝地求生
- 王者荣耀

![image-20210512233650896](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002413.png)

## 2. 客户端与服务器

通常情况下，现在的软件一般由两个部分组成：

- 客户端：用户通过客户端来使用软件。
- 服务器：服务器负责在远程处理业务逻辑。

![image-20210512233922478](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002414.png)

### 2.1. 服务器

服务器开发的语言：

- <mark>Java</mark>
- PHP
- C#
- Python
- <mark>Node.js</mark>
- ……

### 2.2. 客户端

客户端的形式

- 文字客户端：占老的方式，通过命令行来使用软件
- 图形化界面：通过点击拖动等来使用软件。Windows中、macOS中、Android、iOS中的大部分应用。（<mark>C/S架构</mark>）
- <mark>网页</mark>：通过访问网页来使用软件。所有的网站都属于这个范畴。（<mark>B/S架构</mark>）

## 3. 网页的特点

相较于传统的图形化界面，网页具有如下一些优点：

- 不需要安装
- 无需更新
- 跨平台

网页中使用的语言：

- HTML、CSS、JavaScript

![image-20210512234859315](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002415.png)

## 4. 网页简史

蒂姆·伯纳斯·李爵士，万维网的发明人。

![image-20210512235216613](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002416.png)

1991年8月6日，世界上第一个服务器和第一个网站在欧洲核子研究中心上线。

第一个网站：[http://info.cern.ch/hypertext/WWW/TheProject.html](http://info.cern.ch/hypertext/WWW/TheProject.html)

![image-20210512235231005](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002417.png)

## 5. 浏览器和网页

有了浏览器我们只需要一个网址便可以访问任何的网站。

而浏览器中所显示的内容正是我们所说的网页。

网页原本的样子：

```html
...
<!--无障碍占位-->
<div id="J_accessibility"></div>
<!--顶通占位 -->
<div id="J_promotional-top">
</div>
<div id="shortcut">
    <div class="w">
        <ul class="fl" clstag="h|keycount|head|topbar_01">
            <li class="dropdown" id="ttbar-mycity"></li>
        </ul>

        <ul class="fr">
            <li class="fore1 dropdown" id="ttbar-login" clstag="h|keycount|head|topbar_02">
                <a href="//passport.jd.com/uc/login?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F" class="link-login">你好，请登录</a>&nbsp;&nbsp;<a
                                                                                                                                       href="//reg.jd.com/reg/person?ReturnUrl=https%3A//www.jd.com/" class="link-regist style-red">免费注册</a>
            </li>
            <li class="spacer"></li>
            <li class="fore2" clstag="h|keycount|head|topbar_03">
                <div class="dt"><a target="_blank" href="//order.jd.com/center/list.action">我的订单</a></div>
            </li>
            <li class="spacer"></li>
            <li class="fore3 dropdown" id="ttbar-myjd" clstag="h|keycount|head|topbar_04">
                <div class="dt cw-icon"><a target="_blank" href="//home.jd.com/">我的京东</a><i class="iconfont">&#xe610;</i><i
                                                                                                                            class="ci-right"><s>◇</s></i></div>
                <div class="dd dropdown-layer"></div>
            </li>
            <li class="spacer"></li>
            <li class="fore4" clstag="h|keycount|head|topbar_05">
                <div class="dt"><a target="_blank" href="//vip.jd.com/">京东会员</a></div>
            </li>
            <li class="spacer"></li>
            <li class="fore5" clstag="h|keycount|head|topbar_06">
                <div class="dt"><a target="_blank" href="//b.jd.com/">企业采购</a></div>
            </li>
            <li class="spacer"></li>
            <li class="fore8 dropdown" id="ttbar-serv" clstag="h|keycount|head|topbar_07">
                <div class="dt cw-icon">客户服务<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                <div class="dd dropdown-layer"></div>
            </li>
            <li class="spacer"></li>
            <li class="fore9 dropdown" id="ttbar-navs" clstag="h|keycount|head|topbar_08">
                <div class="dt cw-icon">网站导航<i class="iconfont">&#xe610;</i><i class="ci-right"><s>◇</s></i></div>
                <div class="dd dropdown-layer"></div>
            </li>
            <li class="spacer"></li>
            <li class="fore10 mobile" id="J_mobile" clstag="h|keycount|head|topbar_09">
                <div class="dt mobile_txt">手机京东</div>
                <div class="mobile_static">
                    <div class="mobile_static_qrcode"></div>
                </div>
                <div id='J_mobile_pop' class='mod_loading mobile_pop'>
                </div>
            </li>
        </ul>
    </div>
</div>
...
```

浏览器渲染后的样子：

![image-20210513000033830](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002418.png)

前端工程师负责编写网页的源代码。

浏览器负责将网页渲染成我们想要的样子。

### 5.1. 浏览器的问题

市面上存在有很多不同的浏览器。

在万维网的初期，网页编写并没有标准。

于是就出现了这种情况：

![image-20210513000559333](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002419.png)

### 5.2. W3C的建立

伯纳斯李1994年建立<mark>万维网联盟（W3C）</mark>

W3C的出现为了<mark>制订网页开发的标准</mark>，以使同一个网页在不同的浏览器中有相同的效果。

所以，我们需要制订我们编写的网页都需要遵循W3C的规范！

![image-20210513000825367](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513005016.png)

### 5.3. 网页的结构思想

根据W3C标准，一个网页主要由三部分组成：结构、表现还有行为。

![image-20210513001146250](https://gitee.com/vectorx/ImageCloud/raw/master/img/20210513002421.png)

#### 结构、表现、行为

- 结构（骨架）：HTML用于描述页面的结构
- 表现（皮肤）：CSS用于控制页面中元素的样式
- 行为（交互）：JavaScript用于响应用户操作

![nsyjg-dwl0d](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514233853.gif)

## 6. 网页的基本结构

### 6.1. 迭代

网页的版本

- HTML4
- XHTML2.0
- HTML5

### 6.2. 文档声明（doctype）

文档声明用来告诉浏览器当前网页的版本

```html
<!-- html5的文档声明 -->
<!doctype html>
<!-- 或者 -->
<!Doctype HTML>
```

### 6.3. 字符编码

所有的数据在计算机中存储时都是以二进制形式存储的，文字也不例外。

所以一段文字在存储到内存中时，都需要转换为二进制编码当我们读取这段文字时，计算机会将编码转换为字符，供我们阅读

#### 编码

将字符转换为二进制码的过程称为编码

#### 解码

将二进制码转换为字符的过程称为解码

#### 字符集（charset）

编码和解码所采用的规则称为字符集（相当于密码本）

#### 乱码

如果编码和解码所采用的字符集不同就会出现乱码问题。

可以通过meta标签来设置网页的字符集，避免乱码问题

```html
<meta charset="utf-8">
```

### 6.4. 常见的字符集

#### ASCII

ASCII(American Standard Code for Information Interchange)：美国信息交换标准代码

在所有字符集中，最知名的可能要数被称为ASCII的<mark>8位字符</mark>了。美国信息交换标准代码是由美国国家标准学会(American National Standard Institute , ANSI )制定的，是一种标准的<mark>单字节字符编码</mark>方案，用于基于文本的数据。它最初是美国国家标准，供不同计算机在相互通信时用作共同遵守的西文字符编码标准，后来它被国际标准化组织（International Organization for Standardization, ISO）定为国际标准，称为ISO 646标准。适用于所有拉丁文字字母

ASCII 码使用指定的7 位或8 位二进制数组合来表示128 或256 种可能的字符。标准ASCII 码也叫基础ASCII码，使用7 位二进制数（剩下的1位二进制为0）来表示所有的大写和小写字母，数字0 到9、标点符号，以及在美式英语中使用的特殊控制字符

ASCII码表：[Ascii Table - ASCII character codes and html, octal, hex and decimal chart conversion](http://www.asciitable.com/)

#### ISO-8859-1

ISO-8859-1编码是<mark>单字节编码</mark>，向下兼容ASCII，其编码范围是0x00-0xFF，0x00-0x7F之间完全和ASCII一致，0x80-0x9F之间是控制字符，0xA0-0xFF之间是文字符号。

ISO码表：[HTML ISO-8859-1 参考手册](https://www.w3school.com.cn/charsets/ref_html_8859.asp)

#### GB2312

GB2312（信息交换用汉字编码字符集）是由中国国家标准总局1980年发布。基本集共收入汉字6763个和非汉字图形字符682个。GB 2312的出现，基本满足了汉字的计算机处理需要，它所收录的汉字已经覆盖中国大陆99.75%的使用频率。

#### GBK

GBK（即“国标”、“扩展”汉语拼音的第一个字母），汉字编码字符集。2000年已被GB18030-2000国家强制标准替代。 2005年GB18030-2005发布，替代了GB18030-2000。

GBK使用了<mark>双字节编码</mark>方案，其编码范围从8140至FEFE（剔除xx7F），共23940个码位，共收录了21003个汉字，完全兼容GB2312-80标准，支持国际标准ISO/IEC10646-1和国家标准GB13000-1中的全部中日韩汉字，并包含了BIG5编码中的所有汉字。

#### Big5

Big5，又称为大五码或五大码，是使用繁体中文（正体中文）社区中最常用的电脑汉字字符集标准，共收录13,060个汉字。

Big5虽普及于台湾、香港与澳门等繁体中文通行区，但长期以来并非当地的国家/地区标准或官方标准，而只是业界标准。倚天中文系统、Windows繁体中文版等主要系统的字符集都是以Big5为基准，但厂商又各自增加不同的造字与造字区，派生成多种不同版本。

#### UTF-8

UTF-8（8位元，Universal Character Set/Unicode Transformation Format）是针对Unicode的一种<mark>可变长度字符编码</mark>，也叫万国码、统一码。它可以用来表示Unicode标准中的任何字符，而且其编码中的第一个字节仍<mark>与ASCII相容</mark>，使得原来处理ASCII字符的软件无须或只进行少部分修改后，便可继续使用。

#### UTF-16

UTF-16是Unicode的其中一个使用方式。UTF-16比起UTF-8，好处在于大部分字符都以<mark>固定长度的字节</mark>（2字节）储存，但UTF-16却<mark>无法兼容于ASCII编码</mark>。

#### Unicode

Unicode只是一组字符设定或者说是从数字和字符之间的逻辑映射的<mark>概念编码</mark>，但是它并没有指定代码点如何在计算机上存储。UCS4、UTF-8、UTF-16（UTF后的数字代表编码的最小单位，如UTF-8表示最小单位1字节，所以它可以使用1、2、3字节等进行编码，UTF-16表示最小单位2字节，所以它可以使用2、4字节进行编码）都是Unicode的编码方案。UTF-8因可以兼容ASCII而被广泛使用。

如果把各种文字编码形容为各地的方言，那么Unicode就是世界各国合作开发的一种语言。

### 6.5. HTML5的基本结构

```html
<!-- 文档声明，声明当前网页的版本 -->
<!doctype html>
<!-- html的根标签（元素），网页中的所有内容都要写根元素的里边 -->
<html>
    <!-- head是网页的头部，head中的内容不会在网页中直接出现，主要用来帮助浏览器或搜索引擎来解析网页 -->
    <head>
        <!-- meta标签用来设置网页的元数据，这里meta用来设置网页的字符集，避免乱码问题 -->
        <meta charset="utf-8">
        <!-- title中的内容会显示在浏览器的标题栏，搜索引擎会主要根据title中的内容来判断网页的主要内容 -->
        <title>网页的标题</title>
    </head>
    <!-- body是htm1的子元素，表示网页的主体，网页中所有的可见内容都应该写在body里 -->
    <body>
        <!-- h1网页的一级标题 -->
        <h1>网页的大标题</h1>
    </body>
</html>
```