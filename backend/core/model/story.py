

class Story:
    """
    Story model

    Attributes:
    -----------
    id: int
        The story's unique identifier
    title: str
        The story's title
    summary: str
        The story's summary
    user_id: int
        The story's author's unique identifier
    genre: list 
        The story's genre
    created_at: datetime
        The story's creation date
    updated_at: datetime
        The story's last update date
    tags: list
        The story's tags
    status: str
        The story's status
    chapter_no: int
        The story's chapter number

    """
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    summary = Column(Text, limit=500)
    user_id = Column(Integer, ForeignKey('user.id'))
    genre= List(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    tags = List(String, index=True)
    status = Column(String, index=True, default= "Ongoing")
    chapter_no = Column(Integer, index=True, default= 0)

    user = relationship("User", back_populates="stories")
    chapters = relationship("Chapter", back_populates="story", cascade="all, delete-orphan")
