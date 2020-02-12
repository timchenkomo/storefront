"""create user table

Revision ID: eb20c8b19b85
Revises: 
Create Date: 2020-02-07 17:10:55.786028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb20c8b19b85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String(250), nullable=False),
        sa.Column("email", sa.String(50), nullable=False, index=True),
        sa.Column("hashed_password", sa.String(100), nullable=False),
        sa.Column("disabled", sa.Boolean, nullable=False)
    )


def downgrade():
    op.drop_table("users")
