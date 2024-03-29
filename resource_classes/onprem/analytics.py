from . import _OnPrem


class _Analytics(_OnPrem):
    _type = "analytics"
    _icon_dir = "resource_images/onprem/analytics"


class Beam(_Analytics):
    _icon = "beam.png"


class Databricks(_Analytics):
    _icon = "databricks.png"


class Dbt(_Analytics):
    _icon = "dbt.png"


class Flink(_Analytics):
    _icon = "flink.png"


class Hadoop(_Analytics):
    _icon = "hadoop.png"


class Hive(_Analytics):
    _icon = "hive.png"


class Metabase(_Analytics):
    _icon = "metabase.png"


class Norikra(_Analytics):
    _icon = "norikra.png"


class Presto(_Analytics):
    _icon = "presto.png"


class Singer(_Analytics):
    _icon = "singer.png"


class Spark(_Analytics):
    _icon = "spark.png"


class Storm(_Analytics):
    _icon = "storm.png"


class Superset(_Analytics):
    _icon = "superset.png"


class Tableau(_Analytics):
    _icon = "tableau.png"


# Aliases
