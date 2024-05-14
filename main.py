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
