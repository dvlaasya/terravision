from . import _GCP


class _Serverless(_GCP):
    _type = "network"
    _icon_dir = "resource_images/gcp/serverless_computing"

class CloudFunction(_Serverless):
    _icon = "cloud_functions.png"

class CloudRun(_Serverless):
    _icon="cloud_run.png"

class CloudScheduler(_Serverless):
    _icon="cloud_scheduler.png"

class CloudTasks(_Serverless):
    _icon="cloud_tasks.png"

google_cloudfunctions_function=CloudFunction
google_cloud_run_service=CloudRun
google_cloud_scheduler_job=CloudScheduler
google_cloud_tasks_queue=CloudTasks

