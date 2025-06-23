import os
import shutil
import uuid
from markupsafe import Markup

from sqladmin import ModelView
from wtforms import FileField

from src.config import settings
from src.stand_bies.models import StandBiesModel

class StandBiesAdmin(ModelView, model=StandBiesModel):

    name = "Режим ожидания"
    name_plural = "Режим ожидания"
    icon = "fa fa-user"

    column_list = [
        "title",
        "media",
        "sequence"
    ]
    column_sortable_list = column_list
    column_editable_list = [
        "title",
        "media",
        "sequence"
    ]
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
            os.makedirs(settings.stand_bies_dir, exist_ok=True)

            original_name = os.path.splitext(file.filename)[0]
            extension = os.path.splitext(file.filename)[1]
            random_str = uuid.uuid4().hex[:20]
            filename = f"{original_name}-{random_str}{extension}"
            save_path = os.path.join(settings.stand_bies_dir, filename)

            with open(save_path, "wb") as f:
                shutil.copyfileobj(file.file, f)

            model.media = f"/media/stand_bies/{filename}"
            data["media"] = f"/media/stand_bies/{filename}"
        return model

    async def on_model_delete(self, model, request):
        media_path = model.media.lstrip('/')
        file_path = settings.base_dir / media_path
        if file_path.exists():
            try:
                file_path.unlink()
            except Exception as e:
                print(f"Ошибка при удалении файла: {e}")
        else:
            print("Файл не найден")