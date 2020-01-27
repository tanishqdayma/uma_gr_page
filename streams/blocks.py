"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock


# -------------BLOCK FOR GR PAGE--------------
class ListAndButtonBlock(blocks.StructBlock):
    """List and buttons of main"""

    title = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("point", blocks.CharBlock(required=True, max_length=200)),
                ("pdfs", blocks.ListBlock(
                        DocumentChooserBlock(required=True),
                    )
                )
            ]
        )
    )

    class Meta:  #noqa
        template = "streams/list_and_button.html"
        icon="edit"
        label="GR Text & Documents"



# -------------BLOCK FOR RDE PAGE-------------
class ResourcesBlock(blocks.StructBlock):
    """List and buttons of main"""

    title = blocks.CharBlock(required=True)

    points = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("point", blocks.CharBlock(required=True, max_length=200)),
                ("url", blocks.URLBlock(required=True)),
            ]
        )
    )

    class Meta:  #noqa
        template = "streams/resources_page.html"
        icon="edit"
        label="Resources"
