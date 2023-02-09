"""
Provides classes necessary for a scope-based symbol table, including
lexically-enclosing scopes. Suitable for a language with a limited set
of primitive types (see PrimitiveType) and programmer-defined functions.

Author: Greg Phillips

Version: 2023-01-02
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Sequence, Union


class PrimitiveType(Enum):
    Int = auto()
    Bool = auto()
    String = auto()
    Void = auto()
    ERROR = auto()

    def __repr__(self):
        return self.name


@dataclass
class FunctionType:
    parameter_types: Sequence[PrimitiveType]
    return_type: PrimitiveType

    def __repr__(self):
        return f'({", ".join(p.name for p in self.parameter_types)}) -> {self.return_type.name}'


@dataclass
class Symbol:
    name: str
    type: Union[PrimitiveType, FunctionType]
    is_param: bool = False
    index: int = 0

    def __repr__(self):
        return f'Symbol {self.name} : {self.type} {"(param)" if self.is_param else ""}'


class Scope:
    """
    A scope maps names to symbols, using its `__symbols` dictionary. `Symbols` are:

     - defined using `define`,
     - looked up using `resolve` (normal name resolution, including enclosing scopes), or
     - looked up in the local scope only using `resolve_locally` (name resolution restricted
       to current scope, primarily used for detecting duplicate in-scope definitions and
       for definitions).

    `resolve` and `resolve_locally` return the symbol associated with the name, or `None` if
    the name is not found

    Each scope has a `return_type` attribute, for validating `return` statements appearing
    in the `scope`.

    Scopes lexically enclosed in other scopes must have an `enclosing_scope` attribute referring
    to the enclosing scope. E.g., function definitions and main are enclosed in the global scope.
    The global scope must have an `enclosing_scope` of `None`. Scopes with `enclosing_scope`s
    register themselves as children of their enclosing scopes.

    Registering a child scope with a name that has already been used will **silently overwrite**
    the original child scope. It is up to the client to ensure this doesn't happen.

    Scopes are expected to be named:

     - global scope: '$global'  (the $ prevents a name clash if there is a function named 'global')
     - main scope: '$main'
     - function scopes: name of function

    """

    def __init__(self, name, return_type=None, enclosing_scope=None):
        self.__variable_index = 0
        self.__parameter_index = 0
        self.name = name
        self.return_type = return_type
        self.enclosing_scope = enclosing_scope
        self.__child_scopes = {}
        self.__symbols = {}

    def create_child_scope(self, name, return_type):
        new_scope = Scope(name, return_type, enclosing_scope=self)
        self.__child_scopes[name] = new_scope
        return new_scope

    def define(self, name, _type, is_param=False):
        if is_param:
            self.__symbols[name] = Symbol(name, _type, is_param=True, index=self.__parameter_index)
            self.__parameter_index += 1
        elif isinstance(_type, PrimitiveType):
            self.__symbols[name] = Symbol(name, _type, index=self.__variable_index)
            self.__variable_index += 1
        else:
            self.__symbols[name] = Symbol(name, _type)

    def resolve(self, name):
        local_symbol = self.resolve_locally(name)
        if local_symbol:
            return local_symbol
        elif self.enclosing_scope:
            return self.enclosing_scope.resolve(name)
        else:
            return None

    def resolve_locally(self, name):
        return self.__symbols.get(name)

    def child_scope_named(self, name):
        return self.__child_scopes.get(name)

    # ---------------------------------------------------------------------------------
    # Inspection of child scopes is primarily for testing

    @property
    def child_scopes(self):
        return self.__child_scopes

    # ---------------------------------------------------------------------------------
    # The following three methods are used in code generation. Not relevant for semantic
    # analysis.

    def parameters(self):
        return [s for s in self.__symbols.values() if s.is_param]

    def local_variables(self):
        return [s for s in self.__symbols.values() if not s.is_param and
                not isinstance(s.type, FunctionType)]

    def functions(self):
        return [s for s in self.__symbols.values() if isinstance(s.type, FunctionType)]

    def __repr__(self):
        entries = '\n'.join(f'  {n} : {str(t)}'
                            for n, t in self.__symbols.items())
        return f'scope: {self.name} returns {self.return_type}\n{entries}'
