"""create table users

Revision ID: ea7c70f66014
Revises: 17d4c8e53a63
Create Date: 2022-03-09 16:50:07.708751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea7c70f66014'
down_revision = '17d4c8e53a63'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
    sa.Column('email', sa.String(), unique=True, nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', 
        sa.TIMESTAMP(timezone=True), 
            server_default=sa.text('now()'),
            nullable=False))
    pass


def downgrade():
    op.drop_table('users')
    pass
