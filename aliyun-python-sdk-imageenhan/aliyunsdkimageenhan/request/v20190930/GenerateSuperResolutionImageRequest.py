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
from aliyunsdkimageenhan.endpoint import endpoint_data

class GenerateSuperResolutionImageRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageenhan', '2019-09-30', 'GenerateSuperResolutionImage','imageenhan')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Scale(self): # Integer
		return self.get_body_params().get('Scale')

	def set_Scale(self, Scale):  # Integer
		self.add_body_params('Scale', Scale)
	def get_UserData(self): # String
		return self.get_body_params().get('UserData')

	def set_UserData(self, UserData):  # String
		self.add_body_params('UserData', UserData)
	def get_OutputFormat(self): # String
		return self.get_body_params().get('OutputFormat')

	def set_OutputFormat(self, OutputFormat):  # String
		self.add_body_params('OutputFormat', OutputFormat)
	def get_ImageUrl(self): # String
		return self.get_body_params().get('ImageUrl')

	def set_ImageUrl(self, ImageUrl):  # String
		self.add_body_params('ImageUrl', ImageUrl)
	def get_OutputQuality(self): # Integer
		return self.get_body_params().get('OutputQuality')

	def set_OutputQuality(self, OutputQuality):  # Integer
		self.add_body_params('OutputQuality', OutputQuality)