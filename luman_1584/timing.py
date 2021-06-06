from collections import Counter
from contextlib import contextmanager, asynccontextmanager
import logging
import time

logger = logging.getLogger(__name__)

class TimingStats(Counter):

    def __init__(self, verbose: bool = False):
        super().__init__()
        self.verbose = verbose

    @contextmanager
    def scope(self, key, *, verbose=False):
        t1 = time.monotonic()
        yield
        sec = time.monotonic() - t1
        self[key] += sec
        if self.verbose:
            logger.debug(f"{key} took {sec:.3f} seconds")

    @asynccontextmanager
    async def async_scope(self, key, *, verbose=False):
        t1 = time.monotonic()
        yield
        sec = time.monotonic() - t1
        self[key] += sec
        if self.verbose:
            logger.debug(f"{key} took {sec:.3f} seconds")

    def report_strings(self):
        return [f"{key}: {sec:.1f} sec" for key, sec in self.items()]
