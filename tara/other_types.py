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


OneOffs = [
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
    'Unpack']



