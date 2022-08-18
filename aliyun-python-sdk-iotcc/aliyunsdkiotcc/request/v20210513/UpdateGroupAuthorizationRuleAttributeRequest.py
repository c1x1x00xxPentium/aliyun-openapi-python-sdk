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

class UpdateGroupAuthorizationRuleAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'IoTCC', '2021-05-13', 'UpdateGroupAuthorizationRuleAttribute','IoTCC')
		self.set_method('POST')

	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_DestinationType(self): # String
		return self.get_query_params().get('DestinationType')

	def set_DestinationType(self, DestinationType):  # String
		self.add_query_param('DestinationType', DestinationType)
	def get_Destination(self): # String
		return self.get_query_params().get('Destination')

	def set_Destination(self, Destination):  # String
		self.add_query_param('Destination', Destination)
	def get_Protocol(self): # String
		return self.get_query_params().get('Protocol')

	def set_Protocol(self, Protocol):  # String
		self.add_query_param('Protocol', Protocol)
	def get_AuthorizationRuleDescription(self): # String
		return self.get_query_params().get('AuthorizationRuleDescription')

	def set_AuthorizationRuleDescription(self, AuthorizationRuleDescription):  # String
		self.add_query_param('AuthorizationRuleDescription', AuthorizationRuleDescription)
	def get_Policy(self): # String
		return self.get_query_params().get('Policy')

	def set_Policy(self, Policy):  # String
		self.add_query_param('Policy', Policy)
	def get_IoTCloudConnectorGroupId(self): # String
		return self.get_query_params().get('IoTCloudConnectorGroupId')

	def set_IoTCloudConnectorGroupId(self, IoTCloudConnectorGroupId):  # String
		self.add_query_param('IoTCloudConnectorGroupId', IoTCloudConnectorGroupId)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_SourceCidrss(self): # RepeatList
		return self.get_query_params().get('SourceCidrs')

	def set_SourceCidrss(self, SourceCidrs):  # RepeatList
		for depth1 in range(len(SourceCidrs)):
			self.add_query_param('SourceCidrs.' + str(depth1 + 1), SourceCidrs[depth1])
	def get_AuthorizationRuleName(self): # String
		return self.get_query_params().get('AuthorizationRuleName')

	def set_AuthorizationRuleName(self, AuthorizationRuleName):  # String
		self.add_query_param('AuthorizationRuleName', AuthorizationRuleName)
	def get_AuthorizationRuleId(self): # String
		return self.get_query_params().get('AuthorizationRuleId')

	def set_AuthorizationRuleId(self, AuthorizationRuleId):  # String
		self.add_query_param('AuthorizationRuleId', AuthorizationRuleId)
	def get_DestinationPort(self): # String
		return self.get_query_params().get('DestinationPort')

	def set_DestinationPort(self, DestinationPort):  # String
		self.add_query_param('DestinationPort', DestinationPort)
