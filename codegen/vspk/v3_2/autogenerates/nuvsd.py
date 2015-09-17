# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUVSDComponentsFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUVSD(NURESTObject):
    """ Represents a VSD in the VSD

        Notes:
            System Monitoring details for VSD

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NUVSD instead.
    """

    __rest_name__ = u"vsd"
    __resource_name__ = u"vsds"

    def __init__(self, **kwargs):
        """ Initializes a VSD instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vsd = NUVSD(id=u'xxxx-xxx-xxx-xxx', name=u'VSD')
                >>> vsd = NUVSD(data=my_dict)
        """

        super(NUVSD, self).__init__()

        # Read/Write Attributes
        
        self._address = None
        self._already_marked_for_unavailable = None
        self._average_cpuusage = None
        self._average_memory_usage = None
        self._current_cpuusage = None
        self._current_memory_usage = None
        self._description = None
        self._disks = None
        self._entity_scope = None
        self._last_state_change = None
        self._location = None
        self._management_ip = None
        self._messages = None
        self._mode = None
        self._name = None
        self._peak_cpuusage = None
        self._peak_memory_usage = None
        self._peer_addresses = None
        self._product_version = None
        self._status = None
        self._unavailable_timestamp = None
        self._url = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"already_marked_for_unavailable", remote_name=u"alreadyMarkedForUnavailable", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"average_cpuusage", remote_name=u"averageCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"average_memory_usage", remote_name=u"averageMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"current_cpuusage", remote_name=u"currentCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"current_memory_usage", remote_name=u"currentMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"disks", remote_name=u"disks", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"entity_scope", remote_name=u"entityScope", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"last_state_change", remote_name=u"lastStateChange", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"location", remote_name=u"location", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"management_ip", remote_name=u"managementIP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"messages", remote_name=u"messages", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"mode", remote_name=u"mode", attribute_type=str, is_required=False, is_unique=False, choices=[u'CLUSTER', u'STANDALONE'])
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"peak_cpuusage", remote_name=u"peakCPUUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"peak_memory_usage", remote_name=u"peakMemoryUsage", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"peer_addresses", remote_name=u"peerAddresses", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str, is_required=False, is_unique=False, choices=[u'ADMIN_DOWN', u'DOWN', u'UP'])
        self.expose_attribute(local_name=u"unavailable_timestamp", remote_name=u"unavailableTimestamp", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"url", remote_name=u"URL", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self)
        
        self.vsd_components = NUVSDComponentsFetcher.fetcher_with_object(parent_object=self)
        
        self.jobs = NUJobsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_address(self):
        """ Get address value.

            Notes:
                An optional IP to access this component.

                
        """
        return self._address

    def _set_address(self, value):
        """ Set address value.

            Notes:
                An optional IP to access this component.

                
        """
        self._address = value

    address = property(_get_address, _set_address)
    
    def _get_already_marked_for_unavailable(self):
        """ Get already_marked_for_unavailable value.

            Notes:
                Flag to indicate that it is already marked a unavailable.

                
                This attribute is named `alreadyMarkedForUnavailable` in VSD API.
                
        """
        return self._already_marked_for_unavailable

    def _set_already_marked_for_unavailable(self, value):
        """ Set already_marked_for_unavailable value.

            Notes:
                Flag to indicate that it is already marked a unavailable.

                
                This attribute is named `alreadyMarkedForUnavailable` in VSD API.
                
        """
        self._already_marked_for_unavailable = value

    already_marked_for_unavailable = property(_get_already_marked_for_unavailable, _set_already_marked_for_unavailable)
    
    def _get_average_cpuusage(self):
        """ Get average_cpuusage value.

            Notes:
                Average CPU usage percentage.

                
                This attribute is named `averageCPUUsage` in VSD API.
                
        """
        return self._average_cpuusage

    def _set_average_cpuusage(self, value):
        """ Set average_cpuusage value.

            Notes:
                Average CPU usage percentage.

                
                This attribute is named `averageCPUUsage` in VSD API.
                
        """
        self._average_cpuusage = value

    average_cpuusage = property(_get_average_cpuusage, _set_average_cpuusage)
    
    def _get_average_memory_usage(self):
        """ Get average_memory_usage value.

            Notes:
                Average memory usage percentage.

                
                This attribute is named `averageMemoryUsage` in VSD API.
                
        """
        return self._average_memory_usage

    def _set_average_memory_usage(self, value):
        """ Set average_memory_usage value.

            Notes:
                Average memory usage percentage.

                
                This attribute is named `averageMemoryUsage` in VSD API.
                
        """
        self._average_memory_usage = value

    average_memory_usage = property(_get_average_memory_usage, _set_average_memory_usage)
    
    def _get_current_cpuusage(self):
        """ Get current_cpuusage value.

            Notes:
                Current CPU usage percentage.

                
                This attribute is named `currentCPUUsage` in VSD API.
                
        """
        return self._current_cpuusage

    def _set_current_cpuusage(self, value):
        """ Set current_cpuusage value.

            Notes:
                Current CPU usage percentage.

                
                This attribute is named `currentCPUUsage` in VSD API.
                
        """
        self._current_cpuusage = value

    current_cpuusage = property(_get_current_cpuusage, _set_current_cpuusage)
    
    def _get_current_memory_usage(self):
        """ Get current_memory_usage value.

            Notes:
                Current memory usage percentage.

                
                This attribute is named `currentMemoryUsage` in VSD API.
                
        """
        return self._current_memory_usage

    def _set_current_memory_usage(self, value):
        """ Set current_memory_usage value.

            Notes:
                Current memory usage percentage.

                
                This attribute is named `currentMemoryUsage` in VSD API.
                
        """
        self._current_memory_usage = value

    current_memory_usage = property(_get_current_memory_usage, _set_current_memory_usage)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                Description of the entity.

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                Description of the entity.

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
    def _get_disks(self):
        """ Get disks value.

            Notes:
                Set of disk usage details.

                
        """
        return self._disks

    def _set_disks(self, value):
        """ Set disks value.

            Notes:
                Set of disk usage details.

                
        """
        self._disks = value

    disks = property(_get_disks, _set_disks)
    
    def _get_entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    def _set_entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    entity_scope = property(_get_entity_scope, _set_entity_scope)
    
    def _get_last_state_change(self):
        """ Get last_state_change value.

            Notes:
                Last state change timestamp (in millis).

                
                This attribute is named `lastStateChange` in VSD API.
                
        """
        return self._last_state_change

    def _set_last_state_change(self, value):
        """ Set last_state_change value.

            Notes:
                Last state change timestamp (in millis).

                
                This attribute is named `lastStateChange` in VSD API.
                
        """
        self._last_state_change = value

    last_state_change = property(_get_last_state_change, _set_last_state_change)
    
    def _get_location(self):
        """ Get location value.

            Notes:
                Identifies the entity to be associated with a location.

                
        """
        return self._location

    def _set_location(self, value):
        """ Set location value.

            Notes:
                Identifies the entity to be associated with a location.

                
        """
        self._location = value

    location = property(_get_location, _set_location)
    
    def _get_management_ip(self):
        """ Get management_ip value.

            Notes:
                An optional management IP to log into this component.

                
                This attribute is named `managementIP` in VSD API.
                
        """
        return self._management_ip

    def _set_management_ip(self, value):
        """ Set management_ip value.

            Notes:
                An optional management IP to log into this component.

                
                This attribute is named `managementIP` in VSD API.
                
        """
        self._management_ip = value

    management_ip = property(_get_management_ip, _set_management_ip)
    
    def _get_messages(self):
        """ Get messages value.

            Notes:
                An array of degraded messages.

                
        """
        return self._messages

    def _set_messages(self, value):
        """ Set messages value.

            Notes:
                An array of degraded messages.

                
        """
        self._messages = value

    messages = property(_get_messages, _set_messages)
    
    def _get_mode(self):
        """ Get mode value.

            Notes:
                Standalone or cluster mode. Possible values are CLUSTER, STANDALONE, .

                
        """
        return self._mode

    def _set_mode(self, value):
        """ Set mode value.

            Notes:
                Standalone or cluster mode. Possible values are CLUSTER, STANDALONE, .

                
        """
        self._mode = value

    mode = property(_get_mode, _set_mode)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Identifies the entity with a name.

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Identifies the entity with a name.

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_peak_cpuusage(self):
        """ Get peak_cpuusage value.

            Notes:
                Peek CPU usage percentage.

                
                This attribute is named `peakCPUUsage` in VSD API.
                
        """
        return self._peak_cpuusage

    def _set_peak_cpuusage(self, value):
        """ Set peak_cpuusage value.

            Notes:
                Peek CPU usage percentage.

                
                This attribute is named `peakCPUUsage` in VSD API.
                
        """
        self._peak_cpuusage = value

    peak_cpuusage = property(_get_peak_cpuusage, _set_peak_cpuusage)
    
    def _get_peak_memory_usage(self):
        """ Get peak_memory_usage value.

            Notes:
                Peek memory usage percentage.

                
                This attribute is named `peakMemoryUsage` in VSD API.
                
        """
        return self._peak_memory_usage

    def _set_peak_memory_usage(self, value):
        """ Set peak_memory_usage value.

            Notes:
                Peek memory usage percentage.

                
                This attribute is named `peakMemoryUsage` in VSD API.
                
        """
        self._peak_memory_usage = value

    peak_memory_usage = property(_get_peak_memory_usage, _set_peak_memory_usage)
    
    def _get_peer_addresses(self):
        """ Get peer_addresses value.

            Notes:
                A comma separated list of peer addresses, if it is in cluster mode.

                
                This attribute is named `peerAddresses` in VSD API.
                
        """
        return self._peer_addresses

    def _set_peer_addresses(self, value):
        """ Set peer_addresses value.

            Notes:
                A comma separated list of peer addresses, if it is in cluster mode.

                
                This attribute is named `peerAddresses` in VSD API.
                
        """
        self._peer_addresses = value

    peer_addresses = property(_get_peer_addresses, _set_peer_addresses)
    
    def _get_product_version(self):
        """ Get product_version value.

            Notes:
                Product version supported by this entity.

                
                This attribute is named `productVersion` in VSD API.
                
        """
        return self._product_version

    def _set_product_version(self, value):
        """ Set product_version value.

            Notes:
                Product version supported by this entity.

                
                This attribute is named `productVersion` in VSD API.
                
        """
        self._product_version = value

    product_version = property(_get_product_version, _set_product_version)
    
    def _get_status(self):
        """ Get status value.

            Notes:
                Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .

                
        """
        return self._status

    def _set_status(self, value):
        """ Set status value.

            Notes:
                Computed status of the entity. Possible values are UP, DOWN, ADMIN_DOWN, .

                
        """
        self._status = value

    status = property(_get_status, _set_status)
    
    def _get_unavailable_timestamp(self):
        """ Get unavailable_timestamp value.

            Notes:
                The duration the controller is unavailable (in millis).

                
                This attribute is named `unavailableTimestamp` in VSD API.
                
        """
        return self._unavailable_timestamp

    def _set_unavailable_timestamp(self, value):
        """ Set unavailable_timestamp value.

            Notes:
                The duration the controller is unavailable (in millis).

                
                This attribute is named `unavailableTimestamp` in VSD API.
                
        """
        self._unavailable_timestamp = value

    unavailable_timestamp = property(_get_unavailable_timestamp, _set_unavailable_timestamp)
    
    def _get_url(self):
        """ Get url value.

            Notes:
                An optional web url for management.

                
                This attribute is named `URL` in VSD API.
                
        """
        return self._url

    def _set_url(self, value):
        """ Set url value.

            Notes:
                An optional web url for management.

                
                This attribute is named `URL` in VSD API.
                
        """
        self._url = value

    url = property(_get_url, _set_url)
    