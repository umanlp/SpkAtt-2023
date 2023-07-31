# SpkAtt-2023

This repository contains the data and supplementary materials for Task 1 of the 

## 2023 Shared Task on Speaker Attribution (SpkAtt-2023),

co-located with [KONVENS 2023](https://www.thi.de/konvens-2023/).


## Important dates:

 * <strike>February, 2023 - Trial data release</strike>
 * <strike>April 1, 2023 - Training and development data release</strike>
 * <strike>June 15, 2023 - Test data release (blind)</strike>
 * <strike>July 1, 2023 - Submissions open</strike>
 * July 31, 2023 - Submissions for Task1, subtask1 (full task) close
 * August 3, 2023 - Submissions for Task1, subtask 2 (roles only) close
 * August 14, 2023 - System descriptions due
 * September 7, 2023 - Camera-ready system paper deadline
 * September 18-22, 2023 - Workshop at KONVENS 2023


## Task 1 data format:

<p>The data is available in json format where each document (speech) is a json file.</p>

<p>The unit of analysis is a <strike>paragraph</strike> <b>sentence</b> (we changed the format from paragraphs to sentences).</p>

<p>The json dictionary includes a list of Sentences and a list of Annotations. 
Each item in the Sentences list is a dictionary with SentenceID and a list of Tokens for this sentence.
Each item in the Annotations list is a dictionary that includes the ids (sentence:token id) for the cue word(s) that trigger a speech event and the ids for the roles that are realised for this cue.
</p>



<!--![alt text](img/dataformat_task1.pdf "Data format task 1")-->
For a more detailed description of the data format (Task 1) and some examples, see this <a href="./doc/Dataformat_Task1_a.pdf">pdf</a>. 
For more information on our annotation scheme, please refer to the <a href="./doc/Guidelines_SpeakerAttribution_in_Parliamentary_Debates-SpkAtt-2023_Task1.pdf">annotation guidelines</a>. Please note that the guidelines have not yet been finalised and might include some inconsistencies and errors that we try to fix in the next couple of weeks.

We tried to harmonise the data format for Task1 and Task2 as much as possible, which resulted in a file format where the annotations are separated from the text. This makes it a bit harder to inspect the data. We therefore also provide an alternative data format, mostly to make the data more human-readible. This alternative format is described <a href="./doc/Dataformat_Task1_b.pdf">here</a>.
However, the official shared task format is the one described in the first document (Dataformat_Task1_a.pdf) and we do not provide evaluation scripts for the second format.









