import httplib

class BaseCamp:
	"""A simple example classe """
	
	host = ''
	connection = None

	user = ''
	password = ''
	token = ''
	is_auth = False

	headers = {'Accept': 'application/xml',
		   	'Content-Type': 'application/xml'}


	def set_authentication(self, token='', user='', password=''):
		self.token = token
		self.user = user
		self.password = password

		if token == '':
			self.headers['Authorization'] = 'Basic ' + user + ': ' + password # This is most likely not correct
		else:
			self.headers['Authorization'] = 'Basic ' + self.token #MGU3YWQ3NTYzNTJiZWQ3MDlhMGI4MDMzYTFkMDhiZmExNjc3YTc2YTpY'

	def set_host(self, host):
		self.host = host


	def get_account_info(self):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/account.xml', headers=self.headers)
		response = self.connection.getresponse()
		account_info = response.read()
		return response.status, account_info

	def get_files_for_project(self, project):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/projects/' + project + '/attachments.xml?n=1', headers=self.headers)

		response = self.connection.getresponse()
		files = response.read()
		return response.status, files


	def get_projects(self):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/projects.xml', headers=self.headers)

		response = self.connection.getresponse()
		projects = response.read()
		return response.status, projects

	def get_project(self, project_id):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/projects/' + project_id + '.xml', headers=self.headers)

		response = self.connection.getresponse()
		project = response.read()
		return response.status, project



	def get_me(self):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/me.xml', headers=self.headers)

		response = self.connection.getresponse()
		me = response.read()
		return response.status, me

	def get_people(self):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/people.xml', headers=self.headers)

		response = self.connection.getresponse()
		people = response.read()
		return response.status, people

	def get_people_for_project(self, project):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/projects/' + project + '/people.xml', headers=self.headers)

		response = self.connection.getresponse()
		people = response.read()
		return response.status, people

	def get_people_for_company(self, company):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/companies/' + company + '/people.xml', headers=self.headers)

		response = self.connection.getresponse()
		people = response.read()
		return response.status, people



