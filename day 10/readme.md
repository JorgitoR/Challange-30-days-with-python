>>> fname ="hello-wirld.txt"
>>> file_object = open(fname, "w")
>>> file_object.write("Hello World")
11
>>> file_object.close()
>>> with open(fname, "w") as file_object:
...     file_object.write("Hello word againb")
...
17
>>> wiht open(fname, "r") as read:
  File "<stdin>", line 1
    wiht open(fname, "r") as read:
         ^
SyntaxError: invalid syntax
>>> with open(fname, "r") as read:
...     print(read.read())
...
Hello word againb
>>> exit()