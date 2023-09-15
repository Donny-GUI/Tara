import ast
from typing import (
    
    # Primitives
    Annotated, 
    Any,
    Callable,
    ClassVar,
    Concatenate,
    Final,
    ForwardRef,
    Generic,
    Literal,
    Optional,
    ParamSpec,
    Protocol,
    Tuple,
    Type,
    TypeVar,
    TypeVarTuple,
    Union,

    # Structural
    Reversible, 
    SupportsAbs, 
    SupportsBytes, 
    SupportsComplex, 
    SupportsFloat, 
    SupportsIndex, 
    SupportsInt, 
    SupportsRound,
    
    # Abstract Base
    AbstractSet,
    ByteString,
    Container,
    ContextManager,
    Hashable,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    MappingView,
    MutableMapping,
    MutableSequence,
    MutableSet,
    Sequence,
    Sized,
    ValuesView,
    Awaitable,
    AsyncIterator,
    AsyncIterable,
    Coroutine,
    Collection,
    AsyncGenerator,
    AsyncContextManager,

    # Concrete Collection
    ChainMap,
    Counter,
    Deque,
    Dict,
    DefaultDict,
    List,
    OrderedDict,
    Set,
    FrozenSet,
    NamedTuple,
    TypedDict,
    Generator,

    # Uniques 
    AnyStr,
    assert_type,
    assert_never,
    cast,
    clear_overloads,
    dataclass_transform,
    final,
    get_args,
    get_origin,
    get_overloads,
    get_type_hints,
    is_typeddict,
    LiteralString,
    Never,
    NewType,
    no_type_check,
    no_type_check_decorator,
    NoReturn,
    NotRequired,
    overload,
    ParamSpecArgs,
    ParamSpecKwargs,
    Required,
    reveal_type,
    runtime_checkable,
    Self,
    Text,
    TYPE_CHECKING,
    TypeAlias,
    TypeGuard,
    Unpack,
)


class Primitives:
    ALL = (Annotated, Any, 
           Callable, ClassVar, Concatenate, 
           Final, ForwardRef, 
           Generic,
           Literal, 
           Optional, 
           ParamSpec,Protocol, 
           Tuple, Type, TypeVar, TypeVarTuple, 
           Union)
    STRINGS = ("Annotated", "Any", 
               "Callable", "ClassVar", "Concatenate", 
               "Final", "ForwardRef", 
               "Generic",
               "Literal", 
               "Optional",
               "ParameterSpec", "Protocol", 
               "Tuple", "Type", "TypeVar", "TypeVarTuple", 
               "Union")


class Structural:
    ALL = (
        Reversible,
        SupportsAbs,
        SupportsBytes,
        SupportsComplex,
        SupportsFloat,
        SupportsIndex,
        SupportsInt,
        SupportsRound,
    )
    STRINGS = (
        'Reversible',
        'SupportsAbs',
        'SupportsBytes',
        'SupportsComplex',
        'SupportsFloat',
        'SupportsIndex',
        'SupportsInt',
        'SupportsRound'
    )


class Protocol(Structural):
    pass 


class AbstractBase:
    ALL = (
        AbstractSet,
        ByteString,
        Container,
        ContextManager,
        Hashable,
        ItemsView,
        Iterable,
        Iterator,
        KeysView,
        Mapping,
        MappingView,
        MutableMapping,
        MutableSequence,
        MutableSet,
        Sequence,
        Sized,
        ValuesView,
        Awaitable,
        AsyncIterator,
        AsyncIterable,
        Coroutine,
        Collection,
        AsyncGenerator,
        AsyncContextManager,
    )
    STRINGS = (
        # ABCs (from collections.abc).
        'AbstractSet',  # collections.abc.Set.
        'ByteString',
        'Container',
        'ContextManager',
        'Hashable',
        'ItemsView',
        'Iterable',
        'Iterator',
        'KeysView',
        'Mapping',
        'MappingView',
        'MutableMapping',
        'MutableSequence',
        'MutableSet',
        'Sequence',
        'Sized',
        'ValuesView',
        'Awaitable',
        'AsyncIterator',
        'AsyncIterable',
        'Coroutine',
        'Collection',
        'AsyncGenerator',
        'AsyncContextManager'
    )


