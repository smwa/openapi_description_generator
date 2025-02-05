import dataclasses
from src.openapi_description_generator import License, Info, Description, singleton, Operation
from typing import Optional, List

singleton.info.license = License(name="MIT")
singleton.info.title = "My Test"
singleton.info.version = "1.0.0"



# Workspace

op = Operation(
  requestBody=None, # TODO
  responses=None, # TODO
)

# Workspace - End

@dataclasses.dataclass
class RequestExample():
  nomph: dict[str, list[str]]
  floof: Optional[int]
  bop: List[int]
  hrmm: bool

@dataclasses.dataclass
class ResponseSubclassExample():
  zedd: str
  alo: bool

@dataclasses.dataclass
class ResponseExample():
  kerf: bool
  murph: str
  suub: ResponseSubclassExample


singleton.path("/blogs/{blogId}/comments/{commentId}/files", "Blog comments notes!", ["The blog's ID", "The comment's ID"]).post = singleton.operation(
  summary="Create comment notes",
  tags=["creating", "notes"],
  cookieParameters=[('cookieName', 'cookieDescription', not not 'isRequired')],
  queryParameters=[('queryName', 'queryDesc')],
  headerParameters=[('headerName', 'headerDesc', False)],
  requestBody=RequestExample,
  responses={
    '200': singleton.response('my response for 200', [('header-name', 'my response header', False)], ResponseExample),
    '201': singleton.response('response File', responseBody='*/*')
  }
)

singleton.path("/test").post = singleton.operation(summary='upload file', tags=['creating'], requestBody='image/*')

print(singleton)
