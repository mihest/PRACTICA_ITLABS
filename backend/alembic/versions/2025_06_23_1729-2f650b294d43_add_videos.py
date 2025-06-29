"""add videos

Revision ID: 2f650b294d43
Revises: bda5778a11dd
Create Date: 2025-06-23 17:29:52.919577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2f650b294d43'
down_revision: Union[str, Sequence[str], None] = 'bda5778a11dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'videos',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('video', sa.String(), nullable=False),
        sa.Column('sequence', sa.Integer(), nullable=False),
        sa.Column('document_id', sa.UUID(), nullable=False),
        sa.CheckConstraint('sequence > 0', name='sequence_positive'),
        sa.ForeignKeyConstraint(['document_id'], ['documents.id'], onupdate='CASCADE', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('video')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videos')
    # ### end Alembic commands ###
