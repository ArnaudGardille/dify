from app import app, db  # Import your Flask app
from models.account import Tenant
from services.account_service import TenantService, AccountService

user_email = "arnaud.gardille@vigie.ai"
user_password = "Dechiktorren92"

def print_attributes(obj):
    """Prints the attributes and their values of any object."""
    for attribute in dir(obj):
        # Skip built-in attributes
        if not attribute.startswith('__'):
            value = getattr(obj, attribute)
            print(f"{attribute}: {value}")
            
with app.app_context():
    
    db.session.delete(tenant)
    db.session.commit()
        
    if False:
        # Start a new session
        session = db.session

        # Query for the tenant you are interested in
        tenants = session.query(Tenant).all()
        print("\nWorkspaces: \n")
        for tenant in tenants:
            print_attributes(tenant)
            print("\n")

        tenant = session.query(Tenant).first()
        
        session.commit()
        
    
    # Authenticate the main user
    try:
        account = AccountService.authenticate(email=user_email, password=user_password)
    except Exception as e:
        print(f"Authentication failed: {e}")
        exit(1)

    # Create a new tenant
    try:
        tenant_name = f"{account.name}'s Workspace"
        tenant = TenantService.create_tenant(name=tenant_name)
        print(f"Tenant '{tenant_name}' created successfully.")
    except Exception as e:
        print(f"Failed to create tenant: {e}")
        exit(1)

    # Add the authenticated user to the newly created tenant as an owner
    try:
        TenantService.create_tenant_member(tenant=tenant, account=account, role='owner')
        account.current_tenant = tenant
        db.session.commit()
        print(f"User '{account.email}' added to tenant '{tenant_name}' as an owner.")
    except Exception as e:
        print(f"Failed to add user to tenant: {e}")
