import os

FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
os.makedirs(TEMPLATE_DIR, exist_ok=True)

class Template:

	template_name = ""
	context = {}

	def __init__(self, template_name="", context={}, *args, **kwargs):
		self.template_name =template_name
		self.context = context

	def get_template(self):
		template_path = os.path.join(TEMPLATE_DIR, self.template_name)
		if not os.path.exists(template_path):
			raise Exception("Tis path does not exists")
		template_string=""
		with open(template_path, 'r') as f:
			template_string = f.read()
		return template_string

	def render(self, context=None):
		render_ctx = context
		if self.context != None:
			render_ctx = self.context
		if not isinstance(render_ctx, dict): #si render_ctx no es un dict
			render_ctx = {}
		template_string = self.get_template()
		return template_string.format(**render_ctx)

Template()
obj = Template(template_name="hello.txt", context={"name":"jorgito"})
#print(obj)
#print(obj.template_name)
#print(obj.context)
print(obj.get_template())
print(obj.render())