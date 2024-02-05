from . import _GCP
import re

class _Operations(_GCP):
    _type = "operations"
    _icon_dir = "resource_images/gcp/operations"

class CloudLogging(_Operations):
    _icon = "cloud_logging.png"

class CloudMonitoring(_Operations):
    _icon="cloud_monitoring.png"

class CloudProfiler(_Operations):
    _icon="profiler.png"

class CloudTrace(_Operations):
    _icon="trace.png"

google_logging_metric=CloudLogging
google_logging_sink=CloudLogging
google_monitoring_alert_policy=CloudMonitoring
google_monitoring_dashboard=CloudMonitoring



