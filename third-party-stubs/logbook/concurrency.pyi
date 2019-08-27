# Stubs for logbook.concurrency (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from _thread import _local as thread_local, get_ident as thread_get_ident
from typing import Any, Optional

has_gevent: bool
use_gevent: bool

def enable_gevent() -> None: ...
def is_gevent_enabled(): ...

ThreadLock: Any
ThreadRLock: Any
thread_get_ident: Any
thread_local: Any

def thread_get_name(): ...

class GreenletRLock:
    def __init__(self) -> None: ...
    def acquire(self, blocking: int = ...): ...
    def release(self) -> None: ...
    __enter__: Any = ...
    def __exit__(self, t: Any, v: Any, tb: Any) -> None: ...
greenlet_get_ident = thread_get_ident
greenlet_local = thread_local

class GreenletRLock:
    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, t: Any, v: Any, tb: Any) -> None: ...

def new_fine_grained_lock(): ...

has_contextvars: bool
context_ident_counter: Any
context_ident: Any

def context_get_ident(): ...
def is_context_enabled(): ...

class ContextVar:
    name: Any = ...
    local: Any = ...
    def __init__(self, name: Any) -> None: ...
    def set(self, value: Any) -> None: ...
    def get(self, default: Optional[Any] = ...): ...
