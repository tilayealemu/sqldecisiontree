### Intro

The idea of dtsql is to take data from a database, train a decision tree
on it, format the decision tree in the form a SQL and then run the SQL
on a database to predict the column of your choice.

For more information see this two-part blog post,
 - [Part 1](http://ainsightful.com/index.php/2016/12/05/decision-tree-and-sql-part-1-decision-trees/)
   Decision trees
- [Part 2](http://ainsightful.com/index.php/2017/01/23/decision-tree-and-sql-part-2-sql-as-decision-tree/)
   SQL as decision tree

### Requirements

Dtsql requires Python and scikit-learn.

##### Demo

To run dtsql locally,

`python dtsql.py sample/iris.csv`

You can also pull the demo docker image to play with it,
```
docker run tilayealemu/dtsql
docker run -i -t tilayealemu/dtsql /bin/bash
python dtsql.py sample/iris.csv
```

### Training
Use csv files to train a data. Have your target in the last
column. For example in the iris data the column to predict
is `Name`. All columns except the last one will be used
to train the decision tree model.

```
SepalLength,SepalWidth,PetalLength,PetalWidth,Name
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
6.4,3.2,4.5,1.5,Iris-versicolor
```

### Getting training data
There is a helper script to fetch training data from your database 
and put it in a csv. At the moment only mysql is supported. But you
can easily tweak the script for other databases.

```
cd helper
python fetch_mysql.py mymysqlserver mydbname myuname mypassword "select * from table" 
```

Write your query such that
- Columns that are completely unrelated to your target column are removed.
  When in doubt though better to keep columns than remove them.
- Your target column is selected in the end

###### Example
Suppose you have these columns and you want to predict `average_temperature`.

    day_of_week, sunny_or_not, average_temperature, month,order_id

- Leave out day of week and order ID. They are unlikely to be useful 
- Put temperature column in the end.

So the query becomes,
```
python fetch_mysql.py mymysqlserver mydbname myuname mypassword "select sunny_or_not, month, average_temperature from table" 
```

Which will output `training.csv`. Then run dtsql on it,

    python dtsql.py training.csv
