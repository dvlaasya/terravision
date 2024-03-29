from . import _OnPrem


class _Auth(_OnPrem):
    _type = "auth"
    _icon_dir = "resource_images/onprem/auth"


class Boundary(_Auth):
    _icon = "boundary.png"


class BuzzfeedSso(_Auth):
    _icon = "buzzfeed-sso.png"


class Oauth2Proxy(_Auth):
    _icon = "oauth2-proxy.png"


# Aliases
