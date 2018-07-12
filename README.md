# News Report

This project is a Report a database which contain logs about a News website. It will answer 3 questions:
1 - Which pages have more views?<br />
2 - Who are the most popular author?<br />
3 - Which day has more than 1% of bad requests?<br />

To see the result of script, please open: script_result.txt

### Prerequisites

Vagrant and Virtual box installed in your Machine. (See this video for more information: https://www.youtube.com/watch?v=djnqoEO2rLc)


### Installing

How use

1. Clone
2. Reach the folder (using command line)
3. Type "vagrant up" to install Virtual Machine
```
vagrant up
```
4. Type "vagrant ssh"
```
vagrant ssh
``` 
5. Create Views (optional)
```
CREATE or REPLACE VIEW error_view as SELECT time::date, count(status) as requests, status FROM log WHERE status != '200 OK' group by time::date, status;
```

```
CREATE or REPLACE VIEW success_view as SELECT time::date, count(status) as requests, status FROM log WHERE status = '200 OK' group by time::date, status;
```

Obs. Don't worry about that view, you can run the program without it.

6. Run "python new_db.py"
```
python new_db.py
```

### Querys

Find the most view articles
```
SELECT count(path) as sum, articles.title from log JOIN articles on log.path = CONCAT('/article/', articles.slug) GROUP BY articles.title ORDER BY sum desc LIMIT 3
```

Find the most popular authors:
```
SELECT count(path) as sum, authors.name from log JOIN articles on log.path = CONCAT('/article/', articles.slug) JOIN authors on articles.author = authors.id GROUP BY authors.name ORDER BY sum desc;
```

View for bad requests:
```
CREATE or REPLACE VIEW error_view as SELECT time::date, count(status) as requests, status FROM log WHERE status != '200 OK' group by time::date, status;
```

View for success requests:
```
CREATE or REPLACE VIEW success_view as SELECT time::date, count(status) as requests, status FROM log WHERE status = '200 OK' group by time::date, status;
```

Joing views and finding days with more than 1% of error rate:
```
SELECT success_view.time, error_view.requests / success_view.requests::float as rate from success_view, error_view where success_view.time = error_view.time and error_view.requests / success_view.requests::float >= 0.01;
```


### And coding style tests

Usin Pep8 to coding style

```
http://pep8online.com/
```

## Developed With

* Python

## Versioning

Git for versioning.

## Authors

* **Felipe Mayer** - *https://github.com/felipemayer/* 

## License

There is no license.