## Morphological analysis of Lakota verb forms
### Python scripts

The scripts

- test_positive_applydown.py
- test_negative_applydown.py
- test_negative_applyup.py

allow a simple automated test case execution.

```
python test_positive_applydown.py

python test_negative_applydown.py

python test_negative_applyup.py
```

They use the corresponding files

 - upper-correct.txt
 - upper-negative.txt
 - lower-negative.txt

to produce the respective lower or upper forms.
Thereby an output.txt is created, which is compared to the corresponding

- upper-correct-goal.txt
- upper-negative-goal.txt
- lower-negative-goal.txt

Information on phenomena tested by each testcase can be found in [annotated_test_files](annotated_test_files/).

<br>

The script

- create_upper_forms.py

creates all possible upper forms of an input verb.

Prepare your verb as follows:

Determine, whether personal pronouns are prefixed, infixed, or of mixed type.
- in case of prefix, add PP before your verb, e.g.PPyuhá for yuhá 
- in case of infix, add PP at the infix position, e.g. íPPpuzA for ípuzA
- in case of mixed, add M before your verb and PP at the infix position, e.g. MoPPlé for olé

        usage: create_upper_forms.py [-h] word {a,s} valency

        positional arguments:
          word        verb with markers for position of personal pronouns
          {a,s}       active/stative type of the verb: a for active, s for stative
          valency     verb valency: 0 for impersonal, 1 for intransitive, 2 for transitive



For example
```
python create_upper_forms íPPpuzA a 1
```

An output file "upper-forms.txt" is created.


