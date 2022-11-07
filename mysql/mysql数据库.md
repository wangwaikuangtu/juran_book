### mysql数据库

+ 启动与停止

  1. services.msc

     + 启动

       > net start mysql80

       + 停止

         > net stop mysql80





##### 客户端

+ 客户端连接

  1. 使用mysql提供使用的端口命令行工具

     MySQL 8.0 Command Line Client

  2. widows系统自带的命令行工具执行指令

     > mysql[-h 127.0.0.1][-p 3306] -u root -p



##### sql分类

DDL：数据定义语言，用来定义数据库对象（数据库，表，字段）。

DML：数据操作语言，用来对数据表中的数据进行增改删。

DQL：数据查询语言，用来查询数据库中表的记录

DCL：数据控制语言，用来创建数据库用户、控制数据库的访问权限。



##### DDL-数据库操作

+ 查询所有数据库

  > show databases;

  1. 查询当前数据库

  > select database();

  2. 创建

  > create database [if not exists] 数据库 [default charset字符集] [collate 排序规则];
  >
  > （注） [if not exists] 如果这个数据库名存在那么不做任何动作，如果不存在则创建

  3. 删除

     > drop database[if exists]数据库名;

  4. 使用

     > use 数据库名；