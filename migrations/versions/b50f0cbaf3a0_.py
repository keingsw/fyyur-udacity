"""Add columns to `artists`.

Revision ID: b50f0cbaf3a0
Revises: e21ff9c05a1c
Create Date: 2020-02-06 12:52:39.966306

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b50f0cbaf3a0'
down_revision = 'e21ff9c05a1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist_genres', sa.Column('artist_id', sa.Integer(), nullable=False),
                    sa.Column('genre_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['artist_id'],
                        ['artists.id'],
                    ), sa.ForeignKeyConstraint(
                        ['genre_id'],
                        ['genres.id'],
                    ), sa.PrimaryKeyConstraint('artist_id', 'genre_id'))
    op.add_column('artists', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('artists', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_column('artists', 'genres')
    op.add_column('shows', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'shows', 'artists', ['artist_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shows', type_='foreignkey')
    op.drop_column('shows', 'artist_id')
    op.add_column('artists',
                  sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('artists', 'website')
    op.drop_column('artists', 'seeking_venue')
    op.drop_column('artists', 'seeking_description')
    op.drop_table('artist_genres')
    # ### end Alembic commands ###
