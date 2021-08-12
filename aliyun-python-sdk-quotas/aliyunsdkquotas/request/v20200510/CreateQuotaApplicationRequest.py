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
from aliyunsdkquotas.endpoint import endpoint_data

class CreateQuotaApplicationRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quotas', '2020-05-10', 'CreateQuotaApplication','quotas')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Reason(self):
		return self.get_body_params().get('Reason')

	def set_Reason(self,Reason):
		self.add_body_params('Reason', Reason)

	def get_ProductCode(self):
		return self.get_body_params().get('ProductCode')

	def set_ProductCode(self,ProductCode):
		self.add_body_params('ProductCode', ProductCode)

	def get_QuotaActionCode(self):
		return self.get_body_params().get('QuotaActionCode')

	def set_QuotaActionCode(self,QuotaActionCode):
		self.add_body_params('QuotaActionCode', QuotaActionCode)

	def get_DesireValue(self):
		return self.get_body_params().get('DesireValue')

	def set_DesireValue(self,DesireValue):
		self.add_body_params('DesireValue', DesireValue)

	def get_QuotaCategory(self):
		return self.get_body_params().get('QuotaCategory')

	def set_QuotaCategory(self,QuotaCategory):
		self.add_body_params('QuotaCategory', QuotaCategory)

	def get_NoticeType(self):
		return self.get_body_params().get('NoticeType')

	def set_NoticeType(self,NoticeType):
		self.add_body_params('NoticeType', NoticeType)

	def get_AuditMode(self):
		return self.get_body_params().get('AuditMode')

	def set_AuditMode(self,AuditMode):
		self.add_body_params('AuditMode', AuditMode)

	def get_Dimensionss(self):
		return self.get_body_params().get('Dimensions')

	def set_Dimensionss(self, Dimensionss):
		for depth1 in range(len(Dimensionss)):
			if Dimensionss[depth1].get('Key') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Key', Dimensionss[depth1].get('Key'))
			if Dimensionss[depth1].get('Value') is not None:
				self.add_body_params('Dimensions.' + str(depth1 + 1) + '.Value', Dimensionss[depth1].get('Value'))