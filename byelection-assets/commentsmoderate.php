<style>
table tr.even td{
	background-color:#ececec;
}
</style>
<?php
error_reporting(-1);

$fp = fopen('torontotraffic.csv','r');
ini_set('auto_detect_line_endings',TRUE);

$k = 0;
$newData = array();

echo '<table style="width:620px;margin:0 auto">';
while($data = fgetcsv($fp,1000,',')){
	if($k == 0){
		echo '<thead><tr>';
	} else {
		echo '<tr>';
	}
	$j = 0;
	foreach($data as $d){
		echo count($data);
		if($k == 0){
			echo '<th>' . $d . '</th>';
		} else {
			if($j == count($data)-1){
				echo '<td><input type="text" value="' . $d . '" /></td>';
			} else {
				echo '<td>' . $d . '</td>';
			}
		}
		echo $content;
		$j++;
	}
	if($k == 0){
		echo '<thead><tr>';
	} else {
		echo '</tr>';
	}
	$k++;
}
echo '</table>';
//	
echo '<input type="submit" value="Submit" />';
//;

fclose($fp);

?>