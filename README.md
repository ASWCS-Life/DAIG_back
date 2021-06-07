# Repository Info
this is respository of DAIG (Distributed A.I Grid) project server program.
it is based on Django because we need to use various python libraries like numpy for model training and others.

DAIG (Distributed A.I Grid) 프로젝트의 서버 프로그램 저장소입니다. 
본 프로젝트의 서버는 Django를 기반으로 작성하였습니다. numpy를 비롯한 각종 파이썬 라이브러리를 사용하기 위해 Python기반인 Django를 사용하게 되었습니다.
- - -
# What is DAIG?
DAIG (Distributed A.I Grid) is network based distributed deep learning based machine learning system via network.
Usually, deep learning based machine learning methods require more training time than other methods.
One way to solve this long training time problem is using multiple GPUs. However, it is pretty expensive and hard to dispose of them after training.
So, we tried to use other people's left pc resources instead of multiple GPUs

DAIG는 네트워크를 경유하여 딥러닝 기반의 분산 기계학습을 진행하는 시스템입니다.
보통 딥러닝 기반 머신러닝 기법들은 다른 기법들 보다 더 많은 훈련 시간이 요구됩니다.
이러한 긴 학습 시간 문제를 해결하는 하나의 방법으로 다중 GPU들을 사용하는 방법이 있습니다. 하지만 이 방법은 많은 비용이 요구되며 학습 이후 GPU의 처분이 힘듭니다.
그래서 저희는 다중 GPU들을 사용하는 대신에 다른 사람들의 남는 pc 자원을 사용하는 것을 고안했습니다.
- - -
# How DAIG works?
DAIG system consists of Learning requestor, Resource provider and Management server.
Learning requestor makes project and upload train data to Management server.
Then, Management server distribute train data shards and model information to registered Resource providers
When all train data shards are used for learning, Management server save final model and weight result at object storage.
Learning requestor can download trained model at anytime.

DAIG 시스템은 학습요청자, 리소스 제공자 그리고 관리 서버로 구성됩니다.
학습요청자는 프로젝트를 생성하고 관리 서버로 훈련 데이터를 전송합니다.
이후, 관리 서버는 훈련 데이터의 파편과 모델 정보를 해당 프로젝트에 참여하는 리소스 제공자에게 나눠줍니다.
모든 훈련 데이터 파편에 대한 학습이 끝나면, 관리 서버는 훈련된 최종 모델과 가중치 결과를 오브젝트 스토리지에 저장합니다.
학습요청자는 훈련된 최종 모델을 언제든지 다운받을 수 있습니다.

## DAIG structure
![image](https://user-images.githubusercontent.com/22979031/120693675-47bba700-c4e4-11eb-94b6-f079a1ae0f46.png)
![image2](https://user-images.githubusercontent.com/22979031/120912837-895b7600-c6cd-11eb-93a9-890f489ed992.PNG)
- - -
# DAIG server dependency
|Name|version|usage|
|------|---|---|
|Django|3.1.7|for server development|
|boto3|1.17.67|for object storage|
|numpy|1.19.5|for data manipulation|
|requests|2.25.1|for http communication|
|h5py|3.1.0|for model saving|
|iamport||for pay procedure|

- - -
# How DAIG's distribution works?
We constructed DAIG distribution and result gathering system based on K-batch sync SGD.
And it gathers trained gradients based on all-reduce method.
K-batch size can be controlled by Learning requestor.
So, its final result is also contorlled by Learning requestor.

저희는 DAIG을 K-batch sync SGD 기반의 분산 및 결과 수집 시스템으로 구성했습니다.
그리고 훈련된 가중치들은 all-reduce 방식으로 취합됩니다.
K-batch 사이즈는 학습요청자가 조정할 수 있습니다.
그렇기에, 최종 결과는 학습 요청자에 따라 제어될 수 있습니다.
- - -
# How to use DAIG?
This is server program. so, you should better check "https://github.com/ASWCS-Life/DAIG_front"

이곳은 서버 프로그램 저장소입니다. DAIG 프로그램 사용법은 DAIG 프론트엔드 저장소로 가시면 자세히 설명되어있습니다.
DAIG 프론트엔드 링크: "https://github.com/ASWCS-Life/DAIG_front"
- - -
# How to launch server?
First, you need to install python libraries which are listed above.
Or you can use requirement file.
Then use manage.py for Django server launch. One exmaple is 
```python manage.py runserver 0.0.0.0:8000```.
Refer Django reference book for more detail

첫 번째로, 위 리스트에 있는 파이썬 라이브러리를 설치하셔야 합니다.
혹은 requirement file을 이용하여 설치하실 수 있습니다.
그 다음 manage.py를 사용해 서버를 킬 수 있습니다.
예시: ```python manage.py runserver 0.0.0.0:8000```
자세한 내용은 Django reference book을 참고하시기 바랍니다.
- - -
# Some points of DAIG server
## One way to treat numpy file via https
## How K-batch sync SGD is established
However, DAIG also focused on balance among Resource providers. so, it may not be pure K-batch sync SGD. (depends on situation)

- - -
### Caution!
this project has been developed by korean developers. So, there are some korean comments.
And this is server program so please also check "https://github.com/ASWCS-Life/DAIG_front"

본 프로젝트는 한국 개발자들이 개발했습니다. 따라서 코드에 한국어 코멘트들이 많이 있습니다.
이곳은 서버 프로그램 저장소입니다. 그렇기에 "https://github.com/ASWCS-Life/DAIG_front"를 방문하셔서 클라이언트 프로그램 또한 확인해주시기 바랍니다. 
