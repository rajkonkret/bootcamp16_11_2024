from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print("Wykonywanie zaplanowanego zadania...")


scheduler = BlockingScheduler()

scheduler.add_job(job, 'interval', minutes=1)

scheduler.start()
