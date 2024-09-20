from typing import Optional

from fastapi import APIRouter, Query, Depends

from apps.babyname.name_util import check_name_api, get_name_api
from apps.vadmin.auth.utils.current import FullAdminAuth
from apps.vadmin.auth.utils.validation import Auth
from utils.response import SuccessResponse, ErrorResponse

app = APIRouter()


@app.get("/status", summary="查看名字")
async def read_status(param: str = Query(..., min_length=2, max_length=4), auth: Auth = Depends(FullAdminAuth())):
    return SuccessResponse(data=check_name_api(check_name=param))


@app.get("/names", summary="取名")
async def read_names(param: str = Query(..., min_length=1, max_length=2), gender: str = Query(...), source: Optional[int] = 1,
                     auth: Auth = Depends(FullAdminAuth())):
    if source < 0 or source > 7:
        return ErrorResponse("请选择0-7的参数")
    return SuccessResponse(data=get_name_api(name_source=source, last_name=param, gender=gender))
