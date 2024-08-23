import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.account import Account, Tenant, TenantAccountJoin


def list_accounts(db_url):
    """Lists account names, IDs, emails, and associated workspaces with IDs and roles."""

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    accounts = session.query(Account).all()

    for account in accounts:
        print(f"ID: {account.id}, Name: {account.name}, Email: {account.email}")

        tenant_account_joins = session.query(TenantAccountJoin).filter_by(account_id=account.id).all()

        for join in tenant_account_joins:
            tenant = session.query(Tenant).filter_by(id=join.tenant_id).first()
            print(f"  Workspace ID: {tenant.id}, Workspace: {tenant.name}, Role: {join.role}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List account names, IDs, emails, and associated workspaces with IDs and roles")
    parser.add_argument("--db_url", help="Database connection URL", default="postgresql://postgres:difyai123456@docker-db-1/dify")
    args = parser.parse_args()

    list_accounts(args.db_url)
