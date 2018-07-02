"""
set variables for choicefields.

"""

# used admin panel and issuelog
ISSUE_TAG_CHOICES = (
    ('bug', 'bug'),
    ('feature', 'feature')
    )

# used in admin panel    
ISSUE_STATUS_CHOICES = (
    ('open', 'open'),
    ('pending', 'pending'),
    ('closed', 'closed')
    )    
    
# used in admin and issuelog
PRODUCT_CHOICES = (
    ("multifamily", 'multifamly'),
    ('multi-tenant', 'multi-tenant'),
    ('mixed-use', 'mixed-use'),
    ('campus', 'campus'),
    ('developer', 'developer'),
    ('note', 'note'),
    ('other', 'other'),
    ('website', 'website')
    )    