
import os
from typing import List, Dict

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class FetchAdjectivesInputDict(BaseModel):
    pass


class FetchAdjectivesOutputDict(BaseModel):
    adjective_list: Dict[str, List[str]]


class FetchAdjectives(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)
        self.alphabet: str = yaml_data["parameters"]["alphabet"]
        self.min_adjectives_per_letter: int = yaml_data["parameters"]["min_adjectives_per_letter"]

    def fetch_adjectives(self, letter: str) -> List[str]:
        # Retrieve positive or neutral adjectives from an external API or a predefined dataset
        fetched_adjectives = []  # Replace this with a real API call or dataset
        return fetched_adjectives

    def transform(
        self, args: FetchAdjectivesInputDict
    ) -> FetchAdjectivesOutputDict:
        adjectives_dict = {}

        for letter in self.alphabet:
            adjectives = self.fetch_adjectives(letter)
            filtered_adjectives = [adj for adj in adjectives if adj.startswith(letter)]
            while len(filtered_adjectives) < self.min_adjectives_per_letter:
                adjectives = self.fetch_adjectives(letter)
                filtered_adjectives.extend(
                    [adj for adj in adjectives if adj.startswith(letter)]
                )

            adjectives_dict[letter] = filtered_adjectives[: self.min_adjectives_per_letter]

        return FetchAdjectivesOutputDict(adjective_list=adjectives_dict)


load_dotenv()
fetch_adjectives_app = FastAPI()


@fetch_adjectives_app.post("/transform/")
async def transform(
    args: FetchAdjectivesInputDict,
) -> FetchAdjectivesOutputDict:
    fetch_adjectives = FetchAdjectives()
    return fetch_adjectives.transform(args)
