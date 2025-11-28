from django.contrib import admin
from django.utils.html import format_html
from .models import Medicacao, Lembrete, RegistroAdministracao, Estoque

# Configuração Visual do Header do Admin
admin.site.site_header = "Karu Administração"
admin.site.site_title = "Karu Admin"
admin.site.index_title = "Bem-vindo ao Gerenciamento Karu"

# === INLINES ===
# Isso permite editar Lembretes e Estoque DENTRO da tela da Medicação
class LembreteInline(admin.TabularInline):
    model = Lembrete
    extra = 0 # Não mostra linhas vazias extras

class EstoqueInline(admin.StackedInline):
    model = Estoque
    can_delete = False
    verbose_name_plural = 'Estoque Associado'

# === MEDICAÇÃO ===
@admin.register(Medicacao)
class MedicacaoAdmin(admin.ModelAdmin):
    # O que aparece na lista
    list_display = ('nome', 'dosagem', 'frequencia', 'via', 'bebe_id', 'status_estoque')
    # Campos que servem para busca
    search_fields = ('nome', 'bebe_id', 'cuidados_especiais')
    # Filtros na lateral direita
    list_filter = ('via', 'data_inicio')
    # Inserindo os inlines criados acima
    inlines = [LembreteInline, EstoqueInline]
    
    # Organizando o formulário de edição
    fieldsets = (
        ('Dados Principais', {
            'fields': ('nome', 'bebe_id', 'data_inicio')
        }),
        ('Posologia', {
            'fields': ('dosagem', 'frequencia', 'via', 'duracao_dias')
        }),
        ('Outros', {
            'fields': ('cuidados_especiais',),
            'classes': ('collapse',), # Esconde essa seção por padrão para limpar a tela
        }),
    )

    # Função para mostrar o status do estoque na lista de medicações
    def status_estoque(self, obj):
        if hasattr(obj, 'estoque'):
            if obj.estoque.alerta_baixo_estoque:
                return format_html('<span style="color: red; font-weight: bold;">⚠ BAIXO</span>')
            return format_html('<span style="color: green;">✔ OK</span>')
        return "-"
    status_estoque.short_description = "Situação do Estoque"


# === LEMBRETE ===
@admin.register(Lembrete)
class LembreteAdmin(admin.ModelAdmin):
    list_display = ('medicacao', 'horario', 'canal_preferido', 'tolerancia_minutos')
    list_filter = ('canal_preferido', 'horario')
    search_fields = ('medicacao__nome',) # Busca pelo nome da medicação relacionada


# === ESTOQUE ===
@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
    list_display = ('medicacao', 'quantidade_total_ml', 'consumo_diario_estimado_ml', 'visual_alerta')
    list_filter = ('alerta_baixo_estoque',)
    
    # Adicionando ações em massa
    actions = ['recalcular_alertas']

    def visual_alerta(self, obj):
        # Cria um ícone visual baseado no booleano
        return obj.alerta_baixo_estoque
    visual_alerta.boolean = True # O Django transforma True/False em ícone bonito automaticamente
    visual_alerta.short_description = "Alerta Ativo?"

    @admin.action(description='Recalcular alertas selecionados')
    def recalcular_alertas(self, request, queryset):
        count = 0
        for estoque in queryset:
            estoque.atualizar_alerta()
            count += 1
        self.message_user(request, f"{count} estoques atualizados.")


# === REGISTRO DE ADMINISTRAÇÃO ===
@admin.register(RegistroAdministracao)
class RegistroAdministracaoAdmin(admin.ModelAdmin):
    list_display = ('medicacao', 'status_colorido', 'horario_registro', 'observacoes_curtas')
    list_filter = ('status', 'horario_registro', 'medicacao')
    date_hierarchy = 'horario_registro' # Cria uma navegação por data no topo

    def status_colorido(self, obj):
        cores = {
            'TOMEI': 'green',
            'ESQUECI': 'orange',
            'RECUSEI': 'red',
            'VOMITOU': 'purple',
        }
        cor = cores.get(obj.status, 'black')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            cor,
            obj.get_status_display()
        )
    status_colorido.short_description = "Status"

    def observacoes_curtas(self, obj):
        return obj.observacoes[:50] + "..." if obj.observacoes else "-"
    observacoes_curtas.short_description = "Obs"
    