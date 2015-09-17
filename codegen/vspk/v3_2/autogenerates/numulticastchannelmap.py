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
from ..fetchers import NUMultiCastRangesFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUMultiCastChannelMap(NURESTObject):
    """ Represents a MultiCastChannelMap in the VSD

        Notes:
            This is the definition of a MultiCast Channel Map

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NUMultiCastChannelMap instead.
    """

    __rest_name__ = u"multicastchannelmap"
    __resource_name__ = u"multicastchannelmaps"

    def __init__(self, **kwargs):
        """ Initializes a MultiCastChannelMap instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> multicastchannelmap = NUMultiCastChannelMap(id=u'xxxx-xxx-xxx-xxx', name=u'MultiCastChannelMap')
                >>> multicastchannelmap = NUMultiCastChannelMap(data=my_dict)
        """

        super(NUMultiCastChannelMap, self).__init__()

        # Read/Write Attributes
        
        self._description = None
        self._entity_scope = None
        self._name = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"entity_scope", remote_name=u"entityScope", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        
        # Fetchers
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self)
        
        self.multi_cast_ranges = NUMultiCastRangesFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description field provided by the user that identifies the MultiCast Channel Map

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description field provided by the user that identifies the MultiCast Channel Map

                
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
                Name of the current entity

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                Name of the current entity

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    