from sqlalchemy.exc import IntegrityError
from app.database import SessionLocal
from app.models import Link

# Create a database session
db = SessionLocal()

# Try to insert two links with the same code to test the unique constraint
try:
    # Clear existing data first so the test is clean
    db.query(Link).delete()
    db.commit()

    # Add the first link
    link1 = Link(code="test1", long_url="http://google.com")
    db.add(link1)
    db.commit()
    print("Step 1: First link added successfully.")

    # Try to add the second link with the same 'code'
    link2 = Link(code="test1", long_url="http://bing.com")
    db.add(link2)
    db.commit() # This should fail and raise an IntegrityError
    
    print("Bug still exists: Duplicate code allowed.")

except IntegrityError:
    db.rollback()
    print("Fix verified: IntegrityError caught! Duplicate code successfully rejected by the database.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    db.close()