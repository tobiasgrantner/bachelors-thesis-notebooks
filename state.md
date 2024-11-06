# Improvements

## Docker Dependency Removal

Removal of dependecy of direct access to Docker from services to achieve independence of deployment environment as described in [this issue](https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/issues/319).


## Before (2023-06-16)

- **Git**: [8bb23619997f1d6f85d85718eb5eb018f68bd80f](https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/tree/8bb23619997f1d6f85d85718eb5eb018f68bd80f)
- **Pipeline**: [https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/pipelines/5885]()
- **Images**:
    - dbrepo/identifier-service@sha256:75b03c7dc2125e5f34f3dfd9af73e7cb77729332ff7089a48c3033921154e9ce
    - dbrepo/container-service@sha256:3f68b189aa0de238ae18ed1114b017922387661628c10ab8e673ac209f69802b
    - dbrepo/database-service@sha256:207f0d2c92c37017772edd7842bea97c26a8c3babd0090f682ea15059ea5e233
    - dbrepo/query-service@sha256:3323f31216caca56e02bc262ad6daf9bd0c41a9b542b16fccca9a64dce1da248
    - dbrepo/table-service@sha256:bf6ed424d585e6831b7a85c51c1dd5bd2cb83e7fafa64aff661f0897f87ce04a
    - dbrepo/analyse-service@sha256:bcf4a5d1b55860c70ccd3ab9bca07cab36e7ee43b706db24a2759aa981b990c8
    - dbrepo/authentication-service@sha256:f1628ceacc1de8acbcb01a6855b62e9726e637241c189d3327264aaaf8004f27
    - dbrepo/metadata-db@sha256:3bdd373b35f80a5726786ea97f0a4adb86af29de5feb5f383be5fc2836bc47a5
    - dbrepo/ui@sha256:1580b3cd8e14885ac6d407157bc6696bb93d8c9f05b93a7c1cae71c69d0968d4
    - dbrepo/semantics-service@sha256:455bb3c74b59febf8e8b5e12ebdcf80651c482cd314a6e96a879533be73a9b35
    - dbrepo/broker-service@sha256:6c7d210f3325c2b6a71d3df9d174bf556eebcdbf49d4b53626732670720eddab
    - dbrepo/metadata-service@sha256:51194d8e4540de492f06ea852fdee2b87cb3763096fb43e3657d328b072c9d5f
    - dbrepo/user-service@sha256:47081dbf3d69d98313b96063fde1f8e41ac7b2631ed29f2e76f9486a16904874


## After (2023-06-18)

- **Git**: [7cf0c76094c285a02ad3341685969733d6836164](https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/tree/7cf0c76094c285a02ad3341685969733d6836164)
- **Pipeline**: [https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/pipelines/5896]()
- **Images**:
    - dbrepo/identifier-service@sha256:85be08e43f93be08b9adba8d307a739ad1302cffa2b38ffb9ddadccefe9197d6
    - dbrepo/container-service@sha256:3eb0b56b76216c5167b0ae2d75fd07e886a0379e9ca72327654d032424a27588
    - dbrepo/database-service@sha256:1fad3a2a8d4f4d09cb18fa0b377129c4a0c23294246c36dc107f08bc30bb92b1
    - dbrepo/query-service@sha256:cd18f4f8831ca1968eb74713ff034a0d89d14905278e50ad2a8778d715d76f99
    - dbrepo/table-service@sha256:93ed69a9c42fd50dbb343e1e0768e1f58728ef0e542813483cbc934845fcc74d
    - dbrepo/analyse-service@sha256:bcf4a5d1b55860c70ccd3ab9bca07cab36e7ee43b706db24a2759aa981b990c8
    - dbrepo/authentication-service@sha256:985e6434182eca39c096bcc2a712ca3f0a345592cf4df805e908cd5399025035
    - dbrepo/metadata-db@sha256:35e9112eb4a9d357f080335a6fc32876c1c219f768a0351f8d63197e804f8506
    - dbrepo/ui@sha256:273f6794c07843bc34cab3bb229fa65a289b56f8d7d2fe4ca53d95040c58d234
    - dbrepo/semantics-service@sha256:38bff14e0e7d186de9c2f193bf278f39d81a986e08a6f126ffd41cb253013af4
    - dbrepo/broker-service@sha256:6c7d210f3325c2b6a71d3df9d174bf556eebcdbf49d4b53626732670720eddab
    - dbrepo/metadata-service@sha256:3e8cb1f2fa0bd01c473532e720d812be64cac3fd6c6e71c043b2080275e1d722
    - dbrepo/user-service@sha256:0aceaff50fb0d02c7c58057eb5b52a15f8452cddb3e09a59f40c09564ba6fa5c
    - dbrepo/ui@sha256:273f6794c07843bc34cab3bb229fa65a289b56f8d7d2fe4ca53d95040c58d234



