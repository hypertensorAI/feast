# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ValueType(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Enum(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> ValueType.Enum: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[ValueType.Enum]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, ValueType.Enum]]: ...
        INVALID = typing___cast(ValueType.Enum, 0)
        BYTES = typing___cast(ValueType.Enum, 1)
        STRING = typing___cast(ValueType.Enum, 2)
        INT32 = typing___cast(ValueType.Enum, 3)
        INT64 = typing___cast(ValueType.Enum, 4)
        DOUBLE = typing___cast(ValueType.Enum, 5)
        FLOAT = typing___cast(ValueType.Enum, 6)
        BOOL = typing___cast(ValueType.Enum, 7)
        BYTES_LIST = typing___cast(ValueType.Enum, 11)
        STRING_LIST = typing___cast(ValueType.Enum, 12)
        INT32_LIST = typing___cast(ValueType.Enum, 13)
        INT64_LIST = typing___cast(ValueType.Enum, 14)
        DOUBLE_LIST = typing___cast(ValueType.Enum, 15)
        FLOAT_LIST = typing___cast(ValueType.Enum, 16)
        BOOL_LIST = typing___cast(ValueType.Enum, 17)
    INVALID = typing___cast(ValueType.Enum, 0)
    BYTES = typing___cast(ValueType.Enum, 1)
    STRING = typing___cast(ValueType.Enum, 2)
    INT32 = typing___cast(ValueType.Enum, 3)
    INT64 = typing___cast(ValueType.Enum, 4)
    DOUBLE = typing___cast(ValueType.Enum, 5)
    FLOAT = typing___cast(ValueType.Enum, 6)
    BOOL = typing___cast(ValueType.Enum, 7)
    BYTES_LIST = typing___cast(ValueType.Enum, 11)
    STRING_LIST = typing___cast(ValueType.Enum, 12)
    INT32_LIST = typing___cast(ValueType.Enum, 13)
    INT64_LIST = typing___cast(ValueType.Enum, 14)
    DOUBLE_LIST = typing___cast(ValueType.Enum, 15)
    FLOAT_LIST = typing___cast(ValueType.Enum, 16)
    BOOL_LIST = typing___cast(ValueType.Enum, 17)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ValueType: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class Value(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    bytes_val = ... # type: bytes
    string_val = ... # type: typing___Text
    int32_val = ... # type: int
    int64_val = ... # type: int
    double_val = ... # type: float
    float_val = ... # type: float
    bool_val = ... # type: bool

    @property
    def bytes_list_val(self) -> BytesList: ...

    @property
    def string_list_val(self) -> StringList: ...

    @property
    def int32_list_val(self) -> Int32List: ...

    @property
    def int64_list_val(self) -> Int64List: ...

    @property
    def double_list_val(self) -> DoubleList: ...

    @property
    def float_list_val(self) -> FloatList: ...

    @property
    def bool_list_val(self) -> BoolList: ...

    def __init__(self,
        *,
        bytes_val : typing___Optional[bytes] = None,
        string_val : typing___Optional[typing___Text] = None,
        int32_val : typing___Optional[int] = None,
        int64_val : typing___Optional[int] = None,
        double_val : typing___Optional[float] = None,
        float_val : typing___Optional[float] = None,
        bool_val : typing___Optional[bool] = None,
        bytes_list_val : typing___Optional[BytesList] = None,
        string_list_val : typing___Optional[StringList] = None,
        int32_list_val : typing___Optional[Int32List] = None,
        int64_list_val : typing___Optional[Int64List] = None,
        double_list_val : typing___Optional[DoubleList] = None,
        float_list_val : typing___Optional[FloatList] = None,
        bool_list_val : typing___Optional[BoolList] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Value: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"bool_list_val",u"bool_val",u"bytes_list_val",u"bytes_val",u"double_list_val",u"double_val",u"float_list_val",u"float_val",u"int32_list_val",u"int32_val",u"int64_list_val",u"int64_val",u"string_list_val",u"string_val",u"val"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"bool_list_val",u"bool_val",u"bytes_list_val",u"bytes_val",u"double_list_val",u"double_val",u"float_list_val",u"float_val",u"int32_list_val",u"int32_val",u"int64_list_val",u"int64_val",u"string_list_val",u"string_val",u"val"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"bool_list_val",b"bool_list_val",u"bool_val",b"bool_val",u"bytes_list_val",b"bytes_list_val",u"bytes_val",b"bytes_val",u"double_list_val",b"double_list_val",u"double_val",b"double_val",u"float_list_val",b"float_list_val",u"float_val",b"float_val",u"int32_list_val",b"int32_list_val",u"int32_val",b"int32_val",u"int64_list_val",b"int64_list_val",u"int64_val",b"int64_val",u"string_list_val",b"string_list_val",u"string_val",b"string_val",u"val",b"val"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"bool_list_val",b"bool_list_val",u"bool_val",b"bool_val",u"bytes_list_val",b"bytes_list_val",u"bytes_val",b"bytes_val",u"double_list_val",b"double_list_val",u"double_val",b"double_val",u"float_list_val",b"float_list_val",u"float_val",b"float_val",u"int32_list_val",b"int32_list_val",u"int32_val",b"int32_val",u"int64_list_val",b"int64_list_val",u"int64_val",b"int64_val",u"string_list_val",b"string_list_val",u"string_val",b"string_val",u"val",b"val"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"val",b"val"]) -> typing_extensions___Literal["bytes_val","string_val","int32_val","int64_val","double_val","float_val","bool_val","bytes_list_val","string_list_val","int32_list_val","int64_list_val","double_list_val","float_list_val","bool_list_val"]: ...

class BytesList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bytes]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[bytes]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BytesList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"val"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...

class StringList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> StringList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"val"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...

class Int32List(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Int32List: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"val"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...

class Int64List(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[int]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[int]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Int64List: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"val"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...

class DoubleList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[float]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[float]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DoubleList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"val"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...

class FloatList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[float]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[float]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FloatList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"val"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...

class BoolList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    val = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[bool]

    def __init__(self,
        *,
        val : typing___Optional[typing___Iterable[bool]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BoolList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"val"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"val",b"val"]) -> None: ...
