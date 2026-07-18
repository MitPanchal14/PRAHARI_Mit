from app.core.database import Base, engine

from app.models.incident import IncidentEvent

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")