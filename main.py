# Dependencies with yield

"""
FastAPI supports dependencies that do some extra steps after finishing.

To do this, use yield instead of return, and write the extra steps (code) after.
"""

# A database dependency with yield

"""
For example, you could use this to create a database session and close it after finishing.

Only the code prior to and including the yield statement is executed before creating a response:

async def get_db():
  db = DBSession()
  try:
    yield db
  finally:
    db.close()

The yielded value is what is injected into path operations and other dependencies

async def get_db():
  db = DBSession()
  try:
    yield db
  finally:
    db.close()

The code following the yield statement is executed after the response has been delivered:

async def get_db():
  db = DBSession()
  try:
    yield db
  finally:
    db.close()
"""

# A dependency with yield and try

"""
If you use a try block in a dependency with yield, you'll receive any exception that was thrown when using the dependency.
For examples, if some code at the some point in the middle, in another dependenct or in a path operation, made a database transaction rollback or create any other error, you will receive the exception in your dependency.

So, you can look that specific exception inside the dependency with except SomeException.

In the same way, you can use finally to make sure the exit steps are executed, no matter if there was an exception or not.

async def get_db():
  db = DBSession()
  try:
    yield db
  finally:
    db.close()
"""
