# SpkAtt-2023 format check script


This python script reads in all files in a directory (specified in line 113: input_dir = "res") 
and checks whether the json format
- includes empty cues
- inclues partially overlapping cues

In lines 115, 116, you can specify whether you want to remove empty cues and overlapping cues:    

	remove_empty = True 
    	remove_overlap = True

If set to True, then the script will remove those from the system output files and write the
updated output to the output directory specified in ine 114: output_dir = "res_format_checked".

ATTENTION: This might not be optimal as we do not check which of the overlapping cues should
be deleted but simply remove the first overlapping cue.


Please adapt the paths to your setting. Then the output files in "res_format_checked" should 
be in a format that can be scored by the evaluation script.









