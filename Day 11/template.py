
class Template:

	template_name = ""
	context = {}

	def __init__(self, template_name="", context={}, *args, **kwargs):
		self.template_name =template_name
		self.context = context

Template()
obj = Template(template_name="hello.txt", context={"name":"jorgito"})
print(obj)
print(obj.template_name)
print(obj.context)