from fastapi import HTTPException, status
from app.entidades.tag.tag_entities import TagEntities
from app.schemas.tags.tags_schema import TagSchema, TagListSchema
from app.models.tags.tags_model import TagsModel

class TagGateway(TagEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    def incluir_tag(self, cadastro_tag: TagSchema):
       
        try:
            
            tag_model = TagsModel(
                tag=cadastro_tag.tag
            )
            
            self.db_session.add(tag_model)
            self.db_session.commit()
            
            return True
            
        except Exception as e:
            raise False
    
    def listar_tag(self):
        try:
            consult_tags = self.db_session.query(TagsModel).all()
            
            list_tag = []
            
            for consult_tag in consult_tags:
                list_tag.append({
                    "id_tag": consult_tag.id_tag,
                    "tag": consult_tag.tag
                })

            return list_tag
        
        except Exception as e:
            raise False