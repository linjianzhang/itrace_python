# itrace_python

依赖
操作系统：CentOS Linux release 7.2.1511
 系统用户：user1(文中涉及到user1都是指代系统用户名，需要替换成实际部署的用户名)
搭建Python环境
Cent OS 7.2默认装的有python2.7.5
# python -V
Python 2.7.5
如果需要更新的版本需要手动部署安装。
 下载地址：Download Python
 

这里选择下载版本为：2.7.13
 程序包：Python-2.7.13.tgz
上传程序包到服务器
选择自己熟悉的工具上传或者如果服务器可以上外网则可使用wget直接下载
$ wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
上传结果：
$ pwd
/home/user1
$ ll
总用量 16680
-rw-r--r--. 1 user1 user1 17076672 12月 18 2016 Python-2.7.13.tgz
解压编译程序包
把程序包解压到~目录
$ tar -zxf Python-2.7.13.tgz
$ ln -s Python-2.7.13 python
$ cd python
$ ./configure --prefix=/home/user1/python --enable-shared
$ make && make install
修改环境变量
$ echo '
PATH=$HOME/python/bin:$PATH
export PATH
' >> ~/.bash_profile
$ source ~/.bash_profile
$ python -V
Python 2.7.13
安装setuptools
以下离线安装方法需要依赖 setuptools 模块，所以需要先安装 setuptools 模块
 下载地址：Download setuptools
 

这里选择下载版本为：36.4.0
 程序包：setuptools-36.4.0.zip
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-rw-r-- 1 user1 user1 720462 Sep 10 15:29 setuptools-36.4.0.zip
解压编译程序包
把程序包解压到~目录
$ unzip setuptools-36.4.0.zip
$ cd setuptools-36.4.0
$ python setup.py install
...
Finished processing dependencies for setuptools==36.4.0
没提示出错，安装成功 
安装numpy
pandas需要依赖numpy，所以需要先安装numpy
 下载地址：Download numpy
 

这里选择下载版本为：1.13.1
 程序包：numpy-1.13.1.zip
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-r--r--.  1 root  root   5012881 7月   7 09:30 numpy-1.13.1.zip
解压编译程序包
把程序包解压到~目录
$ unzip numpy-1.13.1.zip
$ cd numpy-1.13.1
$ python setup.py install
$ cd ~
$ python
Python 2.7.5 (default, Nov 20 2015, 02:00:19) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> exit()
没提示出错，安装成功 
安装six
python-dateutil 模块需要依赖 six模块，所以需要先安装 six
 下载地址：six
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
-rw-rw-r--  1 user1 user1      29630 Sep 10 15:40 six-1.10.0.tar.gz
解压编译程序包
把程序包解压到~目录
$ tar -zxf six-1.10.0.tar.gz
$ cd six-1.10.0
$ python setup.py install
...
Finished processing dependencies for six==1.10.0
安装python-dateutil
pandas 需要依赖 python-dateutil ，所以需要先安装 python-dateutil
 下载地址：python-dateutil
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-r--r--.  1 root  root    241428 9月   7 11:47 python-dateutil-2.6.1.tar.gz
解压编译程序包
把程序包解压到~目录
$ tar -zxf python-dateutil-2.6.1.tar.gz
$ cd python-dateutil-2.6.1
$ python setup.py install
...
Finished processing dependencies for python-dateutil==2.6.1
安装 pytz
pandas 需要依赖 pytz 模块，所以需要先安装 pytz
 下载地址：pytz
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
-rw-rw-r--  1 user1 user1     502168 Sep 10 15:53 pytz-2017.2.zip
解压编译程序包
把程序包解压到~目录
$ unzip pytz-2017.2.zip
$ cd pytz-2017.2
$ python setup.py install
...
Finished processing dependencies for pytz==2017.2
安装pandas
下载地址：Download pandas
 

这里选择下载版本为：0.20.3
 程序包：pandas-0.20.3.tar.gz
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-r--r--.  1 root  root  10402185 9月   7 11:30 pandas-0.20.3.tar.gz
解压编译程序包
把程序包解压到~目录
$ tar -zxf pandas-0.20.3.tar.gz
$ cd pandas-0.20.3
$ python setup.py install
$ cd ~
$ python
Python 2.7.5 (default, Nov 20 2015, 02:00:19) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> exit()
没提示出错，安装成功 

```
以安装Flask-0.12版本为例，我自己的机器上需要的安装包包括：
Babel-2.3.4.tar.gz
click-6.7.tar.gz
Flask-0.12.tar.gz
itsdangerous-0.24.tar.gz
Jinja2-2.9.4.tar.gz
MarkupSafe-0.23.tar.gz
pytz-2016.10.tar.gz
Werkzeug-0.11.15.tar.gz
```

