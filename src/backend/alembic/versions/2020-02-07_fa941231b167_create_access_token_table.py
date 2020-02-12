"""create access token table

Revision ID: fa941231b167
Revises: e365a7ec9717
Create Date: 2020-02-07 18:19:37.669155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa941231b167'
down_revision = 'e365a7ec9717'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "access_tokens",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), index=True),
        sa.Column("token", sa.String(32), index=True, unique=True),
        sa.Column("expiry", sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table("access_tokens")
