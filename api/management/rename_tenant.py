import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.account import Tenant


def rename_tenant(tenant_id, new_name, db_url):
    """Renames a tenant."""

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    tenant = session.query(Tenant).filter_by(id=tenant_id).first()

    if not tenant:
        print(f"Error: Tenant with ID {tenant_id} not found.")
        return

    old_name = tenant.name
    tenant.name = new_name
    session.commit()

    print(f"Success: Renamed tenant '{old_name}' (ID: {tenant_id}) to '{new_name}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename a tenant")
    parser.add_argument("tenant_id", help="ID of the tenant to rename")
    parser.add_argument("new_name", help="New name for the tenant")
    parser.add_argument("--db_url", help="Database connection URL", default="postgresql://postgres:difyai123456@docker-db-1/dify")
    args = parser.parse_args()

    rename_tenant(args.tenant_id, args.new_name, args.db_url)
