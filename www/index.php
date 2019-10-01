<?php
$parts = (parse_url(getenv('DATABASE_URL') ?: 'postgres://isneqpdtrrraup:d6f221a93bf2e038e37179cf4e0d4a18c321241340b0bf4368439fa212fc9b06@ec2-176-34-183-20.eu-west-1.compute.amazonaws.com:5432/delcjv8nidnnch'));
extract($parts);
$path = ltrim($path, "/");
$connect = new PDO("pgsql:host={$host};port={$port};dbname={$path}", $user, $pass);
?>