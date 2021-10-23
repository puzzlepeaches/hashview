"""empty message

Revision ID: 08224f240668
Revises: a671bad25f89
Create Date: 2021-10-22 22:16:42.926068

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '08224f240668'
down_revision = 'a671bad25f89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hashes', sa.Column('ciphertext_new', mysql.TEXT(), nullable=True))
    op.drop_column('hashes', 'ciphertext_new')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hashes', sa.Column('ciphertext_new', mysql.TEXT(), nullable=True))
    # ### end Alembic commands ###