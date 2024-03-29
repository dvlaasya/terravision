from . import _AWS


class _Iot(_AWS):
    _type = "iot"
    _icon_dir = "resource_images/aws/iot"


class Freertos(_Iot):
    _icon = "freertos.png"


class InternetOfThings(_Iot):
    _icon = "internet-of-things.png"


class Iot1Click(_Iot):
    _icon = "iot-1-click.png"


class IotAction(_Iot):
    _icon = "iot-action.png"


class IotAlexaEcho(_Iot):
    _icon = "iot-alexa-echo.png"


class IotAlexaSkill(_Iot):
    _icon = "iot-alexa-skill.png"


class IotAnalytics(_Iot):
    _icon = "iot-analytics.png"


class IotButton(_Iot):
    _icon = "iot-button.png"


class IotCamera(_Iot):
    _icon = "iot-camera.png"


class IotCertificate(_Iot):
    _icon = "iot-certificate.png"


class IotCore(_Iot):
    _icon = "iot-core.png"


class IotDeviceDefender(_Iot):
    _icon = "iot-device-defender.png"


class IotDeviceManagement(_Iot):
    _icon = "iot-device-management.png"


class IotEvents(_Iot):
    _icon = "iot-events.png"


class IotGreengrassConnector(_Iot):
    _icon = "iot-greengrass-connector.png"


class IotGreengrass(_Iot):
    _icon = "iot-greengrass.png"


class IotHardwareBoard(_Iot):
    _icon = "iot-hardware-board.png"


class IotHttp(_Iot):
    _icon = "iot-http.png"


class IotHttp2(_Iot):
    _icon = "iot-http2.png"


class IotJobs(_Iot):
    _icon = "iot-jobs.png"


class IotLambda(_Iot):
    _icon = "iot-lambda.png"


class IotMqtt(_Iot):
    _icon = "iot-mqtt.png"


class IotPolicyEmergency(_Iot):
    _icon = "iot-policy-emergency.png"


class IotPolicy(_Iot):
    _icon = "iot-policy.png"


class IotRule(_Iot):
    _icon = "iot-rule.png"


class IotShadow(_Iot):
    _icon = "iot-shadow.png"


class IotSitewise(_Iot):
    _icon = "iot-sitewise.png"


class IotThingsGraph(_Iot):
    _icon = "iot-things-graph.png"


class IotTopic(_Iot):
    _icon = "iot-topic.png"


# Aliases

FreeRTOS = Freertos
IotBoard = IotHardwareBoard

# Terraform Resource Mappings
aws_iot_thing = InternetOfThings
aws_iot_policy = IotPolicy
aws_iot_topic_rule = IotTopic
aws_iot_certificate = IotCertificate
