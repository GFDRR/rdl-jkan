---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-entre-le-01-et-le-28-novembre-2022-dans-les-provin
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-entre-le-01-et-le-28-novembre-2022-dans-les-provin
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-entre-le-01-et-le-28-novembre-2022-dans-les-provin
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-entre-le-01-et-le-28-novembre-2022-dans-les-provin
dataset_id: rdls_he-cod_unosat_eauxdesurfacedetecteespar_20221128
description: "UNOSAT code FL20221125COD Cette carte illustre l'\xE9tendue des eaux\
  \ de surface d\xE9tect\xE9es par satellite en utilisant de l'imagerie satellite\
  \ VIIRS au-dessus des provinces de l'Equateur, du Nord-Ubangi et du Sud-Ubangi (R\xE9\
  publique D\xE9mocratique du Congo) entre le 1er et le 28 novembre 2022. Dans la\
  \ zone analys\xE9e d'environ 210 000 km\xB2, un total d'environ 6 800 km\xB2 de\
  \ terres semblent \xEAtre inond\xE9es. L'\xE9tendue des eaux de surface semble \xEA\
  tre plus petite d'environ 4 000 km\xB2 compar\xE9 \xE0 la p\xE9riode du 1er au 30\
  \ novembre 2019. D'apr\xE8s les donn\xE9es d\xE9mographiques de Worldpop et les\
  \ eaux de surface d\xE9tect\xE9es par satellite, environ 245 000 personnes sont\
  \ potentiellement expos\xE9es ou vivent \xE0 proximit\xE9 de zones inond\xE9es.\
  \ Pri\xE8re de bien vouloir noter que ceci est une analyse pr\xE9liminaire qui n'a\
  \ pas \xE9t\xE9 valid\xE9e sur le terrain. Merci d'envoyer vos commentaires au Centre\
  \ Satellitaire des Nations Unies (UNOSAT).. [Source: This metadata record was automatically\
  \ extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-entre-le-01-et-le-28-novembre-2022-dans-les-provin]"
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population exposed to detected surface water inundation derived from
      WorldPop demographic data
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard:
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: fluvial_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: UNOSAT analysts processed VIIRS satellite imagery acquired between
    1-28 November 2022 over three provinces in DRC, comparing multi-temporal images
    to detect surface water extent changes. Population exposure was calculated by
    intersecting detected inundation polygons with WorldPop gridded demographic data
    to quantify affected populations.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-entre-le-01-et-le-28-novembre-2022-dans-les-provin
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Eaux de surface d\xE9tect\xE9es par satellite entre le 01 et le 28\
    \ novembre 2022 dans les provinces de l'Equateur, du Nord-Ubangi et du Sud-Ubangi,\
    \ R\xE9publique D\xE9mocratique du Congo (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3456/FL20221125COD_gdb.zip
  format: Geodatabase
  id: resource_c2af9bc6
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221125COD_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Eaux de surface d\xE9tect\xE9es par satellite entre le 01 et le 28\
    \ novembre 2022 dans les provinces de l'Equateur, du Nord-Ubangi et du Sud-Ubangi,\
    \ R\xE9publique D\xE9mocratique du Congo (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3456/FL20221125COD_SHP.zip
  format: null
  id: resource_e29d5521
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20221125COD_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Eaux de surface d\xE9tect\xE9es par satellite entre le 01 et le 28\
    \ novembre 2022 dans les provinces de l'Equateur, du Nord-Ubangi et du Sud-Ubangi,\
    \ R\xE9publique D\xE9mocratique du Congo (Excel file)"
  download_url: https://unosat.org/static/unosat_filesystem/3456/UNOSAT_Population_Exposure_FL20221125COD_November_2019_2020_2021_2022_Equateur_NordUbangi_SudUbangi_RDC_FR.xlsx
  format: null
  id: resource_d02893a7
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_Population_Exposure_FL20221125COD_November_2019_2020_2021_2022_Equateur_NordUbangi_SudUbangi_RDC_FR.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-cod_unosat_eauxdesurfacedetecteespar_20221128
spatial:
  bbox: null
  centroid: null
  countries:
  - COD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-11-28'
temporal_resolution: null
title: "Eaux de surface d\xE9tect\xE9es par satellite entre le 01 et le 28 novembre\
  \ 2022 dans les provinces de l'Equateur, du Nord-Ubangi et du Sud-Ubangi, R\xE9\
  publique D\xE9mocratique du Congo"
version: null
vulnerability: null
---
