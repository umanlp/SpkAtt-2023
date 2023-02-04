# SpkAtt-2023

This repository contains the data and supplementary materials for the 

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


## Data format:

The data is available in json format (see figure below) where
each document (speech) is a json file.

The unit of analysis is a paragraph. Sometimes, the splits are
not correct and some sentences have been split up so that the 
first part of the sentence is included in one paragraph and the 
second part in another.

The json dictionary keys are the paragraph ids.
For each paragraph, we include the following lists:

  * Tokens: the tokens for this paragraph
  * Annotations: a list of dictionaries, where each item in the list is a dictionary with cue words and roles for this cue.

In the example below, we only have one cue (and therefore only one dictionary in the Annotations list).
The cue has the paragraph id "18" and the token id "3". To retrieve the word form for this cue, you can extract the token with id 3 (i.e., the fourth token in the list) from paragraph 18, which is "lehnen". This is a particle verb and the verb prefix is encoded as 'PTK' (paragraph 18, token id 8 => "ab").
In addition to the cue word(s) and its particle, the Annotations include the roles for this cue (i.e., Source, Message, Addresse, Topic, Medium and Evidence. For more information, see the annotation guidelines (folder: guidelines).

![alt text](img/json-format-task1.png "Data format task 1")

