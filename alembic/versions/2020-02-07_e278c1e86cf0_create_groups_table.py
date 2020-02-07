"""create groups table

Revision ID: e278c1e86cf0
Revises: 710794468fbe
Create Date: 2020-02-07 17:25:34.692416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e278c1e86cf0'
down_revision = '710794468fbe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "groups",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("authors.id"), index=True),
        sa.Column("slug", sa.String(32), nullable=False, index=True, unique=True),
        sa.Column("title", sa.String(128), nullable=False),
        sa.Column("description", sa.UnicodeText(), nullable=False),
        sa.Column("cover_url", sa.String(1024), nullable=False)
    )


def downgrade():
    op.drop_table("groups")
