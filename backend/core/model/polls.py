"""
 Copyright 2025 @Qreater
 Licensed under the Apache License, Version 2.0.
 See: http://www.apache.org/licenses/LICENSE-2.0
"""


class Poll:
    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapter.id"))
    options = Dict(String, Integer)
    created_at = Column(DateTime)
    deadline = Column(DateTime)
