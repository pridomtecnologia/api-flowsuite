from app.entidades.cadastros.cadastro_entities import CadastroEntities
from app.schemas.cadastros.cadastro_schemas import RegisterSchema
from app.models.cadastro.cadastro_model import CadastroModel
from app.models.user_cadastro.user_cadastro_model import UserCadastroModel

class CadastroGateway(CadastroEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    def incluir_cadastro(self, cadastro: RegisterSchema):
        
        try:
            
            cadastro_model = CadastroModel(
                tag_id=cadastro.tag_id,
                razao_social=cadastro.razao_social,
                nome_fantasia=cadastro.nome_fantasia,
                documento=cadastro.documento,
                email=cadastro.email,
                telefone=cadastro.telefone,
                responsavel_contato=cadastro.responsavel_contato,
                observacao=cadastro.observacao
            )
            
            self.db_session.add(cadastro_model)
            self.db_session.commit()
            
            id_cadastro = cadastro_model.id_cadastro
            
            user_cadastro_model = UserCadastroModel(
                user_id=cadastro.id_user,
                cadastro_id=id_cadastro
            )
            
            self.db_session.add(user_cadastro_model)
            self.db_session.commit()

            return id_cadastro
            
        except Exception as e:
            raise False