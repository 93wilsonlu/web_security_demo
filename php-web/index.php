<?php
show_source(__FILE__);
if (isset($_FILES["file"])) {
  $target_dir = "files/" . md5(time()) . '/';
  if (!is_dir($target_dir)) {
    mkdir($target_dir);
  }
  $target_file = $target_dir . $_FILES["file"]["name"];

  if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
    echo "上傳成功! <a href=\"" . htmlspecialchars($target_file) . "\">" . htmlspecialchars($target_file) . "</a>";
  } else {
    echo "上傳失敗";
  }
}
?>

<html>

<head></head>

<body>
  <h1>VERY VERY SECURE Image Upload Platform 😎😎</h1>
  <form method="post" enctype="multipart/form-data">
    <input type="file" name="file" />
    <button class="button" type="submit">Upload</button>
  </form>
</body>

</html>