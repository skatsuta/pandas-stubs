from collections.abc import (
    Callable,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    Sequence,
)
from typing import (
    ClassVar,
    Generic,
    Literal,
    TypeVar,
    overload,
)

import numpy as np
from pandas import (
    DataFrame,
    MultiIndex,
    Series,
)
from pandas.core.arrays import ExtensionArray
from pandas.core.base import (
    IndexOpsMixin,
    PandasObject,
)
from pandas.core.indexes.numeric import NumericIndex
from pandas.core.strings import StringMethods
from typing_extensions import (
    Never,
    Self,
    TypeAlias,
)

from pandas._typing import (
    S1,
    T1,
    Dtype,
    DtypeArg,
    DtypeObj,
    FillnaOptions,
    HashableT,
    Label,
    Level,
    NaPosition,
    Scalar,
    T,
    np_ndarray_anyint,
    np_ndarray_bool,
    np_ndarray_int64,
    npt,
    type_t,
)

class InvalidIndexError(Exception): ...

_str = str

# Type variable used in method arguments
_ArgT = TypeVar("_ArgT")

class _IndexGetitemMixin(Generic[S1]):
    @overload
    def __getitem__(
        self,
        idx: slice
        | np_ndarray_anyint
        | Sequence[int]
        | Index
        | Series[bool]
        | Sequence[bool]
        | np_ndarray_bool,
    ) -> Self: ...
    @overload
    def __getitem__(self, idx: int) -> S1: ...

