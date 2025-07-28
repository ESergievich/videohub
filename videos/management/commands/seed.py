from django.apps.registry import apps
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from videos.models import Video
from django.utils import timezone
from faker import Faker
import random

fake = Faker()
User = get_user_model()


def clear_database():
    for model in apps.get_models():
        model.objects.all().delete()

class Command(BaseCommand):
    help = "Заполняет тестовыми данными"

    def add_arguments(self, parser):
        parser.add_argument('--cleardb', action='store_true', help='Очистить базу данных перед заполнением')
        parser.add_argument('--users', type=int, default=10, help='Количество пользователей')
        parser.add_argument('--videos', type=int, default=10, help='Количество видео')

    def handle(self, *args, **options):
        if options['cleardb']:
            clear_database()

        self.stdout.write(self.style.NOTICE("Создаём пользователей..."))

        user_count = options['users']
        users = []
        for i in range(user_count):
            users.append(
                User(
                    username=f"user_{i}",
                    email=fake.email(),
                    password=make_password("barter_1234"),
                )
            )
        User.objects.bulk_create(users, ignore_conflicts=True)
        users = list(User.objects.all())  # получаем id созданных пользователей

        self.stdout.write(self.style.NOTICE("Создаём видео..."))

        video_count = options['videos']
        videos = []
        for i in range(video_count):
            owner = random.choice(users)
            videos.append(
                Video(
                    owner=owner,
                    is_published=True,
                    name=fake.sentence(nb_words=3),
                    total_likes=0,
                    created_at=timezone.now()
                )
            )
            # Каждые 10к - сохраняем, чтобы не держать в памяти
            if len(videos) >= 10_000:
                Video.objects.bulk_create(videos)
                videos.clear()
                self.stdout.write(self.style.SUCCESS(f"Создано {i + 1} видео"))

        if videos:
            Video.objects.bulk_create(videos)

        self.stdout.write(self.style.SUCCESS("Генерация завершена!"))
