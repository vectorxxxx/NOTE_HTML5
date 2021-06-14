> 笔记来源：[尚硅谷Web前端HTML5&CSS3初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[TOC]

# 前端开发准备

## 1. 离线文档的下载

离线文档：[Zeal - Offline Documentation Browser](https://zealdocs.org/)

如果安装报错，需安装：[Visual C++ Redistributable](https://www.microsoft.com/en-us/download/details.aspx?id=48145)

下载安装完成之后，会在“开始”屏幕或者桌面生成快捷键，双击打开

在第一次使用时，并不是直接就有HTML文档的，还需要Download。

这里点击工具栏的Tools-Assets或者下方的“Install and update docsets”都是OK的

![image-20210514003839690](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514021530.png)

按照步骤安装即可

![image-20210514004521785](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514021531.png)

由于服务器在国外，网络较慢，耐心等待download完毕

在Installed中出现HTML，同时左侧导航栏有了HTML，至此安装完毕

![image-20210514005151906](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514021532.png)

离线使用，在左侧导航栏可以查询HTML标签和属性，右侧显示元素的详细信息

![image-20210514005355719](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514021533.png)

## 2. 文本编辑器的选择

### Notepad++

Notepad++是Windows操作系统下的一套文本编辑器，功能比 Windows 中的 Notepad 强大，除了可以用来制作一般的纯文字说明文件，也十分适合编写计算机程序代码。

有语法高亮度显示、语法折叠功能，并且支持宏以及扩充基本功能的外挂模组。

完全免费，支持众多计算机程序语言：C，C++，Java，C#，XML，SQL，HTML，PHP，ASP等

官方地址：[notepad-plus-plus.org](http://notepad-plus-plus.org/)

Softonic地址：[Notepad++ - Download (softonic.com)](https://notepad-plus.it.softonic.com/)

不过因为国外服务器原因，而且貌似被墙了，所以建议从Softonic下载

- 优点：免费开源，轻量流畅，支持插件
- 缺点：界面丑，虽然可以下载皮肤插件（PS：个人感觉皮肤插件也不好用）

![image-20210514193614660](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514203723.png)

### Sublime

Sublime Text 是一个文本编辑器（收费软件，可以无限期试用，但是会有激活提示弹窗），同时也是一个先进的代码编辑器。

主要功能包括：拼写检查，书签，完整的 Python API ， Goto 功能，即时项目切换，多选择，多窗口等等。

跨平台，同时支持Windows、Linux、Mac OS X等操作系统。

强大的命令面板功能，可以模糊匹配命令。

官方地址：[Sublime Text - A sophisticated text editor for code, markup and prose](https://www.sublimetext.com/)

- 优点：轻量流畅，支持插件，界面简洁，运行速度特别快
- 缺点：不开源，商用收费

![image-20210514193644287](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514203724.png)

### VS Code √

Microsoft出品，轻量但强大，针对于编写现代Web和云应用的跨平台源代码编辑器。可以在Mac OS X、Windows和 Linux等操作平台使用。

具有对JavaScript、TypeScript和Node.js的内置支持，并具有丰富的其他语言（例如C++，C＃，Java，Python，PHP，Go）和运行时（例如.NET和Unity）扩展的生态系统。

官方地址：[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

- 优点：免费开源，轻量流畅，功能丰富，支持插件，界面简洁，智能代码补全，运行速度很快
- 缺点：几乎没有什么太大的缺点（PS：撤销恢复之前的编辑时出现过问题，希望官方能够尽快修复）

![image-20210514193819132](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514203725.png)

### Atom

Atom是Github专门为程序员推出的一个跨平台文本编辑器。完全免费开源的代码编辑器，具有简洁和直观的图形用户界面。

支持CSS，HTML，JavaScript等网页编程语言。支持宏，自动完成分屏功能，集成了文件管理器。

官方地址：[Atom](https://atom.io/)

Github地址：[atom/atom: The hackable text editor (github.com)](https://github.com/atom/atom)

中文地址：[Atom中文网 (baisheng999.com)](http://atom.baisheng999.com/)

- 优点：功能丰富，免费开源，支持插件，界面简洁
- 缺点：相对重量级；打开大文件卡死（PS：产品上经常用它写amWiki，使用时经常卡死；而且安装过程没有任何选项和提示，默认装到C盘）

![image-20210514193916283](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514203726.png)

### WebStorm

JetBrains 出品的智能 JavaScript IDE。誉为“Web前端开发神器”、“最强大的HTML5编辑器”、“最智能的JavaScript IDE”等。与IntelliJ IDEA同源，继承了IntelliJ IDEA强大的JS部分的功能。

IntelliJ IDEA 是java编程语言开发的集成环境。IntelliJ在业界被公认为最好的java开发工具，尤其在智能代码助手、代码自动提示、重构、JavaEE支持、各类版本工具(git、svn等)、JUnit、CVS整合、代码分析、 创新的GUI设计等方面的功能可以说是超常的。它的旗舰版本还支持HTML，CSS，PHP，MySQL，Python等。免费版只支持Java,Kotlin等少数语言。

官方地址：[Download WebStorm: The Smartest JavaScript IDE by JetBrains](https://www.jetbrains.com/webstorm/download/#section=windows)

- 优点：功能强大，支持插件，界面美观，智能代码补全，快速搜索
- 缺点：重量级，占内存；收费

![image-20210514194335432](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514203727.png)

除以之外，市面上还有很多功能强大的前端编辑器。

**HBuilder**：DCloud（数字天堂）推出一款支持HTML5的Web开发IDE。在语法提示、转到定义、重构、调试等方面都非常高效。缺点是不太稳定，有时会出现卡顿。

**Dreamweaver**：简称“DW，老牌的IDE ，国人开发，号称为编码极客而生的IDE。曾经PS+DW+FW（号称网页三剑客）称霸网页领域。然而之前的版本更新较慢，版本陈旧，已经满足不了广大前端开发者的项目需求，逐渐被市场淘汰。

这两款及其他编辑器在这里就不再赘述了（PS：本人没怎么用过，没有太多发言权）

这里我选择以VSCode作为接下来学习的开发编辑器了。当然每个人有每个人的偏好，你也可以选择自己心仪的编辑器进行开发。

## 3. 开发前准备

为VSCode安装以下插件，便于我们进行更好的开发工作

- Chinese (Simplified) Language Pack for Visual Studio Code：中文（简体）语言包（PS1：不完全显示中文，但是大多数都会译为英文；PS2：喜欢原生态或者英文OK的话，可忽略）
- Ayu：简单的主题与明亮的颜色
- vscode-icons：好看的图标
- <mark>Live Server</mark>：A Quick Development Live Server with live browser reload，即提供一个live服务器，并且支持代码与浏览器之间的实时同步刷新（PS：这样我们在写前端代码时就能实时看到效果了）

![image-20210514220735626](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234007.png)

## 4. 使用Live-Server

在当前HTML中右键单击，选择`Open With Live Server`

![image-20210514205943151](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234008.png)

### 踩坑1

`Open a folder or workspace...(File -> Open Folder)`

![image-20210514210102722](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234009.png)

解决方式：需要打开HTML所在的文件夹，通过导航栏 `文件-打开文件夹`，选择我们编写的HTML，再去`Open With Live Server`即可

![image-20210514210432328](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234010.png)

### 踩坑2

```javascript
Server is started at 5500 but failed to open in Browser Preview. 
```

![image-20210514212624752](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234011.png)

解决方式：在liveserver设置中，找到`Live Server>Settings:Use Browser Preview`，取消对 `Open in Browser Preview inside VS Code,instead of default browser`的勾选即可

![image-20210514213018282](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234012.png)

### 踩坑3

```javascript
Error: connect ECONNREFUSED 127.0.0.1:80
	at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1146:16)
```

![image-20210514225932299](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234013.png)

解决方式：取消使用代理，修改enable为false（这里我一直以为是live-server服务器本身的代理端口）。live-server默认使用5500端口

![image-20210514214047881](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234014.png)

实际上，配置端口要在`Live Server › Settings: Port`选项进行设置

![image-20210514214432367](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234015.png)

### 自定义端口号

按照上述说明，点击`在settings.json中编辑`会打开`settings.json`文件

![image-20210514214642662](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234016.png)

这里如果将`liveServer.settings.port`配置为0，会随机选择端口号

![image-20210514230020015](https://gitee.com/vectorx/ImageCloud/raw/master/html5/20210514234017.png)

