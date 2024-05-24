CREATE DATABASE ouvidoria CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE ouvidoria;

CREATE TABLE manifestacoes(
 id INT,
 descricao VARCHAR(255),
 tipo VARCHAR(12),
 PRIMARY KEY(id)
);