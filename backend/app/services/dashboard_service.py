from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def stats(db):
        return DashboardRepository.get_stats(db)

    @staticmethod
    def recent(db):
        return DashboardRepository.recent_incidents(db)

    @staticmethod
    def high_risk(db):
        return DashboardRepository.high_risk(db)

    @staticmethod
    def open_cases(db):
        return DashboardRepository.open_cases(db)

    @staticmethod
    def analytics(db):
        return DashboardRepository.analytics(db)