import httplib
from xml.dom import minidom

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
			self.headers['Authorization'] = 'Basic ' + user + ': ' + password
		else:
			self.headers['Authorization'] = 'Basic ' + self.token

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

	def get_project(self, project):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/projects/' + project + '.xml', headers=self.headers)

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

	def get_person(self, person):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/people/' + person + '.xml', headers=self.headers)

		response = self.connection.getresponse()
		person = response.read()
		return response.status, person


	def get_companies(self):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/companies.xml', headers=self.headers)

		response = self.connection.getresponse()
		companies = response.read()
		return response.status, companies

	def get_companies_for_project(self, project):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/projects/' + project + '/companies.xml', headers=self.headers)

		response = self.connection.getresponse()
		companies = response.read()
		return response.status, companies

	def get_company(self, company):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/companies/' + company + '.xml', headers=self.headers)

		response = self.connection.getresponse()
		company = response.read()
		return response.status, company


	def get_categories_for_project(self, project, type_filter=''):
		self.connection = httplib.HTTPSConnection(self.host)
		if type_filter == 'post' or type_filter == 'attachment':
			path = '/projects/' + project + '/categories.xml?=' + type_filter
		else:
			path = '/projects/' + project + '/categories.xml'
		self.connection.request('GET', path, headers=self.headers)

		response = self.connection.getresponse()
		categories = response.read()
		return response.status, categories

	def get_category(self, category):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/categories/' + category + '.xml', headers=self.headers)

		response = self.connection.getresponse()
		category = response.read()
		return response.status, category

# Should work not tested.
	def create_category_for_project(self, project, category_name, type_filter=''):
		self.connection = httplib.HTTPSConnection(self.host)
		
		xml = minidom.Document()
		category = xml.createElement("category")
		
		if type_filter == 'post' or type_filter == 'attachment':
			type_element = xml.createElement('type')
			type_node = xml.createTextNode(type_filter)
			type_element.appendChild(type_node)
			category.appendChild(type_element)

		name_element = xml.createElement('name')
		name_node = xml.createTextNode(category_name)
		name_element.appendChild(name_node)
		category.appendChild(name_element)
		xml.appendChild(category)

		self.connection.request('POST', '/projects/' + project + '/categories.xml', body=xml.toprettyxml(), headers=self.headers)

		response = self.connection.getresponse()
		category = response.read()
		return response.status, category

# Should work not tested.
	def update_category_for_project(self, project, category, category_name):
		self.connection = httplib.HTTPSConnection(self.host)
		
		xml = minidom.Document()
		category = xml.createElement("category")
		name_element = xml.createElement('name')
		name_node = xml.createTextNode(category_name)
		name_element.appendChild(name_node)
		category.appendChild(name_element)
		xml.appendChild(category)

		self.connection.request('PUT', '/categories/' + category + '.xml', xml.toprettyxml(), headers=self.headers)

		response = self.connection.getresponse()
		category = response.read()
		return response.status, category

# Should work not tested.
	def delete_category(self, category):
		self.connection = httplib.HTTPSConnection(self.host)

		self.connection.request('DELETE', '/categories/' + category + '.xml', headers=self.headers)

		response = self.connection.getresponse()
		category = response.read()
		return response.status, category


	def get_messages_for_project(self, project):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/projects/' + project + '/posts.xml', headers=self.headers)

		response = self.connection.getresponse()
		messages = response.read()
		return response.status, messages

	def get_message(self, message):
		self.connection = httplib.HTTPSConnection(self.host)
		self.connection.request('GET', '/posts/' + message + '.xml', headers=self.headers)

		response = self.connection.getresponse()
		message = response.read()
		return response.status, message

