# News Report

This project is a Report a database which contain logs about a News website. It will answer 3 questions:<br />
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