安装pip
Python的第三方包依赖需要通过 pip 安装： 因此，我们在部署环境上需要先安装好pip，并安装第三方类库。Python2.x版本是没有自带pip 的：
 下载地址：Download pip
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-r--r--.  1 root  root   1197370 9月   7 12:16 pip-9.0.1.tar.gz
解压编译程序包
安装依赖顺序把程序包解压到~目录并编译
$ tar -zxf pip-9.0.1.tar.gz
$ cd pip-9.0.1
$ python setup.py install
$ pip -V
pip 9.0.1 from /home/user1/python/lib/python2.7/site-packages/pip-9.0.1-py2.7.egg (python 2.7)
安装Flask依赖包
Flask依赖包有：

    install_requires=[
        'Werkzeug>=0.7',
        'Jinja2>=2.4',
        'itsdangerous>=0.21',
        'click>=2.0',
    ],
此外，Jinja2模块安装需要依赖MarkupSafe模块，因此安装Jinja2之前需要先安装MarkupSafe
 下载地址：https://pypi.python.org/pypi/xxx
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-r--r--.  1 root  root    279019 9月   7 12:28 click-6.7.tar.gz
-rw-r--r--.  1 root  root     46541 9月   7 12:28 itsdangerous-0.24.tar.gz
-rw-r--r--.  1 root  root    437659 9月   7 12:28 Jinja2-2.9.6.tar.gz
-rw-r--r--.  1 root  root     14356 9月   7 12:37 MarkupSafe-1.0.tar.gz
-rw-r--r--.  1 root  root   1169770 9月   7 12:28 Werkzeug-0.12.2.tar.gz
解压编译程序包
安装依赖顺序把程序包解压到~目录并编译 依赖包安装顺序：
Werkzeug>=0.7
MarkupSafe>=0.23
Jinja2>=2.4
itsdangerous>=0.21
click>=2.0
各个程序包重复执行以下命令解压编译，xxx需要替换成相应的包名

$ tar -zxf xxx.tar.gz
$ cd xxx
$ python setup.py install
$ pip list
安装Flask
Flask是用Python进行web开发时，常见的python web框架。
 下载地址：Download Flask
上传程序包到服务器
选择自己熟悉的工具上传或者如果服务器可以上外网则可使用wget直接下载
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-r--r--.  1 root  root    548510 9月   7 12:27 Flask-0.12.2.tar.gz
解压编译程序包
安装依赖顺序把程序包解压到~目录并编译
$ tar -zxf Flask-0.12.2.tar.gz
$ cd Flask-0.12.2
$ python setup.py install
$ pip list | grep Flask
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
Flask (0.12.2)
测试
$ vi test.py
# -*- coding:utf-8 -*-

#解决代码中的中文报错
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


current_stat = ""


@app.route("/<username>", methods=['GET'])
def hello_with_username(username):
    return "Hello " + username + "!"


@app.route("/itsyc/openstack", methods=['GET'])
def openstack():
    global current_stat

    action = request.args.get('action')
    step = current_stat + "|" + action

    if "|create" == step:
        current_stat = "running"
    elif "running|suspend" == step:
        current_stat = "suspended"
    elif "running|pause" == step:
        current_stat = "paused"
    elif "suspended|resume" == step:
        current_stat = "running"
    elif "paused|unpause" == step:
        current_stat = "running"
    elif "running|stop" == step:
        current_stat = "stop"
    else:
        return "error"
    return current_stat

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
$ python test.py
$ curl http://127.0.0.1:5000/itsyc/openstack?action=create
running
ORM 集成
SQLAlchemy 包是 Python 语言的一个 ORM 包，支持多种数据库。
 依赖包有：

SQLAlchemy
Flask-SQLAlchemy
PyMySQL
下载地址：https://pypi.python.org/pypi/xxx
上传程序包到服务器
选择自己熟悉的工具上传
上传结果：
$ pwd
/home/user1
$ ll
总用量 21584
-rw-r--r--.  1 root  root    100736 9月   7 15:02 Flask-SQLAlchemy-2.2.tar.gz
-rw-r--r--.  1 root  root     71095 9月   7 15:03 PyMySQL-0.7.11.tar.gz
-rw-r--r--.  1 root  root   5183519 9月   7 14:32 SQLAlchemy-1.1.14.tar.gz
解压编译程序包
安装依赖顺序把程序包解压到~目录并编译 依赖包安装顺序：
SQLAlchemy
Flask-SQLAlchemy
PyMySQL
各个程序包重复执行以下命令解压编译，xxx需要替换成相应的包名

$ tar -zxf xxx.tar.gz
$ cd xxx
$ python setup.py install
$ pip list
