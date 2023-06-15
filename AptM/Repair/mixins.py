from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import AccessMixin

from Repair.models import Status
from users.models import Role

User = get_user_model()


class RepairMixin:
    """Миксин для фильтрации заявок по роли пользователя"""

    @staticmethod
    def _get_repair_filter(user: User) -> dict:
        """Возвращаем фильтр для заявки для роли пользователя"""
        repair_filter = {
            Role.CUSTOMER: {
                'user': user
            },
            Role.MASTER: {
                'status__in': [
                    Status.PROGRESS,
                    Status.VERIFICATION,
                ]
            },

        }
        return repair_filter.get(user.role)