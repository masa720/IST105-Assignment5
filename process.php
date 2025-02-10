<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = $_POST["number"];
    $text = $_POST["text"];

    $command = escapeshellcmd("python3 process.py " . escapeshellarg($number) . " " . escapeshellarg($text));
    $output = shell_exec($command);

    echo nl2br($output);
}
?>
