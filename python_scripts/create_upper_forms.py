import argparse
import re

#Argumente
parser = argparse.ArgumentParser(description="determine all possible analyses of a Lakota verb")
parser.add_argument("word", type=str, help="verb with markers for position of personal pronouns")
parser.add_argument("type", type=str, choices=["a", "s"], help="active/stative type of the verb: a for active, s for stative")
parser.add_argument("valency", type=int, help="verb valency: 0 for impersonal, 1 for intransitive, 2 for transitive")
args = parser.parse_args()
word = args.word
type = 'active' if args.type == 'a' else 'stative'
valency = 0 if args.valency < 1 else 2 if args.valency > 1 else 1

#pronoun combinations depending on active/stative and valency
a_1 = [['1PL:ACT'], ['1DUAL:ACT'], ['3PL:ACT'], ['3SG:ACT'], ['2PL:ACT'], ['2SG:ACT'], ['1SG:ACT']]
a_2 = [['1PL:STA'],
 ['1PL:STA', '3PL:ACT'],
 ['1PL:STA', '3SG:ACT'],
 ['1PL:STA', '2PL:ACT'],
 ['1PL:STA', '2SG:ACT'],
 ['1PL:ACT', '2SG:STA'],
 ['1PL:ACT'],
 ['1PL:ACT', '2PL:STA'],
 ['1PL:ACT', '3SG:STA'],
 ['1PL:ACT', '3PL:STA'],
 ['1DUAL:STA'],
 ['1DUAL:STA', '3PL:ACT'],
 ['1DUAL:STA', '3SG:ACT'],
 ['1DUAL:ACT'],
 ['1DUAL:ACT', '3PL:STA'],
 ['1DUAL:ACT', '3SG:STA'],
 ['3PL:ACT'],
 ['2PL:ACT', '3PL:STA'],
 ['2SG:ACT', '3PL:STA'],
 ['1SG:ACT', '3PL:STA'],
 ['3PL:STA', '3PL:ACT'],
 ['3PL:STA', '3SG:ACT'],
 ['3PL:STA'],
 ['3SG:ACT'],
 ['2PL:ACT', '3SG:STA'],
 ['2SG:ACT', '3SG:STA'],
 ['1SG:ACT', '3SG:STA'],
 ['3SG:STA', '3PL:ACT'],
 ['3SG:STA', '3SG:ACT'],
 ['3SG:STA'],
 ['1SG:ACT', '2PL:STA'],
 ['2PL:STA', '3SG:ACT'],
 ['2PL:STA'],
 ['2PL:STA', '3PL:ACT'],
 ['2PL:ACT'],
 ['1SG:ACT', '2SG:STA'],
 ['2SG:STA', '3SG:ACT'],
 ['2SG:STA'],
 ['2SG:STA', '3PL:ACT'],
 ['2SG:ACT'],
 ['1SG:STA', '3SG:ACT'],
 ['1SG:STA'],
 ['1SG:STA', '3PL:ACT'],
 ['1SG:STA', '2PL:ACT'],
 ['1SG:STA', '2SG:ACT'],
 ['1SG:ACT'],
 ['3COLL:STA'],
 ['3COLL:STA', '3PL:ACT'],
 ['3COLL:STA', '3SG:ACT'],
 ['3COLL:STA', '2PL:ACT'],
 ['3COLL:STA', '2SG:ACT'],
 ['3COLL:STA', '1SG:ACT'],
 ['3COLL:STA', '1PL:ACT'],
 ['3COLL:STA', '1DUAL:ACT']]
s_1 = [['1PL:STA'],
 ['1DUAL:STA'],
 ['3PL:STA'],
 ['3SG:STA'],
 ['2PL:STA'],
 ['2SG:STA'],
 ['1SG:STA'],
 ['3COLL:STA']]
