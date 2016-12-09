from .platform.tools import plantool


def run(scheduler):
    scheduler.start()
    plantool.start_scheduler(scheduler)
