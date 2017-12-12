import glob


class Token:
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
    def __init__(self, words):
        self.__words__ = words

    @property
    def words(self):
        """ Words of the sentence


        :return:
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
    def __init__(self, glob_path):
        self.files = glob.glob(glob_path)
        self.__sentences__ = list(self.parse(self.files))

    @property
    def sentences(self):
        return self.__sentences__

    @staticmethod
    def parse(files):
        raise NotImplementedError()

    def __str__(self):
        """ String representation is Conllu format

        :rtype: str
        """
        return "\n\n".join([str(s) for s in self.sentences])