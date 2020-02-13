# Tracker API
An api for all kind of tracking. The initial idea was track money daily transactions for personal financial control. 
After that, I realized that this very same structure could track my wifi connections (login, logout, elapsed time) for organizational purposes.

For now, nothing yet is implemented.

# TODO
## Step 1
Implement the business transactions for track a money entry or wifi connection/disconnection. For this first time, I'll persist data on text files, one for each transaction

## Step 2
Implement a simple database. It could be a SQLite for the beginning and then grow for another database.

## Step 3
Implement multi-threading behavior for the persistence layer using some queue like zeroMQ or RabbitMQ. This step is just for study purpose.

## Step 4
Make some performance tests. I could compare with or without the multi-threading feature, just for fun.

