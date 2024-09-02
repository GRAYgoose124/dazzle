from pydantic import Field, validator
from typing import Any, Dict, Optional, List

from dizzy.daemon.abstract_protocol import BaseRequest, BaseResponse, Status, BaseProtocol


class Request(BaseRequest):
    entity: Optional[str] = None
    workflow: Optional[str] = None
    task: Optional[str] = None
    args: Dict[str, Any] = Field(default_factory=dict)
    options: Dict[str, Any] = Field(default_factory=dict)

    def __str__(self):
        return f"Request(id={self.id}, workflow={self.workflow}, task={self.task}, options={self.options})"


class Response(BaseResponse):
    requester: Optional[str] = None
    request: Optional[Request] = None
    errors: Dict[str, List[str]] = Field(default_factory=dict)
    info: Dict[str, List[str]] = Field(default_factory=dict)
    result: Any = None

    @classmethod
    def from_request(
        cls,
        requester: str,
        request: Request,
        status: Status = "pending",
    ):
        return cls(
            requester=str(requester),
            request=request,
            id=request.id,
            ctx=request.ctx,
            status=status
        )
    

DizzyProtocol = BaseProtocol[Request, Response]
Protocol = DizzyProtocol(Request=Request, Response=Response)