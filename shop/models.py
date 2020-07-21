from uuid import uuid4
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from market.models import Market
from users.models import Profile
from pages.models import Category
# Create your models here.
class Shop(models.Model):
    id = models.UUIDField(
                primary_key = True,
                default = uuid4,
                editable = False)
    title       = models.CharField(
                        _('Name of your shop'),
                        max_length=50,
                        blank=False,
                        default="Mohan supermart",
                        help_text=_("This is the name of your shop/bussiness as in GSTIN registration.")
                        )
    GSTIN       = models.CharField(_('GSTIN Number'),max_length=15,unique=True,blank=False,)
    category    = models.ForeignKey(
                        Category,
                        on_delete=models.SET_NULL,null=True,
                        help_text=_("Category your shop belongs to")
    )
    market      = models.ForeignKey(
                        Market,
                        on_delete=models.SET_NULL,null=True,
                        help_text=_("The market in which your shop is located in.")
    )
    address_line1  = models.CharField(
                        _('Address line 1'),
                        max_length=100,
                        help_text=_('Designates the Address line1 of the Shop.')
    )
    address_line2  = models.CharField(
                        _('Address line 2'),
                        max_length=100,
                        help_text=_('Designates the Address line 2 of the Shop.')
    )
    pincode        = models.CharField(
                        _('Pincode'),
                        max_length=6,
                        help_text=_('Designates the users PINCODE.')
    )
    contact_person = models.CharField(
                        _("Contact person."),
                        max_length=40,
                        # default="Vinay kumar Mishra",
                        help_text=_('Person to contact to for proceeding with the approval process.')
    )
    status      = models.BooleanField(
                        _('Approved'),
                        default=False,
                        help_text=_('Designates the approval status of the shop.')
    )
    description = models.CharField(
                        max_length=200,
                        default="We sell the products you love :)",
                        help_text=_("A sweet little description about your shop.")
    )
    shopno      = models.IntegerField(
                        default=1,
                        help_text=_("Shop number in your market.")
    )
    contactno   = models.CharField(
                        max_length=10,
                        default="9786756453",
                        help_text=_("A contact number")
    )
    image       = models.ImageField(
                        default='default.png',
                        upload_to='static/shops',
                        help_text=_("Please select a picture of your shop.")
    )
    owner       = models.OneToOneField(
                        Profile,
                        on_delete=models.SET_NULL,null=True,
                        help_text=_("Please select the profile of the owner of this shop.")
    )
    pub_ratings = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.title

    #This will redirect to post detail view after creating a new post
    def get_absolute_url(self):
        return reverse('shop-approval')
