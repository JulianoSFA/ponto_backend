#OBJETIVO: Definir datas inicial e final para consulta apartir de filter dos usuários
from rest_framework_json_api.views import ModelViewSet
from rest_framework.decorators import action

#Models importados
from apps.ponto.models.WorkTime import WorkTime

#Serializers Importados
from apps.ponto.serializers.WorkTimeSerializer import WorkTimeSerializer


#ViewSet
class BalanceViewSet(ModelViewSet):
    serializer_class = WorkTimeSerializer
    queryset = WorkTime.objects.all()
    
    @action(methods=['GET'], detail=True, url_path='get-balance')
    def get_balance(self, request, *args, **kwargs):
        assert 'pk' in self.kwargs, ('Expected a pk URL keyword argument')
        user = User.objects.get(self.kwargs['pk']) # Deve ser get mesmo pra dar erro se não tiver
        start = request.GET.get('start')
        end = request.GET.get('end')
        if not start or not end:
            return Response('Start or end of consultation not given',    HTTP_400_BAD_REQUEST)
