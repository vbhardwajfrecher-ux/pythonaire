
<<<#1#1#1#1#################################### returns them in JSON format ##############################################################
"""
Implement a RESTful API endpoint in Python
that retrieves a list of users from a PostgreSQL database
and returns them in JSON format.
"""
################# CODE 1 ################

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# database connection settings
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

@app.route('/users', methods=['GET'])


def get_users():
    # create a cursor object to execute SQL queries
    cur = conn.cursor()

    # execute a SQL query to retrieve all users from the database
    cur.execute("SELECT * FROM users")

    # fetch all results and convert them to a list of dictionaries
    rows = cur.fetchall()
    users = []
    for row in rows:
        user = {
            'id': row[0],
            'name': row[1],
            'email': row[2]
        }
        users.append(user)

    # close the cursor and database connection
    cur.close()
    conn.close()

    # return the list of users as a JSON response
    return jsonify(users)


#### Another method for faster execution ####
"""
>>> Use a connection pool: 
    Creating a new database connection for each request can be expensive. 
    A connection pool can help reduce the overhead of creating new connections by reusing existing connections from a pool. 
    You can use a library like psycopg2.pool to create a connection pool.

>>> Use pagination: 
    If the number of users in the database is large, 
    fetching all the results at once can be slow and consume a lot of memory. 
    You can use pagination to fetch a limited number of results at a time and return them to the client. 
    This can improve the performance of the API and reduce the memory footprint. 
    You can use the LIMIT and OFFSET clauses in the SQL query to implement pagination.

>>> Use a database ORM: 
    Using an ORM (Object-Relational Mapping) library can simplify the code for interacting 
    with the database and make it more readable and maintainable. 
    An ORM can also provide features like query building, schema migration, and data validation. 
    You can use a library like SQLAlchemy to implement an ORM.
"""
################ CODE 2 ##################

from flask import Flask, jsonify, request
from psycopg2 import pool
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

# database connection settings
db_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host="localhost",
    database="mydatabase",
    user="myusername",
    password="mypassword"
)

# SQLAlchemy settings
engine = create_engine('postgresql://myusername:mypassword@localhost/mydatabase')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    offset = (page - 1) * per_page

    # get a connection from the connection pool
    conn = db_pool.getconn()

    # create a session for interacting with the database using SQLAlchemy
    session = Session()

    # query the database using SQLAlchemy and apply pagination
    users = session.query(User).limit(per_page).offset(offset).all()

    # convert the list of users to a list of dictionaries
    users_dict = [user.__dict__ for user in users]
    for user in users_dict:
        user.pop('_sa_instance_state')

    # release the connection back to the connection pool
    db_pool.putconn(conn)

    # return the list of users as a JSON response
    return jsonify(users_dict)

"""
Time and Space Complexity
"""
#The time complexity of this code is O(N) 
# since it retrieves a limited number of users based on the pagination parameters provided in the query string.

# The space complexity of this code is O(N) since it creates a list of dictionaries to 
# hold the retrieved user information, where N is the number of users returned by the query. 
# However, it should be noted that the memory usage can be reduced 
# by removing the SQLAlchemy internal dictionary representation of each user object using the pop method.
>>>




<<<#2#2#2#2############################### returns the sum of all even numbers in the slice ##############################################
"""
Write a python function that takes a slice of integers
as input and returns the sum of all even numbers in the slice.
"""

############### CODE 1 ###############
def sum_even_numbers(numbers):
    
#Returns the sum of all even numbers in the input slice.
    
    return sum(filter(lambda x: x % 2 == 0, numbers))
    
# A lambda function is an anonymous function that is defined without a name. 
# It can have any number of parameters, but can only have one expression. 
# Lambda functions are often used as a shorthand for simple functions 
# or as arguments to higher-order functions that expect a function as input.    
    
