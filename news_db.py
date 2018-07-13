#! /usr/bin/env python
import psycopg2

# Connect database
conn = psycopg2.connect(database="news")

# Open a cursor to perform database operations
c = conn.cursor()

# Query for get the most view articles
c.execute('''SELECT count(path) AS sum, articles.title 
    FROM log 
    JOIN articles ON log.path = CONCAT('/article/', articles.slug) 
    GROUP BY articles.title 
    ORDER BY sum desc 
    LIMIT 3''')  # noqa
results = c.fetchall()

print("Most view articles:")
# loop for get all results
x = 0
for item in results:
    print(results[x][1] + " - " + str(results[x][0]) + " views")
    x = x + 1

print("\nLoading more data... \n")
# Query for get the most popular authors
c.execute('''SELECT count(path) AS sum, authors.name 
    FROM log 
    JOIN articles ON log.path = CONCAT('/article/', articles.slug) 
    JOIN authors ON articles.author = authors.id 
    GROUP BY authors.name 
    ORDER BY sum desc''')  # noqa
results = c.fetchall()

print("Most popular authors:")
# loop for get all results
x = 0
for item in results:
    print(results[x][1] + " - " + str(results[x][0]) + " views")
    x = x + 1

print("\nLoading more data... \n")
# Query for getting days with more than 1% of error rate
c.execute('''CREATE or REPLACE VIEW error_view as 
    SELECT time::date, count(status) as requests, status 
    FROM log WHERE status != '200 OK' 
    GROUP BY time::date, status''')  # noqa
c.execute('''CREATE or REPLACE VIEW requests_view as 
    SELECT time::date, count(status) as requests 
    FROM log 
    GROUP BY time::date''')  # noqa
c.execute('''SELECT TO_CHAR(requests_view.time, 'Mon DD, YYYY'), error_view.requests / requests_view.requests::float as rate 
    FROM requests_view, error_view 
    WHERE requests_view.time = error_view.time 
    AND error_view.requests / requests_view.requests::float >= 0.01''')  # noqa
results = c.fetchall()

print("Days with more than 1% of error rate:")
# loop for get all results
x = 0
for item in results:
    error_rate = "{:.2%}".format(results[x][1])
    print(results[x][0] + " - " + error_rate + " errors")
    x = x + 1

print("\nEnd of report.")

# closing the connection with DB
conn.close()
