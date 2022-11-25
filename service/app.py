import pandas as pd
from fastapi import FastAPI
from typing import Union

from service.models import PDInfo, CSVRow, EmptyResponse


app = FastAPI(
    title="Data Access",
    version="0.1.0"
)


@app.get("/pandas_version")
def get_pandas_version() -> PDInfo:
    return PDInfo(version=pd.__version__)


@app.get("/get_row/{user_id}")
def get_user(user_id: int) -> Union[CSVRow, EmptyResponse]:
    df = pd.read_csv("data/data.csv", index_col="user_id")
    if user_id in df.index:
        row = df.loc[user_id]
        if type(row) == pd.DataFrame:
            row = row.iloc[0]
        row = {"user_id": user_id, **row.to_dict()}
        return CSVRow(**row)
    else:
        return EmptyResponse()
