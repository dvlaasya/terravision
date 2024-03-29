from . import _Generic


class _Network(_Generic):
    _type = "network"
    _icon_dir = "resource_images/generic/network"


class Firewall(_Network):
    _icon = "firewall.png"


class Router(_Network):
    _icon = "router.png"


class Subnet(_Network):
    _icon = "subnet.png"


class Switch(_Network):
    _icon = "switch.png"


class VPN(_Network):
    _icon = "vpn.png"


# Aliases
