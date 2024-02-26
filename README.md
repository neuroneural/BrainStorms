# BrainStorms
Welcome to the BrainStorms repository wiki! Here you can find information about our live projects and ongoing developments.

## About BrainStorms
BrainStorms is a collaborative platform where innovative ideas are brought to life through teamwork and creativity. Our projects span various domains and are driven by a passion for problem-solving and technological advancement.

## How to add a new project to BrainStorms?
**Step 1:** Clone the GitHub repository using
```bash
git clone https://github.com/neuroneural/BrainStorms.git
```
**Step 2:** Run the `run.py` file inside the BrainStorms folder.
```bash
cd BrainStorms
python run.py
```
**Step 3:** Complete all required fields as prompted by the program. You can see a new `.md` file is created in `./wikifiles` folder. Push the changes to BrainStorms repo using
```bash
git add ./wikifiles/<project-category>/<project-name>
git commit -m "add new project"
git push origin main
```
**Step 4:** As soon as you push the changes to the main branch a CI/CD workflow is launched and a Wiki page is created. 

## How to delete/Modify a project in BrainStorms?
**Step 1:** Clone the GitHub repository using
```bash
git clone https://github.com/neuroneural/BrainStorms.git
```
**Step 2:** Modify/Delete the `.md` file of the project in `wikifiles` folder. Then push the changes to BrainStorms repo using
```bash
git add <list the files changed>
git commit -m "Modify/Delete a project"
git push origin main
```
**Step 3:** As soon as you push the changes to the main branch a CI/CD workflow is launched and a Wiki page is updated. 
