"""add foreign key to post table

Revision ID: e025677e2bd4
Revises: ea7c70f66014
Create Date: 2022-03-09 17:28:43.597922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e025677e2bd4'
down_revision = 'ea7c70f66014'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', column_name='owner_id')
    pass
