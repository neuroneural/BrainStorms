import os
import shutil

folder_name = input("\nEnter Your Project Category: ")
path = os.path.join("./", folder_name)
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(folder_name)

path = "../wikifiles/"
if not os.path.exists(path):
    os.mkdir(path)

path = os.path.join("../wikifiles/", folder_name)
if not os.path.exists(path):
    os.mkdir(path)

project_name = input("\n\nEnter Your Project Name: ")
path = os.path.join("./", project_name)
os.mkdir(path)
os.chdir(project_name)
with open("project_name.txt", "w") as file:
    file.write(project_name)

open("abstract.txt", "x")
print("\n\nFill out the Abstract of the Project in the abstract.txt(Follow .md Syntax) that is created in the project folder:")
while 1:
    input("Press Enter if your done:")
    if os.path.getsize('abstract.txt') == 0:
        print("\nText file has not been filled yet")
    else:
        break

with open("info.txt", "w") as file:
    umbrella_project = input("\n\nEnter the Umbrella Project Name: ")
    file.write("###"+" Umbrella Project\n")
    file.write("* "+umbrella_project+"\n")

    emphasis = input("\nEnter the Emphasis of the Project: ")
    file.write("###"+" Emphasis:\n")
    file.write("* "+emphasis+"\n")

    background = input("\nEnter Expected Background: ")
    file.write("###"+" Expected Background\n")
    file.write("* "+background+"\n")

    poc = input("\nEnter the Primary Point of Contact of this Project[name(emailID)]: ")
    file.write("###"+" Primary Point of Contact\n")
    file.write("* "+poc+"\n")

    supervisor = input("\nEnter the Supervisor of this Project[name(emailID)]: ")
    file.write("###"+" Supervisor\n")
    file.write("* "+supervisor)

open("references.txt", "x")
print("\n\nFill out the References of the Project in the references.txt that is created in the project folder(Add \"* \" before each citation(.md syntax)):")
while 1:
    input("Press Enter if your done:")
    if os.path.getsize('references.txt') == 0:
        print("\nText file has not been filled yet")
    else:
        break

open("est_timeline.txt", "x")
print("\n\nEnter Estimated Timeline for this Project in the est_timeline.txt that is created in the project folder(Add \"* \" before each line(.md syntax)):")
while 1:
    input("Press Enter if your done:")
    if os.path.getsize('est_timeline.txt') == 0:
        print("\nText file has not been filled yet")
    else:
        break

open("deliverables.txt", "x")
print("\n\nFill out the Possible Deliverables of the Project in the deliverables.txt that is created in the project folder(Add \"* \" before each line(.md syntax)):")
while 1:
    input("Press Enter if your done:")
    if os.path.getsize('deliverables.txt') == 0:
        print("\nText file has not been filled yet")
    else:
        break

with open(project_name+".md", "w") as file:
    file.write("## "+"Proposal Abstract\n")
    f = open("abstract.txt", "r")
    abstract = f.read()
    file.write(abstract)
    f.close()

    file.write("\n## "+"About the Project\n")
    f = open("info.txt", "r")
    info = f.read()
    file.write(info)
    f.close()

    file.write("\n## "+"References and External Resources\n")
    f = open("references.txt", "r")
    references = f.read()
    file.write(references)
    f.close()

    file.write("\n## "+"Estimated Timelines\n")
    f = open("est_timeline.txt", "r")
    est_timeline = f.read()
    file.write(est_timeline)
    f.close()

    file.write("\n## "+"Possible Deliverables\n")
    f = open("deliverables.txt", "r")
    deliverables = f.read()
    file.write(deliverables)
    f.close()

os.replace("./" + project_name + ".md", "../../wikifiles/" + folder_name + "/"+ project_name + ".md")
shutil.rmtree("../../" + folder_name)