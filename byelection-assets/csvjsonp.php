<?php
header("Content-Type: application/json");
$filename = $_GET['filename'];

$return = $_GET['callback'] .'(' . '[';
$fp = fopen($filename . '.csv','r');

ini_set('auto_detect_line_endings',TRUE);
$k = 0;
$newData = array();
$columns = array();
while($data = fgetcsv($fp,1000,',')){
	$j = 0;
	if($k>1) $return .= ',';
	if($k > 0){
	$return .= '{';
		foreach($data as $d){
			$return .=  "'" . $columns[$j] . "':'" . $d . "'";
			if($j != count($data)-1){
				$return .= ',';
			}
			$j++;
		}
	$return .= '}';
	} else {
		foreach($data as $d){
			array_push($columns,$d);
		}
	}
	$k++;
}
$return .= ']' . ')';
echo $return;
fclose($fp);
//}
?>