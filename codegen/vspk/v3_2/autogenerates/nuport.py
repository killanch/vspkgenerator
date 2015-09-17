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


from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUVLANsFetcher
from ..fetchers import NUEnterprisePermissionsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUPort(NURESTObject):
    """ Represents a Port in the VSD

        Notes:
            Represents Port under a particular gateway object or redundant group object.

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NUPort instead.
    """

    __rest_name__ = u"port"
    __resource_name__ = u"ports"

    def __init__(self, **kwargs):
        """ Initializes a Port instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> port = NUPort(id=u'xxxx-xxx-xxx-xxx', name=u'Port')
                >>> port = NUPort(data=my_dict)
        """

        super(NUPort, self).__init__()

        # Read/Write Attributes
        
        self._associated_egress_qos_policy_id = None
        self._description = None
        self._entity_scope = None
        self._name = None
        self._permitted_action = None
        self._physical_name = None
        self._port_type = None
        self._status = None
        self._template_id = None
        self._use_user_mnemonic = None
        self._user_mnemonic = None
        self._vlan_range = None
        
        self.expose_attribute(local_name=u"associated_egress_qos_policy_id", remote_name=u"associatedEgressQOSPolicyID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"entity_scope", remote_name=u"entityScope", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str, is_required=False, is_unique=False, choices=[u'ALL', u'DEPLOY', u'EXTEND', u'INSTANTIATE', u'READ', u'USE'])
        self.expose_attribute(local_name=u"physical_name", remote_name=u"physicalName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"port_type", remote_name=u"portType", attribute_type=str, is_required=True, is_unique=False, choices=[u'ACCESS', u'NETWORK'])
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str, is_required=False, is_unique=False, choices=[u'INITIALIZED', u'MISMATCH', u'ORPHAN', u'READY'])
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"use_user_mnemonic", remote_name=u"useUserMnemonic", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"user_mnemonic", remote_name=u"userMnemonic", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"vlan_range", remote_name=u"VLANRange", attribute_type=str, is_required=False, is_unique=False)
        
        # Fetchers
        
        self.alarms = NUAlarmsFetcher.fetcher_with_object(parent_object=self)
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.vlans = NUVLANsFetcher.fetcher_with_object(parent_object=self)
        
        self.enterprise_permissions = NUEnterprisePermissionsFetcher.fetcher_with_object(parent_object=self)
        
        self.permitted_actions = NUPermittedActionsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_associated_egress_qos_policy_id(self):
        """ Get associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        return self._associated_egress_qos_policy_id

    def _set_associated_egress_qos_policy_id(self, value):
        """ Set associated_egress_qos_policy_id value.

            Notes:
                ID of the Egress QOS Policy associated with this Vlan.

                
                This attribute is named `associatedEgressQOSPolicyID` in VSD API.
                
        """
        self._associated_egress_qos_policy_id = value

    associated_egress_qos_policy_id = property(_get_associated_egress_qos_policy_id, _set_associated_egress_qos_policy_id)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the Port

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the Port

                
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
    
    def _get_name(self):
        """ Get name value.

            Notes:
                Name of the Port

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the Port

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_permitted_action(self):
        """ Get permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        return self._permitted_action

    def _set_permitted_action(self, value):
        """ Set permitted_action value.

            Notes:
                The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .

                
                This attribute is named `permittedAction` in VSD API.
                
        """
        self._permitted_action = value

    permitted_action = property(_get_permitted_action, _set_permitted_action)
    
    def _get_physical_name(self):
        """ Get physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        return self._physical_name

    def _set_physical_name(self, value):
        """ Set physical_name value.

            Notes:
                Identifier of the Port

                
                This attribute is named `physicalName` in VSD API.
                
        """
        self._physical_name = value

    physical_name = property(_get_physical_name, _set_physical_name)
    
    def _get_port_type(self):
        """ Get port_type value.

            Notes:
                Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .

                
                This attribute is named `portType` in VSD API.
                
        """
        return self._port_type

    def _set_port_type(self, value):
        """ Set port_type value.

            Notes:
                Type of the Port - NETWORK, ACCESS Possible values are ACCESS, NETWORK, .

                
                This attribute is named `portType` in VSD API.
                
        """
        self._port_type = value

    port_type = property(_get_port_type, _set_port_type)
    
    def _get_status(self):
        """ Get status value.

            Notes:
                Status of the port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .

                
        """
        return self._status

    def _set_status(self, value):
        """ Set status value.

            Notes:
                Status of the port. Possible values are - INITIALIZED, ORPHAN, READY, MISMATCH Possible values are INITIALIZED, ORPHAN, READY, MISMATCH, .

                
        """
        self._status = value

    status = property(_get_status, _set_status)
    
    def _get_template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the template that this Port was created from

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    def _set_template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the template that this Port was created from

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    template_id = property(_get_template_id, _set_template_id)
    
    def _get_use_user_mnemonic(self):
        """ Get use_user_mnemonic value.

            Notes:
                determines whether to use user mnemonic of the Port

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        return self._use_user_mnemonic

    def _set_use_user_mnemonic(self, value):
        """ Set use_user_mnemonic value.

            Notes:
                determines whether to use user mnemonic of the Port

                
                This attribute is named `useUserMnemonic` in VSD API.
                
        """
        self._use_user_mnemonic = value

    use_user_mnemonic = property(_get_use_user_mnemonic, _set_use_user_mnemonic)
    
    def _get_user_mnemonic(self):
        """ Get user_mnemonic value.

            Notes:
                user mnemonic of the Port

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        return self._user_mnemonic

    def _set_user_mnemonic(self, value):
        """ Set user_mnemonic value.

            Notes:
                user mnemonic of the Port

                
                This attribute is named `userMnemonic` in VSD API.
                
        """
        self._user_mnemonic = value

    user_mnemonic = property(_get_user_mnemonic, _set_user_mnemonic)
    
    def _get_vlan_range(self):
        """ Get vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        return self._vlan_range

    def _set_vlan_range(self, value):
        """ Set vlan_range value.

            Notes:
                VLAN Range of the Port.  Format must conform to a-b,c,d-f where a,b,c,d,f are integers between 0 and 4095.

                
                This attribute is named `VLANRange` in VSD API.
                
        """
        self._vlan_range = value

    vlan_range = property(_get_vlan_range, _set_vlan_range)
    