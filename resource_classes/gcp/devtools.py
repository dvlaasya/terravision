from . import _GCP


class _Devtools(_GCP):
    _type = "devtools"
    _icon_dir = "resource_images/gcp/devtools"

class ArtifactRegistry(_Devtools):
    _icon = "artifact_registry.png"

class CloudBuild(_Devtools):
    _icon = "cloud_build.png"

class CloudDeploy(_Devtools):
    _icon = "cloud_deploy.png"

class ContainerRegistry(_Devtools):
    _icon = "container_registry.png"


google_artifact_registry_repository=ArtifactRegistry
google_cloudbuild_trigger=CloudBuild
google_clouddeploy_delivery_pipeline=CloudDeploy
google_container_registry=ContainerRegistry
