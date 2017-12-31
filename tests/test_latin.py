from pyperseus_treebank.latin import LatinToken, LatinCorpus
from pyperseus_treebank.base import Sentence, CONLL_MODES
from unittest import TestCase


class TestLatinToken(TestCase):
    def test_features(self):
        """

        Source : <word id="4" form="cano" lemma="cano" postag="v1spia---" relation="PRED" head="0"/>
        :return:
        """
        cano = LatinToken(4, "cano", "cano", 0, "v1spia---", rel="HEAD")
        self.assertEqual(cano.pos, "v")
        self.assertEqual(cano.features, {
            "Person": "1",
            "Number": "Sing",
            "Tense": "Pres",
            "Mood": "Ind",
            "Voice": "Act"
        })


class TestLatinCorpus(TestCase):
    def test_first_word(self):
        """ XML parsing keep original order """
        self.corpus = LatinCorpus("./tests/test_data/tb.latin.xml")
        self.assertEqual(
            self.corpus.sentences[0][0],
            LatinToken("1", "Arma", "arma", features="n-p---na-", rel="A-DO_CO", parent="3")
        )

    def test_sentence_equality(self):
        """ Compare a parsed sentence with expected output
          <word id="1" form="Tantae" lemma="tantus" postag="a-p---fn-" relation="ATR" head="5"/>
          <word id="2" form="-ne" lemma="ne1" postag="d--------" relation="ADV" head="7"/>
          <word id="3" form="animis" lemma="animus" postag="n-p---md-" relation="D-POSS" head="7"/>
          <word id="4" form="caelestibus" lemma="caelestis" postag="a-p---md-" relation="ATR" head="3"/>
          <word id="5" form="irae" lemma="ira" postag="n-p---fn-" relation="N-SUBJ" head="7"/>
      """
        self.corpus = LatinCorpus("./tests/test_data/short.tb.latin.xml")
        expected = Sentence([
            LatinToken("1", "Tantae", "tantus", features="a-p---fn-", rel="ATR", parent="5"),
            LatinToken("2", "-ne", "ne1", features="d--------", rel="ADV", parent="7"),
            LatinToken("3", "animis", "animus", features="n-p---md-", rel="D-POSS", parent="7"),
            LatinToken("4", "caelestibus", "caelestis", features="a-p---md-", rel="ATR", parent="3"),
            LatinToken("5", "irae", "ira", features="n-p---fn-", rel="N-SUBJ", parent="7")
        ])
        self.assertEqual(
            self.corpus.sentences[0],
            expected
        )

    def test_sentence_conllu(self):
        """ Compare a parsed sentence with expected output
          <word id="1" form="Tantae" lemma="tantus" postag="a-p---fn-" relation="ATR" head="5"/>
          <word id="2" form="-ne" lemma="ne1" postag="d--------" relation="ADV" head="7"/>
          <word id="3" form="animis" lemma="animus" postag="n-p---md-" relation="D-POSS" head="7"/>
          <word id="4" form="caelestibus" lemma="caelestis" postag="a-p---md-" relation="ATR" head="3"/>
          <word id="5" form="irae" lemma="ira" postag="n-p---fn-" relation="N-SUBJ" head="7"/>
      """
        self.corpus = LatinCorpus("./tests/test_data/short.tb.latin.xml")
        self.assertEqual(
            str(self.corpus.sentences[0]),
            """1	Tantae	tantus	a	a	Case=Nom|Gender=Fem|Number=Plur	5	ATR	_	_
2	-ne	ne1	d	d		7	ADV	_	_
3	animis	animus	n	n	Case=Dat|Gender=Masc|Number=Plur	7	D-POSS	_	_
4	caelestibus	caelestis	a	a	Case=Dat|Gender=Masc|Number=Plur	3	ATR	_	_
5	irae	ira	n	n	Case=Nom|Gender=Fem|Number=Plur	7	N-SUBJ	_	_""")

    def test_corpus(self):
        self.corpus = LatinCorpus("./tests/test_data/short.tb.latin.xml")
        self.assertEqual(
            str(self.corpus),
            """1	Tantae	tantus	a	a	Case=Nom|Gender=Fem|Number=Plur	5	ATR	_	_
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
7	!	punc1	u	u		0	AuxK	_	_""")

    def test_corpus_export_la_corpus(self):
        self.corpus = LatinCorpus("./tests/test_data/short.tb.latin.xml")
        print(
            self.corpus.export(CONLL_MODES.la_conll))
        self.assertEqual(
            self.corpus.export(CONLL_MODES.la_conll),
            """1	Tantae	tantus	ADJ	ADJ	Case=Nom|Gender=Fem|Number=Plur	5	ATR	_	_
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
7	!	punc1	PUNCT	PUNCT		0	AuxK	_	_""")
