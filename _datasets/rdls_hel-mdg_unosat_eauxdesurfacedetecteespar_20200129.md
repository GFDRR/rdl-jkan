---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-en-republique-de-madagascar
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-en-republique-de-madagascar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-en-republique-de-madagascar
dataset_id: rdls_hel-mdg_unosat_eauxdesurfacedetecteespar_20200129
description: "UNOSAT code: FL20200128MDG Cette carte illustre les eaux de surface\
  \ d\xE9tect\xE9es via le capteur VIIRS-NOAA sur le centre et le nord de la r\xE9\
  publique de Madagascar entre le 23 janvier et le 27 Janvier 2020. Dans la zone analys\xE9\
  e non couverte par les nuages, environ 850,000 personnes sont expos\xE9es ou vivent\
  \ \xE0 proximit\xE9 des zones inond\xE9es qui couvrent 9,475 km2. Les plaines du\
  \ nord-ouest situ\xE9es dans les r\xE9gions de Boeny, Sofia et Alaotra Mangoro semblent\
  \ \xEAtre particuli\xE8rement impact\xE9es par les inondations en cours. Ceci est\
  \ une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain.\
  \ Ne pas h\xE9siter \xE0 envoyer vos commentaires \xE0 UNITAR-UNOSAT.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-en-republique-de-madagascar]"
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
    description: Population exposed to or living in proximity to inundated areas
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
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
  type: flood
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed VIIRS-NOAA satellite imagery acquired between
    23-27 January 2020 over central and northern Madagascar, comparing multi-temporal
    images to detect surface water extent changes and delineate inundated areas. The
    resulting flood extent map was intersected with population data to estimate exposure,
    producing a preliminary post-event flood hazard and exposure assessment.
  sources:
  - id: source_1
    license: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/eaux-de-surface-detectees-par-satellite-en-republique-de-madagascar
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to inundated areas during January 2020 flooding
      event
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
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
  description: "Eaux de surface d\xE9tect\xE9es par satellite en R\xE9publique de\
    \ Madagascar (Zipped geodatabase)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/FL20200128MDG/FL20200128MDG_gdb.zip
  format: Geodatabase
  id: resource_553a99ff
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200128MDG_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Eaux de surface d\xE9tect\xE9es par satellite en R\xE9publique de\
    \ Madagascar (Zipped shapefile)"
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MD/FL20200128MDG/FL20200128MDG_SHP.zip
  format: null
  id: resource_f81cb37c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200128MDG_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-mdg_unosat_eauxdesurfacedetecteespar_20200129
spatial:
  bbox: null
  centroid: null
  countries:
  - MDG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-01-29'
temporal_resolution: null
title: "Eaux de surface d\xE9tect\xE9es par satellite en R\xE9publique de Madagascar"
version: null
vulnerability: null
---
