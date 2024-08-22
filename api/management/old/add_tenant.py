import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.account import Account, Tenant, TenantAccountJoin, TenantAccountRole


def create_tenant(name, db_url):
    """Creates a new tenant."""

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    tenant = Tenant(name=name)
    session.add(tenant)
    session.commit()

    print(f"Success: Created tenant {tenant.id} with name {name}")
    return tenant.id  # Return the ID of the created tenant

def add_tenant_to_account(account_id, tenant_id, role, db_url):
    """Adds a tenant to an existing account."""

    # Connect to the database
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the existing account and tenant
    account = session.query(Account).filter_by(id=account_id).first()
    tenant = session.query(Tenant).filter_by(id=tenant_id).first()

    if not account:
        print(f"Error: Account with id {account_id} not found.")
        return

    if not tenant:
        print(f"Error: Tenant with id {tenant_id} not found.")
        return

    # Create the TenantAccountJoin record
    tenant_account_join = TenantAccountJoin(
        tenant_id=tenant_id,
        account_id=account_id,
        role=role
    )
    session.add(tenant_account_join)
    session.commit()

    print(f"Success: Added tenant {tenant_id} to account {account_id} with role {role}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add tenant to an existing account")
    parser.add_argument("account_id", help="ID of the account")
    parser.add_argument("--tenant_id", help="ID of the tenant (if exists)")
    parser.add_argument("--tenant_name", help="Name of the new tenant (if creating)")
    parser.add_argument("role", choices=[role.value for role in TenantAccountRole], help="Role of the account in the tenant")
    parser.add_argument("--db_url", help="Database connection URL", default="postgresql://postgres:difyai123456@docker-db-1/dify")

    args = parser.parse_args()

    if args.tenant_id:
        tenant_id = args.tenant_id  # Use existing tenant ID
    elif args.tenant_name:
        tenant_id = create_tenant(args.tenant_name, args.db_url)  # Create a new tenant
    else:
        print("Error: Either tenant_id or tenant_name must be provided.")
        exit(1)

    add_tenant_to_account(args.account_id, tenant_id, args.role, args.db_url)