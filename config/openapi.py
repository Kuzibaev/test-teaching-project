import typing

from drf_spectacular.openapi import AutoSchema


class CustomAutoSchema(AutoSchema):

    def get_tags(self) -> typing.List[str]:
        tokenized_path = self._tokenize_path()
        return list(map(lambda s: str.capitalize(s), tokenized_path[:1]))
