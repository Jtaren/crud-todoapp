"""empty message

Revision ID: 8579ff6d1f07
Revises: 3dbcae205ecc
Create Date: 2024-12-01 11:53:24.219558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8579ff6d1f07'
down_revision = '3dbcae205ecc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('list_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'todolists', ['list_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('list_id')

    op.drop_table('todolists')
    # ### end Alembic commands ###
