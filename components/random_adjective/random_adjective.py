
import os
import random
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class RandomAdjectiveInputDict(BaseModel):
    adjective_list: List[str]
    name: str


class RandomAdjectiveOutputDict(BaseModel):
    adjective: str


class RandomAdjective(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: RandomAdjectiveInputDict
    ) -> RandomAdjectiveOutputDict:
        first_letter = args.name[0].lower()
        adjective_list = [adj for adj in args.adjective_list if adj[0].lower() == first_letter]

        if not adjective_list:
            raise ValueError(f"No adjectives found starting with the letter {first_letter}")

        seed = sum(ord(c) for c in args.name)
        random.seed(seed)
        selected_adjective = random.choice(adjective_list)

        return RandomAdjectiveOutputDict(adjective=selected_adjective)


random_adjective_app = FastAPI()


@random_adjective_app.post("/transform/")
async def transform(
    args: RandomAdjectiveInputDict,
) -> RandomAdjectiveOutputDict:
    random_adjective = RandomAdjective()
    return random_adjective.transform(args)
