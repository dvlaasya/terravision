from . import _OnPrem


class _Container(_OnPrem):
    _type = "container"
    _icon_dir = "resource_images/onprem/container"


class Containerd(_Container):
    _icon = "containerd.png"


class Crio(_Container):
    _icon = "crio.png"


class Docker(_Container):
    _icon = "docker.png"


class Firecracker(_Container):
    _icon = "firecracker.png"


class Gvisor(_Container):
    _icon = "gvisor.png"


class Lxc(_Container):
    _icon = "lxc.png"


class Rkt(_Container):
    _icon = "rkt.png"


# Aliases

LXC = Lxc
RKT = Rkt
