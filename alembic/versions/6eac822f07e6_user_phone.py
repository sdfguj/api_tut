"""user-phone

Revision ID: 6eac822f07e6
Revises: e9d7cdefeefd
Create Date: 2022-03-09 20:51:29.877045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6eac822f07e6'
down_revision = 'e9d7cdefeefd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.drop_constraint('posts_users_fk', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'], ondelete='cascade')
    op.drop_column('posts', 'owner_id')
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('posts_users_fk', 'posts', 'users', ['owner_id'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'user_id')
    op.create_table('products',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('inventory', sa.INTEGER(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###