"""
This function uses the built-in sum function and the filter function to compute the sum of all even numbers in the input slice. The filter function takes a lambda function that returns True for even numbers and False otherwise. The sum function then adds up all the even numbers returned by the filter function.
"""
############# CODE 2 ###############
def is_even(number):
    """
    Returns True if the input number is even, False otherwise.
    """
    return number % 2 == 0

def sum_even_numbers(numbers):
    """
    Returns the sum of all even numbers in the input slice.
    """
    return sum(filter(is_even, numbers))
>>>




<<<
#3#3#3#3######################################## returns the string reversed #############################################################

"""
Implementing Python function that takes a string
as input and returns the string reversed.
"""
############# CODE 1 ############

def reverse_string(input_string):
    """
    Returns the reversed string of the input string.
    """
    return input_string[::-1]

#function uses Python's string slicing syntax to reverse the input string. 
# The [::-1] syntax means to start at the end of the string and move backwards, 
# with a step of -1 (i.e. go backwards one character at a time). 
# This effectively reverses the order of the characters in the string.

########### CODE 2 ##############

def reverse_string(string):
    return ''.join(reversed(string))

################# CODE 3 ###########

def reverse_string(string):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

########### CODE 4 ############

def reverse_string(string):
    reversed_string = ''
    i = len(string) - 1
    while i >= 0:
        reversed_string += string[i]
        i -= 1
    return reversed_string

############ CODE 5 ############

def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

>>>




<<<
#4#4#4#4#4################################# reads a file from disk, removes all duplicates ################################################
"""
Write a python program that reads a file from disk, removes all duplicates and writes the unique lines back to disk.
"""

############# CODE 1 ################

def remove_duplicates(input_file, output_file):
    """
    Reads a file from disk, removes all duplicates and writes the unique lines back to disk.
    """
    # read input file into a list
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # remove duplicates by creating a set and then converting it back to a list
    unique_lines = list(set(lines))

    # write unique lines to output file
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

#This will read the contents of input.txt, 
# remove any duplicate lines and write the unique lines to output.txt.
remove_duplicates('input.txt', 'output.txt')

############# CODE 2 Method: Using dictionary #################

def remove_duplicates(input_file, output_file):
    """
    Reads a file from disk, removes all duplicates and writes the unique lines back to disk.
    """
    # read input file into a list
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # remove duplicates using a dictionary
    unique_dict = {}
    for line in lines:
        if line not in unique_dict:
            unique_dict[line] = True

    # write unique lines to output file
    with open(output_file, 'w') as file:
        file.writelines(list(unique_dict.keys()))

############# CODE Method: Using set comprehension #############

def remove_duplicates(input_file, output_file):
    """
    Reads a file from disk, removes all duplicates and writes the unique lines back to disk.
    """
    # read input file into a list
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # remove duplicates using set comprehension
    unique_lines = set(lines)

    # write unique lines to output file
    with open(output_file, 'w') as file:
        file.writelines(list(unique_lines))

############### CODE Method: Using list comprehension.###########

def remove_duplicates(input_file, output_file):
    """
    Reads a file from disk, removes all duplicates and writes the unique lines back to disk.
    """
    # read input file into a list
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # remove duplicates using list comprehension
    unique_lines = [line for i, line in enumerate(lines) if line not in lines[:i]]

    # write unique lines to output file
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

>>>





<<<
#5#5#5#5#5################################## Redis cache to store the results #########################################################

"""
@@@Create a Python script that uses the Redis cache to store the results of an expensive calculation
for a period of time, and retrieves the result from cache if it already exists.
"""
##################### CODE 1 #########################

import redis

# connect to Redis cache
redis_cache = redis.Redis(host='localhost', port=6379, db=0)

def expensive_calculation(arg1, arg2):
    """
    An expensive calculation that takes two arguments.
    """
    # simulate an expensive calculation
    result = arg1 * arg2
    return result

def get_cached_result(key):
    """
    Retrieves the result from cache if it already exists.
    """
    result = redis_cache.get(key)
    if result:
        result = result.decode('utf-8')
    return result

