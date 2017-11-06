# 个人工作脚本集合


## 001 卸载NodeJs脚本
事项         | 备注           |
--------------------|------------------|
脚本语言     | SHELL|
适用系统 | MacOS|
推荐使用场景  | NodeJS出现不可控制错误； 卸载升级等情况|
注意事项     | 需要root运行 |
### 1.1 为什么写

   在工作中需要NodeJs安装一些插件，但是配置过程中（使用国内源及其他步骤）出现错误，无法排查错误，只能卸载，但是NodeJs的文件夹及其杂乱，所以只能写一个脚本把它们一次性删除干净

### 1.2 使用说明

```
# 不需要后台，删的非常快
root sh uninstall_nodejs.sh
```


## 002 拷贝目录并忽略其中的log文件
事项         | 备注           |
--------------------|------------------|
脚本语言     | Python|
适用系统 | Linux|
推荐使用场景  | 需要拷贝目录但是需要过滤某些文件（本脚本内为Log）|
注意事项     | 如果需要过滤其他文件只需要修改第11行的正则表达式就行了 |
### 1.1 为什么写
   2017年11月6日，我需要将worker@10.101.2.27的searcher模块拷贝到另外的一台机器上，然后在另外一台机器上运行 searcher, 简单来说就是把目标文件夹 /home/services/ 搬运到services@10.111.0.54 上，然后运行 start.sh就行了，看起来很简单，直接使用scp就好了，但是出现几个问题  
   
   1. log文件非常多非常大， 总文件夹有104G, 而电脑的剩余空间有限，80多G
   2. log文件不止一处，不排除未知的位置
   3. log文件有两个格式 log.1, abc.log.1, 无法通过shell后缀名判断

所以选择采用了 Python, 基本方法就是遍历文件夹，所有文件名前缀修改为我们的目的地址就可以了, 最后发现有效文件只有123M
    
   

### 1.2 使用实例

```
# 查看帮助
$ python cdwl.py -h
Usage: cdwl.py [options]

Options:
  -h, --help                  show this help message and exit
  -s SRCDIR, --src=SRCDIR     please input source directory
  -d DESTDIR, --dest=DESTDIR  please input destination directory
                        
# 使用实例
$ python cdwl.py -s /home/service  -d /home/service/bak_dir

# 不会有循环引用的错误，脚本先获取列表再建立新的bak_dir，放心使用                      
# 排除了 test.log  test.log.123  log.123等格式
```










-----
## 00x 模板
事项         | 备注           |
--------------------|------------------|
脚本语言     | |
适用系统 | |
推荐使用场景  | |
注意事项     |  |
### 1.1 为什么写

   abc

### 1.2 使用实例

```
# 使用实例
```

