from rest_framework import serializers

from core.models import (
    Grupo,
    GrupoSimulacao,
    Simulacao,
    Resultados,
    Parametros
)


class GrupoSerializer(serializers.ModelSerializer):
    """Serializer for Parametros."""

    class Meta:
        model = Grupo
        fields = ['id', 'nome']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a grupo with auth user."""
        auth_user = self.context['request'].user
        grupo = Grupo.objects.create(
            user=auth_user,
            **validated_data
        )
        return grupo


class ResultadosSerializer(serializers.ModelSerializer):
    """Serializer for Resultados."""

    class Meta:
        model = Resultados
        fields = ['id', 'resultado']
        read_only_fields = ['id']


class ParametrosSerializer(serializers.ModelSerializer):
    """Serializer for Parametros."""

    class Meta:
        model = Parametros
        fields = ['id', 'pop_size', 'generations', 'pop_bottleneck', 'generation_bottleneck', 'p_inicial', 'WAA', 'WAa', 'Waa', 's', 'h', 'u']
        read_only_fields = ['id']


class SimulacaoSerializer(serializers.ModelSerializer):

    """Serializer for Simulacao."""
    resultado = ResultadosSerializer(many=False, required=True)
    parametros = ParametrosSerializer(many=False, required=True)

    class Meta:
        model = Simulacao
        fields = ['id', 'resultado', 'parametros', 'nome']
        read_only_fields = ['id']
    # def create(self):
    #     views.simulacao(self.context['request'])


class GrupoSimulacaoSerializer(serializers.ModelSerializer):

    """Serializer for GrupoSimulacao."""
    simulacao = SimulacaoSerializer(many=False, required=True)

    class Meta:
        model = GrupoSimulacao
        fields = ['id', 'simulacao', 'grupo']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create GrupoSimulacao and objects needed"""
        simulacaoParam = validated_data.pop('simulacao', [])

        resultadosP = simulacaoParam.pop('resultado', [])
        if(not resultadosP['resultado'] in ("", [], None, 0, False, {})):
            resultados = Resultados.objects.create(
                resultado=resultadosP.pop('resultado', [])
            )
        else:
            resultados = None

        parametrosP = simulacaoParam.pop('parametros', [])
        parametros = Parametros.objects.create(**parametrosP)

        simulacaoNome = simulacaoParam.pop('nome', [])
        simulacao = Simulacao.objects.create(
            resultado=resultados,
            parametros=parametros,
            nome=simulacaoNome
        )

        grupo = validated_data.pop('grupo', [])

        grupoSimulação = GrupoSimulacao.objects.create(
            grupo=grupo,
            simulacao=simulacao
        )

        return grupoSimulação

    def update(self, instance, validated_data):
        """Update GrupoSimulacao and objects needed"""
        grupo = validated_data.pop('grupo', [])
        instance.grupo = grupo

        parametrosID = instance.simulacao.parametros.id
        simulacaoID = instance.simulacao.id

        simulacaoParam = validated_data.pop('simulacao', [])

        resultadosP = simulacaoParam.pop('resultado', [])

        try:
            resultadosID = instance.simulacao.resultado.id
            if(not resultadosP['resultado'] in ("", [], None, 0, False, {})):
                resultados = Resultados.objects.update_or_create(
                    id=resultadosID,
                    defaults=resultadosP
                )
                resultados = resultados.__getitem__(0)
            else:
                resultados = None
        except AttributeError:
            if(not resultadosP['resultado'] in ("", [], None, 0, False, {})):
                resultados = Resultados.objects.create(
                    **resultadosP
                )
            else:
                resultados = None

        parametrosP = simulacaoParam.pop('parametros', [])

        parametros = Parametros.objects.update_or_create(
            id=parametrosID,
            defaults=parametrosP
        )
        parametros = parametros.__getitem__(0)

        simulacaoNome = simulacaoParam.pop('nome', [])
        Simulacao.objects.update_or_create(
            id=simulacaoID,
            defaults=dict(
                resultado=resultados,
                parametros=parametros,
                nome=simulacaoNome
            )
        )

        instance.save()

        return instance