def set_cached_result(key, value, ttl):
    """
    Sets the result in cache with a TTL (time to live) value.
    """
    redis_cache.setex(key, ttl, value)

def get_expensive_calculation_result(arg1, arg2, ttl=60):
    """
    Gets the result of an expensive calculation, either from cache or by performing the calculation.
    """
    # create a unique key for this calculation
    cache_key = f"expensive_calculation_{arg1}_{arg2}"

    # check if the result is in cache
    cached_result = get_cached_result(cache_key)
    if cached_result:
        return cached_result

    # perform the expensive calculation
    result = expensive_calculation(arg1, arg2)

    # store the result in cache
    set_cached_result(cache_key, result, ttl)

    # return the result
    return result

# In this script, we first connect to Redis cache using the redis package. 
# We then define an expensive calculation function that takes two arguments and returns the result of the calculation. 
# We also define two functions, get_cached_result and set_cached_result, that get and set values in cache, respectively. 
# Finally, we define a get_expensive_calculation_result function that uses the other functions to retrieve the result of the expensive calculation, 
# either from cache or by performing the calculation and storing the result in cache for a specified TTL (time to live) value. 
# Note that this is just an example and there are many ways to use Redis cache in Python. 
# The exact implementation may depend on the specific use case and requirements.

################ CODE 2 #####################

import time
import functools
import redis

# connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# cache the result of the function call for 10 seconds
@functools.lru_cache(ttl=10)
def expensive_calculation(num):
    print("Performing expensive calculation...")
    time.sleep(5)  # simulate expensive calculation
    return num * 2

# check if the result is already in cache
def get_result(num):
    result = r.get(num)
    if result is not None:
        return int(result)
    else:
        result = expensive_calculation(num)
        r.set(num, result, ex=10)  # cache result for 10 seconds
        return result

# test the function
print(get_result(5))  # should perform expensive calculation
print(get_result(5))  # should retrieve result from cache
time.sleep(10)  # wait for cache to expire
print(get_result(5))  # should perform expensive calculation again

# This implementation uses the redis package to connect to a Redis server 
# and store the result of the function call in cache using the set() method with a specified expiration time. 
# The get_result() function checks if the result is already in cache using the get() method, 
# and retrieves it if it exists. If the result is not in cache, it calls the expensive_calculation() 
# function and stores the result in cache using the set() method. 
# The @functools.lru_cache() decorator caches the result of the function call for a period of time specified by the ttl argument, 
# which is set to 10 seconds in this example.

################ CODE 3 #####################

import redis

# create a Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def expensive_calculation(arg):
    # simulate an expensive calculation
    result = arg * arg
    return result

def get_result(arg):
    # check if result is in Redis cache
    result = redis_client.get(arg)
    if result is not None:
        # result is in cache, return it
        return int(result)
    else:
        # result not in cache, perform expensive calculation
        result = expensive_calculation(arg)
        # store result in cache for 10 seconds
        redis_client.setex(arg, 10, result)
        return result

# In this implementation, the Redis client is created only once and reused for all operations. 
# The get_result function checks if the result for the given argument is already in the Redis cache using the get method. 
# If the result is in the cache, it is returned directly as an integer. Otherwise, the expensive calculation is performed, 
# the result is stored in the cache using the setex method with an expiration time of 10 seconds, and the result is returned.

# This implementation minimizes the number of Redis operations required, 
# as it uses only the get and setex methods for retrieving and storing data, respectively. 
# The data is stored as a single key-value pair in Redis, 
# where the key is the argument for the calculation and the value is the result. 
# Therefore, the space complexity of this implementation is O(1), 
# as it stores only a single key-value pair in Redis for each argument. 
# The time complexity of this implementation is O(1) for retrieving the result from the cache if it already exists, 
# and O(n) for performing the expensive calculation if the result is not in the cache, where n is the time required for the calculation.
>>>






