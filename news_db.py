#! /usr/lib/python2.7
import psycopg2

# Connect database
conn = psycopg2.connect(database="news")

# Open a cursor to perform database operations
c = conn.cursor()

# Query for get the most view articles
c.execute("select count(path) as sum, articles.title from log join articles on log.path = CONCAT('/article/', articles.slug) group by articles.title order by sum desc limit 3")  # noqa
results = c.fetchall()

print("Most view articles:")
# loop for get all results
x = 0
for item in results:
    print(results[x][1] + " - " + str(results[x][0]) + " views")
    x = x + 1

print("\nLoading more data... \n")
# Query for get the most popular authors
c.execute("select count(path) as sum, authors.name from log join articles on log.path = CONCAT('/article/', articles.slug) join authors on articles.author = authors.id group by authors.name order by sum desc")  # noqa
results = c.fetchall()

print("Most popular authors:")
# loop for get all results
x = 0
for item in results:
    print(results[x][1] + " - " + str(results[x][0]) + " views")
    x = x + 1

print("\nLoading more data... \n")
# Query for getting days with more than 1% of error rate
c.execute("CREATE or REPLACE VIEW error_view as SELECT time::date, count(status) as requests, status FROM log WHERE status != '200 OK' group by time::date, status")  # noqa
c.execute("CREATE or REPLACE VIEW success_view as SELECT time::date, count(status) as requests, status FROM log WHERE status = '200 OK' group by time::date, status")  # noqa
c.execute("SELECT success_view.time, error_view.requests / success_view.requests::float as rate from success_view, error_view where success_view.time = error_view.time and error_view.requests / success_view.requests::float >= 0.01")  # noqa
results = c.fetchall()

print("Days with more than 1% of error rate:")
# loop for get all results
x = 0
for item in results:
    day = results[x][0].strftime("%d")
    month = results[x][0].strftime("%B")
    year = results[x][0].strftime("%Y")
    error_rate = "{:.2%}".format(results[x][1])
    print(month + " " + day + ", " + year + " - " + error_rate + " errors")
    x = x + 1

print("\nEnd of report.")

# closing the connection with DB
conn.close()