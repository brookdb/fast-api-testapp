"""add content to post table

Revision ID: b1f24f47a6c5
Revises: d744590f8e18
Create Date: 2024-04-20 18:03:51.501994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b1f24f47a6c5'
down_revision: Union[str, None] = 'd744590f8e18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
