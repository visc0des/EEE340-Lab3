"""
Provides a generic `parse` function which either returns a parse tree or
raises a `SyntaxErrors` exception with a `SyntaxErrorLog`.

Author: Greg Phillips

Version: 2022-02-04
"""

from dataclasses import dataclass

from antlr4 import FileStream, InputStream, CommonTokenStream,\
    Recognizer, RecognitionException, Token


def parse(source_or_path, start_rule_name, lexer_class, parser_class, from_file=False):
    """
    Creates a parser on the provided source or source file, adds a `SyntaxErrorLog` as
    error listener at both the lex and parse stages, and attempts the parse from the given
    rule name. Raises a `SyntaxErrors` exception if any are logged during the lex or parse.

    :param source_or_path: Either a string containing the source code, or
        the path to a source file
    :param start_rule_name: The ANTLR grammar rule to be used as parse root
    :param lexer_class: A generated ANTLR lexer class
    :param parser_class: A generated ANTLR parser class
    :param from_file: True if input is a file
    :return: The computed ANTLR parse tree
    """
    if from_file:
        character_stream = FileStream(source_or_path)
    else:
        character_stream = InputStream(source_or_path)
    lexer = lexer_class(character_stream)
    token_stream = CommonTokenStream(lexer)
    parser = parser_class(token_stream)

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    error_log = SyntaxErrorLog()
    lexer.addErrorListener(error_log)
    parser.addErrorListener(error_log)

    parse_function = parser.__getattribute__(start_rule_name)
    parse_tree = parse_function()

    if error_log.has_errors():
        raise SyntaxErrors(error_log, parse_tree)
    else:
        return parse_tree


class SyntaxErrors(Exception):

    def __init__(self, error_log, parse_tree):
        self.error_log = error_log
        self.parse_tree = parse_tree

    def __repr__(self):
        return repr(self.error_log)


@dataclass
class SyntaxErrorRecord:
    recognizer: Recognizer
    offending_symbol: Token
    line: int
    column: int
    message: str
    exception: RecognitionException

    def __repr__(self):
        return f'line {self.line} : {self.column} {self.message}'


class SyntaxErrorLog:
    """
    Implements the standard ANTLR error listener interface to log errors encountered
    in either the lex or parse. Ignores reports that aren't actual errors.
    """

    def __init__(self):
        self.syntax_errors = []

    def has_errors(self):
        return bool(self.syntax_errors)

    def syntaxError(self, recognizer, offending_symbol, line, char_position, msg, exception):
        self.syntax_errors.append(
            SyntaxErrorRecord(recognizer, offending_symbol, line, char_position, msg, exception))

    def total_entries(self):
        return len(self.syntax_errors)

    def reportAttemptingFullContext(self, recognizer, dfa, start_index, stop_index,
                                    conflicting_alts, configs):
        pass

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

    def __repr__(self):
        return '\n'.join([str(e) for e in self.syntax_errors])
