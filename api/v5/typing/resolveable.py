from __future__ import annotations
from abc import abstractclassmethod
from typing import TypeVar, Type, Generic, Optional
from exceptions import exception_handler


T = TypeVar("T", bound="Resolveable")


class Resolveable(Generic[T]):
    """
    Markup class
    """
    
    @exception_handler
    @abstractclassmethod
    def resolve_from_text(T, text: str, recovered_text: Optional[str] = None) -> T:
        raise NotImplementedError
