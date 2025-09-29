<?php
if (isset($_GET['page'])) {
    highlight_file(__FILE__);
    include($_GET['page']);
} else {
    // redirect to /?page=welcome.php
    header("Location: /?page=welcome.php");
    exit();
}
?>