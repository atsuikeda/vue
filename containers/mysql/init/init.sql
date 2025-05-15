#!/bin/bash

-- データベース作成
CREATE DATABASE IF NOT EXISTS mydb;

-- ユーザー作成
CREATE USER 'user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mydb.* TO 'user'@'%';

-- テーブル作成
USE mydb;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);