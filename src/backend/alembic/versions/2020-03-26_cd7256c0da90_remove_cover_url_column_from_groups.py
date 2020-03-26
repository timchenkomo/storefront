"""Remove cover_url column from groups

Revision ID: cd7256c0da90
Revises: 9ff101fcddfa
Create Date: 2020-03-26 14:44:12.536194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd7256c0da90'
down_revision = '9ff101fcddfa'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('groups', 'cover_url')


def downgrade():
    op.add_column(
        'groups',
        sa.Column(
            'cover_url',
            sa.VARCHAR(length=1024),
            autoincrement=False, nullable=False)
    )
