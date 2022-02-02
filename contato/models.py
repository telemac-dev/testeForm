from django.db import models

# Create your models here.
class Contato(models.Model):
    
    TIPO_CONTATO = [
    ('PF', 'Pessoa Fisica'),
    ('PJ', 'Pessoa Juridica'),
    ]
    
    tipo_contato = models.CharField(max_length=2, choices=TIPO_CONTATO, default='PJ')
    contato_ativa = models.BooleanField(default=True)
    nome = models.CharField(max_length=100, blank=False) # Nome (PF), Razão Social (PJ)
    
    class Meta:
        ordering = ['nome']
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return self.nome
    
    
class Endereco(models.Model):
    
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

    pessoa = models.ForeignKey('Contato', on_delete=models.CASCADE, related_name='enderecos')
    cep = models.CharField(max_length=8, blank=True, null=True)
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2, choices=UNIDADE_DE_FEDERACAO, default='AM')
    
    def __str__(self):
        return f'{self.logradouro}, {self.numero}\n{self.bairro}\n{self.cidade}\{self.uf}'
    