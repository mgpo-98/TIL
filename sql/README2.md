# 2일차 실습

## 사전 확인

### 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

### Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

### table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
    id PRIMARY KEY,        
    sido INTEGER NOT NULL, 
    gender INTEGER NOT NULL,
    age INTEGER NOT NULL,  
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    waist REAL NOT NULL,   
    va_left REAL NOT NULL, 
    va_right REAL NOT NULL,

    blood_pressure INTEGER 
    NOT NULL,
    smoking INTEGER NOT NULL,
    is_drinking BOOLEAN NOT NULL
);
```

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
sqlite> SELECT COUNT(*) FROM healthcare;
```
1000000
```
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
sqlite> SELECT max(age), min(age) FROM healthcare;
```
max(age)  min(age)
--------  --------
18        9
```
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql

SELECT max(height), min(height) FROM healthcare;
```
max(height)  min(height)
-----------  -----------
195          130
```
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare 
WHERE height >= 160 and height <= 170;
```
516930
```
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql

SELECT * FROM healthcare WHERE is_drinking like 1 
ORDER by waist DESC LIMIT 5;

```

```
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
SELECT count(*) FROM healthcare WHERE va_left >= 1.5 AND va_right >=1.5 AND is_drinking = 1;
```
36697
```
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
sqlite> SELECT count(*) FROM healthcare WHERE blood_pressure <120;
```
360808
```
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
SELECT avg(waist) FROM healthcare WHERE blood_pressure > 140;
```
85.8949840614261
```
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
sqlite> SELECT avg(height), avg(weight) FROM healthcare WHERE gender like 1 ;  
```
avg(height)       avg(weight)
----------------  ----------------
167.452735422145  69.7131620222875
```
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
SELECT id, height, weight FROM healthcare WHERE height = 195 AND
weight = 110 ;
```
id      height  weight
------  ------  ------
836005  195     110
sqlite>
```
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
sqlite> SELECT COUNT(*) FROM healthcare WHERE (weight*10000)/(height*height) >= 30;
```
53121
```
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql

SELECT id, (weight*10000)/(height*height) FROM healthcare WHERE smoking = 3 
ORDER BY (weight*10000)/(height*height) DESC LIMIT 5 ;

```
231431  50
934714  49
722707  48
947281  47
948801  47
```
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요. 
90 키로 초과 190 초과인 사람의 몸무게와 키

```sql
SELECT weight, height FROM healthcare WHERE weight > 90 and height >190 ;
```
weight  height
------  ------
95      195
100     195
105     195
105     195
100     195
105     195
105     195
125     195
105     195
100     195
95      195
110     195
100     195
100     195
```
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.
평균 몸무게 나이 키
```sql
SELECT avg(weight), avg(age), avg(height) FROM healthcare;
```
avg(weight)  avg(age)   avg(height)
-----------  ---------  -----------
63.06079     11.917757  160.964085
```
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.
흡연자의 수
```sql
SELECT count(*) FROM healthcare WHERE smoking = 1;
```
626138

```
```