"""Add the command column to job_tasks table

Revision ID: 7f60f9d6bb1c
Revises: 2620b7f7926a
Create Date: 2021-10-23 14:24:17.971687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f60f9d6bb1c'
down_revision = '2620b7f7926a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_tasks', sa.Column('command', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job_tasks', 'command')
    # ### end Alembic commands ###