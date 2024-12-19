from typing import Any
from django.core.management import BaseCommand
from shop.models import Category,Item,Tag, Image,ItemManager
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count,Avg,Sum, Min,Max,F, DecimalField, ExpressionWrapper
from django.apps import apps
from faker import Faker
import time




faker = Faker()
print(faker.word())


class Command(BaseCommand):
    def handle(self, *args, **options):
        start = time.time()

            # item = Item.objects.last()
            
            # category = Category.objects.last()


            # Image.objects.create(url="https://hello-world.com", content_object=item)
            # Image.objects.create(url="https://hello-world.com", content_object=category)
            
            # item = Item.objects.get(id=23)
            # print(type(item))
            # print(item.id)

            # Image.objects.create(url="https://ihate_jews.com",content_objet=item)
            
            # image= Item.objects.first()

            # Content_type = image.content_type
            # object_id = image.id

            # print(str(Content_type))
            # print(object_id)


            # item_content_type = ContentType.objects.get_for_model(Item)
            # print(Image.objects.filter(content_type=item_content_type))

            # print(Category.objects.all().count())
            # print(Category.objects.with_items().count())

            # print(ItemManager.self.expencive_items().count())
            # print(ItemManager.self.cheap_items().count())

            # category = Category(name="toys", description="about toys")
            # category.save()
            # print(category.id)
            
            # category = Category.objects.create(name="cars")
            # print(category.id)

        # for _ in range(1000): # 0-999

        #     category = Category.objects.create(name=faker.word())   

        # categories = []
        # for _ in range(1000):
        #     category = Category(name=faker.word())
        #     categories.append(category)
        # Category.objects.bulk_create(categories)



        # category = Category.objects.first()
        # category.name = "food"
        # category.save()

        # categories = Category.objects.filter(id__gt=50).update(name="cats")
        # to_update = []


        # for category in categories:
        #     category.name = faker.name()
        #     to_update.append(category)

        # Category.objects.bulk_update(to_update, fields=["name"])  
        
        # category = Category.objects.create(name="For blacks")
        # item = Item.objects.create(name="KFC",category=category)

        class Command(BaseCommand):
            def handle(self, *args, **options):
                categories = Category.objects.all()
                item_objects = Item.objects.all()[:5]
                for category in categories:
                    category.items.add(*item_objects)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        end = time.time()
        print(end-start)
