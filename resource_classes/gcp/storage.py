from . import _GCP


class _Storage(_GCP):
    _type = "storage"
    _icon_dir = "resource_images/gcp/storage"

class CloudStorage(_Storage):
    _icon = "cloud_storage.png"

class Filestore(_Storage):
    _icon="filestore.png"

class Firestore(_Storage):
    _icon="firestore.png"

class Persistentdisk(_Storage):
    _icon="persistent_disk.png"

google_storage_bucket=CloudStorage
google_filestore_instance=Filestore
google_firestore_database=Firestore
    