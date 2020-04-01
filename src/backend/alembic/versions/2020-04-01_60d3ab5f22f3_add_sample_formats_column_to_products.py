"""add sample_formats column to Products

Revision ID: 60d3ab5f22f3
Revises: 5f0b4b595d44
Create Date: 2020-04-01 13:41:06.092501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60d3ab5f22f3'
down_revision = '5f0b4b595d44'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('products', sa.Column('sample_formats', sa.String(length=32), nullable=True))


def downgrade():
    op.drop_column('products', 'sample_formats')
