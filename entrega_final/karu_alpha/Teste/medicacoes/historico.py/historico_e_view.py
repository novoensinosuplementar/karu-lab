# tudo isso é implementação de histórico
class MedicacaoHistorico(models.Model):
    medicacao = models.ForeignKey(Medicacao, on_delete=models.CASCADE, related_name='historico')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    campo = models.CharField(max_length=100)
    valor_antigo = models.TextField(null=True, blank=True)
    valor_novo = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicacao.nome} — {self.campo} alterado"

m = Medicacao.objects.get(id=id)

# exemplo de detecção manual das mudanças
if m.nome != request.POST['nome']:
    MedicacaoHistorico.objects.create(
        medicacao=m,
        usuario=request.user,
        campo='nome',
        valor_antigo=m.nome,
        valor_novo=request.POST['nome']
    )

# agora atualiza o objeto
m.nome = request.POST['nome']
m.save()

# exibição de histórico aqui
historico = m.historico.order_by('-data')

# abaixo tem um HTML
# {% for h in historico %}
# <p>
#    <strong>{{ h.data }} – {{ h.usuario.username }}</strong><br>
#    {{ h.campo }}: "{{ h.valor_antigo }}" → "{{ h.valor_novo }}"
#</p>
#{% endfor %}
