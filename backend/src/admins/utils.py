import os
import uuid
import shutil

from passlib.context import CryptContext

from src.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def is_valid_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

async def add_file(file, path):
    os.makedirs(path, exist_ok=True)
    original_name = os.path.splitext(file.filename)[0]
    extension = os.path.splitext(file.filename)[1]
    random_str = uuid.uuid4().hex[:20]
    filename = f"{original_name}-{random_str}{extension}"
    save_path = os.path.join(path, filename)

    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return filename


async def delete_file(url):
    media_path = url.lstrip('/')
    file_path = settings.base_dir / media_path
    if file_path.exists():
        try:
            file_path.unlink()
        except Exception as e:
            print(f"Ошибка при удалении файла: {e}")
    else:
        print("Файл не найден")