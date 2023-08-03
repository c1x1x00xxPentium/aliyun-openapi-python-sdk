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
import json

class ExecuteStatementRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'rds-data', '2022-03-30', 'ExecuteStatement')
		self.set_method('POST')

	def get_IncludeResultMetadata(self): # Boolean
		return self.get_body_params().get('IncludeResultMetadata')

	def set_IncludeResultMetadata(self, IncludeResultMetadata):  # Boolean
		self.add_body_params('IncludeResultMetadata', IncludeResultMetadata)
	def get_FormatRecordsAs(self): # String
		return self.get_body_params().get('FormatRecordsAs')

	def set_FormatRecordsAs(self, FormatRecordsAs):  # String
		self.add_body_params('FormatRecordsAs', FormatRecordsAs)
	def get_TransactionId(self): # String
		return self.get_body_params().get('TransactionId')

	def set_TransactionId(self, TransactionId):  # String
		self.add_body_params('TransactionId', TransactionId)
	def get_Sql(self): # String
		return self.get_body_params().get('Sql')

	def set_Sql(self, Sql):  # String
		self.add_body_params('Sql', Sql)
	def get_ResultSetOptions(self): # Struct
		return self.get_body_params().get('ResultSetOptions')

	def set_ResultSetOptions(self, ResultSetOptions):  # Struct
		self.add_body_params("ResultSetOptions", json.dumps(ResultSetOptions))
	def get_Database(self): # String
		return self.get_body_params().get('Database')

	def set_Database(self, Database):  # String
		self.add_body_params('Database', Database)
	def get_ResourceArn(self): # String
		return self.get_body_params().get('ResourceArn')

	def set_ResourceArn(self, ResourceArn):  # String
		self.add_body_params('ResourceArn', ResourceArn)
	def get_Parameters(self): # Array
		return self.get_body_params().get('Parameters')

	def set_Parameters(self, Parameters):  # Array
		self.add_body_params("Parameters", json.dumps(Parameters))
	def get_ContinueAfterTimeout(self): # Boolean
		return self.get_body_params().get('ContinueAfterTimeout')

	def set_ContinueAfterTimeout(self, ContinueAfterTimeout):  # Boolean
		self.add_body_params('ContinueAfterTimeout', ContinueAfterTimeout)
	def get_SecretArn(self): # String
		return self.get_body_params().get('SecretArn')

	def set_SecretArn(self, SecretArn):  # String
		self.add_body_params('SecretArn', SecretArn)
