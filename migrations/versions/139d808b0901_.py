"""empty message

Revision ID: 139d808b0901
Revises: 8579ff6d1f07
Create Date: 2024-12-01 18:20:10.311026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '139d808b0901'
down_revision = '8579ff6d1f07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.alter_column('completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    # ### end Alembic commands ###
