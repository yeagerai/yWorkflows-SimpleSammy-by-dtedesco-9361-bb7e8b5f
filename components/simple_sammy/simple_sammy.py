
from typing import Any
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow

class AdjectiveOutput(BaseModel):
    adjective: str

class NameCombinationOutput(BaseModel):
    combined_name: str

class NameInput(BaseModel):
    name: str

class SimpleSammy(AbstractWorkflow):

    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: NameInput, callbacks: Any
    ) -> typing.Tuple[AdjectiveOutput, NameCombinationOutput]:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        adjective = results_dict[0].adjective
        combined_name = results_dict[1].combined_name
        out_adjective = AdjectiveOutput(adjective=adjective)
        out_name_combination = NameCombinationOutput(combined_name=combined_name)
        return out_adjective, out_name_combination

load_dotenv()
simple_sammy_app = FastAPI()

@simple_sammy_app.post("/transform/")
async def transform(
    args: NameInput,
) -> typing.Tuple[AdjectiveOutput, NameCombinationOutput]:
    simple_sammy = SimpleSammy()
    return await simple_sammy.transform(args, callbacks=None)