s_2 = [['1PL:STA'],
 ['1DUAL:STA'],
 ['3PL:STA'],
 ['3SG:STA'],
 ['2PL:STA'],
 ['2SG:STA'],
 ['1SG:STA'],
 ['3COLL:STA'],
 ['3COLL:STA', '3PL:STA'],
 ['3COLL:STA', '3SG:STA'],
 ['3COLL:STA', '2PL:STA'],
 ['3COLL:STA', '2SG:STA'],
 ['3COLL:STA', '1SG:STA'],
 ['3COLL:STA', '1PL:STA'],
 ['3COLL:STA', '1DUAL:STA'],
 ['1PL:STA', '3PL:STA'],
 ['1PL:STA', '3SG:STA'],
 ['1PL:STA', '2PL:STA'],
 ['1PL:STA', '2SG:STA'],
 ['1DUAL:STA', '3PL:STA'],
 ['1DUAL:STA', '3SG:STA'],
 ['3PL:STA', '3PL:STA'],
 ['3PL:STA', '3SG:STA'],
 ['3PL:STA', '2PL:STA'],
 ['3PL:STA', '2SG:STA'],
 ['3PL:STA', '1SG:STA'],
 ['3SG:STA', '3PL:STA'],
 ['3SG:STA', '3SG:STA'],
 ['3SG:STA', '2PL:STA'],
 ['3SG:STA', '2SG:STA'],
 ['3SG:STA', '1SG:STA'],
 ['2PL:STA', '3PL:STA'],
 ['2PL:STA', '3SG:STA'],
 ['2PL:STA', '1SG:STA'],
 ['2SG:STA', '3PL:STA'],
 ['2SG:STA', '3SG:STA'],
 ['2SG:STA', '1SG:STA'],
 ['1SG:STA', '3PL:STA'],
 ['1SG:STA', '3SG:STA'],
 ['2PL:STA', '1SG:STA'],
 ['2SG:STA', '1SG:STA']]

#pronoun dictionary
pronouns = {'active1': a_1,
            'active2': a_2,
            'stative1': s_1,
            'stative2':s_2
}

upper = []

pronoun_list = type + str(valency)
if '^K' in word:
    word = word.replace('^K', 'k')
if '^Y' in word:
    word = word.replace('^Y', 'y')

if not word.startswith('M'):
    if word.startswith('PP'):
        upper.append(word[3:] + '+Verb')
        for item in pronouns[pronoun_list]:
            combination = '+'.join(item)
            if 'PL' in combination:
                upper_form =  combination + '+' + word[3:] + '+Verb' + '+Pl'
            else:
                upper_form = combination + '+' + word[3:] + '+Verb'
            upper.append(upper_form)
    else:
        upper.append(re.sub(r'PP', '', word) + '+Verb')
        for item in pronouns[pronoun_list]:
                combination = '+Stem+' + '+'.join(item) + '+'
                if 'PL' in combination:
                    upper_form =  re.sub(r'PP', combination, word) + '+Verb' + '+Pl'
                else:
                    upper_form = re.sub(r'PP', combination, word) + '+Verb'
                upper.append(upper_form)
else:
    upper.append(re.sub(r'PP', '', word[1:]) + '+Verb')
    for item in pronouns[pronoun_list]:
        if ('1PL' in item[0] or '1DUAL' in item[0]):
            prefix_item =  item[0] + '+'
            if len(item) == 1:
                infix_item = ''
            else:
                infix_item = '+Stem+' + item[1] + '+'
            if 'PL' in prefix_item or 'PL' in infix_item:
                upper_form =  re.sub(r'M', prefix_item, re.sub(r'PP', infix_item, word))  + '+Verb' + '+Pl'
            else:
                upper_form =  re.sub(r'M', prefix_item, re.sub(r'PP', infix_item, word)) + '+Verb'    
            upper.append(upper_form)
        elif len(item) > 1 and ('1PL' in item[1] or '1DUAL' in item[1]):
            prefix_item =  item[1] + '+'
            infix_item = ''
            if 'PL' in prefix_item:
                upper_form =  re.sub(r'M', prefix_item, re.sub(r'PP', infix_item, word))  + '+Verb' + '+Pl'
            else:
                upper_form =  re.sub(r'M', prefix_item, re.sub(r'PP', infix_item, word)) + '+Verb'    
            upper.append(upper_form)
        else:
            infix_combination = '+Stem+' + '+'.join(item) + '+'
            if 'PL' in infix_combination:
                upper_form =  re.sub(r'PP', infix_combination, word[1:]) + '+Verb' + '+Pl'
            else:
                upper_form = re.sub(r'PP', infix_combination, word[1:]) + '+Verb'
            upper.append(upper_form) 
            

#write to file
with open("upper-forms.txt", "w") as f:
    for item in upper:
        f.write(item + '\n')
