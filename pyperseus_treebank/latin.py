"""

..source :: https://github.com/perseids-project/perseids_treebanking/blob/ae0305138dacc4a89c5fe6b0f086a4b3b1efdc92/transformations/aldt-util.xsl
"""
from .base import Token, Corpus, Sentence
import lxml.etree as etree
import re


_NUMBER = {"s": "Sing", "p": "Plur"}
_TENSE = {"p": "Pres", "f": "Fut", "r": "Perf", "l": "PQP", "i": "Imp", "t": "FutPerf"}
_MOOD = {"i": "Ind", "s": "Sub", "m": "Imp", "g": "Ger", "p": "Part", "u": "Sup", "n": "Inf"}
_VOICE = {"a": "Act", "p": "Pass", "d": "Dep"}
_GENDER = {"f": "Fem", "m": "Masc", "n": "Neut", "c": "Com"}
_CASE = {"g": "Gen", "d": "Dat", "a": "Acc", "v": "Voc", "n": "Nom", "b": "Abl", "i": "Ins", "l": "Loc"}
_DEGREE = {"p": "Pos", "c": "Comp", "s": "Sup"}


NOTWORD = re.compile("^\W+$")


class LatinToken(Token):

    def parse_features(self, features):
        """ Parse features from the POSTAG of Perseus Latin XML

        .. example :: self.parse_features("n-p---na-")

        :param features: A string containing morphological informations
        :type features: str
        :return: Parsed features
        :rtype: dict
        """

        feats = {}

        self.pos = features[0]

        # Person handling : 3 possibilities
        if features[1] != "-":
            feats["Person"] = features[1]

        # Number handling : two possibilities
        if features[2] != "-":
            feats["Number"] = _NUMBER[features[2]]

        # Tense
        if features[3] != "-":
            feats["Tense"] = _TENSE[features[3]]

        # Mood
        if features[4] != "-":
            feats["Mood"] = _MOOD[features[4]]

        # Voice
        if features[5] != "-":
            feats["Voice"] = _VOICE[features[5]]

        # Tense
        if features[6] != "-":
            feats["Gender"] = _GENDER[features[6]]

        # Tense
        if features[7] != "-":
            feats["Case"] = _CASE[features[7]]

        # Degree
        if features[8] != "-":
            feats["Degree"] = _DEGREE[features[8]]

        return feats


class LatinCorpus(Corpus):
    @staticmethod
    def parse(files):
        for file in files:
            with open(file) as f:
                xml = etree.parse(f)
            for sentence in xml.xpath("//sentence"):
                sent = []
                for word in sentence.xpath(".//word[not(@artificial)]"):
                    postag = word.get("postag")
                    if not postag:
                        if word.get("lemma") == "punc1":
                            postag = "u--------"
                        elif word.get("form") in ",!“":
                            postag = "u--------"
                        elif NOTWORD.match(word.get("form")):
                            postag = "u--------"
                        else:
                            print(etree.tostring(word))
                            raise ValueError("postag is empty")
                    sent.append(LatinToken(
                        index=word.get("id"),
                        form=word.get("form"),
                        lemma=word.get("lemma"),
                        features=postag,
                        rel=word.get("relation"),
                        parent=word.get("head")
                    ))
                yield Sentence(sent)
