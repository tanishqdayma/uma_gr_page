"""Streamfields live in here."""

from wagtail.core import blocks
from wagtail.documents.blocks import DocumentChooserBlock

class MainListAndButtonBlock(blocks.StructBlock):
    """List and buttons of main"""

    # title = blocks.CharBlock(required=True)

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
        template = "streams/main_list_and_button.html"
        icon="edit"
        label="Main GR Text & Documents"

class RelatedListAndButtonBlock(blocks.StructBlock):
    """List and buttons of main"""

    # title = blocks.CharBlock(required=True)

    points_r = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("point_r", blocks.CharBlock(required=True, max_length=200)),
                ("pdfs_r", blocks.ListBlock(
                        DocumentChooserBlock(required=True),
                    )
                )
            ]
        )
    )

    class Meta:  #noqa
        template = "streams/related_list_and_button.html"
        icon="edit"
        label="Related GR Text & Documents"
