"""
Quote class represents a quote and its metadata for easy handling
"""

from datetime import datetime
from lib.date_helper import date_to_string, string_to_date

class Quote():
    def __init__(self, quote: str, who: str, when: datetime=None,
                 where: str=None, how: str=None, context: str=None) -> None:
        """
        :param quote: str, the contents of the quote
            required
        :param who: str, the person who said the quote
            required

        :param when: datetime, when the quote was said
            optional
            only day, month, year are used
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
        if where is not None:
            self.where = where
        if how is not None:
            self.how = how
        if context is not None:
            self.context = context

    def __str__(self) -> str:
        ret = self.quote + ' - ' + self.who + ' (' + date_to_string(self.when) + ')'
        if hasattr(self, 'where'):
            ret += ' [' + self.where + ']'
        if hasattr(self, 'how'):
            ret += ' {' + self.how + '}'
        if hasattr(self, 'context'):
            ret += ' (' + self.context + ')'
        return ret
