import os
rootdir = "../wikifiles"
with open("_Sidebar.md", "w") as file:
    file.write("# **Projects**"+"\n\n")
    for subdir, dirs, files in os.walk(rootdir):    
        if subdir[13:]!='':
            file.write("* ## **"+ subdir[13:] +"**" + "\n")
        for file_name in files:
            file.write("\t"+"* ["+ file_name[:-3] + "](" + file_name[:-3].replace(" ", "%20") + ")" + "\n")
    file.close()
