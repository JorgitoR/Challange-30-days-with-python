import os
import requests
import shutil 

from download_util  import download_file

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
donloads_dirs = os.path.join(BASE_DIR, "downloads")
os.makedirs(donloads_dirs, exist_ok=True)


downloaded_img_path = os.path.join(donloads_dirs, '1.jpg')
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Classic_view_of_a_cloudfree_Peyto_Lake%2C_Banff_National_Park%2C_Alberta%2C_Canada_%284110933448%29.jpg/330px-Classic_view_of_a_cloudfree_Peyto_Lake%2C_Banff_National_Park%2C_Alberta%2C_Canada_%284110933448%29.jpg"


r= requests.get(url, stream=True)
r.raise_for_status() #200
with open(downloaded_img_path, 'wb') as f:
	f.write(r.content)


# dl_filename = os.path.basename(url)
# new_dl_path = os.path.join(DOWNLOADS_DIR, dl_filename)
# with requests.get(url, stream=True) as r:
#     with open(new_dl_path, 'wb') as file_obj:
#         shutil.copyfileobj(r.raw, file_obj)

download_file(url, donloads_dirs)