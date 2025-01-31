# -*- coding: utf-8 -*-

from typing import Any, Callable, NoReturn, TypeVar

from returns.generated.box import _box as box  # noqa: F401, WPS436

# Aliases:
_FirstType = TypeVar('_FirstType')
_SecondType = TypeVar('_SecondType')
_ThirdType = TypeVar('_ThirdType')


def identity(instance: _FirstType) -> _FirstType:
    """
    Function that returns its argument.

    .. code:: python

      >>> identity(1)
      1
      >>> identity([1, 2, 3])
      [1, 2, 3]

    Why do we even need this?
    Identity functions help us with the composition.

    Imagine, that you want to use :func:`returns.converters.coalesce_result`
    like so:

    .. code:: python

      from returns.result import Result
      from returns.converters import coalesce_result

      numbers: Result[int, float]
      # Now you want to fold `number` into `int` type:
      number: int = coalesce_result(identity, int)(numbers)
      # Done!

    See also:
        - https://en.wikipedia.org/wiki/Identity_function
        - https://stackoverflow.com/a/21506571/4842742

    """
    return instance


def compose(
    first: Callable[[_FirstType], _SecondType],
    second: Callable[[_SecondType], _ThirdType],
) -> Callable[[_FirstType], _ThirdType]:
    """
    Allows function composition.

    Works as: ``second . first`` or ``first() |> second()``.
    You can read it as "second after first".

    .. code:: python

      >>> compose(float, int)('123.5')
      123

    We can only compose functions with one argument and one return.
    Type checked.
    """
    return lambda argument: second(first(argument))


def tap(
    function: Callable[[_FirstType], Any],
) -> Callable[[_FirstType], _FirstType]:
    """
    Allows to apply some function and return an argument, instead of a result.

    Is usefull for side-effects like ``print()``, ``logger.log``, etc.

    .. code:: python

      >>> tap(print)(1)
      1
      1
      >>> tap(lambda _: 1)(2)
      2

    See also:
        - https://github.com/dry-python/returns/issues/145

    """
    def decorator(argument_to_return: _FirstType) -> _FirstType:
        function(argument_to_return)
        return argument_to_return
    return decorator


def raise_exception(exception: Exception) -> NoReturn:
    """
    Helper function to raise exceptions as a function.

    It might be required as a compatibility tool for existing APIs.
    That's how it can be used:

    .. code:: python

      >>> from returns.result import Failure, Result
      >>> # Some operation result:
      >>> user: Result[int, ValueError] = Failure(ValueError('boom'))
      >>> # Here we unwrap internal exception and raise it:
      >>> user.fix(raise_exception)
      Traceback (most recent call last):
        ...
      ValueError: boom

    See also:
        - https://github.com/dry-python/returns/issues/56

    """
    raise exception
