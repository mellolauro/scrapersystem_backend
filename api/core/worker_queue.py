import redis
from rq import Queue

redis_conn = redis.Redis(host="redis", port=6379)
task_queue = Queue("scraper_jobs", connection=redis_conn)
