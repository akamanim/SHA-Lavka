from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from shashop.models import Order, Product


@receiver(m2m_changed, sender=Order.products.through)
def update_product_count(sender, instance, action, **kwargs):
    if action == 'post_add' or action == 'post_remove':
        # После добавления или удаления товаров из заказа
        product_ids = instance.products.values_list('id', flat=True)
        count = instance.products.count()

        # Обновление количества товара на складе
        Product.objects.filter(id__in=product_ids).update(count_product=count)