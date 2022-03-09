"""add content column

Revision ID: 17d4c8e53a63
Revises: c10827e9afaf
Create Date: 2022-03-09 16:29:09.161239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17d4c8e53a63'
down_revision = 'c10827e9afaf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
