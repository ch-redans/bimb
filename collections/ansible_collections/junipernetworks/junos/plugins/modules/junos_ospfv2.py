#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for junos_ospfv2
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: junos_ospfv2
short_description: OSPFv2 resource module
description:
- This module manages OSPFv2 configuration on devices running Juniper JUNOS.
version_added: 1.0.0
author:
- Daniel Mellado (@dmellado)
- Rohit Thakur (@rohitthakur2590)
requirements:
- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)
notes:
- This module requires the netconf system service be enabled on the device being managed.
- This module works with connection C(netconf).
- See L(the Junos OS Platform Options,https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
- Tested against JunOS v18.4R1
options:
  config:
    description: A list of OSPFv2 process configuration.
    type: list
    elements: dict
    suboptions:
      router_id:
        description:
        - The OSPFv2 router id.
        type: str
      areas:
        description:
        - A list of OSPFv2 areas' configuration.
        type: list
        elements: dict
        suboptions:
          area_id:
            description:
            - The Area ID as an integer or IP Address.
            type: str
            required: true
          area_range:
            description:
            - Configure an address range for the area.
            - Included for compatibility, remove/deprecate after 2025-07-01.
            - Alternate for this would be area_ranges which is a list.
            type: str
          area_ranges:
            description:
            - Configure IP address ranges for the area.
            type: list
            elements: dict
            suboptions:
              address:
                description:
                - Specify ip address.
                type: str
              exact:
                description:
                - Enforce exact match for advertisement of this area range.
                type: bool
              restrict:
                description:
                - Restrict advertisement of this area range.
                type: bool
              override_metric:
                description:
                - Override the dynamic metric for this area-range.
                type: int
          stub:
            description:
            - Settings for configuring the area as a stub.
            type: dict
            suboptions:
              default_metric:
                description:
                - Metric for the default route in this area.
                type: int
              set:
                description:
                - Configure the area as a stub.
                type: bool
          interfaces:
            description:
            - List of interfaces in this area.
            type: list
            elements: dict
            suboptions:
              authentication:
                description: Specify authentication type
                type: dict
                suboptions:
                  type:
                    description:
                    - Type of authentication to use.
                    - Included for compatibility, remove/deprecate after 2025-07-01.
                    type: dict
                  password:
                    description: Specify authentication key.
                    type: str
                  md5:
                    description: MD5 authentication keys
                    type: list
                    elements: dict
                    suboptions:
                      key_id:
                        description: Specify the key identity
                        type: int
                      key:
                        description: Specify key value
                        type: str
                      start_time:
                        description: Specify Start time for key transmission (YYYY-MM-DD.HH:MM)
                        type: str

              bandwidth_based_metrics:
                description: Specify list of bandwidth based metrics
                type: list
                elements: dict
                suboptions:
                  bandwidth:
                    description:
                    - BW to apply metric to.
                    type: str
                    choices: [1g, 10g]
                  metric:
                    description: Specify metric
                    type: int
              name:
                description:
                - Name of the interface.
                type: str
                required: true
              priority:
                description:
                - Priority for the interface.
                type: int
              metric:
                description:
                - Metric applied to the interface.
                type: int
              flood_reduction:
                description:
                - Enable flood reduction.
                type: bool
              passive:
                description: Specify passive
                type: bool
              timers:
                description: Specify timers
                type: dict
                suboptions:
                  dead_interval:
                    description:
                    - Dead interval (seconds).
                    type: int
                  hello_interval:
                    description:
                    - Hello interval (seconds).
                    type: int
                  poll_interval:
                    description:
                    - Poll interval (seconds).
                    type: int
                  retransmit_interval:
                    description:
                    - Retransmit interval (seconds).
                    type: int
                  transit_delay:
                    description:
                    - Transit delay (seconds).
                    type: int
      external_preference:
        description:
        - Preference of external routes.
        type: int
      overload:
        description: Specify time for overload mode reset
        type: dict
        suboptions:
          allow_route_leaking:
            description: Allow routes to be leaked when overload is configured.
            type: bool
          as_external:
            description: Advertise As External with maximum usable metric.
            type: bool
          stub_network:
            description: Advertise Stub Network with maximum metric.
            type: bool
          timeout:
            description:
            - Time after which overload mode is reset (seconds).
            type: int
      preference:
        description:
        - Preference of internal routes.
        type: int
      prefix_export_limit:
        description:
        - Maximum number of external prefixes that can be exported.
        type: int
      reference_bandwidth:
        description:
        - Bandwidth for calculating metric defaults.
        type: str
        choices: [1g, 10g]
      rfc1583compatibility:
        description:
        - Set RFC1583 compatibility
        type: bool
      spf_options:
        description:
        - Configure options for SPF.
        type: dict
        suboptions:
          delay:
            description:
            - Time to wait before running an SPF (seconds).
            type: int
          holddown:
            description:
            - Time to hold down before running an SPF (seconds).
            type: int
          rapid_runs:
            description:
            - Number of maximum rapid SPF runs before holddown (seconds).
            type: int
          no_ignore_our_externals:
            description: Do not ignore self-generated external and NSSA LSAs.
            type: bool
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the Junos device
      by executing the command B(show protocols ospf).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result
    type: str
  state:
    description:
    - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
"""
EXAMPLES = """
# Using merged
#
# Before state
# ------------
#
# admin# show protocols ospf

- name: Merge provided OSPFv2 configuration into running config.
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.100
            area_ranges:
              - address: 10.200.17.0/24
                exact: true
                restrict: true
                override_metric: 2000
              - address: 10.200.15.0/24
                exact: true
                restrict: true
                override_metric: 2000
                stub:
                  default_metric: 100
                  set: true
                interfaces:
                  - name: so-0/0/0.0
                    priority: 3
                    metric: 5
                    flood_reduction: false
                    passive: true
                    bandwidth_based_metrics:
                      - bandwidth: 1g
                        metric: 5
                      - bandwidth: 10g
                        metric: 40
                    timers:
                      dead_interval: 4
                      hello_interval: 2
                      poll_interval: 2
                      retransmit_interval: 2
        rfc1583compatibility: false
    state: merged

# Task Output:
# ------------
#
# before: []
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/>
#   <nc:area><nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/>
#   <nc:restrict/><nc:override-metric>2000</nc:override-metric></nc:area-range><nc:area-range>
#   <nc:name>10.200.15.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
#   </nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority>
#   <nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name>
#   <nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric>
#   </nc:bandwidth></nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval>
#   <nc:hello-interval>2</nc:hello-interval><nc:poll-interval>2</nc:poll-interval>
#   <nc:retransmit-interval>2</nc:retransmit-interval></nc:interface><nc:stub>
#   <nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
#
# after:
# - areas:
#   - area_id: 0.0.0.100
#     area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
#     area_ranges:
#     - address: 10.200.17.0/24
#       exact: true
#       override_metric: 2000
#       restrict: true
#     - address: 10.200.15.0/24
#       exact: true
#       override_metric: 2000
#       restrict: true
#     interfaces:
#     - bandwidth_based_metrics:
#       - bandwidth: 1g
#         metric: 5
#       - bandwidth: 10g
#         metric: 40
#       metric: 5
#       name: so-0/0/0.0
#       passive: true
#       priority: 3
#       timers:
#         dead_interval: 4
#         hello_interval: 2
#         poll_interval: 2
#         retransmit_interval: 2
#     stub:
#       default_metric: 100
#       set: true
#   reference_bandwidth: 10g
#   rfc1583compatibility: false

# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 10.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }
#
# Using replaced
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 10.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }

