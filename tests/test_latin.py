from pyperseus_treebank.latin import LatinToken
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
