---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 optical satellite imagery
    url: https://data.humdata.org/dataset/eaux-d-inondations-detectees-par-satellite-le-20-octobre-2024-dans-les-departements-de-mat
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/eaux-d-inondations-detectees-par-satellite-le-20-octobre-2024-dans-les-departements-de-mat
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-d-inondations-detectees-par-satellite-le-20-octobre-2024-dans-les-departements-de-mat
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/eaux-d-inondations-detectees-par-satellite-le-20-octobre-2024-dans-les-departements-de-mat
dataset_id: rdls_he-sen_unosat_eauxdinondationsdetectees_20241025
description: "UNOSAT code: FL20241022SEN Cette carte illustre l'\xE9tendue des eaux\
  \ d'inondations d\xE9tect\xE9es par satellite en utilisant une image optique Sentinel-2\
  \ acquise le 20 octobre 2024 dans les d\xE9partements de Matam et Kanel, R\xE9gion\
  \ de Matam. Dans la zone analys\xE9e d'environ 2,700 km\xB2, un total d'environ\
  \ 500 km\xB2 de terres semblent \xEAtre inond\xE9es. D'apr\xE8s les donn\xE9es d\xE9\
  mographique de Worldpop et les eaux d'inondations d\xE9tect\xE9es par imagerie satellite,\
  \ environ 45,000 personnes sont potentiellement expos\xE9es ou vivent \xE0 proximit\xE9\
  \ de zones inond\xE9es. D'apr\xE8s les pr\xE9visions de d\xE9bit du 24 octobre 2024\
  \ provenant de l'ECMWF \xE0 la station hydrom\xE9trique Senegal A Matam le long\
  \ du fleuve S\xE9n\xE9gal, le d\xE9bit moyen actuel a tendance \xE0 diminuer au\
  \ cours des 10 prochains jours. Pri\xE8re de bien vouloir noter que ceci est une\
  \ analyse pr\xE9liminaire qui n'a pas \xE9t\xE9 valid\xE9e sur le terrain. Merci\
  \ d'envoyer vos commentaires au Centre Satellitaire des Nations Unies (UNOSAT)..\
  \ [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/eaux-d-inondations-detectees-par-satellite-le-20-octobre-2024-dans-les-departements-de-mat]"
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
    description: Population potentially exposed or living near inundated zones, derived
      from WorldPop demographic data
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 optical satellite imagery acquired\
    \ on 20 October 2024 and performed visual interpretation and change detection\
    \ to delineate flood water extent in Matam and Kanel departments. Detected inundation\
    \ polygons (approximately 500 km\xB2) were intersected with WorldPop gridded population\
    \ data to estimate exposure of approximately 45,000 people to flood hazard."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 optical satellite imagery
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
- href: https://data.humdata.org/dataset/eaux-d-inondations-detectees-par-satellite-le-20-octobre-2024-dans-les-departements-de-mat
  rel: source
loss: null
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
  description: "Senegal - Eaux d'inondations d\xE9tect\xE9es par satellite le 20 octobre\
    \ 2024 dans les d\xE9partements de Matam et Kanel, S\xE9n\xE9gal (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/4010/FL20241022SEN_gdb.zip
  format: Geodatabase
  id: resource_021baf2f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241022SEN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Senegal - Eaux d'inondations d\xE9tect\xE9es par satellite le 20 octobre\
    \ 2024 dans les d\xE9partements de Matam et Kanel, S\xE9n\xE9gal (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/4010/FL20241022SEN_SHP.zip
  format: null
  id: resource_6989ea49
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20241022SEN_SHP.zip
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-sen_unosat_eauxdinondationsdetectees_20241025
spatial:
  bbox: null
  centroid: null
  countries:
  - SEN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-10-25'
temporal_resolution: null
title: "Senegal - Eaux d'inondations d\xE9tect\xE9es par satellite le 20 octobre 2024\
  \ dans les d\xE9partements de Matam et Kanel, S\xE9n\xE9gal"
version: null
vulnerability: null
---
