<?php

$id = $_GET['id'];
$content = $_GET['content'];
$content2 = $_GET['content2'];
$filename = $_GET['filename'];

$fp = fopen($filename . '.csv','a');
ini_set('auto_detect_line_endings',TRUE);

$line = array($id,$content,$content2,0,0);

fputcsv($fp, $line);

fclose($fp);

?>