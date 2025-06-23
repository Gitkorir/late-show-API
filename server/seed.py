from server.app import create_app
from server.extensions import db
from server.models.guest import Guest

app = create_app()

with app.app_context():
    # Drop and recreate tables (optional but helpful during dev)
    db.drop_all()
    db.create_all()

    # Sample guest data
    guests = [
        Guest(name="Trevor Noah",occupation="Driver"),
        Guest(name="Bill Gates", occupation='Billionare'),
        Guest(name="Zendaya",occupation='Youtuber'),
        Guest(name="Elon Musk",occupation='Certified genius'),
        Guest(name="Simu Liu", occupation='Nuclear Guru'),
    ]

    db.session.add_all(guests)
    db.session.commit()

    print("✅ Database seeded with sample guest data.")