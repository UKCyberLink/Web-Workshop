<?php

require __DIR__ .'/../vendor/autoload.php';

use Snipe\BanBuilder\CensorWords;

$profanity = new CensorWords();

echo '<p>This is santised for your safety as you can see everyones messages</p>';
echo '<p> enjoy the group chat FLAG{ORUURNDNSJEJR}</p>';
$file = __DIR__ . '/../data.txt';
if (file_exists($file)) {
    $lines = file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    echo "<h3>Comments:</h3>";
    echo "<ul>";
    foreach ($lines as $line) {
        // Filter the comment to remove bad words
        $cleanLine = $profanity->censorString($line);
        echo "<li>" . htmlentities($cleanLine['clean'], ENT_QUOTES, 'UTF-8') . "</li>";
    }
    echo "</ul>";
}
echo '<a href="/index.html">Back to Home</a>';
?>