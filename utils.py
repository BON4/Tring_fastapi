import yaml
from concurrent.futures import ProcessPoolExecutor
from constants import BASE_ROOT
import asyncio
from worker import warm


def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    # TODO: add config validation
    return data


async def setup_executor(conf):
    workers = conf['max_workers']
    path = BASE_ROOT / conf['model_path']
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor(max_workers=workers)
    fs = [loop.run_in_executor(
        executor, warm, path) for i in range(0, workers)]
    await asyncio.gather(*fs)  # gather for Futures wait for Tasks
    return executor