## Service Merge

Merging of services to reduce the number of services and improve the maintainability of the system as described in [this issue](https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/issues/327).

## Before (2023-08-11)

> [!IMPORTANT]  
> The following git commit is the second last commit before the service merge. Unfortunately, the build pipeline for the last commit before the service merge ([51ba24f39f13e740075742daf476ce281536e487](https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/tree/51ba24f39f13e740075742daf476ce281536e487)) was cancelled. However, the last commit contained only a one-line change in the `docker-compose.yml` file, which has been included in the [docker-compose.yml](compose/service-merge/before/docker-compose.yml) used for the experiments. Therfore, the experiments are conducted on the changes of the last commit, while using the produced artifacts of the second last commit, which are exactly the same as for the last commit.

- **Git**: [82cd375098246e38cf1da9ad34ee981a637433b7](https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/tree/82cd375098246e38cf1da9ad34ee981a637433b7)
- **Pipeline**: [https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/pipelines/6917]()
- **Images**:
    - dbrepo/identity-service@sha256:a44f3e0fcf6cad423fe80e7b40e7da7fbfdcc6f6584f43a2190a01accb879734
    - dbrepo/container-service@sha256:82669c793dd18554d7f39e5816d737167ea6f9a538b28ecd212c6e029b962f1f
    - dbrepo/query-service@sha256:015b8ad5a9c0368976fa18e90486b915fe3955a01ca433a32bdee306cb1a7c51
    - dbrepo/table-service@sha256:899f08274a37439a911af85b14abffd27e89c83baf1740666956d1a62d29eb9a
    - dbrepo/analyse-service@sha256:f9196f428731850e97c2ad91a2f014acca491f095a8cc37aef379c55f1f13cba
    - dbrepo/authentication-service@sha256:9d18aeb2189c5824756b991e5582e8c4b92d9dd28989522690cc19f4c47540ea 
    - dbrepo/metadata-db@sha256:bd6be0381713615ae0e168364c616c9848d672be4442f95032551193805f2d8f
    - dbrepo/ui@sha256:760b539312edcc839f6e69b66f79a5ff8f4792c241636d2cab8a27a506d8d60b
    - dbrepo/semantics-service@sha256:4042276de61e171dc52909230294f8f94b1fa003cf6cc0c47d7cc73414a4e8bb
    - dbrepo/broker-service@sha256:9d6146d5b3ab569da82123987efb5e1bffe5ccfa19d6d4c3f10f999fe7cbf941
    - dbrepo/metadata-service@sha256:978c5adbd7fa235855bb9c4c93772d83183f2494d0f45201cd1a65054f9e8c08
    - dbrepo/user-service@sha256:8640ae9647b6ad6da9d40bf644f61120f0c2e89727399de621f1092a673bfc19
    - dbrepo/search-sync-agent@sha256:92d8a82cfe87366ba57b76cdff66f22483402fc70c0b801dff360242920e9df5
    - dbrepo/data-service@sha256:04891e5ffc36d56e98b806d82e0c4e92d80c5279eaa2e13bb4aafc15386e6885
    - dbrepo/database-service@sha256:775c9c7e5608186acf613099e0c57eeca8ca787c1dde16ce57758e722429b10d


## After (2023-08-28)

- **Git**: [683d2096bf20fe2c9703aab181c932e17550c3e7](https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/tree/683d2096bf20fe2c9703aab181c932e17550c3e7)
- **Pipeline**: [https://gitlab.phaidra.org/fair-data-austria-db-repository/fda-services/-/pipelines/7113]()
- **Images**:
    - dbrepo/analyse-service@sha256:84fdfb1f7de39a3a7db14622a2a538d1a799bba5c628cae3c001a7689609bc10
    - dbrepo/authentication-service@sha256:245fd6207ed43e69c4f86f9a3b707fa0f25e7775f7c2753963a7c8b1fd7fab5d 
    - dbrepo/metadata-db@sha256:501be1137c08133908a5f6f86ffceeb9a921a20559398a3a1c7c49c1f4264e2a
    - dbrepo/ui@sha256:87b29b62ba3a1c0efffaf44b69c77483affc22c4877b3304a65ae7b05bc697d3
    - dbrepo/broker-service@sha256:6d90c251f24959ebb7c8dcf413185892ebe58bfbeed4b002fc79a9b790a2a2bd
    - dbrepo/metadata-service@sha256:46df137a6566167c880f0cac6ec4f4a750f1c31a2661818c0cbcbeea780dad0d
    - dbrepo/search-sync-agent@sha256:0788eda641558cb4c5e06d6f01ce1cfd6151b9f9875fa55f847ae3cf7ae491ec
