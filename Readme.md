# MathTestMakerWebsite

```
docker build -t mathtestmaker .

docker run -d \
-e MATHTESTMAKER_DEBUG=False \
-e MATHTESTMAKER_SECRET="aklhjglihjaoliuoihjkljansdlgjhaoiwertloikhg" \
-p 9001:80 \
--name mathtestmakersite \
mathtestmaker 

docker exec -ti mathtestmakersite bash
```
or modify the above as seems appropriate.

 For example, to run with nginxproxymanager network:

```
docker run -d \
--network nginxproxymanager_default    \
-e MATHTESTMAKER_DEBUG=False \
-e MATHTESTMAKER_SECRET="aklhjglihjaoliuoihjkljansdlgjhaoiwertloikhg" \
--name mathtestmakersite \
mathtestmaker

```
