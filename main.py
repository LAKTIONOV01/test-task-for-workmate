from fastapi import APIRouter
from typing import Annotated
from fastapi.security import HTTPBasicCredentials, HTTPBasic

router = APIRouter(prefix='/demo-auth', tags=['Demo Auth'])

@router.get('/basic-auth/')
def demo_basic_auth_credentials(
        credentials: Annotated[]
)