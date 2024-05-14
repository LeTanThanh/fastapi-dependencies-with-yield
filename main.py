from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Path
from fastapi import Depends

from typing import Annotated

app = FastAPI()

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

# Dependencies with yield and HTTPException

"""
You saw that you can use dependencies with yield and have try blocks that catch exceptions.

The same way, you could raise an HTTPException or similar in the exit code, after the yield.
"""

data = {
  "plumbus": {
    "description": "Freshly pickled plumbus",
    "owner": "Morty"
  },
  "portal-gun": {
    "description": "Gun to create portals",
    "owner": "Rick"
  }
}

class OwnerException(Exception):
  pass

def get_username():
  try:
    yield "Rick"
  except OwnerException as exception:
    raise HTTPException(
      status_code = status.HTTP_400_BAD_REQUEST,
      detail = f"Owner error: {exception}"
    )

@app.get("/items/{id}")
async def read_item(id: Annotated[str, Path()], username: Annotated[str, Depends(get_username)]):
  if id not in data:
    raise HTTPException(
      status_code = status.HTTP_401_UNAUTHORIZED,
      detail = "Item not found"
    )

  item = data[id]
  if item["owner"] != username:
    raise OwnerException(username)

  return item
