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

class SelectRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rds-data', '2022-03-30', 'Select')
		self.set_method('POST')

	def get_TransactionId(self): # String
		return self.get_body_params().get('TransactionId')

	def set_TransactionId(self, TransactionId):  # String
		self.add_body_params('TransactionId', TransactionId)
	def get_PageNumber(self): # Long
		return self.get_body_params().get('PageNumber')

	def set_PageNumber(self, PageNumber):  # Long
		self.add_body_params('PageNumber', PageNumber)
	def get_Filter(self): # String
		return self.get_body_params().get('Filter')

	def set_Filter(self, Filter):  # String
		self.add_body_params('Filter', Filter)
	def get_Database(self): # String
		return self.get_body_params().get('Database')

	def set_Database(self, Database):  # String
		self.add_body_params('Database', Database)
	def get_PageSize(self): # Long
		return self.get_body_params().get('PageSize')

	def set_PageSize(self, PageSize):  # Long
		self.add_body_params('PageSize', PageSize)
	def get_ResourceArn(self): # String
		return self.get_body_params().get('ResourceArn')

	def set_ResourceArn(self, ResourceArn):  # String
		self.add_body_params('ResourceArn', ResourceArn)
	def get_Table(self): # String
		return self.get_body_params().get('Table')

	def set_Table(self, Table):  # String
		self.add_body_params('Table', Table)
	def get_SecretArn(self): # String
		return self.get_body_params().get('SecretArn')

	def set_SecretArn(self, SecretArn):  # String
		self.add_body_params('SecretArn', SecretArn)
