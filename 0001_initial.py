from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    op.create_table('depots',
        sa.Column('id', pg.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('lat', sa.Numeric(9,6), nullable=False),
        sa.Column('lon', sa.Numeric(9,6), nullable=False),
    )
    op.create_table('service_types',
        sa.Column('id', pg.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('default_service_sec', sa.Integer(), nullable=False, server_default='60'),
        sa.Column('constraints_json', pg.JSON(), nullable=True),
    )
    op.create_table('customers',
        sa.Column('id', pg.UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('lat', sa.Numeric(9,6), nullable=False),
        sa.Column('lon', sa.Numeric(9,6), nullable=False),
        sa.Column('service_type_id', pg.UUID(as_uuid=True), nullable=True),
    )
    op.create_table('stops',
        sa.Column('id', pg.UUID(as_uuid=True), primary_key=True),
        sa.Column('route_date', sa.Date(), nullable=False),
        sa.Column('customer_id', pg.UUID(as_uuid=True), nullable=True),
        sa.Column('service_type_id', pg.UUID(as_uuid=True), nullable=True),
        sa.Column('time_window', pg.TSTZRANGE(), nullable=True),
        sa.Column('service_time_sec', sa.Integer(), nullable=True),
        sa.Column('priority', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('is_disposal', sa.Boolean(), nullable=False, server_default=sa.text('false')),
        sa.Column('disposal_site_id', pg.UUID(as_uuid=True), nullable=True),
    )
    op.create_table('routes',
        sa.Column('id', pg.UUID(as_uuid=True), primary_key=True),
        sa.Column('route_date', sa.Date(), nullable=False),
        sa.Column('total_drive_sec', sa.Integer(), nullable=True),
        sa.Column('total_distance_m', sa.Integer(), nullable=True),
    )
    op.create_table('route_stops',
        sa.Column('route_id', pg.UUID(as_uuid=True), nullable=False),
        sa.Column('stop_id', pg.UUID(as_uuid=True), nullable=False),
        sa.Column('seq', sa.Integer(), nullable=False),
        sa.Column('eta_ts', pg.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('leg_drive_sec', sa.Integer(), nullable=True),
        sa.Column('leg_distance_m', sa.Integer(), nullable=True),
        sa.Column('cum_drive_sec', sa.Integer(), nullable=True),
        sa.Column('cum_distance_m', sa.Integer(), nullable=True),
    )

def downgrade() -> None:
    op.drop_table('route_stops')
    op.drop_table('routes')
    op.drop_table('stops')
    op.drop_table('customers')
    op.drop_table('service_types')
    op.drop_table('depots')
