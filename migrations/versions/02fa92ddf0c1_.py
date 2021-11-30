"""empty message

Revision ID: 02fa92ddf0c1
Revises: d31fa3bc2222
Create Date: 2021-11-22 20:28:35.639462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02fa92ddf0c1'
down_revision = 'd31fa3bc2222'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hashes', sa.Column('plaintext2', sa.Unicode(length=256), nullable=True))
    op.create_index(op.f('ix_hashes_plaintext2'), 'hashes', ['plaintext2'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_hashes_plaintext2'), table_name='hashes')
    op.drop_column('hashes', 'plaintext2')
    # ### end Alembic commands ###