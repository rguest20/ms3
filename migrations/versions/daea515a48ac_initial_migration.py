"""initial migration

Revision ID: daea515a48ac
Revises: 
Create Date: 2020-12-16 13:36:41.978746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daea515a48ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inbox',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outbox',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('read_yn', sa.Boolean(), nullable=True),
    sa.Column('sender_deleted', sa.Boolean(), nullable=True),
    sa.Column('reciever_deleted', sa.Boolean(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('message', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['inbox.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['outbox.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('date_joined', sa.Date(), nullable=True),
    sa.Column('inbox_id', sa.Integer(), nullable=True),
    sa.Column('outbox_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['inbox_id'], ['inbox.id'], ),
    sa.ForeignKeyConstraint(['outbox_id'], ['outbox.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('poster_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('budget', sa.String(length=10), nullable=True),
    sa.Column('hourlypay', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['poster_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_table('messages')
    op.drop_table('roles')
    op.drop_table('outbox')
    op.drop_table('inbox')
    # ### end Alembic commands ###