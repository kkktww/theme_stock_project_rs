import duckdb

conn = duckdb.connect("data.duckdb")

conn.execute("""

CREATE TABLE Theme(

theme_id INTEGER PRIMARY KEY,

theme_name VARCHAR,

description VARCHAR

)

""")

conn.execute("""

INSERT INTO Theme
VALUES
(
1,
'AI',
'인공지능'
)

""")

print("완료")

import duckdb

conn=duckdb.connect(
"data.duckdb"
)

conn.execute("""

ALTER TABLE Theme

ADD COLUMN image_path VARCHAR

""")

conn.execute("""

UPDATE Theme

SET image_path='images/ai.png'

WHERE theme_id=1

""")

print("이미지 경로 저장 완료")