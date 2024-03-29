from . import _OnPrem


class _Ci(_OnPrem):
    _type = "ci"
    _icon_dir = "resource_images/onprem/ci"


class Circleci(_Ci):
    _icon = "circleci.png"


class Concourseci(_Ci):
    _icon = "concourseci.png"


class Droneci(_Ci):
    _icon = "droneci.png"


class GithubActions(_Ci):
    _icon = "github-actions.png"


class Gitlabci(_Ci):
    _icon = "gitlabci.png"


class Jenkins(_Ci):
    _icon = "jenkins.png"


class Teamcity(_Ci):
    _icon = "teamcity.png"


class Travisci(_Ci):
    _icon = "travisci.png"


class Zuulci(_Ci):
    _icon = "zuulci.png"


# Aliases

CircleCI = Circleci
ConcourseCI = Concourseci
DroneCI = Droneci
GitlabCI = Gitlabci
TravisCI = Travisci
TC = Teamcity
ZuulCI = Zuulci
