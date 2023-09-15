from typing import ( 
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
    Reversible, 
    SupportsAbs, 
    SupportsBytes, 
    SupportsComplex, 
    SupportsFloat, 
    SupportsIndex, 
    SupportsInt, 
    SupportsRound,
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


class Primitives:
    Annotated = Annotated
    Any = Any
    Callable = Callable
    ClassVar = ClassVar
    Concatenate = Concatenate
    Final = Final
    ForwardRef = ForwardRef
    Generic = Generic
    Literal = Literal
    Optional = Optional
    ParamSpec = ParamSpec
    Protocol = Protocol
    Tuple = Tuple
    Type = Type
    TypeVar = TypeVar
    TypeVarTuple = TypeVarTuple
    Union = Union
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
    Reversible      = Reversible
    SupportsAbs     = SupportsAbs
    SupportsBytes   = SupportsBytes
    SupportsComplex = SupportsComplex
    SupportsFloat   = SupportsFloat
    SupportsIndex   = SupportsIndex
    SupportsInt     = SupportsInt
    SupportsRound   = SupportsRound
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
        # Structural checks, a.k.a. protocols.
        'Reversible',
        'SupportsAbs',
        'SupportsBytes',
        'SupportsComplex',
        'SupportsFloat',
        'SupportsIndex',
        'SupportsInt',
        'SupportsRound'
    )

class AbstractBase:
    AbstractSet = AbstractSet
    ByteString = ByteString
    Container = Container
    ContextManager = ContextManager
    Hashable = Hashable
    ItemsView = ItemsView
    Iterable = Iterable
    Iterator = Iterator
    KeysView = KeysView
    Mapping = Mapping
    MappingView = MappingView
    MutableMapping = MutableMapping
    MutableSequence = MutableSequence
    MutableSet = MutableSet
    Sequence = Sequence
    Sized = Sized
    ValuesView = ValuesView
    Awaitable = Awaitable
    AsyncIterator = AsyncIterator
    AsyncIterable = AsyncIterable
    Coroutine = Coroutine
    Collection = Collection
    AsyncGenerator = AsyncGenerator
    AsyncContextManager = AsyncContextManager
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
    

ConcreteCollections = [
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
    'TextIO']

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



