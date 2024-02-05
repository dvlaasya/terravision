from . import _GCP


class _Compute(_GCP):
    _type = "compute"
    _icon_dir = "resource_images/gcp/compute"

class VMwareEngine(_Compute):
    _icon = "vmware_engine.png"

class Batch(_Compute):
    _icon = "batch.png"

class AppEngine(_Compute):
    _icon="app_engine.png"

class ComputeEngine(_Compute):
    _icon = "compute_engine.png"

VME=VMwareEngine
CE=ComputeEngine
AE=AppEngine
google_vmwareengine_cluster=VME
google_vmwareengine_network=VME
google_vmwareengine_private_cloud=VME
google_vmwareengine_subnet=VME
google_compute_network=CE
google_compute_disk=CE
google_compute_global_network_endpoint=CE
google_compute_image=CE
google_compute_instance=CE
google_compute_subnetwork=CE
google_app_engine_application=AE


