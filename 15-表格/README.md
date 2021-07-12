> 笔记来源：[尚硅谷 Web 前端 HTML5&CSS3 初学者零基础入门全套完整版](https://www.bilibili.com/video/BV1XJ411X7Ud)

[toc]

# 表格

## 1、表格

在现实生活中，我们经常需要使用表格来表示一些格式化数据：

- 课程表、人名单、成绩单...

同样在网页中我们也需要使用表格，我们通过`table`标签来创建一个表格

在`table`中使用`tr`表示表格中的一行，有几个`tr`就有几行

在`tr`中使用`td`表示一个单元格，有几个 td`就有`几个单元格

- `rowspan` 纵向的合并单元格
- `colspan` 横向的合并单元格

```html
<table border="1" width="50%" align=" center">
  <!--在table中使用tr表示表格中的一行，有几个tr就有几行-->
  <tr>
    <!--在tr中使用td表示一个单元格，有几个td就有几个单元格-->
    <td>A1</td>
    <td>B1</td>
    <td>C1</td>
    <td>D1</td>
  </tr>
  <tr>
    <td>A2</td>
    <td>B2</td>
    <td>C2</td>
    <!--rouspan 纵向的合并单元格-->
    <td rowspan="2">D2</td>
  </tr>
  <tr>
    <td>AB</td>
    <td>B3</td>
    <td>C3</td>
  </tr>
  <tr>
    <td>A4</td>
    <td>B4</td>
    <!-- colspan横向的合并单元格 -->
    <td colspan="2">C4</td>
  </tr>
</table>
```

## 2、长表格

可以将一个表格分成三个部分：

- 头部 `thead`
- 主体 `tbody`
- 底部 `tfoot`

`th` 表示头部的单元格

```html
<table>
  <thead>
    <tr>
      <td>日期</td>
      <td>收入</td>
      <td>支出</td>
      <td>合计</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2000.1.1</td>
      <td>500</td>
      <td>200</td>
      <td>300</td>
    </tr>
    <tr>
      <td>2000.1.1</td>
      <td>500</td>
      <td>200</td>
      <td>300</td>
    </tr>
    <tr>
      <td>2000.1.1</td>
      <td>500</td>
      <td>200</td>
      <td>300</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td></td>
      <td></td>
      <td>合计</td>
      <td>1200</td>
    </tr>
  </tfoot>
</table>
```

## 3、表格的样式

### HTML 代码

```html
<table>
  <tr>
    <td>学号</td>
    <td>姓名</td>
    <td>性别</td>
    <td>年龄</td>
    <td>地址</td>
  </tr>
  <tr>
    <td>1</td>
    <td>孙悟空</td>
    <td>男</td>
    <td>18</td>
    <td>花果山</td>
  </tr>
  <tr>
    <td>2</td>
    <td>猪八戒</td>
    <td>男</td>
    <td>28</td>
    <td>高老庄</td>
  </tr>
  <tr>
    <td>3</td>
    <td>沙和尚</td>
    <td>男</td>
    <td>38</td>
    <td>流沙河</td>
  </tr>
  <tr>
    <td>4</td>
    <td>唐僧</td>
    <td>男</td>
    <td>16</td>
    <td>女儿国</td>
  </tr>
  <tr>
    <td>1</td>
    <td>孙悟空</td>
    <td>男</td>
    <td>18</td>
    <td>花果山</td>
  </tr>
  <tr>
    <td>2</td>
    <td>猪八戒</td>
    <td>男</td>
    <td>28</td>
    <td>高老庄</td>
  </tr>
  <tr>
    <td>3</td>
    <td>沙和尚</td>
    <td>男</td>
    <td>38</td>
    <td>流沙河</td>
  </tr>
  <tr>
    <td>4</td>
    <td>唐僧</td>
    <td>男</td>
    <td>16</td>
    <td>女儿国</td>
  </tr>
  <tr>
    <td>4</td>
    <td>唐僧</td>
    <td>男</td>
    <td>16</td>
    <td>女儿国</td>
  </tr>
  <tr>
    <td>1</td>
    <td>孙悟空</td>
    <td>男</td>
    <td>18</td>
    <td>花果山</td>
  </tr>
  <tr>
    <td>2</td>
    <td>猪八戒</td>
    <td>男</td>
    <td>28</td>
    <td>高老庄</td>
  </tr>
  <tr>
    <td>3</td>
    <td>沙和尚</td>
    <td>男</td>
    <td>38</td>
    <td>流沙河</td>
  </tr>
  <tr>
    <td>4</td>
    <td>唐僧</td>
    <td>男</td>
    <td>16</td>
    <td>女儿国</td>
  </tr>
</table>
```

### CSS 代码

```css
table {
  width: 50%;
  margin: 0 auto;
  border: 1px black solid;

  /* border-spacing：指定边框之间的距离；边框之间虽然没有距离了，但是实际上是两条边框的和，看起来是变粗了 */
  /* border-spacing: 0; */

  /*border-collapse:collapse；设置边框的合并；真正的将两条边框合并成一条边框 */
  border-collapse: collapse;

  /* 默认情况下元素在td中是垂直居中的，可以通过vectical-align来修改 */
  vertical-align: middle;
  text-align: center;
}

/* 如果表格中没有使用tbody而是直接使用tr，那么浏览器会自动创建一个tbody，并且将tr全都放到tbody中
   所以说，tr不是table的子元素 */
tbody tr:nth-child(odd) {
  background-color: rgb(211, 216, 188);
}

td {
  border: 1px black solid;
}
```

![image-20210613195306119](https://img-blog.csdnimg.cn/img_convert/81543159dc1d6a8beed1305693d638f6.png)

其中，

- `border-spacing`：指定边框之间的距离
- `border-collapse`：设置边框的合并

## 4、表单

**表单**

- 在现实生活中表单用于提交数据
- 在网页中也可以使用表单，网页中的表单用于将本地的数据提交给远程的服务器

**form 的属性**

- `action`：表单要提交的服务器的地址

### 文本框

<mark>注意：数据要提交到服务器中，必须要为元素指定一个`name`属性值</mark>

```html
文本框<input type="text" name="username" />
```

### 密码框

```html
密码框<input type="password" name="password" />
```

### 提交按钮

```html
<input type="submit" value="注册" />
```

### 单选框

像这种选择框，必须要措定一个`value`属性，`value`属性最终会作为用户填写的值传递给服务器

```html
单选框
<input type="radio" name="hello" value="a" />
<input type="radio" name="hello" value="b" checked />
```

### 多选框

```html
多选框
<input type="checkbox" name="test" value="1" />
<input type="checkbox" name="test" value="2" />
<input type="checkbox" name="test" value="3" checked />
```

### 下拉列表

```html
下拉列表
<select name="haha">
  <option value="i">选项一</option>
  <option value="ii" selected>选项二</option>
  <option value="iii">选项三</option>
</select>
```

![image-20210613203005016](https://img-blog.csdnimg.cn/img_convert/ea8b0b8806fcebbe73a190b71a09fd3a.png)

## 5、表单补充

### 按钮

```html
<!-- 提交按钮 -->
<input type="submit" />
<!-- 重置按钮 -->
<input type="reset" />
<!-- 普通按钮 -->
<input type="button" value="按钮" />
<br /><br />
<button type="submit">提交</button>
<button type="reset">重置</button>
<button type="button">按钮</button>
```

![image-20210613203343362](https://img-blog.csdnimg.cn/img_convert/02ca926acc195ce5382d791756dca361.png)

上面两种写法实际上效果是一致的，区别在于：

- `input`是自闭合标签，不需要`</input>`就能结束；`button`不是自闭合标签，跟一般标签一样是成对出现的
- `button`因为不是自闭合标签，所以使用起来更灵活，可以嵌套其他的标签
