CREATE TABLE users (
  PK INTEGER PRIMARY KEY AUTOINCREMENT,
  email VARCHAR(50) NOT NULL UNIQUE,
  name VARCHAR(50) NOT NULL,
  age INTEGER NOT NULL,
  phoneNumber INTEGER NOT NULL,
  gender INTEGER,
  address VARCHAR(100) NOT NULL DEFAULT 'no address'
);

-- Column 이름 변경
ALTER TABLE
  users
RENAME COLUMN
  phoneNumber TO number;


-- Table 삭제
DROP TABLE users;
