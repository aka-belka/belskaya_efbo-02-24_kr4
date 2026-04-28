from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class CustomExceptionModel(BaseModel):
    status_code: int
    er_message: str
    er_details: str

class CustomExceptionA(HTTPException):
    def __init__(self, detail: str, status_code: int = 404, message: str = "Item not found"):
        super().__init__(status_code=status_code, detail=detail)
        self.message = message

class CustomExceptionB(HTTPException):
    def __init__(self, detail: str, status_code: int = 400,message: str = "Validation error"):
        super().__init__(status_code=status_code, detail=detail)
        self.message = message

@app.exception_handler(CustomExceptionA)
async def custom_exception_a_handler(request: Request, exc: CustomExceptionA)-> JSONResponse:
    error = jsonable_encoder(CustomExceptionModel(status_code=exc.status_code,
            er_message=exc.message, er_details=exc.detail))
    return JSONResponse(status_code=exc.status_code, content=error)

@app.exception_handler(CustomExceptionB)
async def custom_exception_b_handler(request: Request, exc: CustomExceptionB)-> JSONResponse:
    error = jsonable_encoder(CustomExceptionModel(status_code=exc.status_code,
            er_message=exc.message, er_details=exc.detail))
    return JSONResponse(status_code=exc.status_code, content=error)

@app.get("/resource/{resource_id}")
async def get_resource(resource_id: int):
    if resource_id == 0:
        raise CustomExceptionB(detail="Invalid resource ID (0 not allowed)", message="ID must be positive")
    if resource_id == 999:
        raise CustomExceptionA(detail="Resource 999 not found", message="The requested resource does not exist")
    return {"resource_id": resource_id, "data": "some data"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id < 0:
        raise CustomExceptionB(detail="Item ID cannot be negative", message="ID must be >= 0" )
    if item_id == 42:
        raise CustomExceptionA(detail="Item 42 does not exist", message="Item with this ID was not found")
    return {"item_id": item_id, "name": f"Item {item_id}"}