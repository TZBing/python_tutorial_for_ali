# 模块
在理解 \_\_name\_\_ 之前，必须要明白什么是模块。  
Python中的模块，其实就是一个.py文件，即任何一个.py文件都可以作为一个模块。模块可以被直接执行，如 `python xxx.py`；也可以被导入，如 `import xxx` （import时不需要加.py这个后缀）。

# \_\_name\_\_的值
\_\_name\_\_是Python中的一个内置变量，并且Python给每一个模块都添加了这个变量，即每个模块都会有\_\_name\_\_这个变量，这个变量专门用来表示当前模块的名字。
\_\_name\_\_的特殊之处在于，它的值取决于当前模块的执行方式，即：
+ **如果模块是被直接执行的，那么该模块中的\_\_name\_\_的值会被赋值为"\_\_main\_\_"；**  
如`python module1.py`的执行结果为：
> value of \_\_name\_\_ in module1: \_\_main\_\_  
f1:hello  
f2:just for test
+ **如果模块是被导入的，那么该模块中的\_\_name\_\_的值会被赋值为该模块的名字（即py文件的名字，但是不带.py后缀）；**  
如`python test1.py`的执行结果为（test1.py中导入了module1.py）：
> value of \_\_name\_\_ in module1: module1  
f1:hello
# \_\_name\_\_的作用
模块往往只是用来定义一些函数，然后让其它人可以通过import的方式导入使用；但是模块在编写的时候，除了函数定义以外，往往也会写一些会被直接执行的代码，比如module1.py中的
```python
print("value of __name__ in module1: " + __name__)
f1("hello")
```
上面的两行代码无论是module1.py被直接执行还是被导入时都会执行。
但是有时候，需要有些代码只有在模块被直接执行时才执行，而在模块被导入时不要执行，比如module1.py中的
```python
f2("just for test")
```
这行代码只是用来测试f2这个函数的功能是不是ok，而单独测试模块肯定就是直接执行模块，所以需要在直接执行模块的时候执行这行代码；而当模块被导入时，就不需要执行这种用来测试的代码。  

这时，就可以利用模块在不同执行方式下\_\_name\_\_的值会不同的特性，来区别处理；即
```python
if __name__ == "__main__":
    f2("just for test")
```
因为直接执行时\_\_name\_\_ = "\_\_main\_\_"，所以if判断为True，测试代码`f2("just for test")`就会被执行；
而当module1.py被导入时\_\_name\_\_ = "module1"，所以if判断为False，测试代码`f2("just for test")`就不会被执行。
