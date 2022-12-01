# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkopensearch.endpoint import endpoint_data

class ListAppGroupMetricsRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'OpenSearch', '2017-12-25', 'ListAppGroupMetrics')
		self.set_uri_pattern('/v4/openapi/app-groups/[appGroupIdentity]/metrics')
		self.set_method('GET')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_metricType(self): # String
		return self.get_query_params().get('metricType')

	def set_metricType(self, metricType):  # String
		self.add_query_param('metricType', metricType)
	def get_indexes(self): # String
		return self.get_query_params().get('indexes')

	def set_indexes(self, indexes):  # String
		self.add_query_param('indexes', indexes)
	def get_endTime(self): # Integer
		return self.get_query_params().get('endTime')

	def set_endTime(self, endTime):  # Integer
		self.add_query_param('endTime', endTime)
	def get_startTime(self): # Integer
		return self.get_query_params().get('startTime')

	def set_startTime(self, startTime):  # Integer
		self.add_query_param('startTime', startTime)
	def get_appGroupIdentity(self): # String
		return self.get_path_params().get('appGroupIdentity')

	def set_appGroupIdentity(self, appGroupIdentity):  # String
		self.add_path_param('appGroupIdentity', appGroupIdentity)
