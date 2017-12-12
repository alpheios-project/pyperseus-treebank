class Token:
    def __init__(self, index, form, lemma, parent=0, features="", pos=None, rel="ROOT"):
        self.index = index
        self.form = form
        self.lemma = lemma
        self.parent = parent
        self.pos = pos
        self.rel = rel
        self.features = self.parse_features(features)

    def parse_features(self, features):
        """ Parse features from the POSTAG of Perseus Latin XML

        .. example :: self.parse_features("n-p---na-")

        :param features: A string containing morphological informations
        :type features: str
        :return: Parsed features
        :rtype: dict
        """
        raise NotImplementedError("Parse Features has not been implemented for this class")
