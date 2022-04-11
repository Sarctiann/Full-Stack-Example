# test-project
##### comparaencasa

1. ## To RUN the project just type: ```sh docker-compose up``` on the terminal

1. ### Then, you must inizialize the database table cars and load the test data set go to URI: ```localhost:5000/initialize```.
    You might change the data set on the file ```backend/src/test_data/TEST_DATA.csv``` and run "initialize" again.
    > (Note that plate was defined as UNIQUE field so if the records already exist in the table they will not be reloaded naturally)

1. ## To be continue ...

---

### considerations to be care

* To be able to use "flask-mysql-db" we need to install some extra APKs in ours image
* mysql python connector use "unix sockets" instead of "TCP"

### Some help with the above

* [FLASK-MYSQL](https://stackoverflow.com/questions/56048631/docker-alpine-error-loading-mysqldb-module)
* [MYSQL-PYTHON-CONNECTION](https://stackoverflow.com/questions/58029324/2002-cant-connect-to-local-mysql-server-through-socket-run-mysqld-mysqld-so)

#### Other help

* [To glue front and back](https://www.youtube.com/watch?v=4qYRs0Yzh9I)

### Documentation and tutorials 

* [docker (Video)](https://www.youtube.com/watch?v=6idFknRIOp4)
* [docker-compose (docs)](https://docs.docker.com/compose/gettingstarted/)
* [python-redis](https://redis-py.readthedocs.io/en/latest/examples/set_and_get_examples.html?highlight=set)

> I never had used docker or redis before this time.

---
