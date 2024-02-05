from . import _GCP


class _Security(_GCP):
    _type = "security"
    _icon_dir = "resource_images/gcp/security"

class BinaryAuthorization(_Security):
    _icon = "binary_authorization.png"

class CertificateAuthorityService(_Security):
    _icon = "certificate_authority_service.png"

class CloudAssetInventory(_Security):
    _icon = "cloud_asset_inventory.png"

class SecretManager(_Security):
    _icon = "secret_manager.png"

class SecurityScanner(_Security):
    _icon = "web_security_scanner.png"



google_binary_authorization_attestor=BinaryAuthorization
google_privateca_ca_pool=CertificateAuthorityService
google_cloud_asset_folder_feed=CloudAssetInventory
google_cloud_asset_organization_feed=CloudAssetInventory
google_cloud_asset_project_feed=CloudAssetInventory
google_secret_manager_secret=SecretManager
google_security_scanner_scan_config=SecurityScanner