- name: Replace existing Junos OSPFv2 config with provided config
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.100
            area_ranges:
              - address: 10.200.17.0/24
                exact: true
                restrict: true
              - address: 10.200.16.0/24
                exact: true
                restrict: true
                override_metric: 1000
            stub:
              default_metric: 100
              set: true
            interfaces:
              - name: so-0/0/0.0
                priority: 3
                metric: 5
                flood_reduction: false
                passive: true
                bandwidth_based_metrics:
                  - bandwidth: 1g
                    metric: 5
                  - bandwidth: 10g
                    metric: 40
                timers:
                  dead_interval: 4
                  hello_interval: 2
                  poll_interval: 2
                  retransmit_interval: 2
        rfc1583compatibility: false
    state: replacedd

# Task Output:
# ------------
#
# before:
#   - areas:
#     - area_id: 0.0.0.100
#       area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
#       area_ranges:
#       - address: 10.200.17.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       - address: 10.200.15.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#         timers:
#           dead_interval: 4
#           hello_interval: 2
#           poll_interval: 2
#           retransmit_interval: 2
#       stub:
#         default_metric: 100
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area></nc:ospf><nc:ospf>
#   <nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/><nc:area>
#   <nc:name>0.0.0.100</nc:name><nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/>
#   <nc:restrict/></nc:area-range><nc:area-range><nc:name>10.200.16.0/24</nc:name><nc:exact/>
#   <nc:restrict/><nc:override-metric>1000</nc:override-metric></nc:area-range><nc:interface>
#   <nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/>
#   <nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name><nc:metric>5</nc:metric>
#   </nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric></nc:bandwidth>
#   </nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval><nc:hello-interval>2</nc:hello-interval>
#   <nc:poll-interval>2</nc:poll-interval><nc:retransmit-interval>2</nc:retransmit-interval></nc:interface>
#   <nc:stub><nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
#
# after:
#   - areas:
#     - area_id: 0.0.0.100
#       area_range: '[''10.200.17.0/24'', ''10.200.16.0/24'']'
#       area_ranges:
#       - address: 10.200.17.0/24
#         exact: true
#         restrict: true
#       - address: 10.200.16.0/24
#         exact: true
#         override_metric: 1000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#         timers:
#           dead_interval: 4
#           hello_interval: 2
#           poll_interval: 2
#           retransmit_interval: 2
#       stub:
#         default_metric: 100
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#
# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#     }
#     area-range 10.200.16.0/24 {
#         restrict;
#         exact;
#         override-metric 1000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }
#
# Using overridden
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#     }
#     area-range 10.200.16.0/24 {
#         restrict;
#         exact;
#         override-metric 1000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }

