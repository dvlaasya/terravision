from . import _GCP


class _ContainerServices(_GCP):
    _type = "containerservices"
    _icon_dir = "resource_images/gcp/containerservices"

class KubernetesEngine(_ContainerServices):
    _icon = "google_kubernetes_engine.png"



google_container_cluster=KubernetesEngine