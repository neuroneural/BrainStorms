## Proposal Abstract
Appropriate blood supply is essential to the healthy maintenance of brain tissue. Vascular changes observed in the brain vessels resulting in impaired brain function are associated with many diseases and with progression across the lifespan. Consequential changes to neural tissue can be observed using magnetic resonance imaging (MRI).  Traditional methods used to quantify vascular brain dysfunction have relied upon manual annotations which are   time-consuming and suffer from inter- and intra-rater variability. Challenges in the detection and quantification of these markers are secondary  to their small sizes, irregular shapes, homologous presentation between markers, and similarly appearance to brain structures. To date there is no accepted “gold standard” method to detect and quantify MRI abnormalities. As such, the field lacks consensus for methods to uncover the "real" ground truth.

In this project, we want to utilize Deep Learning methods for Object Detection and Semantic Segmentation to automate the detection of vascular markers of neurodegenerative disease (Periventricular Spaces, Microbleeds, Lacunes, White matter hyperintensities). The Ground Truth labels for these data sets are limited and noisy, and the model’s initial guesses will be reviewed by experts, and refined for further fine-tuning. 

The project has six proposed phases, with the first three phases completed prior to expert review. The remaining phases may be completed by another collaborator.
1) implementing a model (based on MeshNet) on a large corpus of data with robust labels as a baseline (likely Gray/White matter segmentation, or Atlas Segmentation). 
2) Fine-tuning the baseline model to the given task of vascular marker detection with imperfect labels
3) Refining model output using standard ML techniques such as grid-search, data-augmentation, etc

– Expert Review and Manual Refinement of Predicted Labels –

4) Additional fine-tuning of model on Refined data
5) Training of new model from scratch on refined data for comparison
6) Paper publication and Additional final refinement and model deployment on BrainForge or other web service
## About the Project
### Umbrella Project
* BrainVis/BrainForge
### Emphasis:
* Neuroimaging/Deep Learning
### Expected Background
* Graduate-level project. Familiarity with Python, Linear Algebra, Calculus and Intro statistics required. Basic familiarity with Deep Learning is also recommended. Familiarity with PyTorch or an equivalent deep learning library would be useful. Background in Computer Vision would help immensely.
### Primary Point of Contact
* Brad Baker (bbaker43@gsu.edu)
### Supervisor
* H. Jeremy Bockholt, Vince Calhoun
## References and External Resources
* (2023 January 2). CADASIL Study, https://cadasil-consortium.org/cadasil-study/
* https://pytorch.org/
* Fedorov, Alex, et al. "End-to-end learning of brain tissue segmentation from imperfect labeling." 2017 International Joint Conference on Neural Networks (IJCNN). IEEE, 2017.
* I. Di Donato, S. Bianchi, N. De Stefano, Dicghans, M.T.Dotti, M. Duering, et al. Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy
* (CADASIL) as a model of small vessel disease: update on clinical, diagnostic, and management aspects. BMC Med., 15 (1) (2017), p. 41
* S.M. Smith, M. Jenkinson, M.W. Woolrich, C.F. Beckmann, T.E.J. Behrens, H. Johansen-Berg, P.R. Bannister, M. De Luca, I. Drobnjak, D.E. Flitney, R. Niazy, J. Saunders, J. Vickers, Y. Zhang, N. De Stefano, J.M. Brady, and P.M. Matthews. Advances in functional and structural MR image analysis and implementation as FSL. NeuroImage, 23(S1):208-19, 2004
* O. Puonti, J.E. Iglesias, K. Van Leemput. Fast and sequence-adaptive whole-brain segmentation using parametric Bayesian modeling.NeuroImage, 143, 235-249, 2016.
* Nathan C. Wetter, Elizabeth A. Hubbard, Robert W. Motl, Bradley P. Sutton. Fully automated open-source lesion mapping of T2-FLAIR images with FSL correlates with clinical disability in MS. 28 January 2016 https://doi.org/10.1002/brb3.440
* Mann, Henry B.; Whitney, Donald R. (1947). "On a Test of Whether one of Two Random Variables is Stochastically Larger than the Other". Annals of Mathematical Statistics. 18 (1): 50-60. doi:10.1214/aoms/1177730491. MR 0022058. Zbl 0041.26103
* (2023 January 2). The R Project for Statistical Computing. https://www.r-project.org/ 
* Duchesnay E, Hadj Selem F, De Guio F, Dubois M, Mangin JF, Duering M, Ropele S, Schmidt R, Dichgans M, Chabriat H, Jouvent E. Different Types of White Matter Hyperintensities in CADASIL. Front Neurol. 2018 Jul 10;9:526. doi: 10.3389/fneur.2018.00526. PMID: 30042721; PMCID: PMC6048276
* L. Griffanti, G. Zamboni, A. Khan, L. Li, G. Bonifacio, V. Sundaresan, U. G. Schulz, W. Kuker, M. Battaglini, P. M. Rothwell, M. Jenkinson (2016) BIANCA (Brain Intensity AbNormality Classification Algorithm): a new tool for automated segmentation of white matter hyperintensities. Neuroimage. 141:191-205

## Estimated Timelines
* Phases 1-3 can be done in 2-3 months (i.e. a summer or semester project). 
* Expert review timeline may vary.
* Phases 4-6 can be done in 2-3 months minimum (longer for paper publication)

## Possible Deliverables
* Proof of concept model fine-tuned on Vascular data
* Possible conference and journal paper
