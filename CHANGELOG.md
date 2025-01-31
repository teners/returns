# Version history

We follow Semantic Versions since the `1.0.0` release.
Versions before `1.0.0` are `0Ver`-based:
incremental in minor, bugfixes only are patches.
See (0Ver)[https://0ver.org/].


## 0.11.0

### Features

- **Breaking**: now `pipe()` does not require argument to be the first value,
  instead it is required to use: `pipe(f1, f2, f3, f4)(value)`
- **Breaking**: dropped everything from `returns/__init__.py`,
  because we now have quite a lot of stuff
- **Breaking**: dropped support of zero argument functions for `Nothing.fix`
- **Breaking**: dropped support of zero argument functions for `Nothing.rescue`
- `Maybe` now has `.failure()` to match the same API as `Result`
- Adds `identity` function
- Adds `tap` function
- Now `pipe` allows to pipe 8 steps
- Adds `coalesce_result` and `coalesce_maybe` coverters

### Bugfixes

- Fixes that code inside `.fix` and `.rescue` of `Maybe` might be called twice

### Misc

- Now all methods have doctests
- Updates docs about `Success` and `_Success`, `Failure` and `_Failure`
- Updates docs about `@pipeline`
- Typechecks async functions and decorators inside `typesafety/` tests


## 0.10.0

### Features

- **Breaking**: `python>=3.7,<=3.7.2` are not supported anymore,
  because of a bug inside `typing` module
- **Breaking**: Now `bind` does not change the type of an error
- **Breaking**: Now `rescue` does not change the type of a value
- **Breaking**: Renames `map_failure` to `alt`
- Adds `box()` function with the ability
  to box function for direct container composition like:
  `a -> Container[b]` to `Container[a] -> Container[b]`
- Adds `IO.lift()` function to lift `a -> a` to `IO[a] -> IO[a]`
- Adds `pipe()` function to `pipeline.py`
- Adds `__hash__()` magic methods to all containers

### Bugfixes

- Changes `Any` to `NoReturn` in `Success` and `Failure`
- Now all type parameters in `Result`, `Maybe`, and `IO` are covariant

### Misc

- Massive docs rewrite
- Updates `mypy` version
- Updates `wemake-python-styleguide` and introduces `nitpick`
- Updates `pytest-plugin-mypy`, all tests now use `yml`


## 0.9.0

### Features

- Provides a bunch of primitive interfaces to write your own containers
- Adds `.map_failure()` method
- Adds `join()` function to join nested containers

### Bugfixes

- Fixes type of `Maybe.fix` and `Maybe.rescue` to work with both `lambda: 1` and `lambda _: 1`

### Misc

- Improves `README`


## 0.8.0

### Features

- Reintroduces the `Maybe` container, typed!
- Introduces converters from one type to another
- Adds `mypy` plugin to type decorators
- Complete rewrite of `Result` types
- Partial API change, now `Success` and `Failure` are not types, but functions
- New internal types introduced: `FixableContainer` and `ValueUnwrapContainer`

### Bugfixes

- Fixes issue when you could return `IO` container from `Result.bind`
- Fixes `@pipeline` return type

### Misc

- Reapplied all types to `.py` files
- Improved docs about `IO` and `Container` concept
- Adds docs about container composition
- Moves from `Alpha` to `Beta`


## 0.7.0

### Features

- Adds `IO` marker
- Adds `unsafe` module with unsafe functions
- Changes how functions are located inside the project

### Bugfixes

- Fixes container type in `@pipeline`
- Now `is_successful` is public
- Now `raise_exception` is public

### Misc

- Changes how `str()` function works for container types
- Total rename to "container" in the source code


## Version 0.6.0

### Features

- `safe` and `pipeline` now supports `asyncio`
- `is_successful` now returns `Literal` types if possible


## Version 0.5.0

### Features

- Adds `compose` helper function
- Adds public API to `import returns`
- Adds `raise_exception` helper function
- Adds full traceback to `.unwrap()`


### Misc

- Updates multiple dev-dependencies, including `mypy`
- Now search in the docs is working again
- Relicenses this project to `BSD`
- Fixes copyright notice in the docs


## Version 0.4.0 aka Goodbye, containers!

### Features

- Moves all types to `.pyi` files
- Renames all classes according to new naming pattern
- **HUGE** improvement of types
- Renames `fmap` to `map`
- Renames `do_notation` to `pipeline`, moves it to `functions.py`
- Renames `ebind` to `rescue`
- Renames `efmap` to `fix`
- Renames `container` to `Container`
- Removes `Maybe` container, since typing does not have `NonNullable` type


## Version 0.3.1

### Bugfixes

- Adds `py.typed` file to be `PEP561` compatible


## Version 0.3.0, Renamed to `returns`

The project is renamed to `returns` and moved to `dry-python` org.

### Features

- Adds `.pyi` files for all modules,
  to enable `mypy` support for 3rd party users


## Version 0.2.0

### Features

- Adds `Maybe` container
- Adds immutability and `__slots__` to all containers
- Adds methods to work with failures
- Adds `safe` decorator to convert exceptions to `Result` container
- Adds `is_successful()` function to detect if your result is a success
- Adds `failure()` method to unwrap values from failed containers

### Bugfixes

- Changes the type of `.bind` method for `Success` container
- Changes how equality works, so now `Failure(1) != Success(1)`
- Changes how new instances created on unused methods

### Misc

- Improves docs


## Version 0.1.1

### Bugfixes

- Changes how `PyPI` renders package's page

### Misc

- Improves `README` with new badges and installation steps


## Version 0.1.0

Initial release. Featuring only `Result` and `do_notation`.
