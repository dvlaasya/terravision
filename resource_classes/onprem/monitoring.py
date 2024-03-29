from . import _OnPrem


class _Monitoring(_OnPrem):
    _type = "monitoring"
    _icon_dir = "resource_images/onprem/monitoring"


class Cortex(_Monitoring):
    _icon = "cortex.png"


class Datadog(_Monitoring):
    _icon = "datadog.png"


class Grafana(_Monitoring):
    _icon = "grafana.png"


class Newrelic(_Monitoring):
    _icon = "newrelic.png"


class PrometheusOperator(_Monitoring):
    _icon = "prometheus-operator.png"


class Prometheus(_Monitoring):
    _icon = "prometheus.png"


class Sentry(_Monitoring):
    _icon = "sentry.png"


class Splunk(_Monitoring):
    _icon = "splunk.png"


class Thanos(_Monitoring):
    _icon = "thanos.png"


class Zabbix(_Monitoring):
    _icon = "zabbix.png"


# Aliases
