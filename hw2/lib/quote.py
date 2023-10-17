"""
TODO docs
"""

class Quote():
    def __init__(self, quote: str, who: str, when: str=None,
                 where: str=None, how: str=None, context: str=None) -> None:
        """
        :param quote: str, the contents of the quote
            required
        :param who: str, the person who said the quote
            required

        :param when: str, when the quote was said
            optional
            for now this is just an unvalidated string -
            TODO accept datestrings with various levels of granularity
        :param where: str, where the quote was said
            optional
        :param how: str, medium of the quote (e.g. spoken word, blog post, etc.)
            optional
        :param context: str, piece of media or event in which the quote was said
            optional
        """
        self.quote = quote
        self.who = who
        if when is not None:
            self.when = when
        # TODO parse optional params
