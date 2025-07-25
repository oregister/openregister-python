# Changelog

## 1.8.0 (2025-07-23)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/oregister/openregister-python/compare/v1.7.0...v1.8.0)

### Features

* **api:** update via SDK Studio ([069557d](https://github.com/oregister/openregister-python/commit/069557d8c97aa7d86c04120827d820b6163dd00a))
* clean up environment call outs ([23dba14](https://github.com/oregister/openregister-python/commit/23dba14b5be47e714812d0494f6f26bfde98fc6b))


### Bug Fixes

* **ci:** correct conditional ([aa5d0f7](https://github.com/oregister/openregister-python/commit/aa5d0f7e44ffaa3d8ee126c7a4fdedb3a88b85a4))
* **ci:** release-doctor — report correct token name ([94cd33d](https://github.com/oregister/openregister-python/commit/94cd33d48fb18b37ab30934561e533b3527c4f50))
* **client:** don't send Content-Type header on GET requests ([9a7b671](https://github.com/oregister/openregister-python/commit/9a7b6712e647c532c4bc3ed6c30d465c76e5172f))
* **parsing:** correctly handle nested discriminated unions ([c55746e](https://github.com/oregister/openregister-python/commit/c55746e6fa20a4b2a6c300a1e4d36993cbef30fc))
* **parsing:** ignore empty metadata ([3cb44b2](https://github.com/oregister/openregister-python/commit/3cb44b2fe7d306a7ade540449d81b420ab671535))
* **parsing:** parse extra field types ([6a7c90d](https://github.com/oregister/openregister-python/commit/6a7c90dcad29c2355d3a7e507aec80db915e6e84))


### Chores

* **ci:** change upload type ([d59202c](https://github.com/oregister/openregister-python/commit/d59202cb676ce4f7c42d6bdf369d973623855ddb))
* **ci:** only run for pushes and fork pull requests ([0b8d5eb](https://github.com/oregister/openregister-python/commit/0b8d5eb3e8bfc8774e322e6b0e6de710ca3f6878))
* **internal:** bump pinned h11 dep ([2f5a623](https://github.com/oregister/openregister-python/commit/2f5a62376dcc28ed73f5c1b7051afdf6d8231ec1))
* **internal:** codegen related update ([e8a7972](https://github.com/oregister/openregister-python/commit/e8a79726219df809f3b750ce828b052d0f7bca36))
* **package:** mark python 3.13 as supported ([1cceac5](https://github.com/oregister/openregister-python/commit/1cceac5170f4fcca5614f1c2e8126ca46e579373))
* **readme:** fix version rendering on pypi ([1239f10](https://github.com/oregister/openregister-python/commit/1239f10f72aae84b60488b287bd38997d8510a88))

## 1.7.0 (2025-06-24)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/oregister/openregister-python/compare/v1.6.0...v1.7.0)

### Features

* **api:** update via SDK Studio ([dbc7813](https://github.com/oregister/openregister-python/commit/dbc7813839a3563e3d4e74abdf366104ca9487fe))

## 1.6.0 (2025-06-24)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/oregister/openregister-python/compare/v1.5.0...v1.6.0)

### Features

* **api:** update via SDK Studio ([ba142a6](https://github.com/oregister/openregister-python/commit/ba142a6ecc663b673b65deeb6d89e9a8c169155e))
* **api:** update via SDK Studio ([0bd9e3c](https://github.com/oregister/openregister-python/commit/0bd9e3c3deb69a9713ace31371d998f03e503fca))
* **client:** add support for aiohttp ([7edb08a](https://github.com/oregister/openregister-python/commit/7edb08a37f1d0d5df0cd3de806a5406efe857d98))


### Chores

* **tests:** skip some failing tests on the latest python versions ([8d990dd](https://github.com/oregister/openregister-python/commit/8d990dd5dd4f3e8a9a3e01989f7b59a68021f709))

## 1.5.0 (2025-06-20)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/oregister/openregister-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** update via SDK Studio ([4eac8c2](https://github.com/oregister/openregister-python/commit/4eac8c2d786342ab445c9b062a9dc97a997e6d40))

## 1.4.0 (2025-06-20)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/oregister/openregister-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** update via SDK Studio ([c1f7f0b](https://github.com/oregister/openregister-python/commit/c1f7f0bb504bec37a98c229182987eb74cdf7732))
* **api:** update via SDK Studio ([29e115d](https://github.com/oregister/openregister-python/commit/29e115d98dd34e7f2320406e3d71fe9a4c5f34d1))


### Bug Fixes

* **client:** correctly parse binary response | stream ([3178a60](https://github.com/oregister/openregister-python/commit/3178a608d0bea505c36ee0dd53beef0b9637d3e2))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([9ff0d2d](https://github.com/oregister/openregister-python/commit/9ff0d2d45e64f8decc4d4f27f552b92fade72818))


### Chores

* **ci:** enable for pull requests ([2267910](https://github.com/oregister/openregister-python/commit/22679109aeef09c71cbf8297b1540792e9e1238e))
* **internal:** update conftest.py ([3159827](https://github.com/oregister/openregister-python/commit/3159827569407d2abd0a48610ba421cbe8bb1a1f))
* **readme:** update badges ([067d506](https://github.com/oregister/openregister-python/commit/067d5068b7c90cf0285f45e8942c9fd35d12db1a))
* **tests:** add tests for httpx client instantiation & proxies ([933aead](https://github.com/oregister/openregister-python/commit/933aead45e63051438e6d2b7ca22302df1735d3f))
* **tests:** run tests in parallel ([4f120e1](https://github.com/oregister/openregister-python/commit/4f120e11a6c102b6a9e976cb10e780d2d617115a))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([e20479c](https://github.com/oregister/openregister-python/commit/e20479cd0e2e9fd3121713e7f168c503949230aa))

## 1.3.0 (2025-06-09)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/oregister/openregister-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** update via SDK Studio ([50198fb](https://github.com/oregister/openregister-python/commit/50198fb41cbf7c4b93df4fe4c3967126ae0e8b09))
* **api:** update via SDK Studio ([42905b5](https://github.com/oregister/openregister-python/commit/42905b56702cbf59d1ba582f112598fcab4ac435))
* **api:** update via SDK Studio ([ad4e5f4](https://github.com/oregister/openregister-python/commit/ad4e5f4ae5715443f4eddf2e09b2c4137ba89eb9))

## 1.2.0 (2025-06-09)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/oregister/openregister-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** update via SDK Studio ([228c918](https://github.com/oregister/openregister-python/commit/228c918a0281457e4a07ebc56925fa5fb40469e8))

## 1.1.0 (2025-06-07)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/oregister/openregister-python/compare/v1.0.1...v1.1.0)

### Features

* **api:** update via SDK Studio ([87a3573](https://github.com/oregister/openregister-python/commit/87a3573991bc19fadd1c4c92c1d90fab80687c7f))

## 1.0.1 (2025-06-07)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/oregister/openregister-python/compare/v1.0.0...v1.0.1)

### Chores

* **internal:** version bump ([722cc66](https://github.com/oregister/openregister-python/commit/722cc66631a7d16ed42771fcff10b2382c1ee6f1))

## 1.0.0 (2025-06-07)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/oregister/openregister-python/compare/v0.0.1-alpha.0...v1.0.0)

### Features

* **api:** update via SDK Studio ([a018c07](https://github.com/oregister/openregister-python/commit/a018c0797b5296e8029e051d36dda94c909b0128))


### Chores

* configure new SDK language ([82da76d](https://github.com/oregister/openregister-python/commit/82da76d60986b6e1a49752ff77d7616f7e022aab))
* update SDK settings ([b3e38ee](https://github.com/oregister/openregister-python/commit/b3e38ee33379b4d063bef466fcbc69672d266815))
* update SDK settings ([145faf6](https://github.com/oregister/openregister-python/commit/145faf6f39192c044fd30bed4395085af8a487ac))
* update SDK settings ([8c2aa41](https://github.com/oregister/openregister-python/commit/8c2aa412e3660f742e3febc22364937dfb373cc4))
