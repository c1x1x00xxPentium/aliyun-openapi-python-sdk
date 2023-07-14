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

class GetSubCrowdRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'PaiRecService', '2022-12-13', 'GetSubCrowd')
		self.set_uri_pattern('/api/v1/crowds/[CrowdId]/subcrowds/[SubCrowdId]')
		self.set_method('GET')

	def get_CrowdId(self): # String
		return self.get_path_params().get('CrowdId')

	def set_CrowdId(self, CrowdId):  # String
		self.add_path_param('CrowdId', CrowdId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_SubCrowdId(self): # String
		return self.get_path_params().get('SubCrowdId')

	def set_SubCrowdId(self, SubCrowdId):  # String
		self.add_path_param('SubCrowdId', SubCrowdId)
