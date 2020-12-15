from celery import shared_task
from celery_progress.backend import ProgressRecorder
from time import sleep


@shared_task(bind=True)
def go_to_sleep(self, duration):

    # instantiate progress recorder
    progress_recorder = ProgressRecorder(self)

    # set total
    total = 100

    # every task should have some kind of for loop
    for i in range(total):

        # heavy work
        sleep(duration)
        # for the intermediate steps JSON dictionary is returned
        progress_recorder.set_progress(i + 1, total, f'loop: {i}') # (current progress, total [static, needs to be same as in range], note)

    # final step returns string
    return 'done'
