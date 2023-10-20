CREATE TABLE examples (
  ExamID INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL,
);


-- Table의 열 정보 조회
PRAGMA table_info('examples');


-- Column 추가
ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL DEFAULT VALUE;

ALTER TABLE
  examples
ADD COLUMN
  Age INTEGER NOT NULL DEFAULT VALUE;

ALTER TABLE
  examples
ADD COLUMN
  Address VARCHAR(100) NOT NULL DEFAULT VALUE;


-- Column 이름 변경
ALTER TABLE
  examples
RENAME COLUMN
  Address TO PostCode;


-- Column 삭제
ALTER TABLE
  examples
DROP COLUMN
  PostCode;

-- Table 삭제
DROP TABLE examples;