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

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvod.endpoint import endpoint_data

class SubmitAIImageJobRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vod', '2017-03-21', 'SubmitAIImageJob','vod')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # String
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # String
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_AIPipelineId(self): # String
		return self.get_query_params().get('AIPipelineId')

	def set_AIPipelineId(self, AIPipelineId):  # String
		self.add_query_param('AIPipelineId', AIPipelineId)
	def get_UserData(self): # String
		return self.get_query_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_query_param('UserData', UserData)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_VideoId(self): # String
		return self.get_query_params().get('VideoId')

	def set_VideoId(self, VideoId):  # String
		self.add_query_param('VideoId', VideoId)
	def get_AITemplateId(self): # String
		return self.get_query_params().get('AITemplateId')

	def set_AITemplateId(self, AITemplateId):  # String
		self.add_query_param('AITemplateId', AITemplateId)
	def get_OwnerId(self): # String
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # String
		self.add_query_param('OwnerId', OwnerId)