<<<
#6#6#6#6#6############################## writes the results to a Cassandra database ###########################################

"""
@@@Write a python program that reads from a Kafka topic, processes the messages and writes the results to a Cassandra database
"""

# Using the kafka-python and cassandra-driver libraries

############## CODE 1 ################################

from kafka import KafkaConsumer
from cassandra.cluster import Cluster

# create a Kafka consumer
consumer = KafkaConsumer(
    'my-topic',  # topic name
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: m.decode('utf-8')
)

# connect to Cassandra cluster and create a session
cluster = Cluster(['localhost'])
session = cluster.connect('mykeyspace')

# prepare Cassandra statements for inserting data
insert_statement = session.prepare("INSERT INTO mytable (id, message) VALUES (?, ?)")

# read from Kafka topic and write to Cassandra
for message in consumer:
    # process the message
    processed_message = process_message(message.value)

    # write the processed message to Cassandra
    session.execute(insert_statement, (message.key, processed_message))

# close the Kafka consumer and Cassandra session
consumer.close()
session.shutdown()
cluster.shutdown()


# The program creates a KafkaConsumer object that subscribes to a topic named my-topic. 
# The program then connects to a Cassandra cluster and creates a session for interacting with the database. Next, 
# the program prepares a Cassandra statement for inserting data into a table named mytable. 
# The program then enters a loop that reads messages from the Kafka topic 
# and processes them using a process_message function (which is not shown in this example). 
# Finally, the program writes the processed messages to Cassandra using the prepared statement. 
# When the program is finished, it closes the Kafka consumer and Cassandra session.

################### CODE 2 ###################
# importing -> consumer and KafkaError from confuent package "confluent_kafka" 
from confluent_kafka import Consumer, KafkaError
from cassandra.cluster import Cluster

# Kafka consumer configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

# Cassandra configuration
cassandra_config = {
    'contact_points': ['localhost'],
    'port': 9042,
    'keyspace': 'my_keyspace'
}

# Create Kafka consumer and Cassandra cluster connection
consumer = Consumer(kafka_config)
cluster = Cluster(contact_points=cassandra_config['contact_points'], port=cassandra_config['port'])
session = cluster.connect(cassandra_config['keyspace'])

# Create Cassandra table if it doesn't exist
session.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INT PRIMARY KEY,
        result TEXT
    )
