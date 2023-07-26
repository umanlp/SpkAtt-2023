import glob
import json
import optparse
import os, sys
import logging


"""
Takes a file name, reads the content of the file
and returns it as a json dictionary.
"""
def read_json(f):
    with open(f, "r") as inf: 
        dic = json.load(inf)
    return dic


"""
Write json dictionary to file.
"""
def write_to_file(dic, path):
    with open(path, "w") as fout:
        json_str = json.dumps(dic, indent=3)
        print(json_str, file=fout)
    return 



"""
Checks for empty cues and prints out the first token of the role
that doesn't have a cue word.
"""
def check_empty_cue(fname, annot, roles):
    missing = {r:[] for r in roles}
    if len(annot["Cue"]) == 0:
        # check for roles 
        for role in roles:
            if len(annot[role]) >0:
                idx = annot[role][0] 
                missing[role].append(idx)
                logging.warning("EMPTY CUE:\t%s\t%s\t%s", role, idx, fname)
    return missing


"""
Checks for cue overlap (whether the same token belongs to more than one cue).
"""
def check_cue_overlap(fname, dic):
    cues, overlap = [], []
    for annot in dic["Annotations"]:
        for cue in annot["Cue"]:
            if cue in cues:
                logging.warning("CUE OVERLAP\t\t\t%s\t%s", cue, fname) 
                overlap.append(cue)
            cues.append(cue)
    return overlap



def remove_annot_with_empty_cues(dic, empty_cues):
    new_annots = []
    for annot in dic["Annotations"]:
        if len(annot["Cue"]) > 0:
            new_annots.append(annot)
    dic["Annotations"] = new_annots
    return dic



def remove_cue_overlap(dic, overlapping_cues):
    new_annots, removed = [], []
    for cue in overlapping_cues: 
        # simply remove the first overlapping cue (not recommended!)
        for annot in dic["Annotations"]:
            if cue in annot["Cue"] and cue not in removed:
                annot = {}
                removed.append(cue)
            
            new_annots.append(annot)
    # remove empty annotation dictionaries
    new_annots = [x for x in new_annots if x != {}]
    if len(new_annots) >0: dic["Annotations"] = new_annots
    return dic




"""
Takes a file name and a json dictionary and checks for empty cues and for cue overlap.
"""
def check_format(fname, dic, remove_empty, remove_overlap):
    roles = ["Addr", "Evidence", "Medium", "Message", "PTC", "Source", "Topic"]

    for annot in dic["Annotations"]:  
        # check for empty cues
        empty_cues = check_empty_cue(fname, annot, roles)

    # check for cue overlap
    overlapping_cues = check_cue_overlap(fname, dic)

    if remove_empty == True:
        dic = remove_annot_with_empty_cues(dic, empty_cues)

    if remove_overlap == True:
        dic = remove_cue_overlap(dic, overlapping_cues)

    return dic



def main():

    input_dir = "res"
    output_dir = "res_format_checked"
    remove_empty = True 
    remove_overlap = True

    if os.path.exists(output_dir):
        logging.warning("Output dir exists, please remove:", output_dir)
        sys.exit()
    os.mkdir(output_dir)


    files = glob.glob(input_dir+"/*.json")

    for f in files:
        dic = read_json(f)
        dic = check_format(f, dic, remove_empty, remove_overlap)

        write_to_file(dic, output_dir + '/' + f.replace('res/', ''))



if __name__ == "__main__":
    main()
