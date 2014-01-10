<?php
error_reporting(-1);

$filename = $_GET['filename'];

$fp = fopen($filename . '.csv','r');
ini_set('auto_detect_line_endings',TRUE);

$k = 0;
$newData = array();

while($data = fgetcsv($fp,1000,',')){
	if($k==1) $data[2] = $data[2]+1;
	$k++;
	array_push($newData,$data);
}
fclose($fp);
$fp = fopen('electiondata.csv','w');
foreach($newData as $newD){
	fputcsv($fp,$newD);
}


//	

//;

fclose($fp);

echo 'finish';
?>