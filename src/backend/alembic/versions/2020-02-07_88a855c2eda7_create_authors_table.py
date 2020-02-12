"""create authors table

Revision ID: 88a855c2eda7
Revises: eb20c8b19b85
Create Date: 2020-02-07 17:17:34.570046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88a855c2eda7'
down_revision = 'eb20c8b19b85'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String(128), primary_key=False)
    )


def downgrade():
    op.drop_table("authors")
