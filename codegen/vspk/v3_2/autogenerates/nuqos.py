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


from ..fetchers import NUVMsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUQOS(NURESTObject):
    """ Represents a QOS in the VSD

        Notes:
            The object manipulates the QoS parameters attached to a domain, zone, or subnet

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NUQOS instead.
    """

    __rest_name__ = u"qos"
    __resource_name__ = u"qos"

    def __init__(self, **kwargs):
        """ Initializes a QOS instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> qos = NUQOS(id=u'xxxx-xxx-xxx-xxx', name=u'QOS')
                >>> qos = NUQOS(data=my_dict)
        """

        super(NUQOS, self).__init__()

        # Read/Write Attributes
        
        self._active = None
        self._assoc_qos_id = None
        self._associated_dscp_forwarding_class_table_id = None
        self._associated_dscp_forwarding_class_table_name = None
        self._bum_committed_burst_size = None
        self._bum_committed_information_rate = None
        self._bum_peak_burst_size = None
        self._bum_peak_information_rate = None
        self._bum_rate_limiting_active = None
        self._burst = None
        self._committed_burst_size = None
        self._committed_information_rate = None
        self._description = None
        self._entity_scope = None
        self._fip_committed_burst_size = None
        self._fip_committed_information_rate = None
        self._fip_peak_burst_size = None
        self._fip_peak_information_rate = None
        self._fip_rate_limiting_active = None
        self._name = None
        self._peak = None
        self._rate_limiting_active = None
        self._rewrite_forwarding_class = None
        self._service_class = None
        self._trusted_forwarding_class = None
        
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"assoc_qos_id", remote_name=u"assocQosId", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_dscp_forwarding_class_table_id", remote_name=u"associatedDSCPForwardingClassTableID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"associated_dscp_forwarding_class_table_name", remote_name=u"associatedDSCPForwardingClassTableName", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"bum_committed_burst_size", remote_name=u"BUMCommittedBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"bum_committed_information_rate", remote_name=u"BUMCommittedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"bum_peak_burst_size", remote_name=u"BUMPeakBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"bum_peak_information_rate", remote_name=u"BUMPeakInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"bum_rate_limiting_active", remote_name=u"BUMRateLimitingActive", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"burst", remote_name=u"burst", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"committed_burst_size", remote_name=u"committedBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"committed_information_rate", remote_name=u"committedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"entity_scope", remote_name=u"entityScope", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"fip_committed_burst_size", remote_name=u"FIPCommittedBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"fip_committed_information_rate", remote_name=u"FIPCommittedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"fip_peak_burst_size", remote_name=u"FIPPeakBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"fip_peak_information_rate", remote_name=u"FIPPeakInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"fip_rate_limiting_active", remote_name=u"FIPRateLimitingActive", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"peak", remote_name=u"peak", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"rate_limiting_active", remote_name=u"rateLimitingActive", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"rewrite_forwarding_class", remote_name=u"rewriteForwardingClass", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"service_class", remote_name=u"serviceClass", attribute_type=str, is_required=True, is_unique=False, choices=[u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H', u'NONE'])
        self.expose_attribute(local_name=u"trusted_forwarding_class", remote_name=u"trustedForwardingClass", attribute_type=bool, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_active(self):
        """ Get active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        return self._active

    def _set_active(self, value):
        """ Set active value.

            Notes:
                If enabled, it means that this ACL or QOS entry is active

                
        """
        self._active = value

    active = property(_get_active, _set_active)
    
    def _get_assoc_qos_id(self):
        """ Get assoc_qos_id value.

            Notes:
                ID of object associated with this QoS object

                
                This attribute is named `assocQosId` in VSD API.
                
        """
        return self._assoc_qos_id

    def _set_assoc_qos_id(self, value):
        """ Set assoc_qos_id value.

            Notes:
                ID of object associated with this QoS object

                
                This attribute is named `assocQosId` in VSD API.
                
        """
        self._assoc_qos_id = value

    assoc_qos_id = property(_get_assoc_qos_id, _set_assoc_qos_id)
    
    def _get_associated_dscp_forwarding_class_table_id(self):
        """ Get associated_dscp_forwarding_class_table_id value.

            Notes:
                ID of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableID` in VSD API.
                
        """
        return self._associated_dscp_forwarding_class_table_id

    def _set_associated_dscp_forwarding_class_table_id(self, value):
        """ Set associated_dscp_forwarding_class_table_id value.

            Notes:
                ID of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableID` in VSD API.
                
        """
        self._associated_dscp_forwarding_class_table_id = value

    associated_dscp_forwarding_class_table_id = property(_get_associated_dscp_forwarding_class_table_id, _set_associated_dscp_forwarding_class_table_id)
    
    def _get_associated_dscp_forwarding_class_table_name(self):
        """ Get associated_dscp_forwarding_class_table_name value.

            Notes:
                Name of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableName` in VSD API.
                
        """
        return self._associated_dscp_forwarding_class_table_name

    def _set_associated_dscp_forwarding_class_table_name(self, value):
        """ Set associated_dscp_forwarding_class_table_name value.

            Notes:
                Name of the DSCP->Forwarding Class used by this Qos Policy

                
                This attribute is named `associatedDSCPForwardingClassTableName` in VSD API.
                
        """
        self._associated_dscp_forwarding_class_table_name = value

    associated_dscp_forwarding_class_table_name = property(_get_associated_dscp_forwarding_class_table_name, _set_associated_dscp_forwarding_class_table_name)
    
    def _get_bum_committed_burst_size(self):
        """ Get bum_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for BUM Shaper.

                
                This attribute is named `BUMCommittedBurstSize` in VSD API.
                
        """
        return self._bum_committed_burst_size

    def _set_bum_committed_burst_size(self, value):
        """ Set bum_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for BUM Shaper.

                
                This attribute is named `BUMCommittedBurstSize` in VSD API.
                
        """
        self._bum_committed_burst_size = value

    bum_committed_burst_size = property(_get_bum_committed_burst_size, _set_bum_committed_burst_size)
    
    def _get_bum_committed_information_rate(self):
        """ Get bum_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for BUM Shaper.

                
                This attribute is named `BUMCommittedInformationRate` in VSD API.
                
        """
        return self._bum_committed_information_rate

    def _set_bum_committed_information_rate(self, value):
        """ Set bum_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for BUM Shaper.

                
                This attribute is named `BUMCommittedInformationRate` in VSD API.
                
        """
        self._bum_committed_information_rate = value

    bum_committed_information_rate = property(_get_bum_committed_information_rate, _set_bum_committed_information_rate)
    
    def _get_bum_peak_burst_size(self):
        """ Get bum_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for Broadcast/Multicast rate limiting (BUM).

                
                This attribute is named `BUMPeakBurstSize` in VSD API.
                
        """
        return self._bum_peak_burst_size

    def _set_bum_peak_burst_size(self, value):
        """ Set bum_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for Broadcast/Multicast rate limiting (BUM).

                
                This attribute is named `BUMPeakBurstSize` in VSD API.
                
        """
        self._bum_peak_burst_size = value

    bum_peak_burst_size = property(_get_bum_peak_burst_size, _set_bum_peak_burst_size)
    
    def _get_bum_peak_information_rate(self):
        """ Get bum_peak_information_rate value.

            Notes:
                Peak rate setting in Mb/s for Broadcast/Multicast rate limiting 

                
                This attribute is named `BUMPeakInformationRate` in VSD API.
                
        """
        return self._bum_peak_information_rate

    def _set_bum_peak_information_rate(self, value):
        """ Set bum_peak_information_rate value.

            Notes:
                Peak rate setting in Mb/s for Broadcast/Multicast rate limiting 

                
                This attribute is named `BUMPeakInformationRate` in VSD API.
                
        """
        self._bum_peak_information_rate = value

    bum_peak_information_rate = property(_get_bum_peak_information_rate, _set_bum_peak_information_rate)
    
    def _get_bum_rate_limiting_active(self):
        """ Get bum_rate_limiting_active value.

            Notes:
                Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled

                
                This attribute is named `BUMRateLimitingActive` in VSD API.
                
        """
        return self._bum_rate_limiting_active

    def _set_bum_rate_limiting_active(self, value):
        """ Set bum_rate_limiting_active value.

            Notes:
                Flag the indicates whether Broadcast/Multicast rate limiting is enabled or disabled

                
                This attribute is named `BUMRateLimitingActive` in VSD API.
                
        """
        self._bum_rate_limiting_active = value

    bum_rate_limiting_active = property(_get_bum_rate_limiting_active, _set_bum_rate_limiting_active)
    
    def _get_burst(self):
        """ Get burst value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        return self._burst

    def _set_burst(self, value):
        """ Set burst value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        self._burst = value

    burst = property(_get_burst, _set_burst)
    
    def _get_committed_burst_size(self):
        """ Get committed_burst_size value.

            Notes:
                Committed Burst Size :  Burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values are supported.

                
                This attribute is named `committedBurstSize` in VSD API.
                
        """
        return self._committed_burst_size

    def _set_committed_burst_size(self, value):
        """ Set committed_burst_size value.

            Notes:
                Committed Burst Size :  Burst size associated with the rate limiter in kilo-bytes (kilo-octets); only whole values are supported.

                
                This attribute is named `committedBurstSize` in VSD API.
                
        """
        self._committed_burst_size = value

    committed_burst_size = property(_get_committed_burst_size, _set_committed_burst_size)
    
    def _get_committed_information_rate(self):
        """ Get committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed from each VM in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        return self._committed_information_rate

    def _set_committed_information_rate(self, value):
        """ Set committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed from each VM in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        self._committed_information_rate = value

    committed_information_rate = property(_get_committed_information_rate, _set_committed_information_rate)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the QoS object

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the QoS object

                
        """
        self._description = value

    description = property(_get_description, _set_description)
    
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
    
    def _get_fip_committed_burst_size(self):
        """ Get fip_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for FIP Shaper.

                
                This attribute is named `FIPCommittedBurstSize` in VSD API.
                
        """
        return self._fip_committed_burst_size

    def _set_fip_committed_burst_size(self, value):
        """ Set fip_committed_burst_size value.

            Notes:
                Committed burst size setting in kilo-bytes (kilo-octets) for FIP Shaper.

                
                This attribute is named `FIPCommittedBurstSize` in VSD API.
                
        """
        self._fip_committed_burst_size = value

    fip_committed_burst_size = property(_get_fip_committed_burst_size, _set_fip_committed_burst_size)
    
    def _get_fip_committed_information_rate(self):
        """ Get fip_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for FIP Shaper.

                
                This attribute is named `FIPCommittedInformationRate` in VSD API.
                
        """
        return self._fip_committed_information_rate

    def _set_fip_committed_information_rate(self, value):
        """ Set fip_committed_information_rate value.

            Notes:
                Committed information rate setting in Mb/s for FIP Shaper.

                
                This attribute is named `FIPCommittedInformationRate` in VSD API.
                
        """
        self._fip_committed_information_rate = value

    fip_committed_information_rate = property(_get_fip_committed_information_rate, _set_fip_committed_information_rate)
    
    def _get_fip_peak_burst_size(self):
        """ Get fip_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for FIP rate limiting.

                
                This attribute is named `FIPPeakBurstSize` in VSD API.
                
        """
        return self._fip_peak_burst_size

    def _set_fip_peak_burst_size(self, value):
        """ Set fip_peak_burst_size value.

            Notes:
                Peak burst size setting in kilo-bytes (kilo-octets) for FIP rate limiting.

                
                This attribute is named `FIPPeakBurstSize` in VSD API.
                
        """
        self._fip_peak_burst_size = value

    fip_peak_burst_size = property(_get_fip_peak_burst_size, _set_fip_peak_burst_size)
    
    def _get_fip_peak_information_rate(self):
        """ Get fip_peak_information_rate value.

            Notes:
                Peak rate setting for FIP rate limiting in Mb/s;

                
                This attribute is named `FIPPeakInformationRate` in VSD API.
                
        """
        return self._fip_peak_information_rate

    def _set_fip_peak_information_rate(self, value):
        """ Set fip_peak_information_rate value.

            Notes:
                Peak rate setting for FIP rate limiting in Mb/s;

                
                This attribute is named `FIPPeakInformationRate` in VSD API.
                
        """
        self._fip_peak_information_rate = value

    fip_peak_information_rate = property(_get_fip_peak_information_rate, _set_fip_peak_information_rate)
    
    def _get_fip_rate_limiting_active(self):
        """ Get fip_rate_limiting_active value.

            Notes:
                Flag the indicates whether FIP rate limiting is enabled or disabled

                
                This attribute is named `FIPRateLimitingActive` in VSD API.
                
        """
        return self._fip_rate_limiting_active

    def _set_fip_rate_limiting_active(self, value):
        """ Set fip_rate_limiting_active value.

            Notes:
                Flag the indicates whether FIP rate limiting is enabled or disabled

                
                This attribute is named `FIPRateLimitingActive` in VSD API.
                
        """
        self._fip_rate_limiting_active = value

    fip_rate_limiting_active = property(_get_fip_rate_limiting_active, _set_fip_rate_limiting_active)
    
    def _get_name(self):
        """ Get name value.

            Notes:
                A unique name of the QoS object

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                A unique name of the QoS object

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_peak(self):
        """ Get peak value.

            Notes:
                Peak Information Rate :  Peak bandwidth that is allowed from each VM in Mb/s; only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        return self._peak

    def _set_peak(self, value):
        """ Set peak value.

            Notes:
                Peak Information Rate :  Peak bandwidth that is allowed from each VM in Mb/s; only whole values allowed and 'INFINITY' if rate limiting is disabled.

                
        """
        self._peak = value

    peak = property(_get_peak, _set_peak)
    
    def _get_rate_limiting_active(self):
        """ Get rate_limiting_active value.

            Notes:
                Identifies if rate limiting must be implemented

                
                This attribute is named `rateLimitingActive` in VSD API.
                
        """
        return self._rate_limiting_active

    def _set_rate_limiting_active(self, value):
        """ Set rate_limiting_active value.

            Notes:
                Identifies if rate limiting must be implemented

                
                This attribute is named `rateLimitingActive` in VSD API.
                
        """
        self._rate_limiting_active = value

    rate_limiting_active = property(_get_rate_limiting_active, _set_rate_limiting_active)
    
    def _get_rewrite_forwarding_class(self):
        """ Get rewrite_forwarding_class value.

            Notes:
                Specifies if the rewrite flag is set for the QoS policy / template

                
                This attribute is named `rewriteForwardingClass` in VSD API.
                
        """
        return self._rewrite_forwarding_class

    def _set_rewrite_forwarding_class(self, value):
        """ Set rewrite_forwarding_class value.

            Notes:
                Specifies if the rewrite flag is set for the QoS policy / template

                
                This attribute is named `rewriteForwardingClass` in VSD API.
                
        """
        self._rewrite_forwarding_class = value

    rewrite_forwarding_class = property(_get_rewrite_forwarding_class, _set_rewrite_forwarding_class)
    
    def _get_service_class(self):
        """ Get service_class value.

            Notes:
                Class of service to be used. Service classes in order of priority are A(1), B(2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        return self._service_class

    def _set_service_class(self, value):
        """ Set service_class value.

            Notes:
                Class of service to be used. Service classes in order of priority are A(1), B(2), C(3), D(4), E(5), F(6), G(7) and H(8) Possible values are NONE, A, B, C, D, E, F, G, H, .

                
                This attribute is named `serviceClass` in VSD API.
                
        """
        self._service_class = value

    service_class = property(_get_service_class, _set_service_class)
    
    def _get_trusted_forwarding_class(self):
        """ Get trusted_forwarding_class value.

            Notes:
                Specifies if the trusted flag is set for the QoS policy / template

                
                This attribute is named `trustedForwardingClass` in VSD API.
                
        """
        return self._trusted_forwarding_class

    def _set_trusted_forwarding_class(self, value):
        """ Set trusted_forwarding_class value.

            Notes:
                Specifies if the trusted flag is set for the QoS policy / template

                
                This attribute is named `trustedForwardingClass` in VSD API.
                
        """
        self._trusted_forwarding_class = value

    trusted_forwarding_class = property(_get_trusted_forwarding_class, _set_trusted_forwarding_class)
    