Test task

For lauch the application need:
1. clone repository
```bash
    git clone https://github.com/NeverEverLive/test_task_documents.git
```
2. create .env file from example or use my file: <br />
    Example
```
    POSTGRES_USER = nel
    POSTGRES_PASSWORD = 123
    POSTGRES_SERVER = database  #'localhost'# 
    POSTGRES_PORT = 5432
    POSTGRES_DB = document_test
```
3. build and run containers:
```bash
    docker-compose up --build
```
4. Load data to database:
```bash
    cat document_test.sql | sudo docker exec -i postgres psql -U <POSTGRES_USER> <POSTGRES_DB>
```
if use my file:
```bash
    cat document_test.sql | sudo docker exec -i postgres psql -U nel document_test
```

### This completes the project setup.

Test task.postman_collection.json - file with JSON requests <br />
document_test.sql - file for load data to database