- name: Override runnig OSPFv2 config with provided config
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.110
            area_ranges:
              - address: 20.200.17.0/24
                exact: true
                restrict: true
                override_metric: 2000
              - address: 20.200.15.0/24
                exact: true
                restrict: true
                override_metric: 2000
            stub:
              default_metric: 200
              set: true
            interfaces:
              - name: so-0/0/0.0
                priority: 3
                metric: 5
                flood_reduction: false
                passive: true
                bandwidth_based_metrics:
                  - bandwidth: 1g
                    metric: 5
                  - bandwidth: 10g
                    metric: 40
    state: overridden

# Task Output:
# ------------
#
# before:
# - areas:
#   - area_id: 0.0.0.100
#     area_range: '[''10.200.17.0/24'', ''10.200.16.0/24'']'
#     area_ranges:
#     - address: 10.200.17.0/24
#       exact: true
#       restrict: true
#     - address: 10.200.16.0/24
#       exact: true
#       override_metric: 1000
#       restrict: true
#     interfaces:
#     - bandwidth_based_metrics:
#       - bandwidth: 1g
#         metric: 5
#       - bandwidth: 10g
#         metric: 40
#       metric: 5
#       name: so-0/0/0.0
#       passive: true
#       priority: 3
#       timers:
#         dead_interval: 4
#         hello_interval: 2
#         poll_interval: 2
#         retransmit_interval: 2
#     stub:
#       default_metric: 100
#       set: true
#   reference_bandwidth: 10g
#   rfc1583compatibility: false
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area></nc:ospf><nc:ospf>
#   <nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:area><nc:name>0.0.0.110</nc:name>
#   <nc:area-range><nc:name>20.200.17.0/24</nc:name><nc:exact/><nc:restrict/>
#   <nc:override-metric>2000</nc:override-metric></nc:area-range><nc:area-range>
#   <nc:name>20.200.15.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
#   </nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name><nc:priority>3</nc:priority>
#   <nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth><nc:name>1g</nc:name>
#   <nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name><nc:metric>40</nc:metric>
#   </nc:bandwidth></nc:bandwidth-based-metrics></nc:interface><nc:stub>
#   <nc:default-metric>200</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>
#
# after:
#   - areas:
#     - area_id: 0.0.0.110
#       area_range: '[''20.200.17.0/24'', ''20.200.15.0/24'']'
#       area_ranges:
#       - address: 20.200.17.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       - address: 20.200.15.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#       stub:
#         default_metric: 200
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false

