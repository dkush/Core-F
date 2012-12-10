# Created by: Dave Kush
# 10, Nov 2012
#

# Initial code to find sentence-internal matches for pronouns, assuming 
# input parse from Stanford parser of type:
#(ROOT  (S  (NP (NNP John))  (VP (VBD said)  (SBAR  (S  (NP (PRP he))  (VP (VBZ wants)  (S  (VP (TO to)  (VP (VB go)  (NP (NN home)))))))))  (. .)))




def check_in_matrix(parsed_sentence, pronoun, index):
	matrix_verb = ""
	pron = "%s-%d" % (pronoun, index)
	inMatrix = False
	for x in parsed_sentence.typed_dependencies:
		if "root" in x [0:5]:
			matrix_verb = x.split(", ")[1]
			matrix_verb = matrix_verb.rstrip(")")
	for x in parsed_sentence.typed_dependencies:
		if matrix_verb in x and pron in x:
			inMatrix = True
			return inMatrix

def try_sentence_internally(sentence, pronoun, index, internalResolve):
	sent = sentence.split()
	poss_ants = []
	feats = get_feats(pronoun)
	for x in sent[:index+1]:
		if x.tag == "NP" and get_feats(x) == feats:
			poss_ants.append(x)
	
	remove_corefs(poss_ants)
	
	if len(poss_ants) == 0:
		internalResolve == False
	elif len(poss_ants) == 1:
		antecedent = poss_ants.pop()
	else:
		antecedent = find_highest(poss_ants)
	bump_activation(antecedent)
	sentence.assign_antecedent(index, antecedent)	


# TO DO:
#	centering
#	activation
#	sentence external
#	reflexive resolution
#	principle B
#

	


