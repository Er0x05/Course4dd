//哪一部分是变量？

import turtle
fred = turtle.Turtle()
fred.color("red")
fred.forward(100)
fred.right(135)
fred.forward(140)
fred.right(135)
fred.forward(100)

A.import    B.turtle    C."red"     D.fred

--------------------------------------------------------

//哪几行代码是赋值语句？

A.fred = turtle.Turtle()
B.import tutle
C.fred.color("red")
D.34 = some_list

--------------------------------------------------------

//两个语句有什么不同？

A.fred = turtle.Turtle()
B.turtle.Turtle() = fred

--------------------------------------------------------

//代码执行后输出什么？如果有错误问题在哪里？

import turtle
amy = turtle.Turtle()
amy.color(red)
for side in [1,2,3,4,5,6,7,8]:
    amy.forward(100)
    amy.right(135)

--------------------------------------------------------

//哪些是字符串？

A.Hello!    B."Hello!"  C."123"   D.123   E.[1,2,3]

--------------------------------------------------------

//哪些是列表？

A."1,2,3,4,5"
B.[1,2,3,4,5]
C.(1,2,3,4,5)
D.[1 2 3 4 5]
E.["red","orange","yellow","blue","green","blue","purple"]

--------------------------------------------------------

//如果想使用 math 模块，该如何导入？

--------------------------------------------------------

//解释代码每一行的作用

import tutle
amy = turtle.Turtle()
amy.color('yello')
amy.right(90)
amy.forward(100)

--------------------------------------------------------

//请创建这段代码并执行

创建一只叫做duoduo的红色乌龟，画一个五角星。

--------------------------------------------------------

//哪些是赋值语句？

A.pretty_color = "red"
B.color = "blue"
C."blue" = color
D."red" = pretty_color

--------------------------------------------------------

//哪些代码的效果与示例一样？
mary.color("purple")
for side in [1, 2, 3, 4, 5]:
    mary.forward(100)
    mary.right(72)

A.
lovely_color = "purple"
mary.color(lovely_color)
for side in [1, 2, 3, 4, 5]:
    mary.forward(100)
    mary.right(72)

B.
lovely_color = "purple"
mary.color("lovely_color")
for side in [1, 2, 3, 4, 5]:
    mary.forward(100)
    mary.right(72)

C.
blah = "purple"
mary.color(blah)
for side in [1, 2, 3, 4, 5]:
    mary.forward(100)
    mary.right(72)

--------------------------------------------------------

//创建一个叫做 sides 的变量，并将列表 [1, 2, 3, 4, 5] 赋值给该变量。

--------------------------------------------------------

//创建一个叫做 angle 的变量，并将整数 72 赋值给该变量。

--------------------------------------------------------

//将参数, 列表修改成变量,尽可能的放在前面的位置, 方便修改.

import turtle
mary = turtle.Turtle()
mary.color("purple")
for side in [1, 2, 3, 4, 5]:
    mary.forward(100)
    mary.right(72)

--------------------------------------------------------

//如果将循环中的 [1, 2, 3, 4, 5] 替换为 [1, 0, 1, 0, 1]，会发生什么？

//如果将 [1, 0, 1, 0, 1] 替换为 ["red", "orange", "yellow", "green", "blue"]，会发生什么？

--------------------------------------------------------

//在这个循环里的所有行（第一行之后）都缩进了（向右移动了四个空格）。

for side in [1, 2, 3, 4, 5]:
    amy.forward(100)
    amy.right(72)

//如果我们删掉最后一行的缩进，会怎样？如下所示：

for side in [1, 2, 3, 4, 5]:
    amy.forward(100)
amy.right(72)

--------------------------------------------------------

//如果使 amy.right(72) 位于循环内，并使 amy.forward(100) 位于循环外，会发生什么？

for side in [1, 2, 3, 4, 5]:
    amy.right(72)
amy.forward(100)

--------------------------------------------------------

//对于该循环，下面的哪些表述正确？

for side in [1, 2, 3, 4]:
    george.forward(100)
    george.right(90)

A.列表项数量决定了循环的运行次数
B.通过缩进标识一行代码位于循环内
C.列表项必须是数字，否则循环不可行

--------------------------------------------------------

//循环是否可行？

A.
for side in [1, 2, 3, 4]:
    george.forward(100)
    george.right(90)

B.
for side in [1, 2, 3, 4]
    george.forward(100)
    george.right(90)

C.
for side in [0, 7, "fish", "llama"]:
    george.forward(100)
    george.right(90)

D.
for side in (1, 2, 3, 4):
    george.forward(100)
    george.right(90)

E.
for side in [1, 2, 3, 4]:
  george.forward(100)
    george.right(90)

--------------------------------------------------------

//这个循环将运行多少次？

for side in [100]:
    george.forward(100)
    george.right(90)

--------------------------------------------------------

//解释一下代码中的这一行,for , length , in ,lengths 都是什么？

for length in lengths:

--------------------------------------------------------

//循环将运行几次？第三次时变量的值是什么？第五次的时候乌龟前进了多少像素？

for length in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(length)
    dizzy.right(90)

--------------------------------------------------------

//哪些循环将绘制出和这个循环相同的图形？
for length in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(length)
    dizzy.right(90)

A.
for length in [1, 2, 3, 4, 5, 6]:
    dizzy.forward(length)
    dizzy.right(90)

B.
for side in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(side)
    dizzy.right(90)

C.
for angle in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(100)
    dizzy.right(angle)

D.
for angle in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(angle)
    dizzy.right(90)

--------------------------------------------------------

//乌龟6次分别前进多少像素？
for length in [10, 20, 30, 40, 50, 60]:
    length = 100
    dizzy.forward(length)
    dizzy.right(90)

--------------------------------------------------------

//乌龟6次分别前进多少像素？
for length in [10, 20, 30, 40, 50, 60]:
    dizzy.forward(length)
    length = 100
    dizzy.forward(length)

--------------------------------------------------------

//乌龟一共爬了多远？
import turtle
anna = turtle.Turtle()
for path in [1, 2, 3, 4]:
    for step in [1, 2, 3]:
        anna.forward(10)

--------------------------------------------------------

//完成homework