CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO
  zoo
VALUES 
  ('gorilla', 'omnivore', 215, 180, 5),
  ('tiger', 'carnivore', 220, 115, 3),
  ('elephant', 'herbivore', 3800, 280, 10),
  ('dog', 'omnivore', 8, 20, 1),
  ('panda', 'herbivore', 80, 90, 2),
  ('pig', 'omnivore', 70, 45, 5);



BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;
BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;


-- ROLLBACK은 이전 상태로 되돌리고,
-- COMMIT은 트랜잭션을 완료하여 변경 사항을 영구적으로 저장한다.

-- 따라서 BEGIN과 ROLLBACK 사이의 DELETE 문에 의한 변경 사항은 저장되지 않고,
-- BEGIN과 COMMIT 사이의 DELETE문에 의한 변경 사항만 저장된다.

-- 따라서 eat = 'omnivore'인 세 개의 행이 사라지고,
-- 남은 행이 3개이므로 COUNT(*) 결과로 3이 출력된다.