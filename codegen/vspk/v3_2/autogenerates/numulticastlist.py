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


from ..fetchers import NUMultiCastChannelMapsFetcher
from ..fetchers import NUMetadatasFetcher
from bambou import NURESTObject


class NUMultiCastList(NURESTObject):
    """ Represents a MultiCastList in the VSD

        Notes:
            This is the definition of a MultiCast Channel List

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NUMultiCastList instead.
    """

    __rest_name__ = u"multicastlist"
    __resource_name__ = u"multicastlists"

    def __init__(self, **kwargs):
        """ Initializes a MultiCastList instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> multicastlist = NUMultiCastList(id=u'xxxx-xxx-xxx-xxx', name=u'MultiCastList')
                >>> multicastlist = NUMultiCastList(data=my_dict)
        """

        super(NUMultiCastList, self).__init__()

        # Read/Write Attributes
        
        self._entity_scope = None
        self._mcast_type = None
        
        self.expose_attribute(local_name=u"entity_scope", remote_name=u"entityScope", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"mcast_type", remote_name=u"mcastType", attribute_type=str, is_required=False, is_unique=False, choices=[u'RECEIVE', u'SEND'])
        
        # Fetchers
        
        self.multi_cast_channel_maps = NUMultiCastChannelMapsFetcher.fetcher_with_object(parent_object=self)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
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
    
    def _get_mcast_type(self):
        """ Get mcast_type value.

            Notes:
                Type of multicast list - send or receive Possible values are SEND, RECEIVE, .

                
                This attribute is named `mcastType` in VSD API.
                
        """
        return self._mcast_type

    def _set_mcast_type(self, value):
        """ Set mcast_type value.

            Notes:
                Type of multicast list - send or receive Possible values are SEND, RECEIVE, .

                
                This attribute is named `mcastType` in VSD API.
                
        """
        self._mcast_type = value

    mcast_type = property(_get_mcast_type, _set_mcast_type)
    