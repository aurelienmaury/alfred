# Alfred's ears


## Audio profile structure

Un répertoire audio-profile est utile pour le fonctionnement de pocketsphinx

```
./audio-profile/fr-fr   <-- répertoire du modèle acoustic
./audio-profile/fr-fr/feat.params
./audio-profile/fr-fr/LICENSE
./audio-profile/fr-fr/mdef
./audio-profile/fr-fr/means
./audio-profile/fr-fr/mixture_weights
./audio-profile/fr-fr/noisedict
./audio-profile/fr-fr/README
./audio-profile/fr-fr/transition_matrices
./audio-profile/fr-fr/variances

./audio-profile/fr-fr.dic   <-- dictionnaire phonetique
./audio-profile/fr-fr.lm.dmp   <-- language model
```

si vous avez un répertoire de ce format il faut donner (en chemin absolus) :

```-m $(pwd)/audio-profile -n fr-fr```

en se basant sur ces 2 infos, tous sera bien pris en compte. L'option ```-n``` doit
matcher avec le sous-répertoire de audio-profile qui contient le modèle acoustique ET
avec le ```.dic``` et le ```.lm.dmp```
