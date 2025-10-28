from django.contrib import admin
from .models import SafariPackage, Booking


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 1  # how many empty booking rows to show
    readonly_fields = ("created_at",)
    fields = ("name", "phone", "created_at")


@admin.register(SafariPackage)
class SafariPackageAdmin(admin.ModelAdmin):
    list_display = ("name", "days", "price", "has_image")
    search_fields = ("name", "description")
    list_filter = ("days",)
    inlines = [BookingInline]
    ordering = ("id",)

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = "Image Available"


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "safari", "created_at")
    search_fields = ("name", "phone", "safari__name")
    list_filter = ("safari", "created_at")
    ordering = ("-created_at",)
