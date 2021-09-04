import os

this_file_path =os.path.abspath(__file__)
print(this_file_path)

BASE_DIR = os.path.dirname(this_file_path)
entire_project_dir = os.path.dirname(BASE_DIR)


email_txt = os.path.join(BASE_DIR, "templates", "email.txt")

with open(email_txt, 'r') as f:
	content = f.read()


print(content.format(name='jorgito'))