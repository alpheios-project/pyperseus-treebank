import glob
from collections import namedtuple


_CONLLU_CONSTANTS = namedtuple("ConlluConstants", ["alpheios", "la_conll"])

CONLL_MODES = _CONLLU_CONSTANTS(
    0,
    1
)


class Token:
    """ Token (single element in a sentence : a word or a punctuation sign)

    :param index: Index of the token in the sentence
    :param form: Form of the token in the sentence
    :param lemma: Lemma that is attributed to the form
    :param parent: Head word of the current token in the index, aka. token this word is dependant of
    :param features: Features of the Token
    :param pos: Part of Speech tag of the current Token
    :param rel: Relation kind to the head word.

    .. note:: Token can be compared (Token() == Token())
    """
    def __init__(self, index, form, lemma, parent=0, features="", pos=None, rel="ROOT"):
        self.index = index
        self.form = form
        self.lemma = lemma
        self.parent = parent
        self.pos = pos
        self.rel = rel
        self.features = self.parse_features(features.replace("_", "-"))

    def __eq__(self, other):
        return self.index == other.index and \
                self.form == other.form and \
                self.lemma == other.lemma and \
                self.parent == other.parent and \
                self.pos == other.pos and \
                self.rel == other.rel and \
                self.features == other.features

    def parse_features(self, features):
        """ Parse features from the POSTAG of Perseus Latin XML

        .. example :: self.parse_features("n-p---na-")

        :param features: A string containing morphological informations
        :type features: str
        :return: Parsed features
        :rtype: dict
        """
        raise NotImplementedError("Parse Features has not been implemented for this class")


class Sentence:
    """ A sentence of treebanked data

    :param words: Words of the sentence
    :type words: [Token]

    .. note:: str(Corpus()) will release in a conllu export

    .. note:: len(Sentence) tells how many words there is in the sentence

    .. note:: Sentence accepts comparison

    .. note:: You can iter over a sentence directly [token for token in Sentenc(..)]
    """
    def __init__(self, words):
        self.__words__ = words

    @property
    def words(self):
        """ Words of the sentence

        :return: List of sentence's token
        :rtype: [Token]
        """
        return self.__words__

    def __eq__(self, other):
        return len(other) == len(self) and \
                False not in [mine == its for mine, its in zip(self, other)]

    def __len__(self):
        return len(self.words)

    def __iter__(self):
        for w in self.words:
            yield w

    @staticmethod
    def str_features(features):
        return "|".join("{}={}".format(cle, features[cle]) for cle in sorted(features.keys()))

    def __getitem__(self, item):
        return self.words[item]

    def __str__(self):
        """ String representation is Conllu format

        :rtype: str
        """
        return "\n".join(
            "\t".join([
                token.index, token.form, token.lemma, token.pos, token.pos,
                self.str_features(token.features), token.parent, token.rel, "_", "_"
            ])
            for token in self
        ) or "_"


class Corpus:
    """ Corpus is a set of sentences which can be exported to Conllu

    :param glob_path: Path to files that need to be parsed (Can be in the form \
    of a glob : ./path/to/**/*.xml
    :type glob_path: str

    :attr sentences: List of sentences
    :type sentences : [Sentence]

    .. note:: str(Corpus()) will release in a conllu export
    """
    def __init__(self, glob_path):
        self.files = glob.glob(glob_path)
        self.__sentences__ = list(self.parse(self.files))

    @property
    def sentences(self):
        return self.__sentences__

    @staticmethod
    def parse(files):
        """ Parse a set of files

        :param files: List of file's paths that needs to be parsed
        :type files: str

        :yields: Sentence thar were parsed
        :ytype: Sentence
        """
        raise NotImplementedError()

    def __iter__(self):
        for sentence in self.sentences:
            yield sentence

    def __str__(self):
        """ String representation is Conllu format

        :rtype: str
        """
        return "\n\n".join([str(s) for s in self.sentences])

    def export(self, mode=CONLL_MODES.alpheios):
        """ Export the corpus to conllu

        :param mode: A mode of export. There is different modes available in
        CONLL_MODES
        :return: A string conllu representation of the corpus
        """
        if mode == CONLL_MODES.alpheios:
            return str(self)
        else:
            raise NotImplementedError("This mode was not implemented")