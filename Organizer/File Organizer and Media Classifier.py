import os
import datetime
import re
import sys

inputs = sys.argv


src = inputs[1]
dst = inputs[2]
folder = os.walk(src)

for data in folder:
    location = data[0]
    files = data [2]
    for file in files:
        modify_time = os.path.getmtime(os.path.join(location,file))
        name = str(datetime.date.fromtimestamp(modify_time).year)
        if re.match("^\w+\.png|^\w+\.jpeg|^\w+\.jpg",file.lower()):
            if os.path.exists(os.path.join(dst,name)) != True:
                os.makedirs(os.path.join(dst,name), exist_ok=True)
                    # os.mkdir(os.path.join(dst,name))
            if os.path.exists(os.path.join(dst,name,"photos")) != True:
                os.makedirs(os.path.join(dst,name,"photos"), exist_ok=True)
                    # os.mkdir(os.path.join(dst,name,"photos"))
            with open(os.path.join(location,file),"rb") as src_file:
                content = src_file.read()
                with open(os.path.join(dst,name,"photos",file),"wb") as dst_file:
                     dst_file.write(content)
    
        if re.match("\w+\.mov|\w+\.wmv|\w+\.mkv|\w+\.mpeg|\w+\.3gp|\w+\.avi|\w+\.mp4",file.lower()):
            if os.path.exists(os.path.join(dst,name)) != True:
                os.makedirs(os.path.join(dst,name), exist_ok=True)
                # os.mkdir(os.path.join(dst,name))
            if os.path.exists(os.path.join(dst,name,"videos")) != True: 
                os.makedirs(os.path.join(dst,name,"videos"), exist_ok=True)     
                # os.mkdir(os.path.join(dst,name,"videos"))
            with open(os.path.join(location,file),"rb") as src_file:
                content = src_file.read()
                with open(os.path.join(dst,name,"videos",file),"wb") as dst_file:
                     dst_file.write(content)
