"""empty message

Revision ID: f6c5ee9d6c83
Revises: 
Create Date: 2023-02-22 12:07:07.193887

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6c5ee9d6c83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('phone_number', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hotel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area', sa.Integer(), nullable=True),
    sa.Column('number_of_beds', sa.Integer(), nullable=True),
    sa.Column('price_for_a_night', sa.Integer(), nullable=True),
    sa.Column('busy', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('phone_number', sa.String(length=128), nullable=True),
    sa.Column('rented', sa.String(length=10), nullable=True),
    sa.Column('on_days', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['hotel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('hotel')
    op.drop_table('clients')
    # ### end Alembic commands ###
