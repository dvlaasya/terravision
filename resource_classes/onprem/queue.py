from . import _OnPrem


class _Queue(_OnPrem):
    _type = "queue"
    _icon_dir = "resource_images/onprem/queue"


class Activemq(_Queue):
    _icon = "activemq.png"


class Celery(_Queue):
    _icon = "celery.png"


class Kafka(_Queue):
    _icon = "kafka.png"


class Nats(_Queue):
    _icon = "nats.png"


class Rabbitmq(_Queue):
    _icon = "rabbitmq.png"


class Zeromq(_Queue):
    _icon = "zeromq.png"


# Aliases

ActiveMQ = Activemq
RabbitMQ = Rabbitmq
ZeroMQ = Zeromq
