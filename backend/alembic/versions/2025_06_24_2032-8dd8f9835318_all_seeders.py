"""all_seeders

Revision ID: 8dd8f9835318
Revises: a79729cc0698
Create Date: 2025-06-24 20:32:28.410781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8dd8f9835318'
down_revision: Union[str, Sequence[str], None] = 'a79729cc0698'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
               INSERT INTO types (id, title, image, description, sequence)
               VALUES ('a1b2c3d4-e5f6-7890-abcd-ef1234567890', 'Персонал', '/media/images/type/per-tip.png',
                       'Сотрудники предприятия, их подбор, обучение, развитие и мотивация', 1),
                      ('b2c3d4e5-f6a7-8901-bcde-f23456789012', 'Гражданская оборона',
                       '/media/images/type/gra-tip.png', 'Комплекс мер по защите населения и территорий от чрезвычайных ситуаций', 2);
               """)

    op.execute("""
               INSERT INTO sub_types (id, title, image, sequence, type_id)
               VALUES ('c3d4e5f6-a789-0123-cdef-123456789012', 'Гражданская оборона',
                       '/media/images/sub_type/sub_type-1.png', 1, 'b2c3d4e5-f6a7-8901-bcde-f23456789012'),
                      ('d4e5f6a7-8901-2345-def0-234567890123', 'Мотивация',
                       '/media/images/sub_type/sub_type-2.png', 2, 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'),
                      ('e5f6a789-0123-4567-ef01-345678901234', 'Обучение, адаптация, развитие и карьера',
                       '/media/images/sub_type/sub_type-3.png', 3, 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'),
                      ('f6a78901-2345-6789-f012-456789012345', 'Правила внутреннего трудового распорядка',
                       '/media/images/sub_type/sub_type-4.png', 1, 'a1b2c3d4-e5f6-7890-abcd-ef1234567890')
               """)

    op.execute("""
               INSERT INTO documents (id, title, media, sequence, sub_type_id)
               VALUES ('b7890123-4567-8901-1234-678901234567', 'Положение C7.4.PLC.13',
                       '/media/documents/1.pdf', 1, 'c3d4e5f6-a789-0123-cdef-123456789012'),
                      ('c8901234-5678-9012-2345-789012345678', 'Положение о материальном стимулирование на достижение целей Компании за год',
                       '/media/documents/2.pdf', 1, 'd4e5f6a7-8901-2345-def0-234567890123'),
                      ('3f5b9dae-efc5-4c54-b569-96d0895bbf02', 'Положение о проведении Конкурса Лучший работник месяца',
                       '/media/documents/3.pdf', 2, 'd4e5f6a7-8901-2345-def0-234567890123'),
                      ('58a31c6c-96ae-4af2-8c32-e1b5a1f7a0fc', 'Положение об оплате труда и материальном стимулировании работнииков',
                       '/media/documents/4.pdf', 3, 'd4e5f6a7-8901-2345-def0-234567890123'),
                      ('33f0fbfe-5b7b-4af4-b4d9-952e8ba8eb3e', 'Процедура о награждениях и корпоративных праздниках ООО НевРСС.',
                       '/media/documents/5.pdf', 4, 'd4e5f6a7-8901-2345-def0-234567890123'),
                      ('e5afa4c3-e868-47e9-84f2-58718e1a692e', 'Инструкция по организации обучения персонала',
                       '/media/documents/6.pdf', 1, 'e5f6a789-0123-4567-ef01-345678901234'),
                      ('a76a6cad-9229-4ab1-83bb-ecd12fead0be', 'Правила внутреннего трудового распорядка',
                       '/media/documents/7.pdf', 1, 'f6a78901-2345-6789-f012-456789012345');
               """)

    op.execute("""
               INSERT INTO stand_bies (id, title, media, sequence)
               VALUES ('abddff25-c1e8-4136-8974-951fcf61fed2', '1', '/media/stand_bies/kolobov-138d8a8c40c44cbb8f5f.mp4', 1);
               """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
               DELETE
               FROM stand_bies
               WHERE id IN (
                            'abddff25-c1e8-4136-8974-951fcf61fed2',
                   );
               """)

    op.execute("""
               DELETE
               FROM documents
               WHERE id IN (
                            'b7890123-4567-8901-1234-678901234567',
                            'c8901234-5678-9012-2345-789012345678',
                            '3f5b9dae-efc5-4c54-b569-96d0895bbf02',
                            '58a31c6c-96ae-4af2-8c32-e1b5a1f7a0fc',
                            '33f0fbfe-5b7b-4af4-b4d9-952e8ba8eb3e',
                            'e5afa4c3-e868-47e9-84f2-58718e1a692e',
                            'a76a6cad-9229-4ab1-83bb-ecd12fead0be'
                   );
               """)

    op.execute("""
               DELETE
               FROM sub_types
               WHERE id IN (
                            'c3d4e5f6-a789-0123-cdef-123456789012',
                            'd4e5f6a7-8901-2345-def0-234567890123',
                            'e5f6a789-0123-4567-ef01-345678901234',
                            'f6a78901-2345-6789-f012-456789012345',
                   );
               """)

    op.execute("""
               DELETE
               FROM types
               WHERE id IN (
                            'a1b2c3d4-e5f6-7890-abcd-ef1234567890',
                            'b2c3d4e5-f6a7-8901-bcde-f23456789012'
                   );
               """)

