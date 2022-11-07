//声明函数
function test(btn){
		//获取button按钮对象value值
		var num = btn.value;
		// alert(num);	
		// 根据用户点击执行对应的业务逻辑
	switch (num){
		case "=":
			// alert(typeof document.getElementById("inp").value);
			// 查看一下字符是什么类型
			document.getElementById("inp").value=eval(document.getElementById("inp").value);
			// eval通过字符串直接把数字转换成可计算的代码列如12+12=24
			// 直接执行成可执行的JavaScript代码
			break;
		case "c":
			document.getElementById("inp").value="";
			// 给按钮C赋值清楚功能
			break;
		default:
			//将按钮的值赋值给input输入框
			document.getElementById("inp").value=document.getElementById("inp").value+num;
			// 追加value值
			break;
	}
}
