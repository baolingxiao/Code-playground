### 基本用法
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")


### 表达式求值
a = 5
b = 10
print(f"The sum of {a} and {b} is {a + b}.")


### 调用函数
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))


### 字符串格式化
#### 控制小数点位数
value = 3.14159
print(f"Value rounded to two decimal places: {value:.2f}")


#### 字符串对齐
name = "Alice"
print(f"|{name:<10}|")  # 左对齐
print(f"|{name:>10}|")  # 右对齐
print(f"|{name:^10}|")  # 居中对齐


### 使用字典
person = {'name': 'Charlie', 'age': 25}
print(f"{person['name']} is {person['age']} years old.")


### 嵌套 f-string
name = "Diana"
greeting = f"Hello, {name}!"
print(f"{greeting} How are you today?")


### 日期格式化
from datetime import datetime
today = datetime.now()
print(f"Today's date is: {today:%Y-%m-%d}")

### 多行字符串
name = "Eve"
age = 28
profession = "engineer"

info = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Profession: {profession}"
)
print(info)
