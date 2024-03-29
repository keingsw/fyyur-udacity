"""empty message

Revision ID: eae9380da29d
Revises: 1973cab5f729
Create Date: 2020-02-07 12:09:27.839865

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'eae9380da29d'
down_revision = '1973cab5f729'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'city', existing_type=sa.VARCHAR(length=120), nullable=False)
    op.alter_column('artists', 'name', existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column('artists', 'phone', existing_type=sa.VARCHAR(length=120), nullable=False)
    op.alter_column('artists', 'seeking_venue', existing_type=sa.BOOLEAN(), nullable=False)
    op.alter_column('artists', 'state', existing_type=sa.VARCHAR(length=120), nullable=False)
    op.alter_column('venues', 'address', existing_type=sa.VARCHAR(length=120), nullable=False)
    op.alter_column('venues', 'city', existing_type=sa.VARCHAR(length=120), nullable=False)
    op.alter_column('venues', 'name', existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column('venues', 'phone', existing_type=sa.VARCHAR(length=120), nullable=False)
    op.alter_column('venues', 'seeking_talent', existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column('venues', 'state', existing_type=sa.VARCHAR(length=120), nullable=False)

    op.execute('UPDATE venues set seeking_talent = False WHERE seeking_talent IS NULL;')
    op.alter_column('venues', 'seeking_talent', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'state', existing_type=sa.VARCHAR(length=120), nullable=True)
    op.alter_column('venues', 'seeking_talent', existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column('venues', 'phone', existing_type=sa.VARCHAR(length=120), nullable=True)
    op.alter_column('venues', 'name', existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column('venues', 'city', existing_type=sa.VARCHAR(length=120), nullable=True)
    op.alter_column('venues', 'address', existing_type=sa.VARCHAR(length=120), nullable=True)
    op.alter_column('artists', 'state', existing_type=sa.VARCHAR(length=120), nullable=True)
    op.alter_column('artists', 'seeking_venue', existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column('artists', 'phone', existing_type=sa.VARCHAR(length=120), nullable=True)
    op.alter_column('artists', 'name', existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column('artists', 'city', existing_type=sa.VARCHAR(length=120), nullable=True)
    # ### end Alembic commands ###
