
from ..repositories.user_repository import UserRepository
from ..services.user_services import UserService


def users_service():
    return UserService(UserRepository)