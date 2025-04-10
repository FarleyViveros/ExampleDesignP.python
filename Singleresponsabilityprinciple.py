class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user: User):
        print(f"Guardando usuario {user.name} con email {user.email} en la base de datos.")

class EmailService:
    def send_email(self, user: User, message: str):
        print(f"Enviando email a {user.email}: {message}")

class UserRegistrationService:
    def __init__(self, user_repository: UserRepository, email_service: EmailService):
        self.user_repository = user_repository
        self.email_service = email_service

    def register_user(self, name: str, email: str):
        user = User(name, email)

        self.user_repository.save(user)

        self.email_service.send_email(user, "¡Bienvenido a nuestra plataforma!")

if __name__ == "__main__":
    user_repository = UserRepository()
    email_service = EmailService()
    registration_service = UserRegistrationService(user_repository, email_service)

    registration_service.register_user("Juan Pérez", "juan.perez@example.com")