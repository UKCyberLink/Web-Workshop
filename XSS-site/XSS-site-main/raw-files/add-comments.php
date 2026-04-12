<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["comment"];

    // Check if input contains "<script>"
    if (stripos($name, '<script>') !== false) {
        echo "<p style='color: red;'>Congrats your reflected attack! 
        This server side is written in php - if you want to protect against this attack 
        you can use the htmlspecialcharacter function to sanitise. Heres your flag for your time: FLAG{FKSJRBGFHSJS}</p>";
        echo "<p>Your input: <code>$name</code></p>";
    }

    // The file where input will be saved
    $file = __DIR__ . '/../data.txt';

    // Check if file exists and is writable
    if (is_writable($file)) {
        // Append the input to the file with a new line
        file_put_contents($file, ($name . PHP_EOL), FILE_APPEND | LOCK_EX);
        echo "<p>✅ Your input has been saved!</p>";
    } else {
        echo "<p>⚠️ Error: The file is not writable!</p>";
    }
    echo '<a href="/index">Back to Home</a>';
}
?>