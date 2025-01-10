from redis import Redis
from environs import Env


def get_redis_client() -> Redis:
    """
    Get Redis client with evn data.
    :return: Redis client
    """
    env = Env()
    env.read_env(".env")

    return Redis(
        host=env("REDIS_HOST"),
        port=env("REDIS_PORT")
    )

redis_client = get_redis_client()
