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
from aliyunsdkvs.endpoint import endpoint_data

class BatchForbidVsStreamRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'vs', '2018-12-12', 'BatchForbidVsStream')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Channel(self):
		return self.get_query_params().get('Channel')

	def set_Channel(self,Channel):
		self.add_query_param('Channel',Channel)

	def get_ControlStreamAction(self):
		return self.get_query_params().get('ControlStreamAction')

	def set_ControlStreamAction(self,ControlStreamAction):
		self.add_query_param('ControlStreamAction',ControlStreamAction)

	def get_ResumeTime(self):
		return self.get_query_params().get('ResumeTime')

	def set_ResumeTime(self,ResumeTime):
		self.add_query_param('ResumeTime',ResumeTime)

	def get_LiveStreamType(self):
		return self.get_query_params().get('LiveStreamType')

	def set_LiveStreamType(self,LiveStreamType):
		self.add_query_param('LiveStreamType',LiveStreamType)

	def get_DomainName(self):
		return self.get_query_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_query_param('DomainName',DomainName)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)

	def get_Oneshot(self):
		return self.get_query_params().get('Oneshot')

	def set_Oneshot(self,Oneshot):
		self.add_query_param('Oneshot',Oneshot)