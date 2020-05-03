"""empty message

Revision ID: 76552697c74f
Revises: 9041a4b37b76
Create Date: 2020-05-03 09:28:07.381154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76552697c74f'
down_revision = '9041a4b37b76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    op.add_column('post', sa.Column('slug', sa.String(length=140), nullable=True))
    op.create_unique_constraint(None, 'post', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='unique')
    op.drop_column('post', 'slug')
    op.drop_table('post_tags')
    op.drop_table('tag')
    # ### end Alembic commands ###