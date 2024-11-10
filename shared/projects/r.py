import redis

# Create a Redis client
client = redis.StrictRedis(
    host="redis",  # Replace with your Redis server's host name or IP
    port=6379,  # Replace with your Redis server's port if different
    db=0,  # The Redis database to use
)

# Ping the Redis server
response = client.ping()
print(f"Redis server is {'alive' if response else 'not alive'}")
