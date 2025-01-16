
class Poll:
    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey('chapter.id'))
    options = Dict(String, Integer)
    created_at = Column(DateTime)
    deadline = Column(DateTime)