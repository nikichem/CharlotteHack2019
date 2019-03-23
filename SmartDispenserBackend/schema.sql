DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS machine;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  userName TEXT NOT NULL,
  points INTEGER NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE machine (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  address TEXT NOT NULL,
  contentType TEXT NOT NULL,
  maintenancePersonnel TEXT NOT NULL,
  maintenancePersonnelEmail TEXT NOT NULL,
  missing INTEGER,
  empty INTEGER
);
