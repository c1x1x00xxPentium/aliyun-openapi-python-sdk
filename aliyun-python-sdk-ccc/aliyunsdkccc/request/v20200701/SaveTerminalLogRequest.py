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
from aliyunsdkccc.endpoint import endpoint_data

class SaveTerminalLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CCC', '2020-07-01', 'SaveTerminalLog','CCC')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_CallId(self): # String
		return self.get_query_params().get('CallId')

	def set_CallId(self, CallId):  # String
		self.add_query_param('CallId', CallId)
	def get_Content(self): # String
		return self.get_query_params().get('Content')

	def set_Content(self, Content):  # String
		self.add_query_param('Content', Content)
	def get_UniqueRequestId(self): # String
		return self.get_query_params().get('UniqueRequestId')

	def set_UniqueRequestId(self, UniqueRequestId):  # String
		self.add_query_param('UniqueRequestId', UniqueRequestId)
	def get_JobId(self): # String
		return self.get_query_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_query_param('JobId', JobId)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_AppName(self): # String
		return self.get_query_params().get('AppName')

	def set_AppName(self, AppName):  # String
		self.add_query_param('AppName', AppName)
	def get_DataType(self): # Integer
		return self.get_query_params().get('DataType')

	def set_DataType(self, DataType):  # Integer
		self.add_query_param('DataType', DataType)
	def get_Status(self): # String
		return self.get_query_params().get('Status')

	def set_Status(self, Status):  # String
		self.add_query_param('Status', Status)
	def get_MethodName(self): # String
		return self.get_query_params().get('MethodName')

	def set_MethodName(self, MethodName):  # String
		self.add_query_param('MethodName', MethodName)
