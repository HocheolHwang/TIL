CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 열 순서와 값 순서가 일치하지 않음
INSERT INTO
  zoo
VALUES 
  ('gorilla', 'omnivore', 180, 210, 5);

-- 2) rowid의 UNIQUE 제약 조건에 위배됨
INSERT INTO
  zoo (name, eat, weight, age)
VALUES
  ('dolphin', 'carnivore', 210, 3),
  ('alligator', 'carnivore', 250, 50);

-- 3) weight의 NOT NULL 제약 조건에 위배됨
INSERT INTO
  zoo (name, eat, weight, age)
VALUES
  ('dolphin', 'carnivore', 210, 3);
