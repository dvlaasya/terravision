from . import _GCP


class _DataAnalytics(_GCP):
    _type = "dataanalytics"
    _icon_dir = "resource_images/gcp/dataanalytics"

class BigQuery(_DataAnalytics):
    _icon = "bigquery.png"

class BigQuery(_DataAnalytics):
    _icon = "bigquery.png"

class BigQuery(_DataAnalytics):
    _icon = "bigquery.png"

class CloudComposer(_DataAnalytics):
    _icon = "cloud_composer.png"

class DataFusion(_DataAnalytics):
    _icon = "cloud_data_fusion.png"

class DataCatalog(_DataAnalytics):
    _icon = "data_catalog.png"

class Dataflow(_DataAnalytics):
    _icon = "dataflow.png"

class Dataplex(_DataAnalytics):
    _icon = "dataplex.png"

class Dataproc(_DataAnalytics):
    _icon = "dataproc.png"

class DataprocMetastore(_DataAnalytics):
    _icon = "dataproc_metastore.png"

class Looker(_DataAnalytics):
    _icon = "looker.png"

class Pubsub(_DataAnalytics):
    _icon = "pubsub.png"


google_bigquery_dataset=BigQuery
google_composer_environment=CloudComposer
google_data_fusion_instance=DataFusion
google_data_catalog_entry=DataCatalog
google_dataflow_job=Dataflow
google_dataplex_lake=Dataplex
google_dataproc_cluster=Dataproc
google_dataproc_metastore_service=DataprocMetastore
google_looker_instance=Looker
google_pubsub_topic=Pubsub