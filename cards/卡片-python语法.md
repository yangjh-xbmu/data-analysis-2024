# python

## 变量与数据类型

<!-- notecardId: 1729216419766 -->

在Python中，变量就像是一个盒子，你可以把不同的东西（数据）放进这个盒子里。每个盒子都有一个标签（变量名），这样你就可以随时找到盒子里的东西。

**案例**：
```python
name = "Alice"
age = 25
height = 1.65
is_student = True
```

**测试**：
```python
a = 10  # 数据类型：int
b = "Hello"  # 数据类型：str
c = 3.14  # 数据类型：float
d = False  # 数据类型：bool
```

## 控制流：条件语句

<!-- notecardId: 1729216419814 -->

条件语句就像是一个岔路口，根据不同的条件（路况），你会选择不同的路径（执行不同的代码）。

**案例**：
```python
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

**测试**：
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

## 控制流：循环

<!-- notecardId: 1729216419820 -->

循环就像是一个跑步机，你可以设定一个目标（循环条件），然后不断地重复跑步（执行代码），直到达到目标。

**案例**：
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print("Count is", count)
    count += 1
```

**测试**：
```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

## 函数

<!-- notecardId: 1729216419826 -->

函数就像是一个工厂，你给它输入（参数），它给你输出（返回值）。工厂可以重复使用，节省时间和资源。

**案例**：
```python
def greet(name):
    return "Hello, " + name

message = greet("Bob")
print(message)
```

**测试**：
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

## 列表与字典

<!-- notecardId: 1729216419833 -->

列表就像是一个购物清单，你可以按顺序存放多个物品（元素）。字典就像是一个通讯录，每个联系人（键）都有一个电话号码（值）。

**案例**：
```python
numbers = [1, 2, 3, 4, 5]

person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
```

**测试**：
```python
my_list = [10, 20, 30]
my_dict = {"name": "Bob", "age": 30, "city": "New York"}

my_list.pop()
del my_dict["age"]
```

## 字符串操作

<!-- notecardId: 1729216419838 -->

字符串就像是一串珠子，你可以对它们进行各种操作，比如拼接、切割、查找等。

**案例**：
```python
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name

text = "Hello, World!"
substring = text[7:12]
```

**测试**：
```python
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)
```

## 异常处理

<!-- notecardId: 1729216419846 -->

异常处理就像是一个安全网，当程序出现意外情况（错误）时，它可以防止程序崩溃，并让你有机会处理这些错误。

**案例**：
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**测试**：
```python
input_str = "abc"
try:
    num = int(input_str)
except ValueError:
    print("Invalid input")
```

## 模块与导入

<!-- notecardId: 1729216419851 -->

模块就像是一个工具箱，你可以从中选择你需要的工具（函数、类等）来完成任务。

**案例**：
```python
import math

sqrt_result = math.sqrt(16)
```

**测试**：
```python
import random

random_number = random.randint(1, 100)
print(random_number)
```
