"""unique user.email alembic fix

Revision ID: 6db25a930704
Revises: cd7256c0da90
Create Date: 2020-03-26 15:47:30.941105

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '6db25a930704'
down_revision = 'cd7256c0da90'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_index('ix_users_email', table_name='users')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.drop_constraint('users_email_uindex', 'users', type_='unique')


def downgrade():
    op.create_unique_constraint('users_email_uindex', 'users', ['email'])
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
