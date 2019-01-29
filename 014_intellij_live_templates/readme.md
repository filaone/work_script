# IntelliJ Live Templates

> [IntelliJ Live Templates介绍](https://www.jetbrains.com/help/idea/2018.3/edit-template-variables-dialog.html?utm_content=2018.3&utm_medium=link&utm_source=product&utm_campaign=IU)

## 1. 创建单例
- 快捷键名称: csingleton

### 1.1 模板代码
```
private static class SingleHolder{ private static final $CLASS_NAME$ INSTANCE = new $CLASS_NAME$();}
    
public static $CLASS_NAME$ getInstance() {
    return SingleHolder.INSTANCE;
}
    
private $CLASS_NAME$(){
    $END$
}
```
### 1.2 变量声明
- CLASS_NAME : `className()`

###1.3 应用范围
- Java-Declaration

## 2. 创建类起始注释
- 快捷键名称: cinfo

### 2.1 模板代码
```
/**
* 
* @author wangshuguang
* @date   $DATE$
*/
```
### 2.2 变量声明
- DATE : `date("yyyy/MM/dd")`

### 2.3 应用范围
- Java-Declaration


