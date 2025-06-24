from markupsafe import Markup

from sqladmin import ModelView
from wtforms import FileField

from src.admins.utils import add_file, delete_file
from src.config import settings
from src.stand_bies.models import StandBiesModel
from src.sub_types.models import SubTypeModel
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


class SubTypeAdmin(ModelView, model=SubTypeModel):
    name = "подтип"
    name_plural = 'Подтипы'
    icon = "fa fa-list"

    column_list = [
        "title",
        "type.title",
        "sequence",
        "image",
        "open_info"
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
        "type.title": "Тип",
        "image": "Изображение",
        "open_info": "Медиа",
        "sequence": "Порядок отоброжения"
    }

    form_overrides = {
        "image": FileField
    }

    def format_info_modal(self, model: dict):
        document_blocks = ""

        for i, doc in enumerate(model["documents"], start=1):
            video_list = ""
            for j, video in enumerate(doc["videos"], start=1):
                video_list += f'<li><a href="{video["video"]}">{video["video"].split("/")[-1]}</a></li>'

            document_blocks += f"""
                <li>
                    Название: {doc['title']}<br>
                    Файл: {f'<a href="{doc['media']}" target="_blank">{doc['media'].split("/")[-1]}</a>' if doc['media'] else 'документ не загружен'}<br>
                    Порядок: {doc['sequence']}<br>
                    Видео:
                    <ul>{video_list or 'не загружены'}</ul>
                </li>
            """

        html = f"""
        <a href="#" onclick="document.getElementById('modal_{model['id']}').style.display='block'; document.getElementById('modal_overlay_{model['id']}').style.display='block'">
            <i class="fa fa-file-alt fa-2x"></i>
        </a>

        <div id="modal_overlay_{model['id']}" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background-color:rgba(0,0,0,0.5); z-index:999;">
        </div>

        <div id="modal_{model['id']}" style="display:none; position:fixed; top:10%; left:10%; width:80%; background:white; z-index:9999; padding:20px; border:2px solid black; box-shadow: 0 0 10px rgba(0,0,0,0.5); overflow:auto; max-height:80%;">
            <div style="display: flex; padding: 5px; border-bottom: #000000 1px solid; justify-content: space-between; margin-bottom: 10px">
                <h3>Медиа:</h3>
                <button onclick="document.getElementById('modal_{model['id']}').style.display='none'; document.getElementById('modal_overlay_{model['id']}').style.display='none'" style="border: none; background: none; color: red;">X</button>    
            </div>
            <ol style="margin-bottom: 1em; padding-left: 1em; display: flex; flex-flow: column; gap: 10px">
                {document_blocks}
            </ol>
            
        </div>
        """

        return Markup(html)

    column_formatters = {
        "open_info": lambda m, _: SubTypeAdmin.format_info_modal(None, {
            "id": m.id,
            "title": m.title,
            "image": m.image,
            "sequence": m.sequence,
            "documents": [
                {
                    "id": d.id,
                    "media": d.media,
                    "title": d.title,
                    "sequence": d.sequence,
                    "videos": sorted(
                        [{"id": v.id, "video": v.video, "sequence": v.sequence} for v in d.videos],
                        key=lambda x: x["sequence"]
                    )
                } for d in sorted(m.documents, key=lambda d: d.sequence)
            ]
        }),
        "image": lambda m, _: Markup(
            f'<img src="{m.image}">'
        ),
        "type.title": lambda m, _: Markup(
            f'<a href="/admin/type-model/details/{m.type.id}">{m.type.title}</a>'
        ),
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



