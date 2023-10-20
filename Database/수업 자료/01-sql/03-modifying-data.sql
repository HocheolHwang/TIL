CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content CARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

-- 조회
PRAGMA table_info('articles');


INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', '2000-01-01'),
  ('title2', 'content2', '2000-01-01'),
  ('title3', 'content3', '2000-01-01');


INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title4', 'content4', '2000-01-01');





UPDATE
  articles
SET
  title = '바뀌냐?'
WHERE
  id = 1;


UPDATE
  articles
SET
  createdAt = '2025-01-01'
WHERE
  id = 4;



-- 내림차순 정렬
SELECT * FROM
  articles
ORDER BY id DESC;


-- 레코드 지우기
DELETE FROM
  albums
WHERE
  AlbumId = 5;

SELECT * 
FROM albums;


DELETE FROM articles
WHERE createdAt IN (
  SELECT createdAt
  FROM articles
  ORDER BY createdAt DESC
  LIMIT 2
);
