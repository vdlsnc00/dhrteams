from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel


class StaffMember(blocks.StructBlock):
    full_name = blocks.CharBlock()
    title = blocks.CharBlock()
    photo = ImageChooserBlock()

    class Meta:
        label = 'Staff Member'

class Team(blocks.StructBlock):
    title = blocks.CharBlock()
    members = blocks.ListBlock(StaffMember())

    class Meta:
        label = 'Team'

class DepartmentPage(Page):
    intro = RichTextField(blank=True)
    team = StreamField([
        ('title', Team()),
    ])
    logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True
    )
    
    content_panels = Page.content_panels + [ 
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('logo'),
        StreamFieldPanel('team')
    ]

class DepartmentsPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [ 
        FieldPanel('intro', classname="full")
    ]
