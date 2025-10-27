import redis
import json
import os

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True
)

def get_cached_user(user_id: int):
    cached_data = redis_client.get(f"user:{user_id}")
    if cached_data:
        return json.loads(cached_data)
    return None

def set_cached_user(user_id: int, user_data: dict, expire: int = 300):
    redis_client.setex(
        f"user:{user_id}", 
        expire, 
        json.dumps(user_data, default=str)
    )

def delete_user_cache(user_id: int):
    redis_client.delete(f"user:{user_id}")

def clear_users_cache():
    keys = redis_client.keys("user:*")
    if keys:
        redis_client.delete(*keys)