""")

# Subscribe to Kafka topic
consumer.subscribe(['my-topic'])

# Process messages
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached')
        else:
            print(f'Error reading message: {msg.error()}')
    else:
        # Process message and get result
        result = process_message(msg.value())

        # Write result to Cassandra
        session.execute(f"INSERT INTO results (id, result) VALUES ({msg.key().decode()}, '{result}')")

# Close connections
consumer.close()
session.shutdown()
cluster.shutdown()


################ CODE 3 ##################

import asyncio
from aiokafka import AIOKafkaConsumer
from aiocassandra import aiosession
from cassandra.cluster import Cluster


# Kafka consumer configuration
kafka_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

# Cassandra configuration
cassandra_config = {
    'contact_points': ['localhost'],
    'port': 9042,
    'keyspace': 'my_keyspace'
}


async def consume_and_process(loop):
    # Create Kafka consumer
    consumer = AIOKafkaConsumer(
        'my-topic', loop=loop, bootstrap_servers=kafka_config['bootstrap.servers'],
        group_id=kafka_config['group.id'], auto_offset_reset=kafka_config['auto.offset.reset'],
        enable_auto_commit=False
    )
    await consumer.start()

    # Create Cassandra session
    cluster = Cluster(contact_points=cassandra_config['contact_points'], port=cassandra_config['port'])
    session = await aiosession(cluster.connect(), loop=loop)

    # Create Cassandra table if it doesn't exist
    await session.execute_async("""
        CREATE TABLE IF NOT EXISTS results (
            id INT PRIMARY KEY,
            result TEXT
        )
    """)

    try:
        async for msg in consumer:
            # Process message and get result
            result = process_message(msg.value())

            # Write result to Cassandra
            await session.execute_async(f"INSERT INTO results (id, result) VALUES (?, ?)", [msg.key().decode(), result])

            # Commit Kafka offset
            await consumer.commit()

    finally:
        # Stop Kafka consumer and Cassandra session
        await consumer.stop()
        await session.close()
        await cluster.shutdown()


if __name__ == '__main__':
    # Start event loop and run consumer
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume_and_process(loop))


# Asyncio to asynchronously consume messages from Kafka and insert them into Cassandra using aiocassandra. 
# It also uses aiokafka for more efficient Kafka message handling and commits the Kafka offset only
# after successfully writing the result to Cassandra, ensuring at-least-once delivery semantics. 
# Finally, it uses prepared statements for improved Cassandra write performance and closes
# the Kafka consumer and Cassandra session properly in case of any exceptions.
>>>




<<<
#7#7#7#7#7###########################@@@@@@@@@@@@@@@@@@@@@@@@@@@###########################################
"""
@@@Implement a Python function that takes two dictionaries as input, merges them and returns the result. 
If a key exists in both dictionaries, the value from the second dictionary should be used.
"""

############# CODE 1 ##############

def merge_dicts(dict1, dict2):
    """
    Merges two dictionaries and returns the result. If a key exists in both dictionaries,
    the value from the second dictionary is used.
    """
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


#This function first creates a copy of dict1 using the copy() method, 
# and then updates it with the contents of dict2 using the update() method. 
# The update() method overwrites values for keys that exist in both dictionaries, 
# which satisfies the requirement that the value from the second dictionary should be used when a key exists in both dictionaries. 
# Finally, the merged dictionary is returned.


################# CODE 2 ############

def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries and returns the result.
    If a key exists in both dictionaries, the value from the second dictionary is used.
    """
    return {**dict1, **dict2}

# Implementation uses the " ** "operator to unpack the contents of the dictionaries 
# and merge them into a new dictionary. Since the second dictionary is unpacked last, 
# its values will overwrite any values with the same keys in the first dictionary.
>>>




<<<
#8#8#8#8#8############################ Redis stream and writes the messages to a file on disk##########################################
"""
Write a Python program that reads from a Redis stream and writes the messages to a file on disk.
"""

############# CODE 1 ######################

import redis

# Redis configuration
redis_config = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'stream': 'my-stream',
    'group': 'my-group',
    'consumer': 'my-consumer',
    'start': '0'
}

# File configuration
file_config = {
    'path': 'output.txt'
}

# Connect to Redis
r = redis.Redis(host=redis_config['host'], port=redis_config['port'], db=redis_config['db'])

# Create consumer group if it doesn't exist
try:
    r.xgroup_create(redis_config['stream'], redis_config['group'], mkstream=True)
except redis.exceptions.ResponseError:
    pass

# Read messages from Redis
while True:
    messages = r.xreadgroup(redis_config['group'], redis_config['consumer'], {redis_config['stream']: redis_config['start']}, count=10)

    if not messages:
        continue

    for message in messages[0][1]:
        # Write message to file
        with open(file_config['path'], 'a') as f:
            f.write(f"{message['id']} {message['data'].decode()}")

        # Update start ID for consumer group
        redis_config['start'] = message['id']
        r.xack(redis_config['stream'], redis_config['group'], message['id'])


# Program connects to a Redis server, creates a consumer group for a stream, 
# reads messages from the stream in batches of 10, writes each message to a file on disk, 
# and acknowledges each message to the consumer group. The program runs in an infinite loop so that it can continuously 
# read new messages from the stream as they arrive.


################ CODE 2 ####################

import redis

