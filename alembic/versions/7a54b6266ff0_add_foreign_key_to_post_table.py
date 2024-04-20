"""add foreign-key to post table

Revision ID: 7a54b6266ff0
Revises: b5f64a4e29cf
Create Date: 2024-04-20 18:14:53.684817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a54b6266ff0'
down_revision: Union[str, None] = 'b5f64a4e29cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('ownder_id', sa.INTEGER(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['ownder_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
