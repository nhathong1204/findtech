# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from userauths.models import User  
# from .models import Account


# @receiver(post_save, sender=User)
# def handle_post_save(sender, instance, created, **kwargs):
#     if created:
#         Account.objects.create(user=instance)
#     else:
#         instance.account.save()
