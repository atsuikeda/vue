#!/bin/bash

-- データベース作成
CREATE DATABASE IF NOT EXISTS mydb;

-- 既存のユーザーを削除（存在する場合）
DROP USER IF EXISTS 'user'@'%';

-- ユーザー作成
CREATE USER 'user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mydb.* TO 'user'@'%';
FLUSH PRIVILEGES;

-- テーブル作成
USE mydb;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);