class ConcreteCollection:
    ALL = (
        ChainMap,
        Counter,
        Deque,
        Dict,
        DefaultDict,
        List,
        OrderedDict,
        Set,
        FrozenSet,
        NamedTuple,
        TypedDict,
        Generator,
    )
    STRINGS = (
        # Concrete collection types.
        'ChainMap',
        'Counter',
        'Deque',
        'Dict',
        'DefaultDict',
        'List',
        'OrderedDict',
        'Set',
        'FrozenSet',
        'NamedTuple',  # Not really a type.
        'TypedDict',  # Not really a type.
        'Generator',
        # Other concrete types.
        'BinaryIO',
        'IO',
        'Match',
        'Pattern',
        'TextIO'
    )


class Unique:
    ALL = (
        AnyStr,
        assert_type,
        assert_never,
        cast,
        clear_overloads,
        dataclass_transform,
        final,
        get_args,
        get_origin,
        get_overloads,
        get_type_hints,
        is_typeddict,
        LiteralString,
        Never,
        NewType,
        no_type_check,
        no_type_check_decorator,
        NoReturn,
        NotRequired,
        overload,
        ParamSpecArgs,
        ParamSpecKwargs,
        Required,
        reveal_type,
        runtime_checkable,
        Self,
        Text,
        TYPE_CHECKING,
        TypeAlias,
        TypeGuard,
        Unpack,
    )
    STRINGS = (
        # One-off things.
        'AnyStr',
        'assert_type',
        'assert_never',
        'cast',
        'clear_overloads',
        'dataclass_transform',
        'final',
        'get_args',
        'get_origin',
        'get_overloads',
        'get_type_hints',
        'is_typeddict',
        'LiteralString',
        'Never',
        'NewType',
        'no_type_check',
        'no_type_check_decorator',
        'NoReturn',
        'NotRequired',
        'overload',
        'ParamSpecArgs',
        'ParamSpecKwargs',
        'Required',
        'reveal_type',
        'runtime_checkable',
        'Self',
        'Text',
        'TYPE_CHECKING',
        'TypeAlias',
        'TypeGuard',
        'Unpack')


def isprimitive(object: any) -> bool:
    """
    Check if object is structural type object 
    """
    for obj in Primitives.ALL:
        if isinstance(object, obj):
            return True
    return False

def isstructural(object: any) -> bool:
    """
    Check if object is structural type object 
    """
    for obj in Structural.ALL:
        if isinstance(object, obj):
            return True
    return False

def isabstract(object: any) -> bool:
    """
    check if an object is an Abstract Base Class Type object
    """
    for obj in AbstractBase.ALL:
        if isinstance(object, obj):
            return True
    return False

def isconcrete(object: any) -> bool:
    """
    Check if object is a concrete collection type object 
    """
    for obj in ConcreteCollection.ALL:
        if isinstance(object, obj):
            return True
    return False

def isother(object: any) -> bool:
    """
    check if an object is an other-ly type object
    """
    if isprimitive(object):
        return True
    if isstructural(object):
        return True
    if isabstract(object):
        return True
    if isconcrete(object):
        return True
    return False
    
def check_typing_import(filepath: str) -> bool:
    """ 
    Returns True if the given filepath imports anything from typing.
    Returns False if the given filepath does not import anything from typing.

    Warning: if this function cannot parse the python tree, lets say becuase its a cpp file...
             then it will return False. I dont see a problem with this yet.
    """
    
    with open(filepath, 'rb') as bf:
        try:
            content = bf.read()
        except:
            raise UnicodeDecodeError
    
    try:
        tree = ast.parse(content)
    except:
        if filepath.endswith('.py'):
            raise Exception(f"Could not parse {filepath}")
        return False

    for node in ast.walk(tree):
        
        if isinstance(node, ast.ImportFrom):
            if node.module == "typing":
                return True
            
        if isinstance(node, ast.Import):
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.alias) and ast.unparse(subnode) == "typing":
                    return True
    
    return False

def atest():    
    print(check_typing_import(__file__))

