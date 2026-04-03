from django.db import models


class OrderRequest(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.SET_NULL,
        related_name="order_requests",
        null=True,
        blank=True,
    )
    # Snapshot of product name at order time (in case product is deleted)
    product_name = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order Request"
        verbose_name_plural = "Order Requests"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        display_name = self.product_name or (self.product.name if self.product else "Unknown Product")
        return f"{self.name} - {display_name}"

    def save(self, *args, **kwargs):
        # Snapshot product name before saving
        if self.product and not self.product_name:
            self.product_name = self.product.name
        super().save(*args, **kwargs)
