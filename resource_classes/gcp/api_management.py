from . import _GCP


class _APIManagement(_GCP):
    _type = "apimanagement"
    _icon_dir = "resource_images/gcp/apimanagement"

class apigee(_APIManagement):
    _icon = "apigee_api_platform.png"

class CloudEndpoints(_APIManagement):
    _icon="cloud_endpoints.png"

google_apigee_organization=apigee
google_endpoints_service=CloudEndpoints