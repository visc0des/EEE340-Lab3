"""
The errorlog module provides a logging mechanism for semantic errors
discovered in analysis of a Nimble program.

Author: Greg Phillips

Version: 2022-02-04
"""

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum, auto

from antlr4 import ParserRuleContext


class Category(Enum):
    """
    Categories of semantic errors for Nimble programs.
    """
    ASSIGN_TO_WRONG_TYPE = auto()  # left hand side of assignment incompatible with right
    UNDEFINED_NAME = auto()  # variable name not defined
    DUPLICATE_NAME = auto()  # variable name declared multiple times
    INVALID_NEGATION = auto()  # negation ! or - applied to incompatible expression
    INVALID_BINARY_OP = auto()  # binary operator applied to incompatible left and right expressions
    CONDITION_NOT_BOOL = auto()  # condition on if or while statement not a Bool
    UNPRINTABLE_EXPRESSION = auto() # expression in print is not a valid type

    def __str__(self):
        return self.name




@dataclass
class Entry:
    """
    A record of a semantic error, to be stored in the error log. Includes the parse tree
    node on which the error was detected, the ErrorCategory, and a useful descriptive message.
    """
    ctx: ParserRuleContext
    category: Category
    message: str

    def line(self) -> int:
        """The source code line on which the semantic error was detected."""
        return self.ctx.start.line

    def __repr__(self):
        return f'line {self.line()} : {self.category} : {self.message}\n    {self.ctx.getText()}'


class ErrorLog:
    """
    A log of SemanticErrors detected. For each line on which an error was detected, contains
    a dictionary mapping source strings to errors arising from that source string.
    """

    def __init__(self):
        self.__entries = defaultdict(dict)

    def add(self, ctx: ParserRuleContext, category: Category, message: str):
        entry = Entry(ctx, category, message)
        self.__entries[entry.line()][ctx.getText()] = entry

    def includes_exactly(self, category: Category, line: int, source: str) -> bool:
        """
        Returns True if there is an error of the given category recorded for the
        given line corresponding to the given source string. Useful when there may
        be multiple errors on a line and a specific error is of interest.
        """
        return self.__entries[line][source].category == category

    def includes_on_line(self, category: Category, line: int):
        """
        Returns True if there is an error of the given category recorded for the
        given line. Useful when it's inconvenient to include the entire source
        corresponding to the error.
        """
        return any(category == entry.category for entry in self.__entries[line].values())

    def total_entries(self):
        return sum(len(entry) for entry in self.__entries.values())

    def __str__(self):
        error_list = [str(entry)
                      for line in sorted(self.__entries.keys())
                      for entry in self.__entries[line].values()
                      ]
        return '\n'.join(error_list)
