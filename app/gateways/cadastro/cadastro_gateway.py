from fastapi import HTTPException, status
from app.entidades.cadastros.cadastro_entities import CadastroEntities
from app.schemas.cadastros.cadastro_schemas import RegisterSchema
from app.models.cadastro.cadastro_model import CadastroModel
from app.models.user_cadastro.user_cadastro_model import UserCadastroModel
from app.models.cadastro_tag.cadastro_tag_model import CadastroTagModel

class CadastroGateway(CadastroEntities):
    
    def __init__(self, db_session):
        self.db_session = db_session
        
    def incluir_cadastro(self, cadastro: RegisterSchema):
       
        try:
            
            cadastro_model = CadastroModel(
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
            

            for tag in cadastro.tag_id:
                cadastro_tag_model = CadastroTagModel(
                    cadastro_id=id_cadastro,
                    tag_id=tag
                )
                self.db_session.add(cadastro_tag_model)
                self.db_session.commit()
            
            return id_cadastro
            
        except Exception as e:
            raise False
    
    def listar_cadastro(self):
        try:
            return self.db_session.query(CadastroModel).all()
        except Exception as e:
            raise False
        
    def atualizar_cadastro(self, id_cadastro: int, cadastro: RegisterSchema):
        try:
            cadastro_model = self.db_session.query(CadastroModel).filter(CadastroModel.id_cadastro == id_cadastro).first()
            if not cadastro_model:
                raise False

            cadastro_model.tag_id = cadastro.tag_id
            cadastro_model.razao_social = cadastro.razao_social
            cadastro_model.nome_fantasia = cadastro.nome_fantasia
            cadastro_model.documento = cadastro.documento
            cadastro_model.email = cadastro.email
            cadastro_model.telefone = cadastro.telefone
            cadastro_model.responsavel_contato = cadastro.responsavel_contato
            cadastro_model.observacao = cadastro.observacao

            self.db_session.commit()
            return True

        except Exception as e:
            raise False

    def deletar_cadastro(self, id_cadastro):
        try:
            cadastro_on_db = self.db_session.query(CadastroModel).filter_by(id_cadastro=id_cadastro).first()
            
            if not cadastro_on_db:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail='Cadastro não encontrado'
                )

            self.db_session.delete(cadastro_on_db)
            self.db_session.commit()
            
            return True
        
        except Exception as e:
            raise False
          