### Intro

Point blog post

### Requirements

Dtsql requires Python and scikit-learn.

##### Demo

To run dtsql locally,

`python dtsql.py sample/iris.csv`

##### Running demo from docker
```
docker run ainsight...
docker login
python dtsql.py sample/iris.csv
```

##### Demo output

You will see an output ,

```sql
CASE WHEN PetalLength <= 2.45000004768 THEN 
  'Iris-setosa'
ELSE
  CASE WHEN PetalWidth <= 1.75 THEN 
    CASE WHEN PetalLength <= 4.94999980927 THEN 
      CASE WHEN PetalWidth <= 1.65000009537 THEN 
        'Iris-versicolor'
      ELSE
        'Iris-virginica'
      END
    ELSE
      'Iris-virginica'
    END
  ELSE
    CASE WHEN PetalLength <= 4.85000038147 THEN 
      'Iris-virginica'
    ELSE
      'Iris-virginica'
    END
  END
END
```

### Training
To train on your own data, you have to first fetch 
```
cd sample/mysql
127.0.0.1 ainsight root password "select * from iris" 
```
