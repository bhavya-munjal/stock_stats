import asyncio
import time


class RateLimiter:
    def __init__(self, min_interval: float) -> None:
        self.min_interval = min_interval
        self.last_request_time = 0.0
        self.lock = asyncio.Lock()

    async def wait(self) -> None:
        async with self.lock:
            now = time.time()
            diff_elapsed = now - self.last_request_time
            
        self.last_request_time = time.time()

        if diff_elapsed < self.min_interval:
                wait_time = self.min_interval - diff_elapsed
                print(f"Wait! Rate limit active...")
                print(f" Waiting for {round(wait_time, 2)} seconds...\n")
                await asyncio.sleep(wait_time)

        self.last_request_time = time.time()
