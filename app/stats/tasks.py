from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task()
def views_task(time_out, id):
    from time import sleep
    from stats.models import Record
    from stats.utils import release_date
    sleep(time_out)
    record = Record.objects.get(id=id)
    post = release_date(record.link.split('=wall')[1])
    record.views = post['views']['count']
    record.save()


@shared_task
def release_date_task():
    from stats.models import Record
    from stats.utils import release_date
    import datetime
    import time

    record = Record.objects.filter(is_active=True)
    for rec in record:
        if not rec.release_date:
            post = release_date(rec.link.split('=wall')[1])
            if (post):
                rec.release_date = datetime.datetime.fromtimestamp(
                    post['date'])
                stats_date = int(post['date']) + 85800
                rec.stats_date = datetime.datetime.fromtimestamp(stats_date)
                rec.save()
                time_out = stats_date - time.time()
                if time_out > 0:
                    views_task.delay(time_out, rec.id)
                else:
                    rec.is_deleted = True
                    rec.save()


@shared_task
def is_active_task():
    from stats.models import Record

    record = Record.objects.filter(is_active=True)
    for rec in record:
        if rec.views or rec.is_deleted:
            rec.is_active = False
            rec.save()
