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


class NUStatistics(NURESTObject):
    """ Represents a Statistics in the VSD

        Notes:
            Retrieves the statistics for a particular domain, zone, subnet, or VM

        Warning:
            This file has been autogenerated. You should never change it.
            Override .NUStatistics instead.
    """

    __rest_name__ = u"statistics"
    __resource_name__ = u"statistics"

    def __init__(self, **kwargs):
        """ Initializes a Statistics instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> statistics = NUStatistics(id=u'xxxx-xxx-xxx-xxx', name=u'Statistics')
                >>> statistics = NUStatistics(data=my_dict)
        """

        super(NUStatistics, self).__init__()

        # Read/Write Attributes
        
        self._end_time = None
        self._number_of_data_points = None
        self._start_time = None
        self._stats_data = None
        self._version = None
        
        self.expose_attribute(local_name=u"end_time", remote_name=u"endTime", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"number_of_data_points", remote_name=u"numberOfDataPoints", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"start_time", remote_name=u"startTime", attribute_type=long, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"stats_data", remote_name=u"statsData", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name=u"version", remote_name=u"version", attribute_type=long, is_required=False, is_unique=False)
        
        
        self.metadata = NUMetadatasFetcher.fetcher_with_object(parent_object=self)
        

        self._compute_args(**kwargs)

    # Properties
    
    def _get_end_time(self):
        """ Get end_time value.

            Notes:
                End time for the statistics to be retrieved

                
                This attribute is named `endTime` in VSD API.
                
        """
        return self._end_time

    def _set_end_time(self, value):
        """ Set end_time value.

            Notes:
                End time for the statistics to be retrieved

                
                This attribute is named `endTime` in VSD API.
                
        """
        self._end_time = value

    end_time = property(_get_end_time, _set_end_time)
    
    def _get_number_of_data_points(self):
        """ Get number_of_data_points value.

            Notes:
                Number of data points between start time and end time

                
                This attribute is named `numberOfDataPoints` in VSD API.
                
        """
        return self._number_of_data_points

    def _set_number_of_data_points(self, value):
        """ Set number_of_data_points value.

            Notes:
                Number of data points between start time and end time

                
                This attribute is named `numberOfDataPoints` in VSD API.
                
        """
        self._number_of_data_points = value

    number_of_data_points = property(_get_number_of_data_points, _set_number_of_data_points)
    
    def _get_start_time(self):
        """ Get start_time value.

            Notes:
                Start time for the statistics to be retrieved

                
                This attribute is named `startTime` in VSD API.
                
        """
        return self._start_time

    def _set_start_time(self, value):
        """ Set start_time value.

            Notes:
                Start time for the statistics to be retrieved

                
                This attribute is named `startTime` in VSD API.
                
        """
        self._start_time = value

    start_time = property(_get_start_time, _set_start_time)
    
    def _get_stats_data(self):
        """ Get stats_data value.

            Notes:
                Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packets_out_errors, packets_dropped_rate_limit

                
                This attribute is named `statsData` in VSD API.
                
        """
        return self._stats_data

    def _set_stats_data(self, value):
        """ Set stats_data value.

            Notes:
                Map&lt;TCAMetric, Long[]&gt; TCAMetric is an Enum. Possible values are packets_in, bytes_in, packets_in_dropped, packets_in_errors, packets_out, bytes_out, packets_out_dropped, packets_out_errors, packets_dropped_rate_limit

                
                This attribute is named `statsData` in VSD API.
                
        """
        self._stats_data = value

    stats_data = property(_get_stats_data, _set_stats_data)
    
    def _get_version(self):
        """ Get version value.

            Notes:
                Version of this Sequence number.

                
        """
        return self._version

    def _set_version(self, value):
        """ Set version value.

            Notes:
                Version of this Sequence number.

                
        """
        self._version = value

    version = property(_get_version, _set_version)
    