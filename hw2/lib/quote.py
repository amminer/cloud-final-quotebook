"""
Quote class represents a quote and its metadata for easy handling
"""

from datetime import datetime
from lib.date_helper import date_to_string, string_to_date

class Quote():
    def __init__(self, quote: str, who: str, when: datetime='',
                 where: str='', how: str='', context: str='') -> None:
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
        self.when = string_to_date(when)
        self.where = where
        self.how = how
        self.context = context

    def __str__(self) -> str:
        ret = self.quote + ' - ' + self.who
        if self.when:
            ret += ' (' + date_to_string(self.when) + ')'
        if self.where:
            ret += ' [' + self.where + ']'
        if self.how:
            ret += ' {' + self.how + '}'
        if self.context:
            ret += ' (' + self.context + ')'
        return ret
