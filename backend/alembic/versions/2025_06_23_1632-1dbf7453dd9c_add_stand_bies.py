"""add stand_bies

Revision ID: 1dbf7453dd9c
Revises: 35cd26d0fc7e
Create Date: 2025-06-23 16:32:37.311614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '1dbf7453dd9c'
down_revision: Union[str, Sequence[str], None] = '35cd26d0fc7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'stand_bies',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('media', sa.String(), nullable=False),
        sa.Column('sequence', sa.Integer(), nullable=False),
        sa.CheckConstraint('sequence > 0', name='sequence_positive'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('media'),
        sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stand_bies')
    # ### end Alembic commands ###
