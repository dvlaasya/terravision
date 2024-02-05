from . import _GCP


class _Network(_GCP):
    _type = "network"
    _icon_dir = "resource_images/gcp/network"

class APIGateway(_Network):
    _icon = "api_gateway.png"

class CloudArmor(_Network):
    _icon = "cloudarmor.png"

class CloudCDN(_Network):
    _icon = "cloud_cdn.png"

class CloudDNS(_Network):
    _icon = "cloud_dns.png"

class CloudFirewall(_Network):
    _icon = "cloud_firewall_rules.png"

class CloudIDS(_Network):
    _icon = "cloud_ids.png"

class CloudInterconnect(_Network):
    _icon = "cloud_interconnect.png"

class CloudLoadBalancing(_Network):
    _icon = "cloud_load_balancing.png"

class CloudNAT(_Network):
    _icon = "cloud_nat.png"

class CloudRouter(_Network):
    _icon = "cloud_router.png"

class CloudVpn(_Network):
    _icon = "cloud_vpn.png"

class NetworkConnectivityCenter(_Network):
    _icon = "network_connectivity_center.png"

class NetworkIntelligenceCenter(_Network):
    _icon = "network_intelligence_center.png"

class NetworkTiers(_Network):
    _icon = "network_tiers.png"

class ServiceDiscovery(_Network):
    _icon = "service_discovery.png"

class TrafficDirector(_Network):
    _icon = "traffic_director.png"

class VirtualPrivateCloud(_Network):
    _icon = "virtual_private_cloud.png"

google_api_gateway_api = APIGateway     
google_api_gateway_gateway=APIGateway  
google_compute_security_policy=CloudArmor 
google_cdn_endpoint=CloudCDN
google_dns_managed_zone=CloudDNS
google_compute_firewall=CloudFirewall
google_cloud_ids_endpoint=CloudIDS
google_compute_interconnect_attachment=CloudInterconnect
google_compute_target_https_proxy=CloudLoadBalancing
google_compute_target_http_proxy=CloudLoadBalancing
google_compute_router_nat=CloudNAT
google_compute_router=CloudRouter
google_compute_vpn_gateway=CloudVpn
google_compute_vpn_tunnel=CloudVpn
google_compute_network=VirtualPrivateCloud

