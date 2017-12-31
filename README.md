# pyperseus-treebank

[![Coverage Status](https://coveralls.io/repos/github/alpheios-project/pyperseus-treebank/badge.svg?branch=master)](https://coveralls.io/github/alpheios-project/pyperseus-treebank?branch=master)
[![Build Status](https://travis-ci.org/alpheios-project/pyperseus-treebank.svg?branch=master)](https://travis-ci.org/alpheios-project/pyperseus-treebank)
[![PyPI version](https://badge.fury.io/py/pyperseus-treebank.svg)](https://badge.fury.io/py/pyperseus-treebank)

This can be installed from pypi :

```shell
pip install pyperseus-treebank
```

## What's PyPerseus-Treebank

PyPerseus treebank is a really simplistic tool to deal with original Perseus and Perseids treebank XML format (such as
https://github.com/perseids-project/harrington_trees ).

It helps producing conllu format and please feel free to help enhancing cross-compatibility of corpora.

## Example of use

```python
from pyperseus_treebank.latin import LatinCorpus

corpus = LatinCorpus("./tests/test_data/tb.latin.xml")
print(str(corpus))
```

would result in

```conll
1	Tantae	tantus	a	a	Case=Nom|Gender=Fem|Number=Plur	5	ATR	_	_
2	-ne	ne1	d	d		7	ADV	_	_
3	animis	animus	n	n	Case=Dat|Gender=Masc|Number=Plur	7	D-POSS	_	_
4	caelestibus	caelestis	a	a	Case=Dat|Gender=Masc|Number=Plur	3	ATR	_	_
5	irae	ira	n	n	Case=Nom|Gender=Fem|Number=Plur	7	N-SUBJ	_	_

1	Tantae	tantus	a	a	Case=Gen|Gender=Fem|Number=Sing	2	ATR	_	_
2	molis	moles	n	n	Case=Gen|Gender=Fem|Number=Sing	3	G-DESC	_	_
3	erat	sum1	v	v	Mood=Ind|Number=Sing|Person=3|Tense=Imp|Voice=Act	0	PRED	_	_
4	Romanam	Romanus	a	a	Case=Acc|Gender=Fem|Number=Sing	6	ATR	_	_
5	condere	condo	v	v	Mood=Inf|Tense=Pres|Voice=Act	3	N-SUBJ	_	_
6	gentem	gens	n	n	Case=Acc|Gender=Fem|Number=Sing	5	A-DO	_	_
7	!	punc1	u	u		0	AuxK	_	_
```

### Convert to other conllu vocabularies

Thanks to @epageparron


```python
from pyperseus_treebank.latin import LatinCorpus, CONLL_MODES

corpus = LatinCorpus("./tests/test_data/tb.latin.xml")
print(corpus.export(CONLL_MODES.la_conll))
```

would result in

```conll
1	Tantae	tantus	ADJ	ADJ	Case=Nom|Gender=Fem|Number=Plur	5	ATR	_	_
2	-ne	ne1	ADV	ADV		7	ADV	_	_
3	animis	animus	NOUN	NOUN	Case=Dat|Gender=Masc|Number=Plur	7	D-POSS	_	_
4	caelestibus	caelestis	ADJ	ADJ	Case=Dat|Gender=Masc|Number=Plur	3	ATR	_	_
5	irae	ira	NOUN	NOUN	Case=Nom|Gender=Fem|Number=Plur	7	N-SUBJ	_	_

1	Tantae	tantus	ADJ	ADJ	Case=Gen|Gender=Fem|Number=Sing	2	ATR	_	_
2	molis	moles	NOUN	NOUN	Case=Gen|Gender=Fem|Number=Sing	3	G-DESC	_	_
3	erat	sum1	VERB	VERB	Mood=Ind|Number=Sing|Person=3|Tense=Imp|Voice=Act	0	PRED	_	_
4	Romanam	Romanus	ADJ	ADJ	Case=Acc|Gender=Fem|Number=Sing	6	ATR	_	_
5	condere	condo	VERB	VERB	Mood=Inf|Tense=Pres|Voice=Act	3	N-SUBJ	_	_
6	gentem	gens	NOUN	NOUN	Case=Acc|Gender=Fem|Number=Sing	5	A-DO	_	_
7	!	punc1	PUNCT	PUNCT		0	AuxK	_	_
```