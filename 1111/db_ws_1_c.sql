# 장르를 기준으로 그룹화
SELECT 
  genre, count() AS count
FROM
  songs
GROUP BY
  genre;
