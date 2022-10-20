from typing import Generic, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class OkResponseSchemas(GenericModel, Generic[DataT]):
    status: str
    data: DataT
