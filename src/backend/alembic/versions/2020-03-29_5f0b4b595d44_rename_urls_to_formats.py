"""rename urls to formats

Revision ID: 5f0b4b595d44
Revises: 6db25a930704
Create Date: 2020-03-29 17:48:09.578999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f0b4b595d44'
down_revision = '6db25a930704'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('products', sa.Column('formats', sa.String(length=32), nullable=True))
    op.drop_column('products', 'urls')


def downgrade():
    op.add_column('products', sa.Column('urls', sa.VARCHAR(length=1024), autoincrement=False, nullable=True))
    op.drop_column('products', 'formats')
