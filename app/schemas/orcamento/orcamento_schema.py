from typing import List
from pydantic import BaseModel

class PlanilhaOrcamentoCustoSchema(BaseModel):
    status_planilha_custo_id: int
    orcamento_id: int
    nome_custo_orcamento: str
    descricao: str
    quantidade: int
    valor_unitario: str
    dias: int
    unidade: str
    total: str
    observacao: str
    versao: int
    total_planilha: str

class CriarOrcamentoSchema(BaseModel):
    empresa_id: int
    centro_custo_id: int
    agencia_id: int
    cliente_id: int
    titulo: str
    coprodutor_id: int
    diretor_id: int
    tipo_job_id: int
    agrupamento: str
    validade_orcamento: str
    imposto: str
    taxa_impulsionamento: str
    comissao_comercial: str
    total_geral: str
    # planilha: List[PlanilhaOrcamentoCustoSchema]
