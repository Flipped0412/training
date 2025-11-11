# 모든 데이터
SELECT * FROM songs;

# 제목 기준 내림차순 정렬
SELECT * FROM songs
ORDER BY
title DESC

# 특정 장르만 조회
SELECT * FROM songs
where genre is 'Pop'

# 시간이 3분 이상
SELECT * FROM songs
where duration >= 180;
