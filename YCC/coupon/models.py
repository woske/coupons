from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.images.models import Image
from wagtail.images import widgets as wagtail_widgets
from wagtail.fields import StreamField
from wagtail.blocks import StructBlock, CharBlock, RichTextBlock

from wagtail.snippets.models import register_snippet



class CouponIndexPage(Page):
    intro = RichTextField(blank=True)
    index_page = models.BooleanField(default=True, help_text="Check this to allow indexing of the page.")

    content_panels = Page.content_panels + [
        FieldPanel('index_page'),
        FieldPanel('intro')
    ]

    template = "coupon/coupon_index_page.html"


class CouponPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'Coupon',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class StoreIndexPage(Page):
    intro = RichTextField(blank=True)
    index_page = models.BooleanField(default=True, help_text="Check this to allow indexing of the page.")

    content_panels = Page.content_panels + [
        FieldPanel('index_page'),
        FieldPanel('intro')
    ]

    template = "store/store_index_page.html"


class StoreCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return self.name


class Store(Page):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    external_link = models.URLField(default='')
    description = RichTextField(blank=True)
    accordion = StreamField([
        ('accordion', StructBlock([
            ('title', CharBlock()),
            ('content', RichTextBlock())
        ]))
    ], blank=True, use_json_field=True)
    index_page = models.BooleanField(default=True, help_text="Check this to allow indexing of the page.")
    
    # Add a field for template selection
    template = models.CharField(
        max_length=255,
        choices=[
            ('store/store_page.html', 'Template Box'),
            ('store/store_page_line.html', 'Template Lines'),
        ],
        default='store/store_page.html'  # Set a default template
    )
    

    content_panels = [
        FieldPanel('title'),
        FieldPanel('name'),
        FieldPanel('category'),
        FieldPanel('external_link'),
        FieldPanel('description'),
        FieldPanel('template'),  # Include the template field in the admin panel
        FieldPanel('accordion'),
        FieldPanel('index_page'),
    ]

    def get_template(self, request, *args, **kwargs):
        # Get the template path from the template field
        return self.template

    def save(self, *args, **kwargs):
        if not self.external_link and self.store_link:
            self.external_link = self.store_link.external_link
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    @property
    def linked_coupons(self):
        return Coupon.objects.live().public().filter(store_link=self)


# class CouponPageGalleryImage(Orderable):
#     page = ParentalKey(
#         Coupon,
#         on_delete=models.CASCADE,
#         related_name='gallery_images'
#     )
#     image = models.ForeignKey(
#         Image,
#         on_delete=models.CASCADE,
#         related_name='+'
#     )
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]


class Coupon(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    store_link = models.ForeignKey(
        Store,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    external_link = models.URLField(blank=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    code = models.CharField(max_length=50, blank=True)

    # def main_image(self):
    #     gallery_item = self.gallery_images.first()
    #     if gallery_item:
    #         return gallery_item.image
    #     else:
    #         return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    index_page = models.BooleanField(default=True, help_text="Check this to allow indexing of the page.")
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('store_link'),
        FieldPanel('category'),
        FieldPanel('external_link'),
        FieldPanel('code'),
        FieldPanel('featured_image', widget=wagtail_widgets.AdminImageChooser),
        FieldPanel('index_page'),
        
    ]

    template = "coupon/coupon_page.html"

    def save(self, *args, **kwargs):
        if not self.external_link:
            if self.store_link:
                self.external_link = self.store_link.external_link
        super().save(*args, **kwargs)

    
    class BlogIndexPage(Page):
        intro = RichTextField(blank=True)
        search_fields = Page.search_fields + [
            index.SearchField('intro'),
        ]

        content_panels = Page.content_panels + [
            FieldPanel('intro'),
        ]

        template = "blog/blog_index_page.html"
    
    class BlogPostPage(Page):
        intro = RichTextField(blank=True)
        body = RichTextField()
        index_page = models.BooleanField(default=True, help_text="Check this to allow indexing of the page.")
        accordion = StreamField([
            ('accordion', StructBlock([
                ('title', CharBlock()),
                ('content', RichTextBlock())
            ]))
        ], blank=True, use_json_field=True)

        search_fields = Page.search_fields + [
            index.SearchField('intro'),
            index.SearchField('body'),
        ]

        content_panels = Page.content_panels + [
            FieldPanel('intro'),
            FieldPanel('body'),
            FieldPanel('index_page'),
            FieldPanel('accordion'),
        ]

        template = "blog/blog_post_page.html"

    class StandardPage(Page):
        intro = RichTextField(blank=True)
        body = RichTextField()
        index_page = models.BooleanField(default=True, help_text="Check this to allow indexing of the page.")
        accordion = StreamField([
            ('accordion', StructBlock([
                ('title', CharBlock()),
                ('content', RichTextBlock())
            ]))
        ], blank=True, use_json_field=True)

        search_fields = Page.search_fields + [
            index.SearchField('intro'),
            index.SearchField('body'),
        ]

        content_panels = Page.content_panels + [
            FieldPanel('intro'),
            FieldPanel('body'),
            FieldPanel('index_page'),
            FieldPanel('accordion'),
        ]

        template = "pages/page.html"

