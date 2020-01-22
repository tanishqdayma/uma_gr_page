"""Government Resolutions"""

from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from streams import blocks

class GRPage(Page):
    """GR Page Class"""

    template = "GR/govt_res_page.html"

    content = StreamField(
        [
            ("main", blocks.MainListAndButtonBlock()),
            ("related", blocks.RelatedListAndButtonBlock()),
        ],
        null=True,
        blank=True,
        #label = "Main GR Docs",
    )

   
    # subtitle = models.CharField(max_length=100, null=True, blank=True)
    #subtitle2 = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        #FieldPanel("subtitle"),
        StreamFieldPanel("content"),
    ]

    class Meta: #noqa
        verbose_name = "Government Resolutions Page"
        verbose_name_plural = "Government Resolutions Pages"
