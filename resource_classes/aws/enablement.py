from . import _AWS


class _Enablement(_AWS):
    _type = "enablement"
    _icon_dir = "resource_images/aws/enablement"


class Iq(_Enablement):
    _icon = "iq.png"


class ManagedServices(_Enablement):
    _icon = "managed-services.png"


class ProfessionalServices(_Enablement):
    _icon = "professional-services.png"


class Support(_Enablement):
    _icon = "support.png"


# Aliases
