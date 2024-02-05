from . import _GCP


class _Database(_GCP):
    _type = "network"
    _icon_dir = "resource_images/gcp/network"

class Bigtable(_Database):
    _icon = "bigtable.png"

class CloudSpanner(_Database):
    _icon="cloud_spanner.png"

class Cloudsql(_Database):
    _icon="cloud_sql.png"

class Datastore(_Database):
    _icon="datastore.png"

class Firestore(_Database):
    _icon="firestore.png"

class Memorystore(_Database):
    _icon="memorystore.png"

google_bigtable_instance=Bigtable
google_sql_database_instance=Cloudsql
google_spanner_instance=CloudSpanner
google_datastore_index=Datastore
google_filestore_instance=Firestore
google_redis_cluster=Memorystore
google_redis_instance=Memorystore


 