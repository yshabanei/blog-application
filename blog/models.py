from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("title",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % self.slug


class Post(models.Model):
    active = "active"
    draft = "draft"

    CHOICES_STATUS = ((active, "Active"), (draft, "Draft"))
    category = models.ForeignKey(
        Category, related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=active)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/" % (self.category.slug, self.slug)


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
