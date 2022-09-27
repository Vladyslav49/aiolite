# sqlite3
class Warning(Exception):
    pass


class Error(Exception):
    pass


class DatabaseError(Error):
    pass


class DataError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class InterfaceError(Error):
    pass


class InternalError(DatabaseError):
    pass


class NotSupportedError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


# transaction
class TransactionError(Error):
    pass


# pools
class PoolError(Error):
    pass


class PoolAcquireError(PoolError):
    pass


class PoolReleaseError(PoolError):
    pass


class PoolCloseError(PoolError):
    pass
