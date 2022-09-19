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

class UpdateAppInstanceGroupImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'appstream-center', '2021-09-01', 'UpdateAppInstanceGroupImage')
		self.set_method('POST')

	def get_BizRegionId(self): # String
		return self.get_query_params().get('BizRegionId')

	def set_BizRegionId(self, BizRegionId):  # String
		self.add_query_param('BizRegionId', BizRegionId)
	def get_ProductType(self): # String
		return self.get_query_params().get('ProductType')

	def set_ProductType(self, ProductType):  # String
		self.add_query_param('ProductType', ProductType)
	def get_AppInstanceGroupId(self): # String
		return self.get_query_params().get('AppInstanceGroupId')

	def set_AppInstanceGroupId(self, AppInstanceGroupId):  # String
		self.add_query_param('AppInstanceGroupId', AppInstanceGroupId)
	def get_AppCenterImageId(self): # String
		return self.get_query_params().get('AppCenterImageId')

	def set_AppCenterImageId(self, AppCenterImageId):  # String
		self.add_query_param('AppCenterImageId', AppCenterImageId)