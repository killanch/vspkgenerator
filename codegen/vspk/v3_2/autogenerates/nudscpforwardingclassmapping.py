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


from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUDSCPForwardingClassMapping(NURESTObject):
    """ Represents a DSCPForwardingClassMapping in the VSD

        Notes:
            Provides the definition of a single DSCP -> Forwarding class mapping that is part of a Table used in QoS policies.

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NUDSCPForwardingClassMapping instead.
    """

    __rest_name__ = u"dscpforwardingclassmapping"
    __resource_name__ = u"dscpforwardingclassmappings"

    def __init__(self, **kwargs):
        """ Initializes a DSCPForwardingClassMapping instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> dscpforwardingclassmapping = NUDSCPForwardingClassMapping(id=u'xxxx-xxx-xxx-xxx', name=u'DSCPForwardingClassMapping')
                >>> dscpforwardingclassmapping = NUDSCPForwardingClassMapping(data=my_dict)
        """

        super(NUDSCPForwardingClassMapping, self).__init__()

        # Read/Write Attributes
        
        self._dscp = None
        self._entity_scope = None
        self._forwarding_class = None
        
        self.expose_attribute(local_name=u"dscp", remote_name=u"DSCP", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"entity_scope", remote_name=u"entityScope", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"forwarding_class", remote_name=u"forwardingClass", attribute_type=str, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_dscp(self):
        """ Get dscp value.

            Notes:
                DSCP value range from enumeration of 65 values :  *, 0, 1, ..., 63

                
                This attribute is named `DSCP` in VSD API.
                
        """
        return self._dscp

    def _set_dscp(self, value):
        """ Set dscp value.

            Notes:
                DSCP value range from enumeration of 65 values :  *, 0, 1, ..., 63

                
                This attribute is named `DSCP` in VSD API.
                
        """
        self._dscp = value

    dscp = property(_get_dscp, _set_dscp)
    
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
    
    def _get_forwarding_class(self):
        """ Get forwarding_class value.

            Notes:
                Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `forwardingClass` in VSD API.
                
        """
        return self._forwarding_class

    def _set_forwarding_class(self, value):
        """ Set forwarding_class value.

            Notes:
                Class of service to be used.  Service classes in order of priority are A, B, C, D, E, F, G, and H.

                
                This attribute is named `forwardingClass` in VSD API.
                
        """
        self._forwarding_class = value

    forwarding_class = property(_get_forwarding_class, _set_forwarding_class)
    