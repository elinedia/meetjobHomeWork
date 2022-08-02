<?php

/*
陣列 array
全聯一盒雞蛋:12個
在這個盒子中,12位置,我選擇都不放or放1個or放5個or全放。
但不可以超過12個。
*/

$student = array("王曉明","陳美麗","李聰明","羅玉兔","蔡筱英");//array(0,1,2,3,4)位置
echo $student[0];
echo "<br>";
echo $student[3] . "<br>";
echo "<hr>";//html的分隔線
//一般的for loop 抓取值

for($i = 0 ; $i < 5 ; $i++){
	echo $student[$i] . "<br>";
}

echo "<hr>";

//foreach 是php用來輸出陣列方式使用的
//使用上來得比較快且直覺
//結構: foreach(陣列名稱 as $var){  
	//echo $var
//		}
foreach( $student as $value){ //請依陣列值順序給予變數(曉明>美麗>聰明>玉兔>筱英)
	echo $value . "<br>";
}


?>