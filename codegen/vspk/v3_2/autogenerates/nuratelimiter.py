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


class NURateLimiter(NURESTObject):
    """ Represents a RateLimiter in the VSD

        Notes:
            Rate Limiter object that contains peak, burst and cir. Can be associated with Egress QOS policy objects.

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NURateLimiter instead.
    """

    __rest_name__ = u"ratelimiter"
    __resource_name__ = u"ratelimiters"

    def __init__(self, **kwargs):
        """ Initializes a RateLimiter instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> ratelimiter = NURateLimiter(id=u'xxxx-xxx-xxx-xxx', name=u'RateLimiter')
                >>> ratelimiter = NURateLimiter(data=my_dict)
        """

        super(NURateLimiter, self).__init__()

        # Read/Write Attributes
        
        self._committed_information_rate = None
        self._description = None
        self._entity_scope = None
        self._name = None
        self._peak_burst_size = None
        self._peak_information_rate = None
        
        self.expose_attribute(local_name=u"committed_information_rate", remote_name=u"committedInformationRate", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"entity_scope", remote_name=u"entityScope", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name=u"peak_burst_size", remote_name=u"peakBurstSize", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"peak_information_rate", remote_name=u"peakInformationRate", attribute_type=str, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_committed_information_rate(self):
        """ Get committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        return self._committed_information_rate

    def _set_committed_information_rate(self, value):
        """ Set committed_information_rate value.

            Notes:
                Committed Information Rate :  Committed bandwidth that is allowed in Mb/s; only whole values supported.

                
                This attribute is named `committedInformationRate` in VSD API.
                
        """
        self._committed_information_rate = value

    committed_information_rate = property(_get_committed_information_rate, _set_committed_information_rate)
    
    def _get_description(self):
        """ Get description value.

            Notes:
                A description of the Rate Limiter object

                
        """
        return self._description

    def _set_description(self, value):
        """ Set description value.

            Notes:
                A description of the Rate Limiter object

                
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
                A unique name of the Rate Limiter object

                
        """
        return self._name

    def _set_name(self, value):
        """ Set name value.

            Notes:
                A unique name of the Rate Limiter object

                
        """
        self._name = value

    name = property(_get_name, _set_name)
    
    def _get_peak_burst_size(self):
        """ Get peak_burst_size value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.

                
                This attribute is named `peakBurstSize` in VSD API.
                
        """
        return self._peak_burst_size

    def _set_peak_burst_size(self, value):
        """ Set peak_burst_size value.

            Notes:
                Peak Burst Size :  The maximum burst size associated with the rate limiter in kilo-bits; only whole values are supported.

                
                This attribute is named `peakBurstSize` in VSD API.
                
        """
        self._peak_burst_size = value

    peak_burst_size = property(_get_peak_burst_size, _set_peak_burst_size)
    
    def _get_peak_information_rate(self):
        """ Get peak_information_rate value.

            Notes:
                Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.

                
                This attribute is named `peakInformationRate` in VSD API.
                
        """
        return self._peak_information_rate

    def _set_peak_information_rate(self, value):
        """ Set peak_information_rate value.

            Notes:
                Peak Information Rate :  Peak bandwidth allowed in Mb/s; only whole values supported.

                
                This attribute is named `peakInformationRate` in VSD API.
                
        """
        self._peak_information_rate = value

    peak_information_rate = property(_get_peak_information_rate, _set_peak_information_rate)
    