class Index(IndexOpsMixin, PandasObject, Generic[T]):
    __hash__: ClassVar[None]  # type: ignore[assignment]
    @overload
    def __new__(
        cls,
        data: Iterable[T],
        dtype: Literal["int", "uint", "float", "complex"]
        | type_t[int]
        | type_t[float]
        | type_t[complex]
        | type_t[np.number],
        copy: bool = ...,
        name=...,
        tupleize_cols: bool = ...,
        **kwargs,
    ) -> NumericIndex: ...
    @overload
    def __new__(
        cls,
        data: Iterable[T] = ...,
        dtype=...,
        copy: bool = ...,
        name=...,
        tupleize_cols: bool = ...,
        **kwargs,
    ) -> Index[T]: ...
    @property
    def str(self) -> StringMethods[Index[list[T]], MultiIndex]: ...
    @property
    def asi8(self) -> np_ndarray_int64: ...
    def is_(self, other) -> bool: ...
    def __len__(self) -> int: ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __array_wrap__(self, result, context=...): ...
    @property
    def dtype(self) -> DtypeObj: ...
    def ravel(self, order: _str = ...): ...
    def view(self, cls=...): ...
    def astype(self, dtype: DtypeArg, copy: bool = ...) -> Index: ...
    def take(
        self, indices, axis: int = ..., allow_fill: bool = ..., fill_value=..., **kwargs
    ): ...
    def repeat(self, repeats, axis=...): ...
    def copy(self, name=..., deep: bool = ...) -> Self: ...
    def __copy__(self, **kwargs): ...
    def __deepcopy__(self, memo=...): ...
    def format(
        self, name: bool = ..., formatter: Callable | None = ..., na_rep: _str = ...
    ) -> list[_str]: ...
    def tolist(self) -> list[T]: ...
    def to_list(self) -> list[T]: ...
    def to_native_types(self, slicer=..., **kwargs): ...
    def to_flat_index(self): ...
    def to_series(self, index=..., name=...) -> Series: ...
    def to_frame(self, index: bool = ..., name=...) -> DataFrame: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, value) -> None: ...
    @property
    def names(self) -> list[_str]: ...
    @names.setter
    def names(self, names: list[_str]): ...
    def set_names(self, names, *, level=..., inplace: bool = ...): ...
    def rename(self, name, inplace: bool = ...): ...
    @property
    def nlevels(self) -> int: ...
    def sortlevel(self, level=..., ascending: bool = ..., sort_remaining=...): ...
    def get_level_values(self, level: int | _str) -> Self: ...
    def droplevel(self, level: Level | list[Level] = ...): ...
    @property
    def is_monotonic_increasing(self) -> bool: ...
    @property
    def is_monotonic_decreasing(self) -> bool: ...
    @property
    def is_unique(self) -> bool: ...
    @property
    def has_duplicates(self) -> bool: ...
    def is_boolean(self) -> bool: ...
    def is_integer(self) -> bool: ...
    def is_floating(self) -> bool: ...
    def is_numeric(self) -> bool: ...
    def is_object(self) -> bool: ...
    def is_categorical(self) -> bool: ...
    def is_interval(self) -> bool: ...
    def is_mixed(self) -> bool: ...
    def holds_integer(self): ...
    @property
    def inferred_type(self): ...
    def __reduce__(self): ...
    @property
    def hasnans(self) -> bool: ...
    def isna(self): ...
    isnull = ...
    def notna(self): ...
    notnull = ...
    def fillna(self, value=..., downcast=...): ...
    def dropna(self, how: Literal["any", "all"] = ...) -> Self: ...
    def unique(self, level=...) -> Self: ...
    def drop_duplicates(
        self, *, keep: NaPosition | Literal[False] = ...
    ) -> IndexOpsMixin: ...
    def duplicated(
        self, keep: Literal["first", "last", False] = ...
    ) -> np_ndarray_bool: ...
    _Numeric: TypeAlias = int | float | complex
    @overload
    def __truediv__(self: Index[int], other: _Numeric | Index) -> Index[float]: ...
    @overload
    def __truediv__(self, other: _Numeric | Index) -> Index: ...
    @overload
    def __rtruediv__(self: Index[int], other: _Numeric | Index) -> Index[float]: ...
    @overload
    def __rtruediv__(self, other: _Numeric | Index) -> Index: ...
    def __and__(self, other: Never) -> Never: ...
    def __rand__(self, other: Never) -> Never: ...
    def __or__(self, other: Never) -> Never: ...
    def __ror__(self, other: Never) -> Never: ...
    def __xor__(self, other: Never) -> Never: ...
    def __rxor__(self, other: Never) -> Never: ...
    def __neg__(self) -> Self: ...
    def __nonzero__(self) -> None: ...
    __bool__ = ...
    def union(self, other: list[HashableT] | Index, sort=...) -> Index: ...
    def intersection(self, other: list[T1] | Index, sort: bool = ...) -> Index: ...
    def difference(self, other: list | Index, sort: bool | None = None) -> Index: ...
    def symmetric_difference(
        self, other: list[T1] | Index, result_name=..., sort=...
    ) -> Index: ...
    def get_loc(
        self,
        key: Label,
        method: FillnaOptions | Literal["nearest"] | None = ...,
        tolerance=...,
    ): ...
    def get_indexer(self, target, method=..., limit=..., tolerance=...): ...
    def reindex(self, target, method=..., level=..., limit=..., tolerance=...): ...
    def join(
        self,
        other,
        *,
        how: _str = ...,
        level=...,
        return_indexers: bool = ...,
        sort: bool = ...,
    ): ...
    @property
    def values(self) -> np.ndarray: ...
    @property
    def array(self) -> ExtensionArray: ...
    def memory_usage(self, deep: bool = ...): ...
    def where(self, cond, other=...): ...
    def is_type_compatible(self, kind) -> bool: ...
    def __contains__(self, key) -> bool: ...
    def __setitem__(self, key, value) -> None: ...
    @overload
    def __getitem__(
        self,
        idx: slice
        | np_ndarray_anyint
        | Sequence[int]
        | Index
        | Series[bool]
        | Sequence[bool]
        | np_ndarray_bool,
    ) -> Index[T]: ...
    @overload
    def __getitem__(self, idx: int | tuple[np_ndarray_anyint, ...]) -> Scalar: ...
    def append(self, other: Index[_ArgT]) -> Index[T | _ArgT]: ...
    def putmask(self, mask, value): ...
    def equals(self, other) -> bool: ...
    def identical(self, other) -> bool: ...
    def asof(self, label): ...
    def asof_locs(self, where, mask): ...
    def sort_values(self, return_indexer: bool = ..., ascending: bool = ...): ...
    def sort(self, *args, **kwargs) -> None: ...
    def shift(self, periods: int = ..., freq=...) -> None: ...
    def argsort(self, *args, **kwargs): ...
    def get_value(self, series, key): ...
    def set_value(self, arr, key, value) -> None: ...
    def get_indexer_non_unique(self, target): ...
    def get_indexer_for(self, target, **kwargs): ...
    def groupby(self, values) -> dict[Hashable, np.ndarray]: ...
    @overload
    def map(
        self,
        mapper: Callable[[T], _ArgT] | Mapping[T, _ArgT],
        na_action: Literal["ignore"] | None = ...,
    ) -> Index[_ArgT]: ...
    @overload
    def map(
        self, mapper: Series[S1], na_action: Literal["ignore"] | None = ...
    ) -> Index[S1]: ...
    def isin(self, values, level=...) -> np_ndarray_bool: ...
    def slice_indexer(self, start=..., end=..., step=...): ...
    def get_slice_bound(self, label, side): ...
    def slice_locs(self, start=..., end=..., step=...): ...
    def insert(self, loc: int, item: _ArgT) -> Index[T | _ArgT]: ...
    def delete(
        self,
        loc: int | Sequence[int] | npt.NDArray[np.integer] | Series[int] | Index[int],
    ) -> Self: ...
    def drop(
        self, labels: T | Iterable[T], errors: Literal["ignore", "raise"] = ...
    ) -> Self: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    # Extra methods from old stubs
    def __eq__(self, other: object) -> np_ndarray_bool: ...  # type: ignore[override]
    def __iter__(self) -> Iterator[T]: ...
    def __ne__(self, other: object) -> np_ndarray_bool: ...  # type: ignore[override]
    def __le__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]
    def __ge__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]
    def __lt__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]
    def __gt__(self, other: Index | Scalar) -> np_ndarray_bool: ...  # type: ignore[override]

def ensure_index_from_sequences(
    sequences: Sequence[Sequence[Dtype]], names: list[str] = ...
) -> Index: ...
def ensure_index(index_like: Sequence | Index, copy: bool = ...) -> Index: ...
def maybe_extract_name(name, obj, cls) -> Label: ...
