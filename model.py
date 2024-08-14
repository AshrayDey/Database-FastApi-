from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from db1 import Base  # Assuming 'Base' is your SQLAlchemy base class

# Association table for many-to-many relationship between users and posts
liked_posts_association = Table(
    "likes_posts_association",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("user_id", Integer, ForeignKey("users.id"))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  # Added index for faster lookups
    email = Column(String, unique=True, index=True)  # Email should be unique and indexed
    hashed_password = Column(String)  # Column to store hashed password
    is_active = Column(Boolean, default=True)  # Default is True for new users

    # Relationships
    items = relationship("Item", back_populates="owner")
    posts = relationship("Post", back_populates="author")
    posts_liked = relationship("Post", secondary=liked_posts_association, back_populates="liked_by_users")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)  # Added index for faster lookups
    description = Column(String)
    title = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    owner = relationship("User", back_populates="items")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)  # Added index for faster lookups
    content = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    author = relationship("User", back_populates="posts")
    liked_by_users = relationship("User", secondary=liked_posts_association, back_populates="posts_liked")
