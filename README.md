# SpkAtt-2023

This repository contains the data and supplementary materials for Task 1 of the 

## 2023 Shared Task on Speaker Attribution (SpkAtt-2023),

co-located with [KONVENS 2023](https://www.thi.de/konvens-2023/).


## Important dates:

 * February, 2023 - Trial data release
 * April 1, 2023 - Training and development data release
 * June 15, 2023 - Test data release (blind)
 * July 1, 2023 - Submissions open
 * July 31, 2023 - Submissions close
 * August 14, 2023 - System descriptions due
 * September 7, 2023 - Camera-ready system paper deadline
 * September 18-22, 2023 - Workshop at KONVENS 2023


## Task 1 data format:

<p>The data is available in json format where each document (speech) is a json file.</p>

<p>The unit of analysis is a paragraph. A paragraph can include one or more sentences.</p>

<p>The json dictionary keys are the paragraph ids.
For each paragraph, we include the following lists:</p>

  * Tokens: the tokens for this paragraph
  * Annotations: a list of dictionaries, where each item in the list is a dictionary with cue words <br/> and roles for this cue.


<!--![alt text](img/dataformat_task1.pdf "Data format task 1")-->
For a more detailed description of the data format (Task 1) and some examples, see this <a href="./doc/Dataformat_Task1_a.pdf">pdf</a>.
For more information on our annotation schem, please refer to the <a href="./doc/Guidelines_SpeakerAttribution_in_Parliamentary_Debates-SpkAtt-2023_Task1.pdf">annotation guidelines</a>. Please note that the guidelines have not yet been finalised and might include some inconsistencies and errors that we try to fix in the next couple of weeks.

We tried to harmonise the data format for Task1 and Task2 as much as possible, which resulted in a file format where the annotations are separated from the text. This makes it a bit harder to inspect the data. We therefore also provide an alternative data format, mostly to make the data more human-readible. This alternative format is described <a href="./doc/Dataformat_Task1_b.pdf">here</a>.
However, the official shared task format is the one described in the first document (Dataformat_Task1_a.pdf) and we do not provide evaluation scripts for the second format.









