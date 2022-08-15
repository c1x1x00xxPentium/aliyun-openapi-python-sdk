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
from aliyunsdkhitsdb.endpoint import endpoint_data

class CreateLindormInstanceRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'hitsdb', '2020-06-15', 'CreateLindormInstance','hitsdb')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_TsdbSpec(self): # String
		return self.get_query_params().get('TsdbSpec')

	def set_TsdbSpec(self, TsdbSpec):  # String
		self.add_query_param('TsdbSpec', TsdbSpec)
	def get_FilestoreSpec(self): # String
		return self.get_query_params().get('FilestoreSpec')

	def set_FilestoreSpec(self, FilestoreSpec):  # String
		self.add_query_param('FilestoreSpec', FilestoreSpec)
	def get_Duration(self): # String
		return self.get_query_params().get('Duration')

	def set_Duration(self, Duration):  # String
		self.add_query_param('Duration', Duration)
	def get_ResourceGroupId(self): # String
		return self.get_query_params().get('ResourceGroupId')

	def set_ResourceGroupId(self, ResourceGroupId):  # String
		self.add_query_param('ResourceGroupId', ResourceGroupId)
	def get_SecurityToken(self): # String
		return self.get_query_params().get('SecurityToken')

	def set_SecurityToken(self, SecurityToken):  # String
		self.add_query_param('SecurityToken', SecurityToken)
	def get_TsdbNum(self): # Integer
		return self.get_query_params().get('TsdbNum')

	def set_TsdbNum(self, TsdbNum):  # Integer
		self.add_query_param('TsdbNum', TsdbNum)
	def get_DiskCategory(self): # String
		return self.get_query_params().get('DiskCategory')

	def set_DiskCategory(self, DiskCategory):  # String
		self.add_query_param('DiskCategory', DiskCategory)
	def get_LindormSpec(self): # String
		return self.get_query_params().get('LindormSpec')

	def set_LindormSpec(self, LindormSpec):  # String
		self.add_query_param('LindormSpec', LindormSpec)
	def get_SolrNum(self): # Integer
		return self.get_query_params().get('SolrNum')

	def set_SolrNum(self, SolrNum):  # Integer
		self.add_query_param('SolrNum', SolrNum)
	def get_ColdStorage(self): # Integer
		return self.get_query_params().get('ColdStorage')

	def set_ColdStorage(self, ColdStorage):  # Integer
		self.add_query_param('ColdStorage', ColdStorage)
	def get_InstanceStorage(self): # String
		return self.get_query_params().get('InstanceStorage')

	def set_InstanceStorage(self, InstanceStorage):  # String
		self.add_query_param('InstanceStorage', InstanceStorage)
	def get_SolrSpec(self): # String
		return self.get_query_params().get('SolrSpec')

	def set_SolrSpec(self, SolrSpec):  # String
		self.add_query_param('SolrSpec', SolrSpec)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_InstanceAlias(self): # String
		return self.get_query_params().get('InstanceAlias')

	def set_InstanceAlias(self, InstanceAlias):  # String
		self.add_query_param('InstanceAlias', InstanceAlias)
	def get_FilestoreNum(self): # Integer
		return self.get_query_params().get('FilestoreNum')

	def set_FilestoreNum(self, FilestoreNum):  # Integer
		self.add_query_param('FilestoreNum', FilestoreNum)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_LindormNum(self): # Integer
		return self.get_query_params().get('LindormNum')

	def set_LindormNum(self, LindormNum):  # Integer
		self.add_query_param('LindormNum', LindormNum)
	def get_CoreSpec(self): # String
		return self.get_query_params().get('CoreSpec')

	def set_CoreSpec(self, CoreSpec):  # String
		self.add_query_param('CoreSpec', CoreSpec)
	def get_VSwitchId(self): # String
		return self.get_query_params().get('VSwitchId')

	def set_VSwitchId(self, VSwitchId):  # String
		self.add_query_param('VSwitchId', VSwitchId)
	def get_VPCId(self): # String
		return self.get_query_params().get('VPCId')

	def set_VPCId(self, VPCId):  # String
		self.add_query_param('VPCId', VPCId)
	def get_ZoneId(self): # String
		return self.get_query_params().get('ZoneId')

	def set_ZoneId(self, ZoneId):  # String
		self.add_query_param('ZoneId', ZoneId)
	def get_PayType(self): # String
		return self.get_query_params().get('PayType')

	def set_PayType(self, PayType):  # String
		self.add_query_param('PayType', PayType)
	def get_PricingCycle(self): # String
		return self.get_query_params().get('PricingCycle')

	def set_PricingCycle(self, PricingCycle):  # String
		self.add_query_param('PricingCycle', PricingCycle)
