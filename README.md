# sample-flask-sqlalchemy
Sample set up for Flask + SQLAlchemy + py.test + factory_boy with multiple-database


```
$ brew install postgresql
$ initdb /usr/local/var/postgres -E utf8
$ postgres -D /usr/local/var/postgres
```


```
$ psql -d template1
> CREATE ROLE app WITH CREATEDB LOGIN PASSWORD 'dev';
> CREATE DATABASE db1 OWNER app;
> CREATE DATABASE db2 OWNER app;
> CREATE DATABASE t_db1 OWNER app;
> CREATE DATABASE t_db2 OWNER app;
```


```
$ mkvirtualenv sqla
$ wrokon sqla
$ pip install -r requirements.txt
```

```
$ py.test -vs application/tests
```
