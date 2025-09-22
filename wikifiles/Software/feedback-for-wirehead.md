# Feedback for Wirehead

*Category:* Software

*Created:* 2025-09-21

## Abstract

Currently [wirehead](https://github.com/neuroneural/wirehead) deliberately operates in a way that the trainer [mindfultensors](https://github.com/neuroneural/mindfultensors) scripts know nothing about its existence. The training proceeds as if it is training on a dataset and is just looping through it one epoch at a time. This transparency of wirehead is usually idea, but sometimes, as in the case of curriculum training using synthSeg it may be of benefit for the training process to signal to [wirehead](https://github.com/neuroneural/wirehead) how the model is doing on its metrics. The goal is to be able to adjust parameters of synthetic generation to enable smooth curriculum training for the model from easy examples (say, less degrees of variability and smaller variance) to much harder examples when the model is capable handling them.
The goal is to develop a simple, flexible UI in mindfultensors and wirehead to be able to signal the model state via a document in the auxiliary (currently only used by wirehead). The UX should be comfortable for writing the model training script, that could easily report current loss, or DICE, or whatever metric the user training their model decides to report. However, it should also make it simple for the wirehead generator to access what the training script reports.
## Objectives

1. Write a design proposal for the structure that will power information exchange from mindfultensors to wirehead.
2. Design and clearly specify which functions or construct the training loop will use to store the current value of the model state (loss, DICE, accuracy, or whatever). Do teh same for the wirehead generator developer.
3. Get the design approaved with Mike Doan and Sergey Plis.
4. Implement the design (which includes thorough testing and demonstration of maximal efficacy of the solution)
5. Make sure that the solution is minimum possible to get the job done, which includes minimum possible number of code lines, additional functions, additional computation or storage requirements on the wirehead and mindfultensors side.
## Methodology

A suggested solution is to add extra keys to the `counter` collection in the wirehead database and add functions to mindfultensors to write to that collection if it exists. A single function would be enough if it only requires minimum parameters. For the wirehead, design a function that reads the `counter` collection and provides the generator with needed information.
## Estimated Timelines

A proficient programmer should be able to complete the above tasks in no more than 24 working hours (2-3 days). However, a student should be able to provide and defend their design in no more than a week and produce a bug free efficient implementation by the end of another week.
## Possible Deliverables

1. Design documentation
2. PR with implementation to wirehead
3. PR to mindfultensors
4. PR with documentation additions to wirehead and mindfultensors respectively
