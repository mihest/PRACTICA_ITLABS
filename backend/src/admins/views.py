import os
import shutil
import uuid
from markupsafe import Markup

from sqladmin import ModelView
from wtforms import FileField

from src.admins.utils import add_file, delete_file
from src.config import settings
from src.stand_bies.models import StandBiesModel
from src.types.models import TypeModel


class StandBiesAdmin(ModelView, model=StandBiesModel):
    name = "режим ожидания"
    name_plural = "Режим ожидания"
    icon = "fa fa-terminal"

    column_list = [
        "title",
        "media",
        "sequence"
    ]
    column_sortable_list = column_list
    column_editable_list = column_list
    column_searchable_list = [
        "title"
    ]
    column_default_sort = "sequence"
    column_details_list = column_list

    column_labels = {
        "title": "Название",
        "media": "Файл загрузки",
        "sequence": "Порядок отоброжения"
    }

    form_overrides = {
        "media": FileField
    }

    column_formatters = {
        "media": lambda model, _: Markup(
            f'<a href="{model.media}" target="_blank">{model.media.split("/")[-1]}</a>'
        )
    }

    async def on_model_change(self, data, model, is_created, request):
        file = data["media"]

        if file and hasattr(file, "filename"):
            file_path = await add_file(file, settings.stand_bies_dir)

            model.media = f"/media/stand_bies/{file_path}"
            data["media"] = f"/media/stand_bies/{file_path}"
        return model

    async def on_model_delete(self, model, request):
        await delete_file(model.media)

class TypeAdmin(ModelView, model=TypeModel):
    name = "тип"
    name_plural = 'Типы'
    icon = "fa fa-list"

    column_list = [
        "title",
        "description",
        "sequence",
        "image"
    ]
    column_sortable_list = column_list
    column_editable_list = column_list
    column_searchable_list = [
        "title"
    ]
    column_default_sort = "sequence"
    column_details_list = column_list
    form_columns = column_list

    column_labels = {
        "title": "Название",
        "image": "Изображение",
        "description": "Описание",
        "sequence": "Порядок отоброжения"
    }

    form_overrides = {
        "image": FileField
    }

    column_formatters = {
        "image": lambda model, _: Markup(
            f'<img src="{model.image}">'
        )
    }

    async def on_model_change(self, data, model, is_created, request):
        file = data["image"]

        if file and hasattr(file, "filename"):
            file_path = await add_file(file, settings.type_dir)

            model.image = f"/media/images/type/{file_path}"
            data["image"] = f"/media/images/type/{file_path}"
        return model

    async def on_model_delete(self, model, request):
        await delete_file(model.image)


