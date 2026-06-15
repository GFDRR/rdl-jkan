---
attributions:
- entity:
    affiliation: null
    email: null
    name: UN Operational Satellite Applications Programme (UNOSAT)
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendie-dans-les-delegations-de-nefza-ain-draham-et-tabarka-gouverno
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/densite-des-foyers-d-incendie-dans-les-delegations-de-nefza-ain-draham-et-tabarka-gouverno
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendie-dans-les-delegations-de-nefza-ain-draham-et-tabarka-gouverno
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/densite-des-foyers-d-incendie-dans-les-delegations-de-nefza-ain-draham-et-tabarka-gouverno
dataset_id: rdls_he-tun_unosat_densitedesfoyersdincendie_20230727
description: "UNOSAT code FR20230725TUN, GDACS Id: 1015980 Cette carte illustre la\
  \ densit\xE9 des foyers d'incendie d\xE9tect\xE9s \xE0 partir des donn\xE9es VIIRS\
  \ acquises le 25 juillet 2023. La d\xE9l\xE9gation de Tabarka compte un nombre total\
  \ de 45 foyers d'incendie. En se basant sur les donn\xE9es d\xE9mographiques Worldpop,\
  \ environ 2,200 personnes dans le gouvernorat de Jendouba vivent \xE0 proximit\xE9\
  \ des foyers d'incendie, dont 1,900 dans la d\xE9l\xE9gation de Tabarka. Ceci est\
  \ une analyse pr\xE9liminaire et n'a pas encore \xE9t\xE9 valid\xE9e sur le terrain.\
  \ Ne pas h\xE9siter \xE0 envoyer vos commentaires au Centre Satellitaire des Nations\
  \ Unies (UNOSAT).. [Source: This metadata record was automatically extracted from\
  \ the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/densite-des-foyers-d-incendie-dans-les-delegations-de-nefza-ain-draham-et-tabarka-gouverno]"
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
    description: Population living in proximity to wildfire hotspots in Jendouba Governorate,
      estimated using WorldPop demographic data
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
    wildfire:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: wildfire
        trigger: null
        type: wildfire
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: VIIRS satellite imagery acquired on 25 July 2023 was processed by UNOSAT
    analysts to detect and map fire hotspot density across the delegations of Nefza,
    Ain Draham, and Tabarka in Jendouba Governorate, Tunisia. WorldPop demographic
    data was spatially intersected with the hotspot locations to estimate exposed
    population counts at the delegation level. The resulting dataset provides a preliminary,
    satellite-based situational assessment of wildfire extent and population exposure
    for emergency response purposes.
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
- href: https://data.humdata.org/dataset/densite-des-foyers-d-incendie-dans-les-delegations-de-nefza-ain-draham-et-tabarka-gouverno
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
  description: "Tunisia - Densit\xE9 des foyers d'incendie dans les d\xE9l\xE9gations\
    \ de Nefza, Ain Draham et Tabarka, Gouvernorat de Jendouba le 25 juillet 2023\
    \ (Zipped geodatabase)"
  download_url: https://unosat.org/static/unosat_filesystem/3645/FR20230725TUN.gdb.zip
  format: Geodatabase
  id: resource_0291df7e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230725TUN.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tunisia - Densit\xE9 des foyers d'incendie dans les d\xE9l\xE9gations\
    \ de Nefza, Ain Draham et Tabarka, Gouvernorat de Jendouba le 25 juillet 2023\
    \ (Zipped shapefile)"
  download_url: https://unosat.org/static/unosat_filesystem/3645/FR20230725TUN_SHP.zip
  format: null
  id: resource_1972f25f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FR20230725TUN_SHP.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Tunisia - Densit\xE9 des foyers d'incendie dans les d\xE9l\xE9gations\
    \ de Nefza, Ain Draham et Tabarka, Gouvernorat de Jendouba le 25 juillet 2023\
    \ (Excel file)"
  download_url: https://unosat.org/static/unosat_filesystem/3645/UNOSAT_PopulationExposed_Hotspot_GovernorateJendouba_FR20230725TUN_25072023.xlsx
  format: null
  id: resource_b1daa91b
  media_type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: UNOSAT_PopulationExposed_Hotspot_GovernorateJendouba_FR20230725TUN_25072023.xlsx
risk_data_type:
- hazard
- exposure
schema: rdls-10
slug: rdls_he-tun_unosat_densitedesfoyersdincendie_20230727
spatial:
  bbox: null
  centroid: null
  countries:
  - TUN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2023-07-27'
temporal_resolution: null
title: "Tunisia - Densit\xE9 des foyers d'incendie dans les d\xE9l\xE9gations de Nefza,\
  \ Ain Draham et Tabarka, Gouvernorat de Jendouba le 25 juillet 2023"
version: null
vulnerability: null
---