# Redis stream configuration
redis_config = {
    'host': 'localhost',
    'port': 6379,
    'password': None,
    'db': 0,
    'stream_name': 'my-stream'
}

# File configuration
file_path = 'messages.txt'

# Create Redis connection and open file for writing
r = redis.Redis(host=redis_config['host'], port=redis_config['port'], password=redis_config['password'], db=redis_config['db'])
with open(file_path, 'w') as f:

    # Read from Redis stream and write to file
    for message in r.xread({redis_config['stream_name']: '$'}, count=None, block=0):
        f.write(f"{message[1][0][1].decode()}\n")


# We use the Redis-py library to create a connection to Redis and read from the specified stream. 
# We then open a file for writing using the built-in open function and write each message to the file as a new line. 
# The decode() function is used to convert the byte-string message to a regular string.
>>>



<<<
#9#9#9#9#9##############################################################################################################
"""
Create a Python script that uses the Spark/Map-Reduce framework 
to count the number of occurrences of each word in a large text file
"""

################### CODE 1################

from pyspark import SparkContext, SparkConf

# Create a Spark configuration object with appropriate settings
conf = SparkConf().setAppName("Word Count").setMaster("local")
sc = SparkContext(conf=conf)

# Load the text file into an RDD
text_file = sc.textFile("path/to/text/file")

# Split the text into words and count the occurrences of each word
word_counts = text_file.flatMap(lambda line: line.split(" ")) \
                      .map(lambda word: (word, 1)) \
                      .reduceByKey(lambda a, b: a + b)

# Save the results to a text file
word_counts.saveAsTextFile("path/to/output/file")

# Stop the Spark context
sc.stop()


# Code uses the PySpark library, which is the Python interface for Apache Spark. 
# The SparkConf object is used to configure the Spark application, including the application name and master URL. 
# The SparkContext object is used to create a connection to the Spark cluster 
# and provides methods for loading data into RDDs and performing transformations and actions.

# The textFile method is used to load the text file into an RDD, 
# which is then transformed using the "flatMap, map, and reduceByKey" methods to split the text into words, 
# count the occurrences of each word, and sum the counts for each word, respectively. 
# Finally, the saveAsTextFile method is used to write the results to a text file on disk.

############## CODE 2 ##############

import dask.bag as db

# Read text file into a Dask bag
b = db.read_text('input_file.txt')

# Split each line into words and count occurrences
counts = b.str.split().flatten().frequencies()

# Save counts to output file
counts.to_textfiles('output_file-*.txt')


# Code reads the input text file into a Dask bag, which is a parallelizable collection of items. 
# The bag is split into lines and then each line is split into words using the "str.split()" method. 
# The resulting bag of words is then flattened into a single bag 
# and the "frequencies()" method is used to count the number of occurrences of each word. 
# Finally, the counts are saved to multiple text files using the "to_textfiles()" method. 
# Dask takes care of parallelizing the computation across multiple threads or cores if available, 
# making it a good choice for processing large text files on a single machine.

>>>



<<<
#10#10#10#10###########################################################################################################
"""
python function that takes a slice of strings as input, sorts them in ascending order and returns the sorted slice.
"""

######### CODE 1 #############

def sort_strings(strings):
    """
    Sorts a slice of strings in ascending order and returns the sorted slice.
    """
    return sorted(strings)

########## CODE 2 #############

import heapq

def sort_strings(strings):
    heap = []
    for s in strings:
        heapq.heappush(heap, s)
    return [heapq.heappop(heap) for i in range(len(heap))]


#Using a heap to sort the strings in ascending order. 
# It iterates over each string in the input list, pushing it onto the heap. 
# It then pops the smallest string off the heap until the heap is empty, constructing a sorted list in the process.

#The time complexity of this implementation is O(n log n), where n is the length of the input list. 
# This is because the "heappush and heappop" operations each take O(log n) time in the worst case, 
# and they are performed n times. The space complexity is also O(n), 
# because the heap contains all n elements of the input list.