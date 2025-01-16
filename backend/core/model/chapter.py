

class Chapter:
    """
    Chapter model

    Attributes:
    -----------
    id: int
        The chapter's unique identifier
    title: str
        The chapter's title
    content: str
        The chapter's content
    story_id: int
        The chapter's story's unique identifier
    created_at: datetime
        The chapter's creation date
    updated_at: datetime
        The chapter's last update date
    chapter_no: int
        The chapter's number
    """
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    story_id = Column(Integer, ForeignKey('story.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    chapter_no = Column(Integer, index=True)

    story = relationship("Story", back_populates="chapters")
