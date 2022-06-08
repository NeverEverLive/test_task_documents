Test task

For lauch the application need:
1. clone repository
'''
    git clone https://github.com/NeverEverLive/test_task_documents.git
'''
2. create .env file from example or use my file:
    Example
'''
    POSTGRES_USER = nel
    POSTGRES_PASSWORD = 123
    POSTGRES_SERVER = database  #'localhost'# 
    POSTGRES_PORT = 5432
    POSTGRES_DB = document_test
'''
3. build and run containers:
'''
    docker-compose up --build
'''
4. Load data to database:
'''
    cat document_test.sql | sudo docker exec -i postgres psql -U <POSTGRES_USER> <POSTGRES_DB>
'''
if use my file:
'''
    cat document_test.sql | sudo docker exec -i postgres psql -U nel document_test
'''

#######This completes the project setup.