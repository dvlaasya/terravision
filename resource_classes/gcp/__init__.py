"""
AWS provides a set of services for Amazon Web Service provider.
"""

from resource_classes import Node


class _GCP(Node):
    _provider="google"
    _icon_dir="resource_images/gcp"
    fontcolor = "#ffffff"