import asyncio
from sqlalchemy import text
from datetime import datetime, timezone
from app.database import SessionLocal

async def delete_old_events():
    '''
    This function runs every hour and deletes events older than today from the database.
    It uses the SQLAlchemy ORM to interact with the database.

        Inputs: None
        Outputs: None
    '''
    while True:
        # run the cleanup every hour (3600 seconds)
        await asyncio.sleep(3600)

        # get the running database session
        db = SessionLocal()
        try:
            # get the current date
            today = datetime.now(timezone.utc).date()

            # delete events older than today
            # note: The date format in the database is assumed to be 'YYYY-MM-DD'
            query = text("""
                DELETE FROM events
                WHERE TO_DATE(date, 'YYYY-MM-DD') + INTERVAL '1 day' < CURRENT_DATE
            """)
            # execute the query
            db.execute(query)
            # commit the changes
            db.commit()

        # handle any exceptions that occur during the database operation
        except Exception as e:
            print(e)
        finally:
            db.close()
