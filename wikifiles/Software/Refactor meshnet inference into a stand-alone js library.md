## Proposal Abstract
Start with the code https://github.com/neuroneural/brainchop and re-factor the model inference part into a standalone javascript library for MeshNet deep learning architecture learning and inference. There should be a library, say meshnet.js, that is able to take as input models in tfjs format (we will provide pretrained models) , apply these models to 3d T1 images, and produce 3D volumes of brain semantic segmentation labels. Depending on the model used the output could be atlas or tissue segmentation, or simply brain mask generation or brain extraction. The main condition is simplicity and code maintainability. Suggested functions in the library:
* model_segment(T1image, model.arch) - returns 3D volume of the T1image size with labels from 0 to maxnum
* brain_mask(T1image, model.arch) - returns just a binary volume with T1image dimensions
* extract_brain(T1image, model.arch) - as above, but returns the product of the binary mask and T1image

For https://ohbm.github.io/hackathon2022/

## About the Project
### Umbrella Project
* brainchop.org
### Emphasis:
* Front-end tool development in JavaScript
### Expected Background
* Strong ability to develop in  JavaScript. Preferred understanding of tensorflow.js and deep learning
### Primary Point of Contact
* Mohamed Masoud (mmasoud1@gsu.edu)
### Supervisor
* Sergey Plis (splis@gsu.edu)
## References and External Resources
* https://github.com/neuroneural/brainchop
* https://trendscenter.org/in-browser-3d-mri-segmentation-brainchop-org/
* https://github.com/catalyst-team/neuro/blob/13af35b8e5b4ff1bf9f356ec0f0d45a64c495aac/neuro/model.py#L299

## Estimated Timelines
* 1 month (summer project)

## Possible Deliverables
* JS package and APIs 
* Integration with brainchop.org as a stand-alone JS library.  