# After state
# -----------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.110 {
#     stub default-metric 200;
#     area-range 20.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 20.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#     }
# }
# Using deleted
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.110 {
#     stub default-metric 200;
#     area-range 20.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 20.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#     }
# }

- name: Delete OSPFv2 running config.
  junipernetworks.junos.junos_ospfv2:
    config:
    state: deleted

# Task Output:
# ------------
#
# before:
#   - areas:
#     - area_id: 0.0.0.110
#       area_range: '[''20.200.17.0/24'', ''20.200.15.0/24'']'
#       area_ranges:
#       - address: 20.200.17.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       - address: 20.200.15.0/24
#         exact: true
#         override_metric: 2000
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#       stub:
#         default_metric: 200
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#
# commands:
# - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:ospf><nc:area delete="delete">0.0.0.100</nc:area><nc:reference-bandwidth delete="delete"/>
#   <nc:no-rfc-1583 delete="delete"/></nc:ospf></nc:protocols>
#
# after: []
#
#
# After state
# -----------
#
# admin# show protocols ospf

# Using gathered
#
# Before state
# ------------
#
# admin# show protocols ospf
# reference-bandwidth 10g;
# no-rfc-1583;
# area 0.0.0.100 {
#     stub default-metric 100;
#     area-range 10.200.17.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     area-range 10.200.15.0/24 {
#         restrict;
#         exact;
#         override-metric 2000;
#     }
#     interface so-0/0/0.0 {
#         passive;
#         bandwidth-based-metrics {
#             bandwidth 1g metric 5;
#             bandwidth 10g metric 40;
#         }
#         metric 5;
#         priority 3;
#         retransmit-interval 2;
#         hello-interval 2;
#         dead-interval 4;
#         poll-interval 2;
#     }
# }

- name: Gather Junos OSPFv2 running-configuration
  junipernetworks.junos.junos_ospfv2:
    config:
    state: gathered
#
#
# Task Output:
# ------------
#
# gathered:
#
#  - areas:
# - area_id: 0.0.0.100
#   area_range: '[''10.200.17.0/24'', ''10.200.15.0/24'']'
#   area_ranges:
#   - address: 10.200.17.0/24
#     exact: true
#     override_metric: 2000
#     restrict: true
#   - address: 10.200.15.0/24
#     exact: true
#     override_metric: 2000
#     restrict: true
#   interfaces:
#   - bandwidth_based_metrics:
#     - bandwidth: 1g
#       metric: 5
#     - bandwidth: 10g
#       metric: 40
#     metric: 5
#     name: so-0/0/0.0
#     passive: true
#     priority: 3
#     timers:
#       dead_interval: 4
#       hello_interval: 2
#       poll_interval: 2
#       retransmit_interval: 2
#   stub:
#     default_metric: 100
#     set: true
# reference_bandwidth: 10g
# rfc1583compatibility: false

# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <protocols>
#             <ospf>
#             <reference-bandwidth>10g</reference-bandwidth>
#             <no-rfc-1583/>
#             <area>
#                 <name>0.0.0.100</name>
#                 <stub>
#                     <default-metric>100</default-metric>
#                 </stub>
#                 <area-range>
#                     <name>10.200.16.0/24</name>
#                     <exact/>
#                     <override-metric>10000</override-metric>
#                 </area-range>
#                 <area-range>
#                     <name>10.200.11.0/24</name>
#                     <restrict/>
#                     <exact/>
#                 </area-range>
#                 <interface>
#                     <name>so-0/0/0.0</name>
#                     <passive>
#                     </passive>
#                     <bandwidth-based-metrics>
#                         <bandwidth>
#                             <name>1g</name>
#                             <metric>5</metric>
#                         </bandwidth>
#                         <bandwidth>
#                             <name>10g</name>
#                             <metric>40</metric>
#                         </bandwidth>
#                     </bandwidth-based-metrics>
#                     <metric>5</metric>
#                     <priority>3</priority>
#                     <retransmit-interval>2</retransmit-interval>
#                     <hello-interval>2</hello-interval>
#                     <dead-interval>4</dead-interval>
#                     <poll-interval>2</poll-interval>
#                 </interface>
#             </area>
#         </ospf>
#         </protocols>
#         <routing-options>
#             <static>
#                 <route>
#                     <name>172.16.17.0/24</name>
#                     <discard />
#                 </route>
#             </static>
#             <router-id>10.200.16.75</router-id>
#             <autonomous-system>
#                 <as-number>65432</as-number>
#             </autonomous-system>
#         </routing-options>
#     </configuration>
# </rpc-reply>


- name: Parsed the ospfv2 config into structured ansible resource facts.
  junipernetworks.junos.junos_ospfv2:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
# Task Output:
# ------------
#
# parsed:
# - areas:
#     - area_id: 0.0.0.100
#       area_range: '[''10.200.16.0/24'', ''10.200.11.0/24'']'
#       area_ranges:
#       - address: 10.200.16.0/24
#         exact: true
#         override_metric: 10000
#       - address: 10.200.11.0/24
#         exact: true
#         restrict: true
#       interfaces:
#       - bandwidth_based_metrics:
#         - bandwidth: 1g
#           metric: 5
#         - bandwidth: 10g
#           metric: 40
#         metric: 5
#         name: so-0/0/0.0
#         passive: true
#         priority: 3
#         timers:
#           dead_interval: 4
#           hello_interval: 2
#           poll_interval: 2
#           retransmit_interval: 2
#       stub:
#         default_metric: 100
#         set: true
#     reference_bandwidth: 10g
#     rfc1583compatibility: false
#     router_id: 10.200.16.75

# Using rendered
#
- name: Render the commands for provided  configuration
  junipernetworks.junos.junos_ospfv2:
    config:
      - reference_bandwidth: 10g
        areas:
          - area_id: 0.0.0.100
            area_ranges:
              - address: 10.200.17.0/24
                exact: true
                restrict: true
                override_metric: 2000
              - address: 10.200.15.0/24
                exact: true
                restrict: true
                override_metric: 2000
            stub:
              default_metric: 100
              set: true
            interfaces:
              - name: so-0/0/0.0
                priority: 3
                metric: 5
                flood_reduction: false
                passive: true
                bandwidth_based_metrics:
                  - bandwidth: 1g
                    metric: 5
                  - bandwidth: 10g
                    metric: 40
                timers:
                  dead_interval: 4
                  hello_interval: 2
                  poll_interval: 2
                  retransmit_interval: 2
        rfc1583compatibility: false
    state: rendered

# Task Output:
# ------------
#
# rendered: "<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:ospf><nc:reference-bandwidth>10g</nc:reference-bandwidth><nc:no-rfc-1583/><nc:area><nc:name>0.0.0.100</nc:name>
# <nc:area-range><nc:name>10.200.17.0/24</nc:name><nc:exact/><nc:restrict/><nc:override-metric>2000</nc:override-metric>
# </nc:area-range><nc:area-range><nc:name>10.200.15.0/24</nc:name><nc:exact/><nc:restrict/>
# <nc:override-metric>2000</nc:override-metric></nc:area-range><nc:interface><nc:name>so-0/0/0.0</nc:name>
# <nc:priority>3</nc:priority><nc:metric>5</nc:metric><nc:passive/><nc:bandwidth-based-metrics><nc:bandwidth>
# <nc:name>1g</nc:name><nc:metric>5</nc:metric></nc:bandwidth><nc:bandwidth><nc:name>10g</nc:name>
# <nc:metric>40</nc:metric></nc:bandwidth></nc:bandwidth-based-metrics><nc:dead-interval>4</nc:dead-interval>
# <nc:hello-interval>2</nc:hello-interval><nc:poll-interval>2</nc:poll-interval>
# <nc:retransmit-interval>2</nc:retransmit-interval></nc:interface><nc:stub>
# <nc:default-metric>100</nc:default-metric></nc:stub></nc:area></nc:ospf></nc:protocols>"
"""
RETURN = """
before:
  description: The configuration prior to the module invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration module invocation.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><
  nc:ospf><nc:area delete="delete">0.0.0.100</nc:area><nc:reference-bandwidth delete="delete"/>
  <nc:no-rfc-1583 delete="delete"/></nc:ospf></nc:protocols>', 'xml 2', 'xml 3']
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - <nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.ospfv2.ospfv2 import (
    Ospfv2Args,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.ospfv2.ospfv2 import (
    Ospfv2,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    module = AnsibleModule(
        argument_spec=Ospfv2Args.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )
    result = Ospfv2(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
