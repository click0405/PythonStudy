import re 

# s = "Hello World"
# pattern = r"hello"
# regex = re.compile(pattern,flags=re.I)

# s = '''hello world
# hello kitty
# 你好，北京
# '''
# pattern = r".+"
# regex = re.compile(pattern,re.S)

# s = '''hello world
# nihao beijing
# '''
# pattern = r"^nihao"
# regex = re.compile(pattern,re.M)

s = '''hello world
nihao beijing
'''
pattern = r'''Hello #匹配hello
\s+ #匹配空格
world #匹配world
'''

regex = re.compile(pattern,re.X|re.I)

try:
    s = regex.search(s).group()
except Exception :
    print("没有匹配到内容")
else:
    print(s)
