"""empty message

Revision ID: 955f3777c159
Revises: 889abea60f0e
Create Date: 2023-04-28 22:41:41.229315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955f3777c159'
down_revision = '889abea60f0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('list_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('list_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###