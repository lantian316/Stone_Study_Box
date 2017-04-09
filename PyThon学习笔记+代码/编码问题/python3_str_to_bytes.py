#!/usr/bin/python
# -*- coding: utf-8 -*-

def python3StrToBytes():     
    zhcnUnicode = "1.此处的，Python 3.x中，默认字符串的写法，就已经是unicode类型的字符串了。2.当然，还是有一点前提的，那就是，你在(1)此处python文件所指定的编码类型(2)要和你当前python文件实际所采用的编码类型，要匹配和一致，即此处，两者均是UTF-8，所以，Python解析器，才能正确的将我们此处所输入的UTF-8的中文字符，正确地解码为对应的Unicode字符串的；3.接下来将要演示的是，打印对于的此处字符的类型；然后再直接输出显示到windows的GBK编码的cmd中";
    print("type(zhcnUnicode)=",type(zhcnUnicode)); #type(zhcnUnicode)= <class 'str'>
    zhcnGbkBytes = zhcnUnicode.encode("GBK");
    print("You should see these zh-CN bytes in windows cmd normally, which begin with b preffix: zhcnGbkBytes=%s"%(zhcnGbkBytes)); #You should see these zh-CN bytes in windows cmd normally, which begin with b preffix: zhcnGbkBytes=b'1.\xb4\xcb\xb4\xa6\xb5 ...... \xc2\xeb\xb5\xc4cmd\xd6\xd0'
     

if __name__=="__main__":
    python3StrToBytes();