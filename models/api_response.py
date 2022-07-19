from dataclasses import dataclass


@dataclass
class ApiResponse:
    code: int
    type: str
    message: str
