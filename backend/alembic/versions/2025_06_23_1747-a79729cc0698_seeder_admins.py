"""seeder admins

Revision ID: a79729cc0698
Revises: 8fcad086d66a
Create Date: 2025-06-23 17:47:25.657174

"""
import uuid
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

from src.admins.utils import get_password_hash

# revision identifiers, used by Alembic.
revision: str = 'a79729cc0698'
down_revision: Union[str, Sequence[str], None] = '8fcad086d66a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()
    session = Session(bind=bind)

    session.execute(
        sa.text(f"""
            INSERT INTO admins (id, username, hashed_password)
            VALUES ('{uuid.uuid4()}', 'admin', '{get_password_hash('foo')}')
        """)
    )

    session.commit()


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    session = Session(bind=bind)

    session.execute(
        sa.text("""
                DELETE FROM admins WHERE username='admin'
            """)
    )

    session.commit()
