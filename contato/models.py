from curses.ascii import NUL
from django.db import models

# Create your models here.
class Marcador(models.Model):
    nome = models.CharField(max_length=100, blank=False, unique=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Marcador"
        verbose_name_plural = "Marcadores"

    def __str__(self):
        return self.nome

class Contato(models.Model):
    
    TIPO_CONTATO = [
    ('PF', 'Pessoa Fisica'),
    ('PJ', 'Pessoa Juridica'),
    ]
    
    UNIDADE_DE_FEDERACAO = [
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins')
    ]

    tipo_contato = models.CharField(max_length=2, choices=TIPO_CONTATO, default='PJ')
    contato_ativa = models.BooleanField(default=True)
    nome = models.CharField(max_length=100, blank=False) # Nome (PF), Razão Social (PJ)
    apelido = models.CharField(max_length=100, blank=False) # Apelido (PF), Nome Fantasia (PJ)
    inscricao_federal = models.CharField(max_length=14, blank=True, null=True, unique=True) # CPF (PF), CNPJ (PJ)
    contato_de = models.ForeignKey('self', unique=False, on_delete=models.PROTECT, related_name='contato_relacionado')
    carga = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    site_web = models.CharField(max_length=100, blank=True)
    marcador = models.ManyToManyField(Marcador, blank=True)
    observacao = models.TextField()
    
    cep = models.CharField(max_length=8, blank=True, null=True)
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2, choices=UNIDADE_DE_FEDERACAO, default='AM')
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return self.nome

    def endereco_get(self):
        return f'{self.logradouro}, {self.numero}\n{self.bairro}\n{self.cidade}\{self.uf}'
    
    def marcadores_get(self):
        return f'{self.nome}'
   
# class Endereco(models.Model):
    
#     UNIDADE_DE_FEDERACAO = [
#     ('AC', 'Acre'),
#     ('AL', 'Alagoas'),
#     ('AP', 'Amapá'),
#     ('AM', 'Amazonas'),
#     ('BA', 'Bahia'),
#     ('CE', 'Ceará'),
#     ('DF', 'Distrito Federal'),
#     ('ES', 'Espírito Santo'),
#     ('GO', 'Goiás'),
#     ('MA', 'Maranhão'),
#     ('MT', 'Mato Grosso'),
#     ('MS', 'Mato Grosso do Sul'),
#     ('MG', 'Minas Gerais'),
#     ('PA', 'Pará'),
#     ('PB', 'Paraíba'),
#     ('PR', 'Paraná'),
#     ('PE', 'Pernambuco'),
#     ('PI', 'Piauí'),
#     ('RJ', 'Rio de Janeiro'),
#     ('RN', 'Rio Grande do Norte'),
#     ('RS', 'Rio Grande do Sul'),
#     ('RO', 'Rondônia'),
#     ('RR', 'Roraima'),
#     ('SC', 'Santa Catarina'),
#     ('SP', 'São Paulo'),
#     ('SE', 'Sergipe'),
#     ('TO', 'Tocantins')
#     ]

#     pessoa = models.OneToOneField('Contato', on_delete=models.CASCADE, related_name='endereco')
#     cep = models.CharField(max_length=8, blank=True, null=True)
#     logradouro = models.CharField(max_length=50)
#     numero = models.CharField(max_length=5)
#     bairro = models.CharField(max_length=50)
#     cidade = models.CharField(max_length=60)
#     uf = models.CharField(max_length=2, choices=UNIDADE_DE_FEDERACAO, default='AM')
    
#     def __str__(self):
#         return f'{self.logradouro}, {self.numero}\n{self.bairro}\n{self.cidade}\{self.uf}'
