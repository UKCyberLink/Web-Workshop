<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $feedback = $_POST['feedback'];

    if (stripos($feedback, '<script') !== false) {
        echo "<p style='color: red;'>Congrats your blind attack worked! FLAG{BVJDSKOWORNF}</p>";
    }
    // You can add code here to save the data to a database or send an email

    // Display confirmation message
    echo "<h2>Thank you for your feedback!</h2>";
    echo "<p>We have received your feedback.</p>";

}
?>